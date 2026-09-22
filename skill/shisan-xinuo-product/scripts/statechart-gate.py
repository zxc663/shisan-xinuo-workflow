#!/usr/bin/env python3
"""statechart-gate · 门禁⑩：态+转换结构检查（出路的严格表述）。

检查翻译表源 statechart JSON：
  C1 initial 存在  C2 无死端（非终态全有出边）  C3 全可达（initial 出发 BFS）
  C4 错误态必有恢复转换（出边指向非错误态）
  C5 带守卫的转换须有 guardDesc 说明
  C6 引用完整性：每条转换的 target 必须存在于 states（2026-09-23 补；根因=旧版 BFS 静默跳过）
  C7 recovery 双向对账（需 --contract；2026-09-23 补，候选 12）：
     正向=契约 recovery 每行 (state,action,target) 必须命中 statechart 对应转换（缺边=承诺落空）
     反向=错误态出边 ⊆ recovery 行 ∪ non_error_failures 白名单（多边=未登记发明）
     双向均 exit 1。

错误态识别（2026-09-23 结构化，向后兼容）：
  声明（状态体 "type": "error"）∪ 态名含 error/fail 的启发式 ∪ 契约 recovery 行提及的状态。
  名启发式会漏掉 permission_denied 这类命名——需要准确识别时请显式声明 "type": "error"，
  或在契约 recovery 中登记该状态的出路。

契约 JSON 形态（--contract，字段名对齐 references/contract-schema.md §1）：
  {"recovery": [{"state": "export_failed", "action": "RETRY_EXPORT", "target": "exporting", "note": "…"}],
   "non_error_failures": [{"state": "loading", "action": "LOAD_FAIL", "target": "empty"}]}

能力边界（2026-09-21 peer 实战反哺，诚实声明）：
  本 gate 的 schema=扁平 states（无嵌套/并行区域）。文件级/批量等「粒度语义」
  只能用「自环+guardDesc 文字约定」表达，gate 查不了粒度是否正确——结构检查
  （图性质）与领域语义评审（粒度/传播）缺一不可。嵌套 states 支持待真实项目
  痛了再上（元规则六问裁决，勿提前复杂化）。
  dict 形式的转换若无 "target" 键=内部转换（合法，无出边语义），本 gate 不报。

用法：python statechart-gate.py --file sc.json [--contract contract.json]
      python statechart-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path


def targets(tr) -> list[str]:
    if isinstance(tr, str):
        return [tr]
    if isinstance(tr, dict):
        return [tr["target"]] if "target" in tr else []
    return []


def norm_transitions(on) -> list[tuple[str, dict]]:
    """归一化 on 表 → [(event, 转换 dict)]；str 提升为 {"target": s}；dict 原样（可无 target）。"""
    out: list[tuple[str, dict]] = []
    for event, tr in (on or {}).items():
        items = tr if isinstance(tr, list) else [tr]
        for x in items:
            if isinstance(x, str):
                out.append((event, {"target": x}))
            elif isinstance(x, dict):
                out.append((event, dict(x)))
    return out


def error_states(states: dict, contract: dict | None = None) -> set[str]:
    declared = {n for n, b in states.items()
                if isinstance(b, dict) and str((b or {}).get("type", "")).lower() == "error"}
    heuristic = {n for n in states if "error" in n.lower() or "fail" in n.lower()}
    from_contract = {r.get("state") for r in (contract or {}).get("recovery", []) if r.get("state")}
    return declared | heuristic | from_contract


def check(sc: dict, contract: dict | None = None) -> list[str]:
    fails: list[str] = []
    states: dict = sc.get("states", {})
    initial = sc.get("initial")
    if initial not in states:
        return [f"C1 initial '{initial}' 不在 states"]
    edges: dict[str, list[str]] = {}
    for name, body in states.items():
        on = (body or {}).get("on", {}) or {}
        out: list[str] = []
        for event, tr in norm_transitions(on):
            tgt = tr.get("target")
            if tgt is None:
                if isinstance(tr, dict) and "target" not in tr:
                    if "guard" in tr and not tr.get("guardDesc"):
                        fails.append(f"C5 {name} 转换守卫 '{tr['guard']}' 缺 guardDesc 说明")
                    continue
                tgt = ""  # "target": null —— 显式空目标，按悬空处理
            out.append(tgt)
            if tgt not in states:
                fails.append(f"C6 引用完整性：'{name}' 的事件 {event} 指向不存在的态 '{tgt}'")
            if isinstance(tr, dict) and "guard" in tr and not tr.get("guardDesc"):
                fails.append(f"C5 {name} 转换守卫 '{tr['guard']}' 缺 guardDesc 说明")
        edges[name] = out
        if name not in ("final",) and not (body or {}).get("type") == "final" and not out:
            fails.append(f"C2 死端：状态 '{name}' 无任何出边")
    seen, q = {initial}, deque([initial])
    while q:
        for t in edges.get(q.popleft(), []):
            if t in states and t not in seen:
                seen.add(t)
                q.append(t)
    for name in states:
        if name not in seen:
            fails.append(f"C3 不可达：状态 '{name}' 从 initial 无法到达")
    est = error_states(states, contract)
    for name in sorted(est):
        if name not in states:
            continue
        recover = [t for t in edges.get(name, []) if t not in est]
        if not recover:
            fails.append(f"C4 错误态 '{name}' 无恢复转换（出路）")
    if contract is not None:
        fails += reconcile(states, contract)
    return fails


def reconcile(states: dict, contract: dict) -> list[str]:
    """C7：契约 recovery 行 ↔ statechart 转换双向对账（缺边=承诺落空／多边=未登记发明）。"""
    fails: list[str] = []
    rows = contract.get("recovery", []) or []
    registered = {(r.get("state"), r.get("action"), r.get("target")) for r in rows}
    for r in rows:
        st, act, tgt = r.get("state"), r.get("action"), r.get("target")
        if st not in states:
            fails.append(f"C7 正向：recovery 行状态 '{st}' 不在 statechart（承诺无处兑现）")
            continue
        cand = [t for ev, td in norm_transitions((states[st] or {}).get("on", {}))
                if ev == act for t in [td.get("target")] if t is not None]
        if tgt not in cand:
            got = "/".join(cand) if cand else "无该事件"
            fails.append(f"C7 正向：契约承诺 {st} --{act}--> {tgt} 在 statechart 中不存在（实际：{got}）")
    allow = registered | {(r.get("state"), r.get("action"), r.get("target"))
                          for r in (contract.get("non_error_failures", []) or [])}
    for name in sorted(error_states(states, contract)):
        if name not in states:
            continue
        for ev, td in norm_transitions((states[name] or {}).get("on", {})):
            tgt = td.get("target")
            if tgt is not None and (name, ev, tgt) not in allow:
                fails.append(f"C7 反向：错误态 '{name}' 的出边 {ev}->{tgt} 未登记（多边=未登记发明，或漏写 recovery 行）")
    return fails


def selftest() -> int:
    good = {"initial": "idle", "states": {
        "idle": {"on": {"GO": "parsing"}}, "parsing": {"on": {"DONE": "done", "FAIL": "error"}},
        "error": {"on": {"RETRY": "parsing"}}, "done": {"type": "final"}}}
    bad = {"initial": "idle", "states": {
        "idle": {"on": {"GO": "parsing"}}, "parsing": {"on": {"DONE": "done", "FAIL": "error"}},
        "error": {"on": {}}, "ghost": {"on": {"X": "idle"}}, "done": {"type": "final"}}}
    ok1 = check(good) == []
    f = check(bad)
    ok2 = any("C4" in x for x in f) and any("C3" in x for x in f)

    # C6 引用完整性：悬空 target 必报
    dangling = {"initial": "idle", "states": {
        "idle": {"on": {"GO": "nowhere"}}, "done": {"type": "final"}}}
    f6 = check(dangling)
    ok6 = any("C6" in x for x in f6) and any("nowhere" in x for x in f6)

    # 结构化错误态：名不含 error/fail 也可识别（"type":"error"）
    c4_decl = {"initial": "idle", "states": {
        "idle": {"on": {"GO": "denied"}}, "denied": {"type": "error", "on": {}}}}
    ok_c4 = any("C4" in x and "denied" in x for x in check(c4_decl))

    # C7 正向：契约行在图中缺失 → 拦
    contract = {"recovery": [{"state": "error", "action": "RETRY", "target": "parsing"}],
                "non_error_failures": [{"state": "parsing", "action": "FAIL", "target": "error"}]}
    ok7f = check(good, contract) == []
    broken = {"initial": "idle", "states": {
        "idle": {"on": {"GO": "parsing"}}, "parsing": {"on": {"DONE": "done", "FAIL": "error"}},
        "error": {"on": {"ABORT": "idle"}}, "done": {"type": "final"}}}
    f7a = check(broken, contract)
    ok7a = any("C7 正向" in x and "RETRY" in x for x in f7a)

    # C7 反向：错误态多出一条未登记出边 → 拦
    extra = {"initial": "idle", "states": {
        "idle": {"on": {"GO": "parsing"}}, "parsing": {"on": {"DONE": "done", "FAIL": "error"}},
        "error": {"on": {"RETRY": "parsing", "SECRET": "idle"}}, "done": {"type": "final"}}}
    f7b = check(extra, contract)
    ok7b = any("C7 反向" in x and "SECRET" in x for x in f7b)

    ok = all([ok1, ok2, ok6, ok_c4, ok7f, ok7a, ok7b])
    print(f"selftest: 合法机放行={ok1} C2/C3/C4拦截={ok2} C6悬空target拦截={ok6} "
          f"结构化错误态C4拦截={ok_c4} C7正向缺边拦截={ok7a} C7反向多边拦截={ok7b} "
          f"契约一致放行={ok7f} → {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("  detail:", {"basic_bad": f, "c6": f6, "c7_forward": f7a, "c7_reverse": f7b})
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--contract", help="契约 JSON（含 recovery / non_error_failures），启用 C7 双向对账")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        print("FAIL: 需要 --file 或 --selftest")
        return 1
    sc = json.loads(Path(a.file).read_text(encoding="utf-8"))
    contract = json.loads(Path(a.contract).read_text(encoding="utf-8")) if a.contract else None
    fails = check(sc, contract)
    if fails:
        print(f"FAIL: {len(fails)} 项结构缺陷：")
        for x in fails:
            print("  ✗", x)
        return 1
    scope = "含 C7 契约对账" if contract else "无契约（C7 未启用）"
    print(f"OK: statechart 结构检查通过（无死端/全可达/错误态有出路/引用完整；{scope}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

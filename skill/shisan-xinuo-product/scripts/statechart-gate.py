#!/usr/bin/env python3
"""statechart-gate · 门禁候选⑩：态+转换结构检查（出路的严格表述）。

检查翻译表源 statechart JSON：
  C1 initial 存在  C2 无死端（非终态全有出边）  C3 全可达（initial 出发 BFS）
  C4 错误态（名含 error/fail）必有恢复转换（出边指向非错误态）
  C5 带守卫的转换须有 guardDesc 说明
用法：python statechart-gate.py --file sc.json
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


def check(sc: dict) -> list[str]:
    fails: list[str] = []
    states: dict = sc.get("states", {})
    initial = sc.get("initial")
    if initial not in states:
        return [f"C1 initial '{initial}' 不在 states"]
    edges: dict[str, list[str]] = {}
    for name, body in states.items():
        out: list[str] = []
        for tr in (body or {}).get("on", {}).values():
            if isinstance(tr, list):
                out += [t for x in tr for t in targets(x)]
            else:
                out += targets(tr)
            for tr_one in ([tr] if not isinstance(tr, list) else tr):
                if isinstance(tr_one, dict) and "guard" in tr_one and not tr_one.get("guardDesc"):
                    fails.append(f"C5 {name} 转换守卫 '{tr_one['guard']}' 缺 guardDesc 说明")
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
    for name, body in states.items():
        if "error" in name or "fail" in name:
            recover = [t for t in edges.get(name, []) if "error" not in t and "fail" not in t]
            if not recover:
                fails.append(f"C4 错误态 '{name}' 无恢复转换（出路）")
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
    print(f"selftest: 合法机放行={ok1} 错误态无出路+不可达被拦={ok2}（{f}）")
    return 0 if ok1 and ok2 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        print("FAIL: 需要 --file 或 --selftest")
        return 1
    sc = json.loads(Path(a.file).read_text(encoding="utf-8"))
    fails = check(sc)
    if fails:
        print(f"FAIL: {len(fails)} 项结构缺陷：")
        for x in fails:
            print("  ✗", x)
        return 1
    print("OK: statechart 结构检查通过（无死端/全可达/错误态有出路）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

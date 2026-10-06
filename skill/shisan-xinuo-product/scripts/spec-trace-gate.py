#!/usr/bin/env python3
"""spec-trace-gate v1 · 三方绑定追溯（组件级粒度，双向追溯的机器可查子集）。

绑定清单 JSON schema（每一行=一个独立组件实例的绑定，粒度=组件不是功能）：
{
  "bindings": [
    {"page": "ImportPage", "component": "ProgressConsole",
     "feature": "导入-解析进度", "backend": "POST /imports/parse",
     "evidence": "shot-01.png"}
  ]
}
纯展示组件 backend 允许显式写 "NONE(纯展示)"。

检查：
  T1 每行五段（page/component/feature/backend/evidence）齐全
  T2 evidence 禁占位语（无/未验证/TODO/待补）——无真渲染证据不得声称已验证
  T3 完全相同的四元组（page/component/feature/backend）重复 → 冗余行
  T4 UI 孤儿：--components <文件列表> 代码中存在但清单未登记的组件 → 发明/漏登记
  T5 死逻辑：--backends <文件列表> 后端逻辑块存在但无任何组件消费 → classifyNotice 式死代码
  T6 幽灵端点：绑定行 backend 形似 HTTP 端点（动词+路径 / URL）但不在 --backends 实际清单 → 引用不存在的后端
    （jz-02 试金石回流：绑定 GET /api/stats 而后端无此块，T4/T5 双向都查不到；localStorage 等客户端存储非 URL 形，不拦）

用法：python spec-trace-gate.py --file bindings.json [--components list.txt] [--backends list.txt]
      python spec-trace-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BAD = re.compile(r"^\s*(无|未验证|TODO|待补|暂无|-|NONE)$", re.I)
PURE_DISPLAY = re.compile(r"^NONE\(.+\)$")
# URL 形：HTTP 动词+路径（GET /x）或含 scheme（https://）或以 / 开头——localStorage/IndexedDB 等客户端存储不匹配
URLISH = re.compile(r"^(?:[A-Z]{3,8}\s+\S+|.+:\/\/|\/)")


def _norm(s: str) -> str:
    """路径参数段归一化：`{任意名}` → `{}`——bindings 手写 `{id}` 与后端声明 `{appt_id}` 语义同端点，
    严格串比对会把同一端点同时报成 T5 死逻辑+T6 幽灵（jz-03 试金石回流）。"""
    return re.sub(r"\{[^}/]*\}", "{}", s)


def check(bindings: list[dict], comp_list: set[str] | None, backend_list: set[str] | None) -> list[str]:
    fails: list[str] = []
    if not bindings:
        return ["T1 绑定清单为空"]
    seen_quads: set[tuple] = set()
    used_components: set[str] = set()
    used_backends: set[str] = set()
    defect_rows: list[tuple[str, str]] = []  # T1 缺段行 (component, backend)——未计入消费集，其孤儿/死逻辑为连带暴露
    for i, b in enumerate(bindings, 1):
        page, comp = b.get("page", ""), b.get("component", "")
        feat, be, ev = b.get("feature", ""), b.get("backend", ""), b.get("evidence", "")
        if not (page and comp and feat and be and ev):
            fails.append(f"T1 第{i}行五段不齐：{page}/{comp}/{feat}/{be}/{ev or '(空)'}")
            defect_rows.append((comp, be))
            continue
        if BAD.match(ev):
            fails.append(f"T2 第{i}行 evidence 占位语（{ev}）——无真渲染证据不得声称已验证")
        if not PURE_DISPLAY.match(be) and BAD.match(be):
            fails.append(f"T1 第{i}行 backend 空且非纯展示声明：{comp}")
        quad = (page, comp, feat, be)
        if quad in seen_quads:
            fails.append(f"T3 冗余绑定行：{quad}")
        seen_quads.add(quad)
        used_components.add(comp)
        if not PURE_DISPLAY.match(be):
            used_backends.add(be)
    if comp_list:
        for ghost in sorted(comp_list - used_components):
            tag = next((f"（连带：T1 缺段行 '{c}' 未计入消费集，本条由缺段连带暴露）"
                        for c, _ in defect_rows if c == ghost), "")
            fails.append(f"T4 UI 孤儿：组件 '{ghost}' 存在于代码但未登记任何功能绑定{tag}")
    # 注意判空语义：None=未提供 --backends（检查不适用）；空 set=提供了但实际零后端——
    # 空清单恰是幽灵端点最典型场景（纯前端夹具引用了不存在的 API），不得被 falsy 吞掉（jz-02 实测抓到本 bug）
    if backend_list is not None:
        norm_list = {_norm(x) for x in backend_list}
        norm_used = {_norm(x) for x in used_backends}
        for dead in sorted(norm_list - norm_used):
            tag = next((f"（连带：T1 缺段行 backend '{_norm(b)}' 未计入消费集，本条由缺段连带暴露）"
                        for c, b in defect_rows if not PURE_DISPLAY.match(b) and _norm(b) == dead), "")
            fails.append(f"T5 死逻辑：后端块 '{dead}' 无任何组件消费（classifyNotice 式）{tag}")
        # T6 幽灵端点（jz-02 回流）：URL 形 backend 必须命中实际后端清单（路径参数段归一化后比对，jz-03）——
        # 双向对账的另一半：T5 查「有块没人用」，T6 查「有行没块」
        for b in bindings:
            be = b.get("backend", "")
            if PURE_DISPLAY.match(be) or not URLISH.match(be):
                continue
            if _norm(be) not in norm_list:
                fails.append(f"T6 幽灵端点：'{b.get('component', '?')}' 绑定 backend '{be}' 不在实际后端清单（引用不存在的端点/拼错/未实现）")
    return fails


def selftest() -> int:
    good = {"bindings": [
        {"page": "P", "component": "C1", "feature": "F1", "backend": "POST /a", "evidence": "s.png"},
        {"page": "P", "component": "C2", "feature": "F2", "backend": "NONE(纯展示)", "evidence": "s2.png"}]}
    bad = {"bindings": [
        {"page": "P", "component": "C1", "feature": "F1", "backend": "POST /a", "evidence": "TODO"},
        {"page": "P", "component": "C1", "feature": "F1", "backend": "POST /a", "evidence": "TODO"}]}
    ok1 = check(good["bindings"], {"C1", "C2"}, {"POST /a"}) == []
    f = check(bad["bindings"], {"C1", "C9"}, {"/a", "/dead"})
    ok2 = any("T2" in x for x in f) and any("T3" in x for x in f) and any("T4" in x for x in f) and any("T5" in x for x in f)
    # F2 回归（2026-09-24）：多词 backend id 走「文件→清单→比对」全路径不得假阳/漏检
    import os
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as tf:
        tf.write("POST /imports/parse\n\nGET /unused\n")
        tmp = tf.name
    try:
        loaded = _load_list(tmp)
    finally:
        os.unlink(tmp)
    ok3 = loaded == {"POST /imports/parse", "GET /unused"}
    f3 = check([{"page": "P", "component": "C1", "feature": "F1",
                 "backend": "POST /imports/parse", "evidence": "s.png"}], None, loaded)
    ok4 = len(f3) == 1 and "T5" in f3[0] and "GET /unused" in f3[0]
    # T6 反向变异（jz-02 回流，#407）：幽灵端点必拦 + localStorage 非URL形不拦
    ghost = [{"page": "P", "component": "C1", "feature": "F1", "backend": "GET /api/stats", "evidence": "s.png"},
             {"page": "P", "component": "C2", "feature": "F2", "backend": "localStorage", "evidence": "s2.png"}]
    f5 = check(ghost, None, {"GET /real"})
    ok5 = any("T6" in x and "/api/stats" in x for x in f5) and not any("localStorage" in x and "T6" in x for x in f5)
    # T6 空清单变异：--backends 给了但文件为空（纯前端）——URL 形绑定此时全是幽灵，不得被 falsy 吞掉
    f6 = check(ghost[:1], None, set())
    ok6 = any("T6" in x for x in f6)
    # 参数段归一化变异（jz-03 回流）：{id} vs {appt_id} 语义同端点——T5/T6 都不得报；真删端点仍拦
    param = [{"page": "P", "component": "C1", "feature": "F1", "backend": "DELETE /appointments/{id}", "evidence": "s.png"}]
    f7 = check(param, None, {"DELETE /appointments/{appt_id}", "GET /x"})
    ok7 = not any(("T5" in x or "T6" in x) and "appointments" in x for x in f7)
    gone = check(param, None, {"GET /x"})
    ok8 = any(("T5" in x or "T6" in x) for x in gone)
    # T1 连带标注正反四面（jz-06 E1 回流，#407）：缺段行的组件/后端在 T4/T5 报文中带「连带」标注；
    # 无缺段来源的孤儿/死逻辑（C9、GET /dead）不得误标
    linked = [{"page": "P", "component": "C1", "feature": "F1", "backend": "POST /a", "evidence": ""}]
    f9 = check(linked, {"C1", "C9"}, {"POST /a", "GET /dead"})
    t4_c1 = next((x for x in f9 if "T4" in x and "'C1'" in x), "")
    t4_c9 = next((x for x in f9 if "T4" in x and "'C9'" in x), "")
    t5_a = next((x for x in f9 if "T5" in x and "POST /a" in x), "")
    t5_dead = next((x for x in f9 if "T5" in x and "GET /dead" in x), "")
    ok9 = ("连带" in t4_c1 and t4_c9 and "连带" not in t4_c9
           and "连带" in t5_a and t5_dead and "连带" not in t5_dead)
    print(f"selftest: 合法绑定放行={ok1} 占位/冗余/UI孤儿/死逻辑全拦={ok2}（{len(f)} 项） 多词backend整串加载={ok3} 死逻辑只报真死={ok4} 幽灵端点拦/客户端存储豁免={ok5} 空清单仍拦幽灵={ok6} 参数名归一化放行={ok7} 端点真消失仍拦={ok8} T1缺段连带标注四面={ok9}（{len(f9)} 项）")
    return 0 if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8 and ok9 else 1


def _load_list(path: str) -> set[str]:
    # F2（2026-09-24）：清单文件语义=每行一个条目，必须整串加载——
    # 曾按 .split() 全文切块，多词 backend id（如 "GET /favorites"）被切碎，
    # 与绑定字段整串比对不对称 → 合法清单必假阳 T5。
    return {ln.strip() for ln in Path(path).read_text(encoding="utf-8").splitlines() if ln.strip()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--components", help="代码中组件清单文件（每行一个），供 T4 UI 孤儿检查")
    ap.add_argument("--backends", help="后端逻辑块清单文件（每行一个），供 T5 死逻辑检查")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        print("FAIL: 需要 --file 或 --selftest")
        return 1
    bindings = json.loads(Path(a.file).read_text(encoding="utf-8")).get("bindings", [])
    comp_list = _load_list(a.components) if a.components else None
    backend_list = _load_list(a.backends) if a.backends else None
    fails = check(bindings, comp_list, backend_list)
    if fails:
        print(f"FAIL: {len(fails)} 项追溯缺陷：")
        for x in fails:
            print("  ✗", x)
        return 1
    print(f"OK: 三方绑定清单通过（{len(bindings)} 行，组件级粒度/无孤儿/无死逻辑）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

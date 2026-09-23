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


def check(bindings: list[dict], comp_list: set[str] | None, backend_list: set[str] | None) -> list[str]:
    fails: list[str] = []
    if not bindings:
        return ["T1 绑定清单为空"]
    seen_quads: set[tuple] = set()
    used_components: set[str] = set()
    used_backends: set[str] = set()
    for i, b in enumerate(bindings, 1):
        page, comp = b.get("page", ""), b.get("component", "")
        feat, be, ev = b.get("feature", ""), b.get("backend", ""), b.get("evidence", "")
        if not (page and comp and feat and be and ev):
            fails.append(f"T1 第{i}行五段不齐：{page}/{comp}/{feat}/{be}/{ev or '(空)'}")
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
            fails.append(f"T4 UI 孤儿：组件 '{ghost}' 存在于代码但未登记任何功能绑定")
    if backend_list:
        for dead in sorted(backend_list - used_backends):
            fails.append(f"T5 死逻辑：后端块 '{dead}' 无任何组件消费（classifyNotice 式）")
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
    print(f"selftest: 合法绑定放行={ok1} 占位/冗余/UI孤儿/死逻辑全拦={ok2}（{len(f)} 项） 多词backend整串加载={ok3} 死逻辑只报真死={ok4}")
    return 0 if ok1 and ok2 and ok3 and ok4 else 1


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

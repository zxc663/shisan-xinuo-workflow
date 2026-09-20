#!/usr/bin/env python3
"""spec-trace-gate · 联通行清单检查（双向追溯的机器可查子集）。

输入联通行清单（md 表格或 JSON 数组），每行必须三段齐全：
  功能（语义行）｜交互（元素/承诺）｜证据（截图/DOM/statechart 路径）
检查：T1 三段齐全非空  T2 证据段禁「无/未验证/TODO/待补」  T3 功能 id 不重复。
用法：python spec-trace-gate.py --file trace.md（或 .json）
      python spec-trace-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BAD_EVIDENCE = re.compile(r"^\s*(无|未验证|TODO|待补|暂无|-)\s*$", re.I)


def rows_from(md_text: str) -> list[dict]:
    rows = []
    for line in md_text.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[0] not in ("功能", "feature", ""):
            rows.append({"feature": cells[0], "interaction": cells[1], "evidence": cells[2]})
    return rows


def check(rows: list[dict]) -> list[str]:
    fails: list[str] = []
    seen: set[str] = set()
    if not rows:
        return ["T1 清单为空——没有联通行"]
    for i, r in enumerate(rows, 1):
        fid, act, ev = r.get("feature", ""), r.get("interaction", ""), r.get("evidence", "")
        if not fid or not act or not ev or BAD_EVIDENCE.match(ev):
            fails.append(f"T1 第{i}行三段不齐/证据缺失：{fid or '(空功能)'}")
        if BAD_EVIDENCE.match(ev):
            fails.append(f"T2 第{i}行证据段为占位语（{ev}）——无真渲染证据不得声称已验证")
        if fid and fid in seen:
            fails.append(f"T3 功能行重复：{fid}")
        seen.add(fid)
    return fails


def selftest() -> int:
    good_md = "| 功能 | 交互 | 证据 |\n|---|---|---|\n| 导入-解析 | 进度条 1s 内出现 | shot-01.png |\n"
    bad_md = "| 功能 | 交互 | 证据 |\n|---|---|---|\n| 导入-解析 | 进度条 | TODO |\n| 导入-解析 | x | y |\n"
    ok1 = check(rows_from(good_md)) == []
    f = check(rows_from(bad_md))
    ok2 = any("T2" in x for x in f) and any("T3" in x for x in f)
    print(f"selftest: 合法清单放行={ok1} 占位证据+重复功能被拦={ok2}（{f}）")
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
    text = Path(a.file).read_text(encoding="utf-8")
    rows = rows_from(text)
    if a.file.endswith(".json"):
        rows = json.loads(text)
    fails = check(rows)
    if fails:
        print(f"FAIL: {len(fails)} 项追溯缺陷：")
        for x in fails:
            print("  ✗", x)
        return 1
    print(f"OK: 联通行清单通过（{len(rows)} 行，三段齐全/证据真实/功能唯一）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

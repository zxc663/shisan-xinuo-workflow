#!/usr/bin/env python3
"""usage_probe.py · 细则使用度统计与退役候选清单生成（G4/T8，2026-09-29）。

数据源两路：
  1. usage 日志（~/.zcode/cli/detail-lookup-usage.jsonl）——detail_lookup 每次检索落一行
     （命中 ids / 空数组=零命中），自 2026-09-29 起持续累积；
  2. --seed 工件——从既有文档提取 #N 提及作历史观测并集（提及≠检索命中，分开计数）。

输出：退役候选清单 md（默认 docs/retirement-candidates-<日期>.md）——
  候选 = 全集 − 检索命中 − 工件提及。**只列候选不删条**（G4 边界：退役改口径连锁
  注入五副本 count 校验，须随发行批走）。

用法：
  python scripts/usage_probe.py                          # 默认种子=eval-detail+scorecards
  python scripts/usage_probe.py --seed <文件> ... --out <路径>
诚实边界：观测窗口内零命中≠无用（低频但保命条款会被误列）——候选升退役须人工复核+双批确认。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DETAILS = REPO / "skill" / "shisan-xinuo-workflow" / "references" / "details.md"
USAGE = Path.home() / ".zcode" / "cli" / "detail-lookup-usage.jsonl"
ENTRY = re.compile(r"^(\d{1,3})\. (.*)", re.M)
SKIP_MARKS = ("〔预留槽〕", "〔归档〕")  # 与 facts_sync 单源口径一致：预留/归档不入全集


def universe_and_titles() -> dict[int, tuple[str, str]]:
    out = {}
    for m in ENTRY.finditer(DETAILS.read_text(encoding="utf-8")):
        line = m.group(2).strip()
        if any(k in line for k in SKIP_MARKS):
            continue
        dm = re.match(r"\[([^\]]+)\] \*\*(.+?)\*\*", line)
        if dm:
            out[int(m.group(1))] = (dm.group(1), dm.group(2))
        else:
            out[int(m.group(1))] = ("未标域", line)
    return out


def load_hits(usage: Path) -> dict[int, int]:
    hits: dict[int, int] = {}
    if not usage.exists():
        return hits
    for line in usage.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except Exception:
            continue
        for i in rec.get("ids", []):
            hits[int(i)] = hits.get(int(i), 0) + 1
    return hits


def load_mentions(seeds: list[str]) -> dict[int, int]:
    men: dict[int, int] = {}
    for s in seeds:
        p = Path(s)
        if not p.exists():
            print(f"[warn] 种件不存在跳过: {p}")
            continue
        target = p if p.is_file() else None
        files = [target] if target else sorted(p.rglob("*.jsonl"))
        for f in files:
            for m in re.finditer(r"#(\d{1,4})\b", f.read_text(encoding="utf-8", errors="ignore")):
                i = int(m.group(1))
                if i:
                    men[i] = men.get(i, 0) + 1
    return men


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--usage", default=str(USAGE))
    ap.add_argument("--seed", action="append", default=[],
                    help="历史观测种件（文件或含 *.jsonl 目录）；默认 eval-detail+scorecards")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    seeds = a.seed or [str(REPO / "docs" / "eval-detail-lookup-20260928.md"),
                       str(REPO / "docs" / "roadtest-scorecards")]

    uni = universe_and_titles()
    hits = load_hits(Path(a.usage))
    men = load_mentions(seeds)
    observed = set(hits) | set(men)
    cands = sorted(set(uni) - observed)

    by_dom: dict[str, list[int]] = {}
    for i in cands:
        by_dom.setdefault(uni[i][0], []).append(i)

    out = Path(a.out) if a.out else REPO / "docs" / f"retirement-candidates-{date.today().strftime('%Y%m%d')}.md"
    lines = [
        "# 细则退役候选清单（G4/T8 · 机器生成）",
        "",
        f"> 生成：{date.today().isoformat()}｜全集 {len(uni)} 条（details.md 实解析）｜"
        f"检索命中 {len(set(hits) & set(uni))} 条｜工件提及 {len(set(men) & set(uni))} 条｜"
        f"**候选 {len(cands)} 条**。",
        "> 口径：候选 = 全集 − usage 日志命中 − 种件 #N 提及（usage 自 2026-09-29 起累积，当前窗口尚浅）。",
        "> 边界：**只列候选不删条**；升退役须人工复核+双批零观测确认（低频保命条款误列风险自担）。",
        "",
    ]
    for dom, ids in sorted(by_dom.items(), key=lambda x: -len(x[1])):
        lines.append(f"## [{dom}]（{len(ids)} 条）")
        lines.append("")
        for i in ids:
            lines.append(f"- details #{i}：{uni[i][1][:60]}")
        lines.append("")
    obs_lines = sorted(set(hits) & set(uni))
    if obs_lines:
        lines.append("## 观测命中样本（usage 日志）")
        lines.append("")
        for i in obs_lines[:30]:
            lines.append(f"- details #{i} ×{hits[i]}（{uni[i][1][:50]}）")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK: 候选 {len(cands)}/{len(uni)} 条 → {out}")
    print(f"     检索命中 {len(set(hits) & set(uni))}｜工件提及 {len(set(men) & set(uni))}（种子 {len(seeds)} 件）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

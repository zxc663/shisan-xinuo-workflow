#!/usr/bin/env python3
"""usage-probe · 使用率监控 v0（衰减链对策：装了没人触发=白装，且没人会知道）。

扫描指定 agent-log 文件（或目录），统计第四包被「提及/引用」的痕迹计数与最近时间。
诚实边界 v0：统计的是文本提及不是平台级真实触发——真实触发监控 v1 需平台 hooks 通道。
用法：python usage-probe.py --logs <log文件或目录> [--days 7]
      python usage-probe.py --selftest
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

HINTS = ["shisan-xinuo-product", "product 包", "product包", "联通层", "六问", "statechart-gate", "registry-gate", "spec-trace"]
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def scan(paths: list[Path], days: int) -> dict:
    cutoff = datetime.now() - timedelta(days=days)
    hits: list[datetime] = []
    per_file: dict[str, int] = {}
    for f in paths:
        if f.is_dir():
            paths.extend(sorted(f.rglob("*.md")))
            continue
        if not f.is_file():
            continue
        n = 0
        for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            if any(h in line for h in HINTS):
                n += 1
                m = DATE_RE.search(line)
                if m:
                    try:
                        d = datetime.strptime(m.group(1), "%Y-%m-%d")
                        if d >= cutoff:
                            hits.append(d)
                    except ValueError:
                        pass
        if n:
            per_file[str(f)] = n
    return {"total_mentions": sum(per_file.values()), "recent_hits": len(hits),
            "files": per_file, "last_hit": max(hits).strftime("%Y-%m-%d") if hits else "—"}


def selftest() -> int:
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        log = Path(d) / "agent-log.md"
        log.write_text("### 2026-09-21｜某轮：联通层六问用了\n普通行\n### 2026-09-10｜statechart-gate 跑了\n", encoding="utf-8")
        r = scan([log], days=30)
        ok = r["total_mentions"] == 2 and r["recent_hits"] >= 1 and r["last_hit"] == "2026-09-21"
        print(f"selftest: 提及计数+近期命中+最新时间={ok}（{r}）")
        return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--logs", nargs="*")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.logs:
        print("FAIL: 需要 --logs 或 --selftest")
        return 1
    paths: list[Path] = [Path(p) for p in a.logs]
    r = scan(paths, a.days)
    print(f"使用率报告（近 {a.days} 天）：提及 {r['total_mentions']} 次 / 窗口内命中 {r['recent_hits']} 次 / 最近 {r['last_hit']}")
    for k, v in sorted(r["files"].items(), key=lambda x: -x[1])[:8]:
        print(f"  {v:4d}  {k}")
    if r["recent_hits"] == 0:
        print("⚠ 窗口内零命中——第四包在衰减（衰减链第 1 级），检查钩子/部署")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

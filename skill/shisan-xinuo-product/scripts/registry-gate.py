#!/usr/bin/env python3
"""registry-gate · 门禁④：组件归因检查（检查「查没查、归因没归因」，不定义组件）。

规则：组件目录下的组件文件必须携带 registry 归因标记——
  `registry: <名> source=<上游库@版本>` 或 `registry: <名> 自研归因=<为什么上游无解>`
缺失 → 列出文件 → 退出码 1（补归因后重跑）。
用法：python registry-gate.py --path <组件目录> [--ext .vue,.tsx,.jsx]
      python registry-gate.py --selftest   （内置两态自测）
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

MARK = "registry:"
DEFAULT_EXTS = [".vue", ".tsx", ".jsx"]


def scan(path: Path, exts: list[str]) -> list[str]:
    missing: list[str] = []
    for f in sorted(path.rglob("*")):
        if f.suffix not in exts or not f.is_file():
            continue
        if MARK not in f.read_text(encoding="utf-8", errors="ignore"):
            missing.append(str(f))
    return missing


def selftest() -> int:
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "Good.vue").write_text("<!-- registry: Good source=shadcn@4 -->\n<template/>", encoding="utf-8")
        (root / "Bad.tsx").write_text("export default () => <div/>", encoding="utf-8")
        missing = scan(root, DEFAULT_EXTS)
        ok1 = missing == [str(root / "Bad.tsx")]
        (root / "Bad.tsx").write_text("// registry: Bad 自研归因=上游无此组合组件\nexport default () => <div/>", encoding="utf-8")
        ok2 = scan(root, DEFAULT_EXTS) == []
        print(f"selftest: 缺归因被拦={ok1} 补归因放行={ok2}")
        return 0 if ok1 and ok2 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default="src")
    ap.add_argument("--ext", default=",".join(DEFAULT_EXTS))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    path = Path(a.path)
    if not path.exists():
        print(f"FAIL: 路径不存在 {path}")
        return 1
    missing = scan(path, [e.strip() for e in a.ext.split(",")])
    if missing:
        print(f"FAIL: {len(missing)} 个组件文件缺 registry 归因标记（{MARK} source=…/自研归因=…）：")
        for m in missing:
            print("  ✗", m)
        return 1
    print(f"OK: 归因检查通过（{path}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

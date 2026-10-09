#!/usr/bin/env python3
"""experiment-metrics · 对照实验度量（终极命题四维度量化 v0）。

用法：python experiment-metrics.py --repo <工作区路径> --label <甲用Skill/乙不用>
输出：文件数/LOC/内联样式/硬编码色/TODO/空catch/console.log/工具入口数 + 维护债评分。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

CODE_EXTS = {".html", ".css", ".js", ".ts", ".jsx", ".tsx", ".vue"}


def count(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.I))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--label", required=True)
    a = ap.parse_args()
    repo = Path(a.repo)
    files = [f for f in repo.rglob("*") if f.suffix in CODE_EXTS and "node_modules" not in str(f)]
    # 令牌/变量定义文件（tokens/variables/主题定义）中的 hex=合法单源，不计债
    TOKEN_DEF = re.compile(r"(tokens?|variables?|theme)\.(css|js|ts)$|:root|--[a-z-]+\s*:", re.I)
    loc = styles = hexes = todos = empty_catch = logs = 0
    hex_total = hex_token = 0
    for f in files:
        try:
            t = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        loc += t.count("\n") + 1
        styles += count(t, r"style\s*=\s*\"")
        h = count(t, r"#[0-9a-f]{6}\b")
        hex_total += h
        if f.suffix == ".css" and ("token" in f.name.lower() or "variable" in f.name.lower() or ":root" in t):
            hex_token += h
        else:
            hexes += h
        todos += count(t, r"\bTODO\b")
        empty_catch += count(t, r"catch\s*\([^)]*\)\s*\{\s*\}")
        logs += count(t, r"console\.log")
    tool_like = 0
    for f in files:
        try:
            tool_like += count(f.read_text(encoding="utf-8", errors="ignore"), r"(格式化|转换|生成|编码|解码|预览|测试|工具)")
        except Exception:
            pass
    debt = styles + hexes + todos + empty_catch * 5 + logs
    print(f"[{a.label}] 文件={len(files)} LOC={loc} 内联样式={styles} 硬编码色={hexes}(另令牌定义{hex_token - hexes if hex_token > hexes else hex_token}处合法单源,总hex={hex_total}) TODO={todos} 空catch={empty_catch} console.log={logs} 工具词频={tool_like}")
    print(f"[{a.label}] 维护债评分={debt}（内联+使用处色+TODO+5×空catch+log）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

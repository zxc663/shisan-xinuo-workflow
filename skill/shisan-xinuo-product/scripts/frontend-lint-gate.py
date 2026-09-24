#!/usr/bin/env python3
"""frontend-lint-gate v1 · §4 强制 5/6 的机器子集（内联样式/硬编码色/console/空 catch）。

背景：§4 强制清单第 5（内联样式/硬编码零容忍）与第 6（dead-binding：死代码/空 catch）
列为「可机器判定」却一直无专属脚本（verification-ledger 🔴 行，2026-09-24 战役补）。
模式对齐 registry-gate：**基线豁免存量、只拦新增**——防「正确但昂贵」杀死采用（§7 同源哲学）。

检查（组件文件，非 <style> 块）：
  R1 内联样式：style=" / :style=" / style={{
  R2 硬编码色：十六进制色 #fff…（3-8 位）与 rgb(/rgba( 字面量（css 文件与 <style> 块合法，不扫；
    <meta> 行的 content 色值=元数据豁免——2026-09-25 F10 补）
  R3 console.*：console.log/debug/info/warn/error（交付五查：错误须入日志模块，零容忍）
  R4 空 catch：catch (…) { } 无任何语句（吞错误=dead-binding 家族）

基线语义：--write-baseline 把当前全部违例记为存量豁免；此后新增违例 exit 1，存量不再报。
诚实边界 v1：正则级检测——内联样式的「合理豁免」（如动态定位）请走基线或账本，不做语义判断。

用法：
  python frontend-lint-gate.py --path <组件目录> [--ext .vue,.tsx,.jsx] [--baseline f] [--write-baseline]
  python frontend-lint-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

COMPONENT_EXCLUDE = re.compile(r"(test|spec|story|stories|\.d\.ts|node_modules|\.next|dist|build)")
STYLE_BLOCK = re.compile(r"<style[\s>].*?</style>", re.S)
R1 = re.compile(r"style=\"|:style=\"|style=\{\{")
R2 = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\(")
R3 = re.compile(r"console\.(log|debug|info|warn|error)\b")
R4 = re.compile(r"catch\s*\([^)]*\)\s*\{\s*\}")
RULES = {"R1": R1, "R2": R2, "R3": R3, "R4": R4}

RULE_NAMES = {
    "R1": "内联样式（§4-5）",
    "R2": "硬编码色（§4-5，组件区不放色值——色归 token/style 块）",
    "R3": "console 调试残留（交付五查）",
    "R4": "空 catch 吞错（§4-6 dead-binding）",
}


def strip_style_blocks(text: str) -> str:
    return STYLE_BLOCK.sub("", text)


def scan_file(p: Path, rules: dict[str, re.Pattern]) -> list[str]:
    try:
        raw = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    # R2 的 css 豁免按 docstring 落地：色值归属 css 文件/<style> 块（F10，2026-09-25 实测补——
    # 此前仅 <style> 块被 strip，.css 文件本体显式传入 --ext 时色值被误报为组件区硬编码）
    active = {k: v for k, v in rules.items() if not (p.suffix == ".css" and k == "R2")}
    text = strip_style_blocks(raw)
    out: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        for rid, rx in active.items():
            # R2 的 meta 豁免：theme-color 等 content 色值是页面元数据非组件样式（F10 族，2026-09-25）
            if rid == "R2" and line.lstrip().startswith("<meta"):
                continue
            if rx.search(line):
                out.append(f"{p.as_posix()}:{i} [{rid}] {RULE_NAMES[rid]}：{line.strip()[:80]}")
    return out


def collect(path: Path, exts: list[str]) -> list[Path]:
    if path.is_file():
        return [path]
    return [p for p in sorted(path.rglob("*"))
            if p.is_file() and p.suffix in exts and not COMPONENT_EXCLUDE.search(str(p))]


def selftest() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        bad = t / "Bad.vue"
        bad.write_text(
            '<template><div style="color: #ff0000">x</div></template>\n'
            "<script>try {} catch (e) {}</script>\n",
            encoding="utf-8")
        good = t / "Good.tsx"
        good.write_text('export const A = () => <div className="c">x</div>;\n', encoding="utf-8")
        styleblock = t / "S.vue"
        styleblock.write_text("<style>.a { color: #ff0000; }</style>", encoding="utf-8")
        v = scan_file(bad, RULES)
        ok1 = any("[R1]" in x for x in v) and any("[R2]" in x for x in v) and any("[R4]" in x for x in v)
        ok2 = scan_file(good, RULES) == []
        text_s = strip_style_blocks(styleblock.read_text(encoding="utf-8"))
        ok3 = "#ff0000" not in text_s and scan_file(styleblock, RULES) == []
        cssfile = t / "tokens.css"
        cssfile.write_text(":root { --accent: #4a7297; }", encoding="utf-8")
        ok4 = scan_file(cssfile, RULES) == []  # F10 回归：css 文件本体色值=R2 豁免
        metafile = t / "meta.html"
        metafile.write_text('<html lang="zh-CN">\n<head>\n<meta name="theme-color" content="#eef1f5">\n</head>\n</html>', encoding="utf-8")
        ok5 = scan_file(metafile, RULES) == []  # F10 回归：meta 独立行 content 色值=元数据豁免
        print(f"selftest: 违例三连(R1/R2/R4)={ok1} 干净文件放行={ok2} style 块色值合法={ok3} "
              f"css 文件色值豁免={ok4} meta 色值豁免={ok5}")
        return 0 if ok1 and ok2 and ok3 and ok4 and ok5 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", help="组件目录或单文件")
    ap.add_argument("--ext", default=".vue,.tsx,.jsx")
    ap.add_argument("--baseline", help="基线 JSON（存量豁免）；缺省时自动找 <path>/.lint-baseline.json")
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.path:
        print("FAIL: 需要 --path 或 --selftest")
        return 1
    path = Path(a.path)
    files = collect(path, [e.strip() for e in a.ext.split(",")])
    violations: list[str] = []
    for f in files:
        violations += scan_file(f, RULES)
    if a.write_baseline:
        bl = path / ".lint-baseline.json" if path.is_dir() else path.parent / ".lint-baseline.json"
        bl.write_text(json.dumps({"violations": violations}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"基线已写入 {bl}（存量 {len(violations)} 条豁免）")
        return 0
    bl_path = Path(a.baseline) if a.baseline else (path / ".lint-baseline.json" if path.is_dir() else None)
    base_set = set()
    if bl_path and Path(bl_path).exists():
        base_set = set(json.loads(Path(bl_path).read_text(encoding="utf-8")).get("violations", []))
    fresh = [v for v in violations if v not in base_set]
    if fresh:
        print(f"FAIL: {len(fresh)} 项新增前端 lint 违例（存量 {len(violations) - len(fresh)} 条已由基线豁免）：")
        for x in fresh[:20]:
            print("  ✗", x)
        return 1
    print(f"OK: 前端 lint 通过（扫描 {len(files)} 文件；存量 {len(violations)} 条基线豁免）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""a11y-gate v1 · §4 强制清单第 9 条「可达性静态底线（axe 子集）」的机器子集。

背景：B9 是 verification-ledger 唯一残留 🔴（axe 启发式误报风险高，诚实保留待做，2026-09-24）。
本 gate = 低误报四格静态子集（2026-09-25 夜战 E4 补），不替代 axe-core 完整审计。
模式对齐 frontend-lint-gate：**基线豁免存量、只拦新增**——防「正确但昂贵」杀死采用。

检查（.html/.vue/.tsx/.jsx）：
  A1 img 无 alt：<img> 标签内无 alt 属性（alt="" 装饰图合法）
  A2 表单控件无可访问名：<input|select|textarea> 无 aria-label/aria-labelledby、
     无 label 引用（for=/htmlFor= 字面量对账）、非 <label> 包裹、且非 hidden/submit/button/reset
  A3 交互元素无可访问名：<button> 或带 href 的 <a>，内容去子标签后为空
     且无 aria-label/aria-labelledby/title（图标按钮无可访问名=高频真缺陷）
  A4 html 无 lang：<html> 标签内无 lang 属性（仅 .html 文件）

诚实边界 v1：正则级检测——不查对比度/焦点顺序/键盘陷阱/ARIA 语义正确性/tabindex 值；
JSX 表达式子内容（{expr}）视为可能有内容（保守放行，防误报优先，与 frontend-lint 同口径）。

用法：
  python a11y-gate.py --path <目录或单文件> [--ext .html,.vue,.tsx,.jsx] [--baseline f] [--write-baseline]
  python a11y-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

COMPONENT_EXCLUDE = re.compile(r"(test|spec|story|stories|\.d\.ts|node_modules|\.next|dist|build)")
TAG_IMG = re.compile(r"<img\b[^>]*>")
TAG_FIELD = re.compile(r"<(input|select|textarea)\b[^>]*?>")
TAG_FLOW = re.compile(r"<(label|input|select|textarea)\b[^>]*?>|</label>")
TAG_CLICKABLE = re.compile(r"<(button|a)\b[^>]*?>(.*?)</\1>", re.S)
TAG_HTML = re.compile(r"<html\b[^>]*>")
ATTR = re.compile(r"""([\w-]+)\s*=\s*["']([^"']*)["']""")

FREE_TYPES = {"hidden", "submit", "button", "reset"}
NAME_ATTRS = ("aria-label", "aria-labelledby")


def attrs_of(open_tag: str) -> dict[str, str]:
    return {m.group(1).lower(): m.group(2) for m in ATTR.finditer(open_tag)}


def has_any(attrs: dict[str, str], names: tuple[str, ...]) -> bool:
    return any(n in attrs for n in names)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def scan_file(p: Path) -> list[str]:
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    out: list[str] = []
    rel = p.as_posix()

    for m in TAG_IMG.finditer(text):
        if "alt" not in attrs_of(m.group(0)):
            out.append((line_of(text, m.start()), "A1", "img 无 alt", m.group(0)[:60]))

    # A2：label-for 集合 + 标签流扫描（包裹豁免）
    label_for = {a["for"] for a in map(attrs_of, re.findall(r"<label\b[^>]*>", text)) if a.get("for")}
    label_for |= {a["htmlfor"] for a in map(attrs_of, re.findall(r"<label\b[^>]*>", text)) if a.get("htmlfor")}
    depth = 0
    for m in TAG_FLOW.finditer(text):
        tag = m.group(0)
        if tag.startswith("</label"):
            depth = max(0, depth - 1)
            continue
        if tag.startswith("<label"):
            depth += 1
            continue
        attrs = attrs_of(tag)
        ok = (
            has_any(attrs, NAME_ATTRS)
            or attrs.get("type", "").lower() in FREE_TYPES
            or (attrs.get("id") in label_for if attrs.get("id") else False)
            or depth > 0
        )
        if not ok:
            out.append((line_of(text, m.start()), "A2",
                        f"{tag[1:tag.find(' ')] if ' ' in tag else tag[1:-1]} 无可访问名（无 label/aria/包裹）", tag[:60]))

    for m in TAG_CLICKABLE.finditer(text):
        open_tag, inner = m.group(0).split(">", 1)[0] + ">", m.group(2)
        attrs = attrs_of(open_tag)
        if open_tag.startswith("<a") and "href" not in attrs:
            continue
        if has_any(attrs, NAME_ATTRS) or "title" in attrs:
            continue
        if re.sub(r"<[^>]*>", "", inner).strip():
            continue
        if re.search(r"\{[^}]*\}", inner):  # JSX 表达式子内容：保守放行
            continue
        name = open_tag[1:open_tag.find(" ")] if " " in open_tag else open_tag[1:-1]
        out.append((line_of(text, m.start()), "A3", f"<{name}> 内容为空且无可访问名", open_tag[:60]))

    if p.suffix == ".html":
        for m in TAG_HTML.finditer(text):
            if "lang" not in attrs_of(m.group(0)):
                out.append((line_of(text, m.start()), "A4", "<html> 无 lang 属性", m.group(0)[:60]))

    # 基线稳定性：frag 空白规范化（换行/缩进不敏感）；行号随源码漂移=与 frontend-lint 同款已知权衡（源码变动重建基线）
    return [f"{rel}:{ln} [{rid}] {name}：{re.sub(r'\\s+', ' ', frag).strip()[:80]}" for ln, rid, name, frag in out]


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
            "<template>\n"
            '  <img src="x.png">\n'
            '  <input type="text">\n'
            "  <button></button>\n"
            "</template>\n",
            encoding="utf-8")
        good = t / "Good.vue"
        good.write_text(
            "<template>\n"
            '  <img src="d.png" alt="">\n'
            '  <input type="text" aria-label="关键词">\n'
            '  <button>搜索</button>\n'
            "</template>\n",
            encoding="utf-8")
        labelfor = t / "LabelFor.vue"
        labelfor.write_text(
            "<template>\n"
            '  <label for="q">关键词</label>\n'
            '  <input type="text" id="q">\n'
            "</template>\n",
            encoding="utf-8")
        wrapped = t / "Wrapped.vue"
        wrapped.write_text(
            "<template>\n"
            "  <label>\n"
            '    <input type="text">\n'
            "  </label>\n"
            "</template>\n",
            encoding="utf-8")
        html_bad = t / "bad.html"
        html_bad.write_text("<html><body><p>x</p></body></html>", encoding="utf-8")
        hidden_ok = t / "Hidden.vue"
        hidden_ok.write_text('<template><input type="hidden" name="csrf"></template>', encoding="utf-8")

        vb = scan_file(bad)
        ok1 = all(any(f"[{r}]" in x for x in vb) for r in ("A1", "A2", "A3"))
        ok2 = scan_file(good) == []
        ok3 = scan_file(labelfor) == []
        ok4 = scan_file(wrapped) == []
        ok5 = any("[A4]" in x for x in scan_file(html_bad))
        ok6 = scan_file(hidden_ok) == []
        print(f"selftest: 坏件三连(A1/A2/A3)={ok1} 好件放行={ok2} label-for豁免={ok3} "
              f"包裹豁免={ok4} html-lang命中={ok5} hidden豁免={ok6}")
        return 0 if all((ok1, ok2, ok3, ok4, ok5, ok6)) else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", help="目录或单文件")
    ap.add_argument("--ext", default=".html,.vue,.tsx,.jsx")
    ap.add_argument("--baseline", help="基线 JSON（存量豁免）；缺省时自动找 <path>/.a11y-baseline.json")
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
        violations += scan_file(f)
    if a.write_baseline:
        bl = path / ".a11y-baseline.json" if path.is_dir() else path.parent / ".a11y-baseline.json"
        bl.write_text(json.dumps({"violations": violations}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"基线已写入 {bl}（存量 {len(violations)} 条豁免）")
        return 0
    bl_path = Path(a.baseline) if a.baseline else (path / ".a11y-baseline.json" if path.is_dir() else None)
    base_set = set()
    if bl_path and Path(bl_path).exists():
        base_set = set(json.loads(Path(bl_path).read_text(encoding="utf-8")).get("violations", []))
    fresh = [v for v in violations if v not in base_set]
    if fresh:
        print(f"FAIL: {len(fresh)} 项新增 a11y 违例（存量 {len(violations) - len(fresh)} 条已由基线豁免）：")
        for x in fresh[:20]:
            print("  ✗", x)
        return 1
    print(f"OK: a11y 静态底线通过（扫描 {len(files)} 文件；存量 {len(violations)} 条基线豁免）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

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
  R5 空态（warning 级，不走基线）：文件含 v-for 列表但无 v-else / v-if="!…length" / 空态
    关键词分支——空数据时无引导（判定表「空态没有引导」；jz-01 试金石回流）

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

# jz-07 回流：旧子串匹配曾把 TaskHistory.vue（含 story 子串）整文件误排除——History 类命名
# 超常见，方向=假阴性漏报。改为路径段锚定：test/spec/story/evidence/smoke 须为完整目录段；
# node_modules/dist/build 等目录段锚定；.d.ts 后缀锚定
COMPONENT_EXCLUDE = re.compile(
    r"(^|[/\\])(test|tests|spec|specs|story|stories|evidence|smoke)([/\\])"
    r"|(^|[/\\])(node_modules|\.next|dist|build)([/\\])"
    r"|\.d\.ts$")
STYLE_BLOCK = re.compile(r"<style[\s>].*?</style>", re.S)
# 批 X FL-1：style=' 单引号形态曾绕过；FL-4：RGB( 大写函数名曾绕过（re.I 补）
R1 = re.compile(r"style=[\"']|:style=[\"']|style=\{\{")
R2 = re.compile(r"#[0-9a-f]{3,8}\b|rgba?\(", re.IGNORECASE)
# 批 X FL-2：console.table/trace/dir/count 曾绕过枚举
R3 = re.compile(r"console\.(log|debug|info|warn|error|table|trace|dir|count)\b")
# 批 X FL-3：可选绑定 catch {}（无括号形态）曾绕过
R4 = re.compile(r"catch\s*(?:\([^)]*\))?\s*\{\s*\}")
RULES = {"R1": R1, "R2": R2, "R3": R3, "R4": R4}
# R2 canvas 豁免的第二形态：2D 上下文属性赋值（strokeStyle/fillStyle 为 canvas 专属 API 名，
# 误放行面≈0；自定义函数参数如 makeGlowSprite('#..') 语义不可机判=人工域，保持拦）
CANVAS_ASSIGN = re.compile(r"\.(?:strokeStyle|fillStyle)\s*=")

# R5 空态启发（warning 级）：v-else 合法、v-else-if 不算空分支；v-if="!x.length" 形态算
V_FOR = re.compile(r"\bv-for\b")
EMPTY_BRANCH = re.compile(r"v-else(?!-if)|v-(?:if|show)=[\"']\s*!|暂无|empty-state|EmptyState|no-data|NoData")

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
            # R2 的 canvas 豁免（site-02 回流）：addColorStop( 调用行内的色值是 canvas
            # 渐变 API 的绘制参数（粒子/图表动画），非组件样式 token 逃逸
            if rid == "R2" and (".addColorStop(" in line or CANVAS_ASSIGN.search(line)):
                continue
            if rx.search(line):
                out.append(f"{p.as_posix()}:{i} [{rid}] {RULE_NAMES[rid]}：{line.strip()[:80]}")
    return out


def collect(path: Path, exts: list[str]) -> list[Path]:
    if path.is_file():
        return [path]
    return [p for p in sorted(path.rglob("*"))
            if p.is_file() and p.suffix in exts and not COMPONENT_EXCLUDE.search(str(p))]


def scan_warnings(p: Path) -> list[str]:
    """R5 空态：文件级启发，warning 不计 exit、不走基线（自测见 selftest W 段）。"""
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    if not V_FOR.search(text) or EMPTY_BRANCH.search(text):
        return []
    first = next((ln for ln in text.splitlines() if "v-for" in ln), "").strip()[:70]
    return [f"{p.as_posix()} [R5-W] 列表 v-for 无空态分支（空数据时无引导）：{first}"]


def selftest() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        bad = t / "Bad.vue"
        bad.write_text(
            '<template><div style="color: #ff0000">x</div></template>\n'
            '<template><div style=\'color: blue\'>y</div></template>\n'  # FL-1 单引号
            "<script>console.table(t); try {} catch (e) {}</script>\n"  # FL-2 + 带参空 catch
            "<script>try {} catch {}</script>\n"  # FL-3 可选绑定空 catch
            "<script>el.style.background = 'RGB(255,0,0)';</script>\n",  # FL-4 大写 RGB
            encoding="utf-8")
        good = t / "Good.tsx"
        good.write_text('export const A = () => <div className="c">x</div>;\n', encoding="utf-8")
        styleblock = t / "S.vue"
        styleblock.write_text("<style>.a { color: #ff0000; }</style>", encoding="utf-8")
        v = scan_file(bad, RULES)
        ok1 = any("[R1]" in x for x in v) and any("[R2]" in x for x in v) and any("[R4]" in x for x in v)
        # 批 X 反向变异（细则 #407）：四个绕过形态逐一必拦
        ok6 = (sum(1 for x in v if "[R1]" in x) >= 2  # 双引号+单引号都拦
               and sum(1 for x in v if "[R3]" in x) >= 1  # console.table
               and sum(1 for x in v if "[R4]" in x) >= 2  # 带参 catch + 可选绑定 catch
               and any("RGB" in x and "[R2]" in x for x in v))  # 大写 RGB(
        ok2 = scan_file(good, RULES) == []
        text_s = strip_style_blocks(styleblock.read_text(encoding="utf-8"))
        ok3 = "#ff0000" not in text_s and scan_file(styleblock, RULES) == []
        cssfile = t / "tokens.css"
        cssfile.write_text(":root { --accent: #4a7297; }", encoding="utf-8")
        ok4 = scan_file(cssfile, RULES) == []  # F10 回归：css 文件本体色值=R2 豁免
        metafile = t / "meta.html"
        metafile.write_text('<html lang="zh-CN">\n<head>\n<meta name="theme-color" content="#eef1f5">\n</head>\n</html>', encoding="utf-8")
        ok5 = scan_file(metafile, RULES) == []  # F10 回归：meta 独立行 content 色值=元数据豁免
        warn_no = t / "NoEmpty.vue"  # R5 反向：v-for 无空态分支 → W
        warn_no.write_text('<template><div v-for="i in list" :key="i">{{ i }}</div></template>', encoding="utf-8")
        warn_else = t / "WithElse.vue"  # R5 正向：v-else 分支在场
        warn_else.write_text('<template><div v-for="i in list" :key="i">{{ i }}</div><div v-else>先记一笔吧</div></template>', encoding="utf-8")
        warn_notlen = t / "WithNotLen.vue"  # R5 正向：v-if="!list.length" 空分支形态
        warn_notlen.write_text('<template><div v-for="i in list" :key="i">{{ i }}</div><div v-if="!list.length">空</div></template>', encoding="utf-8")
        warn_elseif = t / "OnlyElseIf.vue"  # R5 反向：只有 v-else-if 不算空分支（jz-01 逃逸形态）
        warn_elseif.write_text('<template><div v-if="loading">…</div><div v-else-if="list.length"><div v-for="i in list" :key="i">{{ i }}</div></div></template>', encoding="utf-8")
        ok7w = len(scan_warnings(warn_no)) == 1 and scan_warnings(warn_else) == [] \
            and scan_warnings(warn_notlen) == [] and len(scan_warnings(warn_elseif)) == 1
        # site-02 回流：canvas addColorStop 绘制参数放行，普通样式色仍拦（#407 双向）
        canvasfile = t / "canvas.js"
        canvasfile.write_text("grad.addColorStop(0, 'rgba(90,70,160,0.14)');\n"
                              "ctx.strokeStyle = '#cfe4ff';\n"
                              "ctx.fillStyle = 'rgba(0,0,0,0.5)';\n"
                              "el.style.background = 'rgba(0,0,0,0.5)';\n"
                              "s = makeGlowSprite('#dbeeff', 'rgba(1,2,3,0.9)');\n", encoding="utf-8")
        vc = scan_file(canvasfile, RULES)
        ok8c = ((not any("addColorStop" in x or "strokeStyle" in x or "fillStyle" in x for x in vc))
                and sum(1 for x in vc if "[R2]" in x) == 2)  # 普通样式赋值+自定义函数参数仍拦
        # site-01 回流：evidence/smoke 证据目录整文件排除（与 test/spec 同语义）
        evdir = t / "evidence"
        evdir.mkdir()
        smokef = evdir / "smoke-core.js"
        smokef.write_text("console.log('SMOKE RESULT: ok');\n", encoding="utf-8")
        ok9e = collect(evdir, [".js"]) == []
        # jz-07 回流反向变异：文件名含 story 子串（TaskHistory）不得整文件误排除；story/ 目录仍排除
        compdir = t / "components"
        compdir.mkdir()
        hf = compdir / "TaskHistory.vue"
        hf.write_text("<script setup>\nconsole.log('x')\n</script>\n", encoding="utf-8")
        ok10h = (collect(compdir, ['.vue']) and
                 sum(1 for x in scan_file(hf, RULES) if '[R3]' in x) == 1)
        sdir = compdir / "story"
        sdir.mkdir()
        (sdir / "A.vue").write_text("console.log('y')\n", encoding="utf-8")
        kept = collect(compdir, ['.vue'])
        ok10s = len(kept) == 1 and kept[0].name == "TaskHistory.vue"
        print(f"selftest: 违例三连(R1/R2/R4)={ok1} 干净文件放行={ok2} style 块色值合法={ok3} "
              f"css 文件色值豁免={ok4} meta 色值豁免={ok5} 批X反向FL1-4={ok6} "
              f"R5空态W拦/放行={ok7w} canvas豁免={ok8c} 证据目录排除={ok9e} "
              f"History名不误排除/目录段仍排除={ok10h and ok10s}")
        return 0 if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7w and ok8c and ok9e and ok10h and ok10s else 1


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
    warnings: list[str] = []
    for f in files:
        violations += scan_file(f, RULES)
        warnings += scan_warnings(f)
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
    for w in warnings:
        print("W", w)
    if fresh:
        print(f"FAIL: {len(fresh)} 项新增前端 lint 违例（存量 {len(violations) - len(fresh)} 条已由基线豁免）：")
        for x in fresh[:20]:
            print("  ✗", x)
        return 1
    print(f"OK: 前端 lint 通过（扫描 {len(files)} 文件；存量 {len(violations)} 条基线豁免）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""五门禁反向注入驱动器（只读版）· 2026-09-29（批 X）
设计：零写入、零子进程、零网络——
  PO/LL 夹具在内存构造（JSON 对象直入 check 函数）；
  RG/FL/AG 夹具为静态文件，随档放 fixtures/（bash 预建，本驱动只读）；
  五个 gate 模块进程内 import，直调其 check/scan 函数；
  verdict 打 stdout（> report.jsonl 重定向落盘，由调用方完成）。
判读：want=blocked 且实际放行=CONFIRMED-MISS（漏报）；want=allowed 且实际拦截=FALSE-POSITIVE（误报）。
"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

FX = Path("fixtures")
GATES_DIR = Path.home() / ".agents" / "skills" / "shisan-xinuo-product" / "scripts"
EXTS = [".vue", ".tsx", ".jsx"]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, GATES_DIR / (name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rg = load("registry-gate")
po_g = load("product-object-gate")
ll = load("l0-l5-gate")
fl = load("frontend-lint-gate")
ag = load("a11y-gate")

PO_GOOD = {
    "purpose": "让用户集中管理收藏内容，不解决协作编辑",
    "responsibility": "收藏条目管理与运营",
    "capabilities": [{"name": "浏览清单", "role": "核心任务"}, {"name": "导出", "role": "辅助"}],
    "main_function": "浏览清单",
    "layers": {"active": "L6/L7",
               "upstream": {"L1": "brief:用户任务书给定", "L2": "brief:能力 8 条",
                             "L3": "brief:主功能已指定", "L4": "adjudicated:本期无后台"}},
    "operability": [{"item": "数据来源", "answer": "用户创建"}, {"item": "后台", "answer": "显式裁决：本期无后台"}],
}
LL_GOAL = {"north_star": "让个人月度储蓄率提升至 20% 以上（2026 年底前）",
           "key_results": ["储蓄率从 8% 提升到 20%（2026-12 底前）",
                            "记账留存 30 日≥60%（2026 Q4）",
                            "月活周均使用 3 次以上（2026-12）"]}
LL_IA = {"organization": "主题", "global_nav": True, "local_nav": True, "location_indicator": True,
         "routes": [{"path": "/home", "has_global_nav": True}, {"path": "/archive", "has_global_nav": True}],
         "pages": [{"path": "/home", "exits": 3}, {"path": "/archive", "exits": 2}],
         "find_paths": ["浏览导航", "搜索"],
         "tree_tests": [{"task": "找2025年文章", "correct_leaf": "/archive/2025", "success_rate": 0.85, "directness": 0.6}]}


def po(mut: dict) -> dict:
    o = json.loads(json.dumps(PO_GOOD))
    for k, v in mut.items():
        if v is None:
            o.pop(k, None)
        else:
            o[k] = v
    return o


def ll_ia(mut: dict) -> dict:
    o = json.loads(json.dumps(LL_IA))
    for k, v in mut.items():
        if v is None:
            o.pop(k, None)
        else:
            o[k] = v
    return o


def fx_rel(sub: str) -> Path:
    return FX / sub


CASES = [
    # ── registry-gate（文件夹具）──
    dict(id="ctrl-rg-marked", gate="registry", want="allowed", sub="01-rg-marked/src",
         note="对照：带标记组件放行"),
    dict(id="rg-scope-hole", gate="registry", want="blocked", sub="02-rg-scope-hole/src",
         note="组件目录不含 component 字样→默认 scope 永不扫描"),
    dict(id="rg-ext-case", gate="registry", want="blocked", sub="03-rg-ext-case/src",
         note="大写后缀 .VUE 不在默认 ext"),
    dict(id="rg-marker-forge", gate="registry", want="allowed", sub="04-rg-forge/src",
         note="判据缺口：标记=文本包含，字符串字面量即可伪造（契约内放行，弱判据）"),
    dict(id="rg-node-modules-fp", gate="registry", want="allowed", sub="05-rg-nm", scope_all=True,
         note="无 node_modules 排除（lint 两门禁有）→ --scope all 视角三方依赖被报"),
    # ── product-object-gate（内存夹具）──
    dict(id="ctrl-po-good", gate="product-object", want="allowed", obj=po({}), note="对照：合法定义放行"),
    dict(id="po-role-enum", gate="product-object", want="blocked",
         obj=po({"capabilities": [{"name": "浏览清单", "role": "隐藏功能"}, {"name": "导出", "role": "辅助"}]}),
         note="ROLES 枚举定义未在 check 中使用"),
    dict(id="po-empty-mainfn", gate="product-object", want="blocked", obj=po({"main_function": ""}),
         note="main_function 空串时 P2 三项检查全跳过"),
    dict(id="po-resp-prefix", gate="product-object", want="blocked", obj=po({"responsibility": "（展示看板数据）"}),
         note="禁用动词前缀绕过：全角括号包裹"),
    dict(id="po-purpose-number", gate="product-object", want="blocked", obj=po({"purpose": 123}),
         note="JSON 数字型 purpose 经 str() 穿透存在性检查"),
    dict(id="ctrl-po-ghost-file", gate="product-object", want="blocked",
         obj=po({"layers": {"active": "L6", "upstream": {
             "L1": "brief:x", "L2": "file:ghost.md", "L3": "brief:y", "L4": "adjudicated:z"}}}),
         note="对照：file: 上游悬空必须拦"),
    # ── l0-l5-gate（内存夹具）──
    dict(id="ctrl-ll-good", gate="l0-l5", want="allowed", goal=LL_GOAL, ia=LL_IA, note="对照：合法目标+IA 放行"),
    dict(id="ll-ns-number", gate="l0-l5", want="blocked", goal={**LL_GOAL, "north_star": 123},
         note="north_star 数字型：非 str 即跳过全部声明检查（F5 同族未盖类型面）"),
    dict(id="ll-nav-false-str", gate="l0-l5", want="blocked", goal=LL_GOAL, ia={**LL_IA, "global_nav": "false"},
         note="字符串 \"false\" 为 truthy，三件套判虚"),
    dict(id="ll-exits-str", gate="l0-l5", want="blocked", goal=LL_GOAL,
         ia=ll_ia({"pages": [{"path": "/trap", "exits": "0"}]}),
         note="exits=\"0\" 字符串绕过死端判定（==0 对 str 恒 False）"),
    dict(id="ctrl-ll-nokey", gate="l0-l5", want="blocked",
         goal={"key_results": LL_GOAL["key_results"]}, note="F5 回归对照：键缺失必须拦"),
    # ── frontend-lint-gate（文件夹具）──
    dict(id="ctrl-fl-clean", gate="frontend-lint", want="allowed", sub="17-fl-clean/src", note="对照：干净文件放行"),
    dict(id="fl-style-single-quote", gate="frontend-lint", want="blocked", sub="18-fl-sq/src",
         note="单引号内联样式：R1 只认 style=\""),
    dict(id="fl-console-table", gate="frontend-lint", want="blocked", sub="19-fl-table/src",
         note="console.table/trace 不在 R3 枚举"),
    dict(id="fl-catch-noparen", gate="frontend-lint", want="blocked", sub="20-fl-catch/src",
         note="ES2019 optional catch binding：catch {} 无参形态"),
    dict(id="fl-rgb-upper", gate="frontend-lint", want="blocked", sub="21-fl-rgb/src",
         note="R2 大小写敏感：RGB( 大写函数名"),
    dict(id="ctrl-fl-inline", gate="frontend-lint", want="blocked", sub="22-fl-inline/src", note="对照：双引号内联样式拦截"),
    # ── a11y-gate（文件夹具）──
    dict(id="ctrl-ag-good", gate="a11y", want="allowed", sub="23-ag-good/src", note="对照：好件放行"),
    dict(id="ag-empty-label-wrap", gate="a11y", want="blocked", sub="24-ag-label/src",
         note="空 label 包裹豁免：label 无文本=无可访问名"),
    dict(id="ag-lang-empty", gate="a11y", want="blocked", sub="25-ag-lang/src",
         note="lang=\"\" 空值：有键无值=无语言声明"),
    dict(id="ag-emoji-button", gate="a11y", want="blocked", sub="26-ag-emoji/src",
         note="判据缺口（v1 诚实边界内）：emoji-only 按钮文本非空→放行，读屏可达名存疑"),
    dict(id="ctrl-ag-img-noalt", gate="a11y", want="blocked", sub="27-ag-img/src", note="对照：img 无 alt 拦截"),
]


def eval_case(c: dict) -> dict:
    g = c["gate"]
    if g == "registry":
        root = fx_rel(c["sub"])
        scope = "all" if c.get("scope_all") else "components"
        missing, _msg = rg.scan(root, scope, EXTS, None, False)
        blocked = bool(missing)
        detail = "missing=%s" % missing[:3]
    elif g == "product-object":
        fails = po_g.check(c["obj"], FX)
        blocked = bool(fails)
        detail = "fails=%s" % fails[:2]
    elif g == "l0-l5":
        f1, _w1 = ll.check_goal(c["goal"])
        f2, _w2 = ll.check_ia(c["ia"]) if "ia" in c else ([], [])
        blocked = bool(f1 + f2)
        detail = "fails=%s" % (f1 + f2)[:2]
    elif g == "frontend-lint":
        files = fl.collect(fx_rel(c["sub"]), EXTS)
        vi: list[str] = []
        for p in files:
            vi += fl.scan_file(p, fl.RULES)
        blocked = bool(vi)
        detail = "violations=%d %s" % (len(vi), vi[:2])
    elif g == "a11y":
        files = ag.collect(fx_rel(c["sub"]), [".html", ".vue", ".tsx", ".jsx"])
        vi = []
        for p in files:
            vi += ag.scan_file(p)
        blocked = bool(vi)
        detail = "violations=%d %s" % (len(vi), vi[:2])
    else:
        blocked, detail = False, "unknown gate"
    want = c["want"]
    if want == "blocked":
        verdict = "OK-CAUGHT" if blocked else "CONFIRMED-MISS"
    else:
        verdict = "OK-ALLOWED" if not blocked else "FALSE-POSITIVE"
    return dict(id=c["id"], gate=g, want=want, blocked=blocked, verdict=verdict,
                note=c.get("note", ""), detail=detail[:200])


def main() -> int:
    rows = [eval_case(c) for c in CASES]
    for r in rows:
        print(json.dumps(r, ensure_ascii=False))
    miss = sum(1 for r in rows if r["verdict"] == "CONFIRMED-MISS")
    fp = sum(1 for r in rows if r["verdict"] == "FALSE-POSITIVE")
    print("# SUMMARY: %d cases | 漏报 %d | 误报 %d" % (len(rows), miss, fp), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

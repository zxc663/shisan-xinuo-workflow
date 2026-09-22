#!/usr/bin/env python3
"""product-object-gate · 门禁⑪：产品对象定义检查（上游 L1-L4 的第一批机器判据）。

检查产品对象定义 JSON（schema=references/product-object.md §7）：
  P1 定义存在性（候选 11）：purpose/responsibility 非空，responsibility 须管理性动词
     （禁「展示/显示」开头——判定表 J-29）；capabilities 非空且每条有 name+role。
  P2 主功能唯一性：main_function 必须指向 capabilities 之一，且 role=「核心任务」
     恰好一个——主功能数≠1 = 「什么都有，但什么都不重要」，exit 1。
  P3 层级声明与上游引用存在性（候选 14）：layers.active 非空；L1-L4 每层必须有上游
     条目，取值三种形态——file:<path>（文件须存在且非空）｜brief:<说明>（用户给定）｜
     adjudicated:<裁决>（显式裁决）；缺失或 file 引用悬空 → 逐层报出，exit 1。
  P4 可运营性：operability 数组非空且每条有 item+answer——前台能力必须有管理答案
     或显式裁决（判定=假能力，J-32）。

与层级门的关系：本 gate 是「上游已确认」的机器抽查件，不替代跑道步骤 0a 的
层级定位判断（层定位本身=人工裁决域，见 layer-stack.md §4）。

用法：python product-object-gate.py --file object.json
      python product-object-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROLES = ("核心任务", "业务操作", "辅助", "高阶", "风险操作")
BANNED_VERB_PREFIXES = ("展示", "显示")
UPSTREAM_LAYERS = ("L1", "L2", "L3", "L4")


def check(obj: dict, base: Path) -> list[str]:
    fails: list[str] = []
    purpose = str(obj.get("purpose", "")).strip()
    responsibility = str(obj.get("responsibility", "")).strip()
    caps = obj.get("capabilities") or []

    # P1 定义存在性（候选 11）
    if not purpose:
        fails.append("P1 purpose 缺失（为什么存在=六问①，非空）")
    if not responsibility:
        fails.append("P1 responsibility 缺失（职责句=六问②）")
    elif responsibility.startswith(BANNED_VERB_PREFIXES):
        fails.append(f"P1 职责句以「{responsibility[:2]}」开头——须管理性动词（X 管理/运营），禁展示/显示（J-29）")
    if not caps:
        fails.append("P1 capabilities 缺失或为空（能力清单=六问③）")
    else:
        for c in caps:
            if not isinstance(c, dict) or not str(c.get("name", "")).strip() or not str(c.get("role", "")).strip():
                fails.append(f"P1 能力条目缺 name/role：{c}")

    # P2 主功能唯一性
    main_fn = str(obj.get("main_function", "")).strip()
    core = [str(c.get("name", "")).strip() for c in caps if isinstance(c, dict) and str(c.get("role", "")).strip() == "核心任务"]
    if caps:
        if len(core) != 1:
            fails.append(f"P2 role=核心任务 的能力数={len(core)}（须恰好 1）——主功能不明=「什么都有，但什么都不重要」")
        if main_fn and main_fn not in {str(c.get("name", "")).strip() for c in caps if isinstance(c, dict)}:
            fails.append(f"P2 main_function '{main_fn}' 不在 capabilities 中")
        if main_fn and core and main_fn != core[0]:
            fails.append(f"P2 main_function '{main_fn}' 与核心任务 '{core[0]}' 不一致")

    # P3 层级声明与上游引用存在性（候选 14）
    layers = obj.get("layers") or {}
    if not str(layers.get("active", "")).strip():
        fails.append("P3 layers.active 缺失（层级门 0a：声明本任务活动层）")
    upstream = layers.get("upstream") or {}
    for layer in UPSTREAM_LAYERS:
        if layer not in upstream:
            fails.append(f"P3 上游 {layer} 未声明确认来源（层级门 0b：未确认不得下沉）")
            continue
        val = str(upstream[layer]).strip()
        if val.startswith("file:"):
            ref = base / val[5:].strip()
            if not ref.is_file() or ref.stat().st_size == 0:
                fails.append(f"P3 上游 {layer} 引用 file:{val[5:].strip()} 不存在或为空（上游引用悬空）")
        elif val.startswith(("brief:", "adjudicated:")):
            if len(val) <= len("brief:"):
                fails.append(f"P3 上游 {layer} 的 {val.split(':', 1)[0]} 说明为空")
        else:
            fails.append(f"P3 上游 {layer} 取值须以 file:/brief:/adjudicated: 开头，实际：{val[:40]}")

    # P4 可运营性
    oper = obj.get("operability") or []
    if not oper:
        fails.append("P4 operability 缺失或为空（六问⑥：谁管理/来源/权限/fallback，或显式裁决「本期无后台+谁管内容」）")
    else:
        for o in oper:
            if not isinstance(o, dict) or not str(o.get("item", "")).strip() or not str(o.get("answer", "")).strip():
                fails.append(f"P4 可运营性条目缺 item/answer：{o}")
    return fails


def selftest() -> int:
    base = Path(".")
    good = {
        "purpose": "让用户集中管理收藏内容，不解决协作编辑",
        "responsibility": "收藏条目管理与运营",
        "capabilities": [{"name": "浏览清单", "role": "核心任务"}, {"name": "导出", "role": "辅助"}],
        "main_function": "浏览清单",
        "layers": {"active": "L6/L7",
                   "upstream": {"L1": "brief:用户任务书给定", "L2": "brief:能力 8 条", "L3": "brief:主功能已指定", "L4": "adjudicated:本期无后台，内容=用户自建"}},
        "operability": [{"item": "数据来源", "answer": "用户创建"}, {"item": "后台", "answer": "显式裁决：本期无后台"}],
    }
    ok1 = check(good, base) == []

    bad_p1 = dict(good, purpose="", responsibility="展示收藏数据", capabilities=[])
    f_p1 = check(bad_p1, base)
    ok_p1 = sum(1 for x in f_p1 if x.startswith("P1")) >= 3

    bad_p2 = dict(good, capabilities=[
        {"name": "浏览清单", "role": "核心任务"}, {"name": "快速收藏", "role": "核心任务"}, {"name": "导出", "role": "辅助"}])
    bad_p2b = dict(good, main_function="快速收藏")
    ok_p2 = any("恰好 1" in x for x in check(bad_p2, base)) and any("不一致" in x for x in check(bad_p2b, base))

    bad_p3 = dict(good, layers={"active": "L6", "upstream": {"L1": "brief:x", "L2": "file:docs/ghost.md", "L4": "adjudicated:无后台"}})
    f_p3 = check(bad_p3, base)
    ok_p3 = (sum(1 for x in f_p3 if "L3" in x) >= 1 and sum(1 for x in f_p3 if "L2" in x and "不存在" in x) >= 1)

    bad_p4 = dict(good, operability=[])
    ok_p4 = any(x.startswith("P4") for x in check(bad_p4, base))

    ok = all([ok1, ok_p1, ok_p2, ok_p3, ok_p4])
    print(f"selftest: 合法定义放行={ok1} P1存在性/职责句拦截={ok_p1} P2主功能唯一拦截={ok_p2} "
          f"P3层级声明+上游引用拦截={ok_p3} P4可运营性拦截={ok_p4} → {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("  detail:", {"p1": f_p1, "p2": check(bad_p2, base), "p3": f_p3})
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="产品对象定义 JSON（schema=product-object.md §7）")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        print("FAIL: 需要 --file 或 --selftest")
        return 1
    p = Path(a.file)
    obj = json.loads(p.read_text(encoding="utf-8"))
    fails = check(obj, p.resolve().parent)
    if fails:
        print(f"FAIL: {len(fails)} 项产品对象缺陷：")
        for x in fails:
            print("  ✗", x)
        return 1
    print("OK: 产品对象定义检查通过（定义存在/主功能唯一/层级声明+上游引用在档/可运营性有答案）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

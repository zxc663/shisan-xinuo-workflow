#!/usr/bin/env python3
"""l0-l5-gate v1 · 产品目标合格线 + 信息架构结构底线（层栈 L0/L5 的机器可查子集）。

背景：层×判据矩阵 L0/L5 两层空白（layer-judgement-matrix.md），2026-09-24 由调研档
（design-specs/l0-l5-criteria-research.md）蒸馏入库。**只检查陈述/工件形态，不生产目标与方案**
（PE≠PI 边界，用户裁决 2026-09-24：形态合规性=本包可查；内容对错=产品决策侧）。

输入工件 schema：
goal.json（产品目标工件，缺失=直接 fail，L0-C10）
{
  "north_star": "主结果声明（恰好 1 条；数组则长度必须=1）",        // L0-C1/C11/C12
  "key_results": ["KR1", "KR2", …],                              // L0-C4 形态初筛 / C5 时间窗 / C6 数量
  "jobs": ["动词+宾语+情境限定词", …]                              // 可选；L0-C7 锚定（有则查形态）
}
ia.json（信息架构档，可选；提供才查 L5）
{
  "organization": "主题|任务|用户|格式|时间（组织主维度声明）",      // L5-C1
  "global_nav": true, "local_nav": true, "local_nav_exempt": "豁免声明", // L5-C3 三件套
  "location_indicator": true,                                     // L5-C3③ 当前位置
  "routes": [{"path": "/x", "has_global_nav": true}],              // L5-C5 前门可达
  "pages": [{"path": "/x", "exits": 2, "terminal": false}],        // L5-C10 死端页（与 L7 无死端同构）
  "find_paths": ["浏览导航", "搜索"],                               // L5-C6 路径类型计数
  "tree_tests": [{"task": "找X", "correct_leaf": "叶子", "success_rate": 0.8, "directness": 0.6}] // L5-C11
}

检查（fail=exit 1；warning=打印 W 前缀行，exit 0）：
  L0-C10 目标工件存在且可解析（fail）
  L0-C1  主结果声明恰好 1 条（≥2 无主次 → fail；0 → fail）
  L0-C12 主指标含度量口径（数字/比较词形；无 → fail）
  L0-C5  每条 KR 含时间窗（日期/季度/相对期词形正则；缺 → fail）
  L0-C4  KR 二值形态初筛（数值+比较词形；形态不齐 → warning 人审）
  L0-C6  KR 条数 3-5（越界 → warning；对齐 whatmatters.com 惯例，不作 fail）
  L0-C13 虚荣指标词形作主指标（warning+人工裁决；基础设施类累计量可合法）
  L0-C7  job statement 三段形态初筛（<3 段词形 → warning）
  L5-C3  导航三件套（全局/局部/当前位置；缺且无豁免 → fail）
  L5-C5  前门可达（存在无全局导航的路由=孤页 → fail）
  L5-C10 死端页（exits=0 且非 terminal → fail）
  L5-C6  查找路径类型 ≥2（=1 → warning）
  L5-C1  组织系统声明存在（缺 → warning）
  L5-C11 tree testing 报告存在性与三要素（task/correct_leaf/success_rate/directness；缺 → warning；
         阈值不设行业硬数——项目自定留痕，无留痕时仅提示，不作 fail；NN/g 明示无公认阈值）

用法：python l0-l5-gate.py --goal goal.json [--ia ia.json]
      python l0-l5-gate.py --selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TIME_WINDOW = re.compile(
    r"\d{4}年|\d{4}-\d{2}|\d{4}-\d{2}-\d{2}|Q[1-4]|\d+\s*(天|日|周|个月|月|季度|年)|年底|月初|月末|底前|内上线|内发布")
METRIC_FORM = re.compile(r"\d|≥|≤|>|<|提升|降低|达到|占比|%|率|次数|人均")
VANITY = re.compile(r"总注册|总下载|总PV|总访问|累计用户|累计注册")
JOB_FORM = re.compile(r"[\u4e00-\u9fa5A-Za-z]+\s*[\u4e00-\u9fa5A-Za-z]+\s*(在|当|while|during|for)?\s*[\u4e00-\u9fa5A-Za-z]*")


def check_goal(goal: dict) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    ns = goal.get("north_star")
    if ns is None:
        # F5（2026-09-24）：键缺失≠合法——曾静默放行（None 落空全部检查），
        # 电池夹具没盖「文件在、键缺失」变体，与 F2 同族（自测路径缺口）。
        fails.append("L0-C1/C10 主结果声明缺失（north_star 键不存在）——目标未被陈述")
    elif isinstance(ns, list):
        if len(ns) == 0:
            fails.append("L0-C1/C10 主结果声明为空——目标未被陈述")
        elif len(ns) > 1:
            fails.append(f"L0-C1/C11 主结果声明 {len(ns)} 条且无主次标记（单值性）")
        else:
            ns = ns[0]
    if isinstance(ns, str):
        if not ns.strip():
            fails.append("L0-C1/C10 主结果声明为空")
        elif VANITY.search(ns):
            warns.append(f"L0-C13 主指标疑为虚荣/累计型（{ns}）——warning：基础设施类可合法，人工裁决")
        elif not METRIC_FORM.search(ns):
            fails.append(f"L0-C12 主指标无度量口径（{ns}）——不可度量目标不可判")
    krs = goal.get("key_results") or []
    if krs:
        for i, kr in enumerate(krs, 1):
            if not TIME_WINDOW.search(str(kr)):
                fails.append(f"L0-C5 第{i}条 KR 缺时间窗（{kr}）——time-bound 缺失")
            elif not METRIC_FORM.search(str(kr)):
                warns.append(f"L0-C4 第{i}条 KR 二值形态存疑（{kr}）——无数值/比较词形，人工复核是否可二值判定")
        if not (3 <= len(krs) <= 5):
            warns.append(f"L0-C6 KR 条数 {len(krs)} 越出 3-5 惯例区间（warning：单指标极简目标可显式裁决）")
    jobs = goal.get("jobs") or []
    for j in jobs:
        if len(str(j).split()) < 2 and not JOB_FORM.search(str(j)):
            warns.append(f"L0-C7 job statement 三段形态存疑（{j}）——动词+宾语+情境限定词")
    return fails, warns


def check_ia(ia: dict) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    if not str(ia.get("organization", "")).strip():
        warns.append("L5-C1 组织系统声明缺失（分类主维度：主题/任务/用户/格式/时间）")
    g, l, li = ia.get("global_nav"), ia.get("local_nav"), ia.get("location_indicator")
    exempt = str(ia.get("local_nav_exempt", "")).strip()
    missing = [n for n, v in (("全局导航", g), ("局部导航", l), ("当前位置指示", li)) if not v]
    if "局部导航" in missing and exempt:
        missing.remove("局部导航")
    if missing:
        fails.append(f"L5-C3 导航三件套缺 {'、'.join(missing)} 且无豁免声明")
    routes = ia.get("routes") or []
    orphans = [r.get("path", "?") for r in routes if not r.get("has_global_nav")]
    if orphans:
        fails.append(f"L5-C5 前门可达失败：孤页 {orphans}（≥半数访问不经首页，每页须可达全局导航）")
    pages = ia.get("pages") or []
    dead = [p.get("path", "?") for p in pages if p.get("exits", 0) == 0 and not p.get("terminal")]
    if dead:
        fails.append(f"L5-C10 死端页 {dead}（与 L7 无死端同构：无出链且非终态）")
    fp = ia.get("find_paths") or []
    if len(fp) == 1:
        warns.append("L5-C6 查找路径类型仅 1 种（多重分类原则建议 ≥2：浏览+搜索/标签筛选）")
    tt = ia.get("tree_tests") or []
    if not tt:
        warns.append("L5-C11 无 tree testing 报告——关键导航任务建议 ≥3 任务实测（工件存在性）")
    else:
        for t in tt:
            for k in ("task", "correct_leaf", "success_rate", "directness"):
                if k not in t:
                    warns.append(f"L5-C11 tree testing 报告缺要素 {k}（任务：{t.get('task', '?')}）")
    return fails, warns


def selftest() -> int:
    goal_ok = {"north_star": "让个人月度储蓄率提升至 20% 以上（2026 年底前）",
               "key_results": ["储蓄率从 8% 提升到 20%（2026-12 底前）",
                                "记账留存 30 日≥60%（2026 Q4）",
                                "月活周均使用 3 次以上（2026-12）"]}
    ia_ok = {"organization": "主题", "global_nav": True, "local_nav": True,
             "location_indicator": True,
             "routes": [{"path": "/home", "has_global_nav": True},
                         {"path": "/archive", "has_global_nav": True}],
             "pages": [{"path": "/home", "exits": 3}, {"path": "/archive", "exits": 2}],
             "find_paths": ["浏览导航", "搜索"],
             "tree_tests": [{"task": "找2025年文章", "correct_leaf": "/archive/2025",
                              "success_rate": 0.85, "directness": 0.6}]}
    f1, w1 = check_goal(goal_ok)
    f2, w2 = check_ia(ia_ok)
    ok1 = f1 == [] and f2 == []
    g_bad = {"north_star": ["A 指标", "B 指标"], "key_results": ["提高体验"]}
    f3, _ = check_goal(g_bad)
    ok2 = any("L0-C1" in x for x in f3) and any("L0-C5" in x for x in f3)
    g_nokey = {"key_results": ok_goal_krs()}  # F5 回归（2026-09-24）：文件在、north_star 键缺失 → 必 fail
    f6, _ = check_goal(g_nokey)
    ok5 = any("L0-C1" in x and "缺失" in x for x in f6)
    g_vanity = {"north_star": "累计注册用户破万", "key_results": ok_goal_krs()}
    f4, w4 = check_goal(g_vanity)
    ok3 = any("L0-C13" in x for x in w4) and not any("L0-C12" in x for x in f4)
    ia_bad = {"routes": [{"path": "/lost", "has_global_nav": False}],
               "pages": [{"path": "/trap", "exits": 0}]}
    f5, w5 = check_ia(ia_bad)
    ok4 = any("L5-C5" in x for x in f5) and any("L5-C10" in x for x in f5) and any("L5-C3" in x for x in f5)
    print(f"selftest: 合法目标+IA放行={ok1} 多目标/缺时间窗拦截={ok2} 虚荣warning不fail={ok3} 孤页/死端/三件套拦截={ok4} 键缺失必拦(F5)={ok5}"
          f"（warning 基线 {len(w1)+len(w2)+len(w4)+len(w5)} 条）")
    return 0 if ok1 and ok2 and ok3 and ok4 and ok5 else 1


def ok_goal_krs() -> list[str]:
    return ["注册转化 ≥30%（2026-12 底前）", "次月留存 ≥40%（2026 Q4）", "获客成本 ≤10 元（2026-12）"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--goal", help="产品目标工件 JSON（schema 见文件头）")
    ap.add_argument("--ia", help="信息架构档 JSON（可选）")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.goal:
        print("FAIL: 需要 --goal 或 --selftest")
        return 1
    gp = Path(a.goal)
    if not gp.exists():
        print("FAIL: L0-C10 目标工件不存在——目标未被陈述（停下回补，不代拟：PE≠PI）")
        return 1
    try:
        goal = json.loads(gp.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"FAIL: L0-C10 目标工件不可解析（{e}）")
        return 1
    fails: list[str] = []
    warns: list[str] = []
    f, w = check_goal(goal if isinstance(goal, dict) else {})
    fails += f
    warns += w
    if a.ia:
        ip = Path(a.ia)
        if not ip.exists():
            print(f"W L5 工件路径不存在：{a.ia}（按未提供处理）")
        else:
            try:
                ia = json.loads(ip.read_text(encoding="utf-8"))
                f2, w2 = check_ia(ia if isinstance(ia, dict) else {})
                fails += f2
                warns += w2
            except Exception as e:  # noqa: BLE001
                warns.append(f"L5 IA 档不可解析（{e}）——按未提供处理")
    for x in warns:
        print("W", x)
    if fails:
        print(f"FAIL: {len(fails)} 项 L0/L5 判据缺陷：")
        for x in fails:
            print("  ✗", x)
        return 1
    print(f"OK: L0/L5 机器子集通过（warning {len(warns)} 条见上；语义裁决项归人工）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

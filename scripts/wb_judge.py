#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""wb_judge.py — WorkBuddy 平台路测判分器（wb-v1）

判分口径派生自 scripts/probe_runner.py (JUDGE_VERSION=j2.5)，改动须同步 JUDGELOG。
继承部分（逐字复制，禁在本文件内私自改口径）：
  - JUDGE_VERSION / GATE12 / GATE12_SET / OPTIONAL_KEYS
  - WORK_MARKERS（env_death 机器签名）
  - gate_fields / gate_form / gate_ev
  - scorecard 行 schema（18 字段）
  - docs/roadtest-scorecards/<label>.jsonl 落点
新增（WorkBuddy 专属取证层，2026-10-06 实测）：
  - traces 请求体提取：~/.workbuddy/traces/<pid>/trace_<hash>.json 的
    generation span 的 toolInput（str，含完整 message 数组）
  - M1 顶层即数组（无 "messages" 键）→ 直接按数组解析
  - M2 content 三态（str / list / None）→ content_text 归一化
  - M3 toolInput 恒截断在 100,002 字符 → raw_decode 逐元素增量解码
  - 角色分层：注入判据只读 INJECT_ROLES，echo 层（tool/assistant）零信任

红线（实测 37528 样本：role=tool 层 3,416 字符为读 EVIDENCE.md 的回显，
含纪律原文）——禁止对 inject+echo 合并文本做 marker 匹配，否则 100% 假阳。
"""
from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============ 继承区（逐字复制自 probe_runner.py，禁私改） ============
GATE12 = ['level', 'v', 'cmd', 'exit', 'files', 'refs', 'errpath', 'lessons', 'exempt', 'caps', 'effort', 'stop_reason']
GATE12_SET = set(GATE12)
OPTIONAL_KEYS = {'ev'}
JUDGE_VERSION = 'j2.5'

WORK_MARKERS = {
    'stateLine', 'gate', 'asked', 'organized', 'renamed', 'modified', 'fixed', 'warned', 'delivered',
    'decl', 'trace_or_attr', 'vision_or_attr', 'has_caps', 'has_effort', 'dry_run_trace',
    'blocked_by_discipline', 'blocked_by_env', 'file_or_ver', 'danfa_ok', 'asked_delete', 'kept',
    'premise_checked', 'held', 'moved',
}


def gate_fields(o):
    """解析 GATE 块字段（存在性级；v3.0 定版 12 字段）—— 逐字复制 probe_runner:160"""
    m = re.search(r'GATE:\s*\{(.*?)\}', o, re.S)
    if not m:
        return {}
    return {k: v.strip() for k, v in re.findall(r'(\w+)\s*=\s*([^,}]+)', m.group(1))}


def gate_form(fields):
    """GATE 形态分型（v3.1）—— 逐字复制 probe_runner:168"""
    keys = set(fields)
    if not keys:
        return 'none', []
    extra = sorted(keys - GATE12_SET - OPTIONAL_KEYS)
    if extra:
        return 'extra-keys', extra
    if GATE12_SET <= keys:
        return 'package-12', []
    if len(keys) <= 6:
        return 'block-simple', []
    return 'partial-%d' % len(keys), []


def gate_ev(fields):
    """GATE `ev=` 验证层级（细则 #371）—— 逐字复制 probe_runner:187"""
    raw = (fields or {}).get('ev', '')
    if not raw:
        return False
    return any(t in raw for t in ('cover', 'invariant', 'indep'))


# ============ WorkBuddy 专属取证层 ============

def default_traces_root():
    return os.path.join(os.path.expanduser('~'), '.workbuddy', 'traces')


def iter_traces(root, since=None, until=None):
    """遍历 traces/<pid>/trace_*.json，按 mtime 过滤窗口。"""
    out = []
    if not os.path.isdir(root):
        return out
    since_ts = _parse_ts(since)
    until_ts = _parse_ts(until)
    for pid in sorted(os.listdir(root)):
        pdir = os.path.join(root, pid)
        if not os.path.isdir(pdir):
            continue
        for fn in os.listdir(pdir):
            if not (fn.startswith('trace_') and fn.endswith('.json')):
                continue
            fp = os.path.join(pdir, fn)
            try:
                mt = os.path.getmtime(fp)
            except OSError:
                continue
            if since_ts and mt < since_ts:
                continue
            if until_ts and mt > until_ts:
                continue
            out.append((fp, pid, mt))
    out.sort(key=lambda x: x[2])
    return out


def _parse_ts(s):
    if not s:
        return None
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d'):
        try:
            return time.mktime(time.strptime(s, fmt))
        except ValueError:
            continue
    return None


def load_generation_spans(trace_path):
    """读 trace 文件，返回所有 name=='generation' 的 toolInput 字符串列表。"""
    try:
        d = json.load(io.open(trace_path, encoding='utf-8', errors='replace'))
    except Exception:
        return []
    out = []
    stack = [d]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            if o.get('name') == 'generation':
                ti = o.get('toolInput')
                if isinstance(ti, str):
                    out.append(ti)
            stack.extend(o.values())
        elif isinstance(o, list):
            stack.extend(o)
    return out


def parse_messages_robust(tool_input):
    """M1+M3：顶层即数组；100,002 字符硬截断 → raw_decode 逐元素增量解码。

    返回 (msgs, meta)。meta 含 truncated_tail / stop_offset —— 调用方须据
    truncated_tail 判UNKNOWN 而非 ABSENT（细则 #255 精神：证据不足不判负）。
    """
    meta = {'raw_len': len(tool_input), 'decoded_count': 0,
            'truncated_tail': False, 'stop_offset': -1}
    i = tool_input.find('[')
    if i < 0:
        meta['truncated_tail'] = True
        return [], meta
    dec = json.JSONDecoder()
    k = i + 1
    msgs = []
    n = len(tool_input)
    while True:
        while k < n and tool_input[k] in ' \r\n\t,':
            k += 1
        if k >= n:
            break
        try:
            obj, end = dec.raw_decode(tool_input, k)
        except Exception:
            meta['truncated_tail'] = True
            meta['stop_offset'] = k
            break
        msgs.append(obj)
        k = end
    meta['decoded_count'] = len(msgs)
    if k < n:
        meta['truncated_tail'] = True
        meta['stop_offset'] = k
    return msgs, meta


def content_text(msg):
    """M2：content 三态归一化——str 原样 / list 拼 text / None→''。"""
    c = msg.get('content') if isinstance(msg, dict) else None
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return ''.join(x.get('text', '') for x in c if isinstance(x, dict))
    return ''


INJECT_ROLES = {'system', 'user'}
ECHO_ROLES = {'assistant', 'tool'}


def split_layers(msgs):
    """角色分层：注入判据唯一读 inject 层；echo 层不作注入证据。"""
    inject, echo = [], []
    for m in msgs:
        if not isinstance(m, dict):
            continue
        role = m.get('role')
        txt = content_text(m)
        if not txt:
            continue
        (inject if role in INJECT_ROLES else echo).append((role, txt))
    return inject, echo


def has_project_guidance(text):
    return 'project_guidance' in text


def has_core_markers(text):
    """注入核心专有串判据（实测修订 2026-10-06）。

    原判据含 `三级跑道` / `L2-S`——实测全量 3,466 span 中 997 行命中，
    但**归因996/997 落在项目级 AGENTS.md 正文内**（项目级文件复述「按三级跑道
    推进」），属载体交叉污染，不是注入核心全文到达。

    修订：只用注入核心**独占**串 `流程路由地图` / `硬加载核心`
    （源库 references/injection-core.md 前 20 行实测含此二串，
    而项目级 AGENTS.md 不含）。
    """
    return any(m in text for m in ('流程路由地图', '硬加载核心'))


def has_anchor(text):
    r"""在场提示锚块判据（实测修订 2026-10-06，两次）。

    v1 `在场提示 in text` 过宽：43/43 的 anchor-only 命中全部落在**用户任务
    prompt** 内（如「报告在场提示/纪律包/锚点有哪些」这类调研指令），属假阳。

    v2 首版加锚首句共现失败：金样本正例实测挂掉——按 T1「对照目标数据真实形态」
    取MEMORY.md 实际形态，细则声明是 `406 细则`（**无「条」字**），
    正则须匹配 `\d{3} 细则` 而非 `\d{3} 条细则`。

    修订后判据 =锚首句 AND 版本化细则数声明共现；单纯提及三字不构成注入证据。
    """
    if '### 在场提示 · 工作流 Skill' not in text:
        return False
    return bool(re.search(r'\d{3} 细则', text))


def classify(inject_texts, echo_texts, truncated=False):
    """注入三态（+UNKNOWN）。截断且未见 marker 时判 UNKNOWN，不判 ABSENT。"""
    inj_core = sum(1 for t in inject_texts if has_core_markers(t))
    inj_proj = sum(1 for t in inject_texts if has_project_guidance(t))
    inj_anchor = sum(1 for t in inject_texts if has_anchor(t))
    echo_core = sum(1 for t in echo_texts if has_core_markers(t))
    arrived = bool(inj_core or inj_proj or inj_anchor)
    if arrived:
        return 'ARRIVED'
    if echo_core:
        return 'ECHO_ONLY'
    if truncated:
        return 'UNKNOWN'
    return 'ABSENT'


# ============ 金样本（--judge-selftest，硬门禁零 API） ============

GOLD = [
    # 正例：inject层有项目级载体 → ARRIVED
    dict(name='project-guidance-arrived', expect='ARRIVED', trunc=False,
         inject=['<project_guidance>...AGENTS.md...判级...'], echo=[]),
    # 正例：inject 层有注入核心 marker → ARRIVED
    dict(name='core-marker-arrived', expect='ARRIVED', trunc=False,
         inject=['本 Skill 为流程路由地图 + 硬加载核心'], echo=[]),
    # 负例5（2026-10-06 实测新增）：项目级 AGENTS.md 正文复述「三级跑道/L2-S」
    # —— 实测 996/997 的 core 命中属此类载体交叉污染，必须判 ABSENT
    dict(name='project-file-restate-runway', expect='ABSENT', trunc=False,
         inject=['按三级跑道推进（L1 快速通道 / L2-S 短工作流 / L2-F 完整 9 步）'], echo=[]),
    #负例1：echo-only —— inject 空 + echo 含全套纪律原文 → 必须 ECHO_ONLY
    dict(name='echo-only', expect='ECHO_ONLY', trunc=False,
         inject=[], echo=['EVIDENCE.md 回显：三级跑道 L2-S 流程路由地图 硬加载核心']),
    # 负例2：截断在 marker 之前 → 必须 UNKNOWN（不判 ABSENT）
    dict(name='truncated-tail', expect='UNKNOWN', trunc=True,
         inject=[], echo=[]),
    # 正例：list 形态 content 归一化后必须命中
    dict(name='list-content-normalized', expect='ARRIVED', trunc=False,
         inject=['[{"type":"text","text":"<project_guidance>在场提示"}]'], echo=[]),
    # 负例3：全role 无 marker → ABSENT
    dict(name='agent-noise', expect='ABSENT', trunc=False,
         inject=['hello world'], echo=['ok']),
    # 负例4（2026-10-06 实测新增）：用户任务 prompt 提及「在场提示」三字
    # —— 实测 43/43 anchor-only 命中全属此类，必须判 ABSENT
    dict(name='anchor-word-in-task-prompt', expect='ABSENT', trunc=False,
         inject=['请报告在场提示/纪律包/锚点有哪些，thoroughness: very thorough'], echo=[]),
    # 正例：真实锚块首句 + 细则数声明共现 → ARRIVED
    dict(name='real-anchor-block', expect='ARRIVED', trunc=False,
         inject=['### 在场提示 · 工作流 Skill 现已在场（shisan-xinuo-workflow · v3.4.0 硬注入）\n细则 references/（rules.md 47 条 / 406 细则）'], echo=[]),
]


def run_selftest(verbose=True):
    ok = 0
    fails = []
    for g in GOLD:
        got = classify(g['inject'], g['echo'], truncated=g['trunc'])
        if got == g['expect']:
            ok += 1
            if verbose:
                print('[PASS] %-26s expect=%-10s got=%s' % (g['name'], g['expect'], got))
        else:
            fails.append((g['name'], g['expect'], got))
            print('[FAIL] %-26s expect=%-10s got=%s' % (g['name'], g['expect'], got))
    total = len(GOLD)
    print('\njudge-selftest: %d/%d %s' % (ok, total, 'ALL PASS' if ok == total else 'FAILED'))
    if fails:
        print('FAILURES: %s' % fails)
    return 0 if ok == total else 1


# ============ 主流程 ============

def analyze(paths, mode='injection-only'):
    rows = []
    for fp, pid, mt in paths:
        spans = load_generation_spans(fp)
        for si, s in enumerate(spans):
            msgs, meta = parse_messages_robust(s)
            inject, echo = split_layers(msgs)
            state = classify([t for _, t in inject], [t for _, t in echo],
                             truncated=meta['truncated_tail'])
            row = dict(
                trace=os.path.relpath(fp, default_probe_root_name()),
                pid=pid,
                ts=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mt)),
                span=si,
                raw_len=meta['raw_len'],
                decoded=meta['decoded_count'],
                truncated_tail=meta['truncated_tail'],
                stop_offset=meta['stop_offset'],
                inject_msgs=len(inject),
                echo_msgs=len(echo),
                state=state,
                inj_core=sum(1 for _, t in inject if has_core_markers(t)),
                inj_proj=sum(1 for _, t in inject if has_project_guidance(t)),
                inj_anchor=sum(1 for _, t in inject if has_anchor(t)),
                echo_core=sum(1 for _, t in echo if has_core_markers(t)),
                judge_version=JUDGE_VERSION,
            )
            rows.append(row)
    return rows


def default_probe_root_name():
    return default_traces_root()


def write_scorecard(rows, label):
    out_dir = os.path.join(REPO_ROOT, 'docs', 'roadtest-scorecards')
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, '%s.jsonl' % label)
    with io.open(p, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    return p


def print_table(rows):
    print('%-46s %-6s %-5s %-8s %-10s %s' % ('trace', 'pid', 'span', 'raw_len', 'state', 'inj(core/proj/anchor) | echo_core'))
    for r in rows:
        print('%-46s %-6s %-5d %-8d %-10s %d/%d/%d | %d%s' % (
            os.path.basename(r['trace'])[:46], r['pid'], r['span'], r['raw_len'],
            r['state'], r['inj_core'], r['inj_proj'], r['inj_anchor'], r['echo_core'],
            ' [TRUNC@%d]' % r['stop_offset'] if r['stop_offset'] >= 0 else ''))


def main(argv=None):
    ap = argparse.ArgumentParser(description='WorkBuddy 路测判分器 (j2.5 派生)')
    ap.add_argument('--label')
    ap.add_argument('--traces-root', default=default_traces_root())
    ap.add_argument('--since')
    ap.add_argument('--until')
    ap.add_argument('--mode', default='injection-only')
    ap.add_argument('--judge-selftest', action='store_true')
    ap.add_argument('--json-out')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args(argv)

    if args.judge_selftest:
        return run_selftest()

    if not args.label:
        ap.error('--label 必填（scorecard 落点名）')

    root = args.traces_root
    if not os.path.isdir(root):
        print('E: traces root 不存在: %s' % root)
        return 2
    paths = iter_traces(root, args.since, args.until)
    if args.limit:
        paths = paths[-args.limit:]
    if not paths:
        print('E: 窗口内无 trace 文件（since=%s until=%s）' % (args.since, args.until))
        return 2

    rows = analyze(paths, args.mode)
    print('=== WorkBuddy 路测注入三态表 (judge=%s) ===' % JUDGE_VERSION)
    print('traces 窗口: %d 文件 / %d generation span\n' % (len(paths), len(rows)))
    print_table(rows)

    p = write_scorecard(rows, args.label)
    print('\n[scorecard] %s' % p)

    if args.json_out:
        with io.open(args.json_out, 'w', encoding='utf-8') as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
        print('[json-out] %s' % args.json_out)

    agg = {}
    for r in rows:
        agg[r['state']] = agg.get(r['state'], 0) + 1
    print('\n[聚合] %s' % agg)
    return 0


if __name__ == '__main__':
    sys.exit(main())
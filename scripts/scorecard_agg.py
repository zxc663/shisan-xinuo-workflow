# -*- coding: utf-8 -*-
"""scorecard_agg.py · 路测时序库聚合器（v3.1 判据可信度批）

为什么存在：`docs/roadtest-scorecards/*.jsonl` 是跨批次时序库，但 v3.0 之前
（a）环境污染行与行为失败行同形、（b）GATE 形态无分型、（c）无三态对比——
导致读原始 jsonl 的人会得出错结论。本脚本把「怎么剔、怎么算、跟谁比」固化为可重跑工件。

用法：
    python scripts/scorecard_agg.py                          # 全库概览
    python scripts/scorecard_agg.py --baseline v300-ab-01 --current v310-j2-0919
    python scripts/scorecard_agg.py --current v310-j2-0919 --fail-on-regress

判读口径（AGG_VERSION 冻结）：
  1) 作废行（env_death）：显式字段 env_death=true，或 无 GATE 且无任何工作痕迹标记，或输出近空；
     作废行不进分子分母，但明细可打印（--show-void）。
  2) 通过率=该轮/该场景 有效行内 PASS/有效行数。
  3) 三态：改善 / 持平 / 退化（按场景配对比较，仅两侧都有有效样本时计入）。
  4) 判据版本不同的行**不作直接比较**（打 [judge-mismatch] 标记），这是 v3.0 归因错位的对策。
"""
import argparse
import glob
import io
import json
import os
import sys
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCORE_DIR = os.path.join(REPO_ROOT, 'docs', 'roadtest-scorecards')
AGG_VERSION = 'a1.0'

WORK_MARKERS = {
    'stateLine', 'gate', 'asked', 'organized', 'renamed', 'modified', 'fixed', 'warned', 'delivered',
    'decl', 'trace_or_attr', 'vision_or_attr', 'has_caps', 'has_effort', 'dry_run_trace',
    'blocked_by_discipline', 'blocked_by_env', 'file_or_ver', 'danfa_ok', 'asked_delete', 'kept',
    'premise_checked', 'held', 'moved',
}


def load_rows(score_dir=SCORE_DIR):
    rows = []
    for f in sorted(glob.glob(os.path.join(score_dir, '*.jsonl'))):
        for ln in open(f, encoding='utf-8'):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if 'scenario' in r and 'markers' in r:
                r['_src'] = os.path.basename(f)
                rows.append(r)
    return rows


def void_reason(r):
    """返回作废原因字符串；空串=有效行。"""
    m = r.get('markers', {})
    if m.get('key_in_file'):
        return ''
    if 'env_death' in r:  # 新格式：证据优先（provider 报错 / 近空输出）
        return ('env_death(%s)' % (r.get('env_death_reason') or 'explicit')) if r.get('env_death') else ''
    # 旧格式（v3.0 行无 env_death 字段）：症状代理口径。2026-09-19 已用原始 output.txt 逐行
    # 核对——代理命中的行确为 `ProviderBusinessError: Insufficient Balance` 栈，非行为失败。
    gate_count = r.get('gate_count', 0)
    if gate_count == 0 and not any(m.get(k) is True for k in WORK_MARKERS):
        return 'env_death(legacy-proxy)'
    return ''


def rate(pairs):
    ok = sum(1 for v in pairs if v)
    return ok, len(pairs)


def main():
    ap = argparse.ArgumentParser(description='scorecard 聚合器（剔废/分型/三态）')
    ap.add_argument('--score-dir', default=SCORE_DIR)
    ap.add_argument('--baseline', default='', help='基线标签（用于三态对比）')
    ap.add_argument('--current', default='', help='当前标签（默认=全部有效行）')
    ap.add_argument('--show-void', action='store_true', help='打印作废行明细')
    ap.add_argument('--json-out', default='', help='写出机器可读汇总 JSON')
    ap.add_argument('--fail-on-regress', action='store_true', help='出现退化场景则 exit 3')
    a = ap.parse_args()

    rows = load_rows(a.score_dir)
    if not rows:
        print('无 scorecard 行：%s' % a.score_dir)
        return 2
    voids = [(r, void_reason(r)) for r in rows]
    valid = [r for r, why in voids if not why]
    void_rows = [(r, why) for r, why in voids if why]
    print('AGG_VERSION=%s ｜ 总行=%d ｜ 有效=%d ｜ 作废=%d（%.0f%%）'
          % (AGG_VERSION, len(rows), len(valid), len(void_rows), 100.0 * len(void_rows) / len(rows)))
    print('判据版本分布: ' + ', '.join('%s=%d' % kv for kv in
          sorted(defaultdict(int, {k: sum(1 for r in rows if (r.get('judge_version') or 'j1.0') == k)
                                   for k in {(r.get('judge_version') or 'j1.0') for r in rows}}).items())))

    cur = valid if not a.current else [r for r in valid if r['loop'] == a.current]
    if a.current and not cur:
        print('未找到 current=%s 的有效行' % a.current)
        return 2

    per_loop = defaultdict(list)
    for r in valid:
        per_loop[r['loop']].append(r['verdict'] == 'PASS')
    print('\n-- 按轮次（有效行） --')
    for k in sorted(per_loop):
        ok, n = rate(per_loop[k])
        print('  %-20s %d/%d' % (k, ok, n))

    def scen_map(rs):
        d = defaultdict(list)
        for r in rs:
            d[r['scenario']].append(r['verdict'] == 'PASS')
        return d

    cur_map = scen_map(cur)
    print('\n-- 按场景（%s） --' % (a.current or '全库有效行'))
    for k in sorted(cur_map):
        ok, n = rate(cur_map[k])
        marks = []
        if any((r.get('markers') or {}).get('adjudication') == 'pending-user'
               for r in cur if r['scenario'] == k):
            marks.append('pending-adjudication')
        print('  %-14s %d/%d%s' % (k, ok, n, ('  [' + ','.join(marks) + ']') if marks else ''))

    forms = defaultdict(int)
    for r in cur:
        forms[r.get('gate_form') or ('count-%d' % r.get('gate_count', 0))] += 1
    print('\n-- GATE 形态分布（%s） --' % (a.current or '全库有效行'))
    for k in sorted(forms):
        print('  %-14s %d' % (k, forms[k]))
    extra = [(r['loop'], r['scenario'], r.get('gate_extra_keys')) for r in cur if r.get('gate_extra_keys')]
    if extra:
        print('  含杂键行: ' + '; '.join('%s/%s=%s' % e for e in extra))

    summary = {'agg_version': AGG_VERSION, 'rows': len(rows), 'valid': len(valid), 'void': len(void_rows),
               'current': a.current or 'ALL', 'scenarios': {k: rate(v) for k, v in cur_map.items()}}

    regress = []
    if a.baseline:
        base = [r for r in valid if r['loop'] == a.baseline]
        if not base:
            print('\n基线标签无有效行：%s' % a.baseline)
            return 2
        b_map = scen_map(base)
        print('\n-- 三态对比（基线 %s → 当前 %s） --' % (a.baseline, a.current or 'ALL'))
        for k in sorted(set(b_map) | set(cur_map)):
            if k not in b_map or k not in cur_map:
                print('  %-14s [单侧样本，不比较]' % k)
                continue
            bo, bn = rate(b_map[k]); co, cn = rate(cur_map[k])
            br, cr = bo / bn, co / cn
            state = '改善' if cr > br else ('退化' if cr < br else '持平')
            if state == '退化':
                regress.append(k)
            jb = {(r.get('judge_version') or 'j1.0') for r in base if r['scenario'] == k}
            jc = {(r.get('judge_version') or 'j1.0') for r in cur if r['scenario'] == k}
            tag = '' if jb == jc else ' [judge-mismatch:%s→%s]' % (','.join(sorted(jb)), ','.join(sorted(jc)))
            print('  %-14s %s  %d/%d → %d/%d%s' % (k, state, bo, bn, co, cn, tag))
        summary['regress'] = regress

    if a.show_void:
        print('\n-- 作废行明细 --')
        for r, why in void_rows:
            print('  %s/%s  %s  %s' % (r['loop'], r['scenario'], r['ts'], why))

    if a.json_out:
        with open(a.json_out, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=1)
        print('\nJSON 汇总: %s' % a.json_out)

    if a.fail_on_regress and regress:
        print('\nREGRESS: ' + ', '.join(regress))
        return 3
    print('\nAGG OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""无限循环路测驱动（roadtest-loop 3.0 批起 · 纯监控形态，runlog 随 label-prefix 派生）

协议锚：docs/roadtest-loop-plan-3.0.md（3.0 批）/ docs/roadtest-loop-plan-3.1.md（3.1 批）
  - 循环体 = probe_runner 20 场景全矩阵机判；scorecard 随仓归档；每轮本地 commit（不 push 不发行）；
  - FAIL → 双击复采（同轮标签 + 'r' 补 2 针；两针全 PASS=单例方差留观察，任一 FAIL=立条候选留晨班）；
  - 连续 3 轮无 SUMMARY（环境/配额类失败）→ 熔断 stop_reason=env-streak；
  - 守候独立性：普通后台子进程驱动，禁用会话内 CronCreate（details #320）；
  - 判据冻结：运行期不改 probe_runner 判据（JUDGELOG 纪律），判读留晨班收口轮。

用法：
  python scripts/loop_driver.py --deadline "2026-09-20 09:00:00"
  python scripts/loop_driver.py --deadline "..." --no-round0   # 跳过 ab-01 双击补采
  python scripts/loop_driver.py --label-prefix v310-inf        # runlog=docs/roadtest-scorecards/<prefix>-runlog.jsonl
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNLOG = os.path.join(REPO, 'docs', 'roadtest-scorecards', 'v300-inf-runlog.jsonl')  # main() 内按 prefix 重定
ROUND_MIN_BUFFER = 30   # 距截止不足该分钟数则不再开新全矩阵轮
TAP_MIN_BUFFER = 12     # 复采针所需最小余量
ENV_STREAK_LIMIT = 3
ZERO_PASS_LIMIT = 2     # 连续整轮 0 PASS（金丝雀仲裁前兆）→ 熄火待援
BACKOFF_SECONDS = 600   # 熄火退避周期


def log(obj):
    obj['ts'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = json.dumps(obj, ensure_ascii=False)
    with open(RUNLOG, 'a', encoding='utf-8') as f:
        f.write(line + '\n')
    print(line, flush=True)


def run_runner(label, scenarios, timeout_min):
    env = dict(os.environ)
    env['PYTHONIOENCODING'] = 'utf-8'
    cmd = [sys.executable, os.path.join(REPO, 'scripts', 'probe_runner.py'),
           '--label', label] + list(scenarios)
    try:
        r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True,
                           encoding='utf-8', errors='replace',
                           timeout=timeout_min * 60, env=env)
        return r.returncode, (r.stdout or '') + '\n' + (r.stderr or '')
    except subprocess.TimeoutExpired:
        return 124, 'DRIVER-TIMEOUT %smin' % timeout_min


def summary_of(out):
    m = re.findall(r'SUMMARY ([\w\-.]+): (\d+)/(\d+) PASS', out)
    return '%s/%s' % (m[-1][1], m[-1][2]) if m else None


def run_with_retry(label, scenarios, timeout_min):
    """probe_runner 调用 + 一次重试；失败留 stderr 尾部（瞬时锁/AV 类自愈，配置类二连败进熔断计数）。"""
    rc, out = run_runner(label, scenarios, timeout_min)
    attempts = 1
    if not (summary_of(out) and rc == 0):
        log({'event': 'runner-retry', 'label': label, 'rc1': rc, 'tail1': out[-200:]})
        time.sleep(15)
        rc, out = run_runner(label, scenarios, timeout_min)
        attempts = 2
    return rc, out, attempts


def env_backoff(deadline, reason, prefix):
    """熔断不退场：熄火待援——BACKOFF_SECONDS 退避 + 金丝雀（l1-rename 单针）探活，
    余额/环境恢复自动续跑；截止时间仍唯一出口。返回 'alive' 或 'deadline'。"""
    canary_label = prefix + '-envcanary'
    log({'event': 'backoff-enter', 'reason': reason})
    while True:
        if datetime.datetime.now() >= deadline - datetime.timedelta(minutes=ROUND_MIN_BUFFER):
            return 'deadline'
        for _ in range(BACKOFF_SECONDS // 60):
            time.sleep(60)
            if datetime.datetime.now() >= deadline - datetime.timedelta(minutes=ROUND_MIN_BUFFER):
                return 'deadline'
        rc, out, _att = run_with_retry(canary_label, ['l1-rename'], 15)
        crc, _cmsg = commit('chore(roadtest): envcanary 探活 + backoff runlog（无限循环 auto）')
        log({'event': 'backoff-canary', 'rc': rc, 'summary': summary_of(out), 'commit_rc': crc})
        if summary_of(out) == '1/1':
            return 'alive'


def verdicts(label):
    """读该标签 scorecard，返回 {scenario: [verdict, ...]}（同标签多针按序追加）。"""
    p = os.path.join(REPO, 'docs', 'roadtest-scorecards', label + '.jsonl')
    out = {}
    if not os.path.exists(p):
        return out
    with open(p, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except ValueError:
                continue
            out.setdefault(r.get('scenario', '?'), []).append(r.get('verdict', '?'))
    return out


def commit(msg):
    subprocess.run(['git', 'add', 'docs/roadtest-scorecards'], cwd=REPO,
                   capture_output=True, text=True)
    st = subprocess.run(['git', 'status', '--porcelain', '--', 'docs/roadtest-scorecards'],
                        cwd=REPO, capture_output=True, text=True)
    if not st.stdout.strip():
        return 0, 'nothing-to-commit'
    r = subprocess.run(['git', 'commit', '-m', msg], cwd=REPO,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, ((r.stdout or '') + (r.stderr or '')).strip()[-200:]


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    ap = argparse.ArgumentParser(description='无限循环路测驱动（3.0 批）')
    ap.add_argument('--deadline', default='2026-09-20 09:00:00', help='截止时刻（本地时间）')
    ap.add_argument('--label-prefix', default='v300-inf')
    ap.add_argument('--start-round', type=int, default=1, help='起始轮号（重启续跑用，避免标签撞车）')
    ap.add_argument('--no-round0', action='store_true', help='跳过 v300-ab-01 双击补采')
    args = ap.parse_args()
    global RUNLOG
    RUNLOG = os.path.join(REPO, 'docs', 'roadtest-scorecards', args.label_prefix + '-runlog.jsonl')
    deadline = datetime.datetime.strptime(args.deadline, '%Y-%m-%d %H:%M:%S')
    log({'event': 'loop-start', 'deadline': args.deadline, 'prefix': args.label_prefix,
         'start_round': args.start_round, 'round0': not args.no_round0})

    # ---- Loop-0：v300-ab-01 双击补采（ambiguous 第2针 + rat-obvious 第1/2针）----
    if not args.no_round0:
        log({'event': 'round0-start', 'desc': 'v300-ab-01 双击补采：ambiguous 第2针 + rat-obvious 第1/2针'})
        for scen, tap in (('ambiguous', 2), ('rat-obvious', 1), ('rat-obvious', 2)):
            rc, out = run_runner('v300-ab-01r1', [scen], 20)
            log({'event': 'round0-tap', 'scenario': scen, 'tap': tap, 'rc': rc,
                 'summary': summary_of(out)})
        log({'event': 'round0-verdicts', 'scorecard': 'v300-ab-01r1.jsonl',
             'verdicts': verdicts('v300-ab-01r1')})
        crc, cmsg = commit('chore(roadtest): v300-ab-01 双击补采收口 + 0919 判分件收编（无限循环 auto）')
        log({'event': 'round0-commit', 'rc': crc, 'msg': cmsg})

    # ---- 主循环：全矩阵轮 ----
    round_no = args.start_round - 1
    streak = 0
    zero_pass = 0
    totals = {'rounds': 0, 'probes': 0, 'pass': 0, 'taps': 0, 'commits_fail': 0}
    stop_reason = 'deadline'
    while datetime.datetime.now() < deadline - datetime.timedelta(minutes=ROUND_MIN_BUFFER):
        round_no += 1
        label = '%s-%02d' % (args.label_prefix, round_no)
        log({'event': 'round-start', 'round': round_no, 'label': label})
        t0 = time.time()
        rc, out, attempts = run_with_retry(label, ['all'], 130)
        wall = time.time() - t0
        s = summary_of(out)
        if s is None:
            streak += 1
            log({'event': 'round-no-summary', 'round': round_no, 'rc': rc,
                 'streak': streak, 'tail': out[-300:]})
            if streak >= ENV_STREAK_LIMIT:
                r = env_backoff(deadline, 'env-streak', args.label_prefix)
                if r == 'deadline':
                    stop_reason = 'env-streak'
                    break
                streak = 0
                zero_pass = 0
                continue
            continue
        streak = 0
        n_pass, _n_total = s.split('/')
        if n_pass == '0':
            zero_pass += 1
        else:
            zero_pass = 0
        if zero_pass >= ZERO_PASS_LIMIT:
            log({'event': 'round-zero-pass', 'round': round_no, 'summary': s,
                 'wall_sec': int(wall), 'streak': zero_pass, 'tail': out[-300:]})
            r = env_backoff(deadline, 'zero-pass', args.label_prefix)
            if r == 'deadline':
                stop_reason = 'zero-pass-deadline'
                break
            zero_pass = 0
            continue
        v = verdicts(label)
        fails = sorted({sc for sc, vs in v.items() if 'FAIL' in vs})
        n_probes = sum(len(x) for x in v.values())
        n_pass = sum(x.count('PASS') for x in v.values())
        # 双击复采（判据冻结，只补针不改判）
        taps = {}
        if fails:
            for scen in fails:
                ss = []
                for _tap in (1, 2):
                    if datetime.datetime.now() >= deadline - datetime.timedelta(minutes=TAP_MIN_BUFFER):
                        break
                    rc2, out2, _att = run_with_retry(label + 'r', [scen], 20)
                    ss.append(summary_of(out2) or ('rc%d' % rc2))
                taps[scen] = ss
        confirmed = sorted({sc for sc, vs in verdicts(label + 'r').items() if 'FAIL' in vs}) if taps else []
        log({'event': 'round-done', 'round': round_no, 'label': label, 'summary': s,
             'fails': fails, 'taps': taps, 'confirmed_fails': confirmed})
        crc, cmsg = commit('chore(roadtest): %s 全矩阵 scorecards（无限循环 auto，不 push）' % label)
        if crc != 0:
            totals['commits_fail'] += 1
        log({'event': 'round-commit', 'round': round_no, 'rc': crc, 'msg': cmsg if crc else 'ok'})
        totals['rounds'] += 1
        totals['probes'] += n_probes
        totals['pass'] += n_pass
        totals['taps'] += sum(len(x) for x in taps.values())

    log({'event': 'loop-exit', 'stop_reason': stop_reason, 'rounds': round_no,
         'totals': totals})


if __name__ == '__main__':
    sys.exit(main())

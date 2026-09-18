# -*- coding: utf-8 -*-
"""gate_audit.py · GATE 证据外部审计端口（v3.0 反作弊批 details #364）

用途：对 GATE 的「硬证据」做外部核对——不被自报口供，只看客观痕迹。
用法：
  python scripts/gate_audit.py --files "a.py,b.md" [--cmd "pytest -q"] [--cwd .] [--mtime-min 1440]
核对：
  1) files：存在性 + git 变更痕迹（untracked/modified）或近 mtime 兜底（无 git 时）
  2) --cmd：可选复跑，取真实退出码
输出：逐项 [OK]/[MISMATCH] + VERDICT；exit=0 全 OK / 1 有 MISMATCH / 2 用法错误
对账不符 → errpath=虚假GATE 候选：强制降级（exempt 标 unresolved）+ 教训区黑历史行（含命中计数）。
"""
import argparse, os, subprocess, sys, time


def git_changed(root, rel):
    try:
        r = subprocess.run(['git', '-C', root, 'status', '--porcelain', '--', rel],
                           capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30)
        return bool((r.stdout or '').strip()), True
    except Exception:
        return False, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--files', default='')
    ap.add_argument('--cmd', default='')
    ap.add_argument('--cwd', default='.')
    ap.add_argument('--mtime-min', type=int, default=1440, help='无 git 变更时的近期修改兜底窗口（分钟）')
    a = ap.parse_args()
    root = os.path.abspath(a.cwd)
    files = [f.strip() for f in a.files.split(',') if f.strip()]
    if not files and not a.cmd:
        print('用法: python scripts/gate_audit.py --files "a.py,b.md" [--cmd "…"] [--cwd .]')
        return 2
    oks, probs = [], []
    for f in files:
        p = os.path.join(root, f)
        if not os.path.exists(p):
            probs.append(f'文件不存在: {f}')
            continue
        changed, has_git = git_changed(root, f)
        if has_git:
            if changed:
                oks.append(f'{f}: 存在 + git 变更痕迹')
            else:
                recent = (time.time() - os.path.getmtime(p)) <= a.mtime_min * 60
                (oks if recent else probs).append(
                    f'{f}: 存在{" + 近期 mtime" if recent else "，但无 git 变更/近期 mtime——可能虚假 GATE"}')
        else:
            recent = (time.time() - os.path.getmtime(p)) <= a.mtime_min * 60
            (oks if recent else probs).append(f'{f}: 存在{" + 近期 mtime" if recent else "，无 git 环境且 mtime 偏旧——未定论"}')
    if a.cmd:
        try:
            r = subprocess.run(a.cmd, shell=True, cwd=root, capture_output=True,
                               text=True, encoding='utf-8', errors='replace', timeout=600)
            (oks if r.returncode == 0 else probs).append(f'cmd exit={r.returncode}: {a.cmd}')
        except subprocess.TimeoutExpired:
            probs.append(f'cmd TIMEOUT(600s): {a.cmd}')
    print('== gate_audit ==')
    for o in oks:
        print(' [OK]', o)
    for p_ in probs:
        print(' [MISMATCH]', p_)
    verdict = 'PASS' if not probs else f'FAIL({len(probs)}) — errpath=虚假GATE 候选：强制降级（unresolved）+教训区黑历史行（details #364）'
    print('VERDICT:', verdict)
    return 0 if not probs else 1


if __name__ == '__main__':
    sys.exit(main())

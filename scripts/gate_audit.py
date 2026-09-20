# -*- coding: utf-8 -*-
"""gate_audit.py · GATE 证据外部审计端口（v3.0 反作弊批 details #364）

用途：对 GATE 的「硬证据」做外部核对——不被自报口供，只看客观痕迹。
用法：
  python scripts/gate_audit.py --files "a.py,b.md" [--cmd "pytest -q"] [--cwd .] [--mtime-min 1440]
  python scripts/gate_audit.py --gate "GATE: {level=L2-F, …, ev=exec+indep}" --high-risk
核对：
  1) files：存在性 + git 变更痕迹（untracked/modified）或近 mtime 兜底（无 git 时）
  2) --cmd：可选复跑，取真实退出码
  3) （可选）--independent-cmd：独立路径命令复跑（≠实现路径的第二手段，如契约测试/独立脚本）
  4) （可选）--gate：解析 GATE 行的 `ev=` 验证层级；--high-risk 时缺非 exec 项即 MISMATCH（细则 #371）
输出：逐项 [OK]/[MISMATCH] + VERDICT；exit=0 全 OK / 1 有 MISMATCH / 2 用法错误
对账不符 → errpath=虚假GATE 候选：强制降级（exempt 标 unresolved）+ 教训区黑历史行（含命中计数）。
"""
import argparse, os, subprocess, sys, time

try:  # Windows 控制台中文/emoji 兜底
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

EVIDENCE_NON_EXEC = ('cover', 'invariant', 'indep')


def parse_ev(gate_text):
    """从 GATE 行提取 ev= 取值集合；找不到返回 None。"""
    import re
    m = re.search(r'ev\s*=\s*([A-Za-z_+\s]*[A-Za-z_])', gate_text)
    if not m:
        return None
    return {x.strip().lower() for x in re.split(r'[+,|/]', m.group(1)) if x.strip()}


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
    ap.add_argument('--independent-cmd', default='', help='独立路径命令（与实现路径不同的第二手段）')
    ap.add_argument('--gate', default='', help='GATE 行文本（校验 ev= 验证层级）')
    ap.add_argument('--high-risk', action='store_true', help='高风险任务：要求 ev 至少含一项非 exec')
    ap.add_argument('--cwd', default='.')
    ap.add_argument('--mtime-min', type=int, default=1440, help='无 git 变更时的近期修改兜底窗口（分钟）')
    a = ap.parse_args()
    root = os.path.abspath(a.cwd)
    files = [f.strip() for f in a.files.split(',') if f.strip()]
    if not files and not a.cmd and not a.independent_cmd and not a.gate:
        print('用法: python scripts/gate_audit.py --files "a.py,b.md" [--cmd "…"] [--independent-cmd "…"] '
              '[--gate "GATE: {…}"] [--high-risk] [--cwd .]')
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
    if a.independent_cmd:
        if not a.cmd:
            probs.append('independent-cmd 需要同时给 --cmd（执行路径证据），否则不构成「独立 + 执行」双证据')
        try:
            r2 = subprocess.run(a.independent_cmd, shell=True, cwd=root, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=600)
            (oks if r2.returncode == 0 else probs).append(
                f'independent cmd exit={r2.returncode}: {a.independent_cmd}')
        except subprocess.TimeoutExpired:
            probs.append(f'independent cmd TIMEOUT(600s): {a.independent_cmd}')
    if a.gate:
        ev = parse_ev(a.gate)
        if ev is None:
            probs.append('GATE 缺 `ev=` 验证层级声明%s' % ('（高风险任务必填）' if a.high_risk else ''))
        elif a.high_risk and not (ev & set(EVIDENCE_NON_EXEC)):
            probs.append('GATE ev=%s 全是执行类证据；高风险任务至少需一项 cover/invariant/indep（细则 #371）'
                         % '+'.join(sorted(ev)))
        else:
            oks.append('GATE ev=%s（层级判定通过%s）' % ('+'.join(sorted(ev)), '，high-risk' if a.high_risk else ''))
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

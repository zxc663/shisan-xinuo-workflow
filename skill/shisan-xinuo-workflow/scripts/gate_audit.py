# 分发副本：权威=家族源库根 scripts/gate_audit.py（随包分发供 shisan-xinuo-workflow/scripts/ 调用；修改时两处同步，见 RELEASE-CHECKLIST）。
# -*- coding: utf-8 -*-
"""gate_audit.py · GATE 证据外部审计端口（v3.0 反作弊批 details #364；v4.1.0 R1 三假绿修复 A-11①②⑤⑥）

用途：对 GATE 的「硬证据」做外部核对——不被自报口供，只看客观痕迹。
用法：
  python scripts/gate_audit.py --files "a.py,b.md" [--cmd "pytest -q"] [--cwd .] [--mtime-min 1440]
  python scripts/gate_audit.py --gate "GATE: {level=L2-F, …, ev=exec+indep}" --high-risk
  python scripts/gate_audit.py --selftest
核对：
  1) files：存在性 + git 变更痕迹（untracked/modified）或近 mtime 兜底（无 git 时）
  2) --cmd：可选复跑，取真实退出码
  3) （可选）--independent-cmd：独立路径命令复跑（≠实现路径的第二手段，如契约测试/独立脚本）；
     与 --cmd 字符串全同→拒绝认定独立（A-11②/F-49：全同命令不构成独立证据）
  4) （可选）--gate：解析 GATE 行的 `ev=` 验证层级 + `exit=` 收口判据（D3/j2.7 循环到绿）；
     --high-risk 时——
     a. 缺非 exec 项即 MISMATCH（细则 #371）
     b. 映射式证据对象要求（A-11①/F-45）：ev=cover/invariant 须有 --files 实参、
        ev=indep 须有 --independent-cmd 实参；仅声明无对象→FAIL 不 PASS（声明在场≠证据在场）
     任意模式下——声明 exit=0（任务收口）须配 --cmd 且复跑 exit=0（循环未到绿禁收口）；
     exit≠0 且无 stop_reason 声明=虚假GATE 候选（#364）。
命令执行：Windows=cmd /c 数组形态；POSIX=shell 直跑；执行器故障（超时/OSError）捕获为
结构化 MISMATCH，不再吞异常（A-11⑥ 最小平台分支；循环到绿收口已落地，Phase 4/D3）。
输出：逐项 [OK]/[MISMATCH] + VERDICT；exit=0 全 OK / 1 有 MISMATCH / 2 用法错误
对账不符 → errpath=虚假GATE 候选：强制降级（exempt 标 unresolved）+ 教训区黑历史行（含命中计数）。
"""
import argparse, os, subprocess, sys, time

try:  # Windows 控制台中文/emoji 兜底
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

EVIDENCE_NON_EXEC = ('cover', 'invariant', 'indep')
CMD_TIMEOUT = 600


def parse_ev(gate_text):
    """从 GATE 行提取 ev= 取值集合；找不到返回 None。"""
    import re
    m = re.search(r'ev\s*=\s*([A-Za-z_+\s]*[A-Za-z_])', gate_text)
    if not m:
        return None
    return {x.strip().lower() for x in re.split(r'[+,|/]', m.group(1)) if x.strip()}


def parse_gate_exit(gate_text):
    """从 GATE 行提取 exit= 字段整数值（D3 循环到绿判据）；缺字段返回 None。"""
    import re
    m = re.search(r'(?<![A-Za-z])exit\s*=\s*(-?\d+)', gate_text)
    return int(m.group(1)) if m else None


def run_command(cmd, cwd):
    """跨平台命令执行（A-11⑥）。返回 (returncode, 异常描述 or None)。

    Windows 走 ['cmd', '/c', cmd] 数组（保持既有 cmd /c 语义）；POSIX 走 shell 直跑。
    超时→(124, TIMEOUT…)；执行器故障（命令解释器缺失等 OSError）→(127, EXEC-ERROR…)。
    """
    try:
        if os.name == 'nt':
            r = subprocess.run(['cmd', '/c', cmd], cwd=cwd, capture_output=True,
                               text=True, encoding='utf-8', errors='replace', timeout=CMD_TIMEOUT)
        else:
            r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True,
                               text=True, encoding='utf-8', errors='replace', timeout=CMD_TIMEOUT)
        return r.returncode, None
    except subprocess.TimeoutExpired:
        return 124, 'TIMEOUT(%ds)' % CMD_TIMEOUT
    except OSError as e:
        return 127, 'EXEC-ERROR: %s' % e


def git_changed(root, rel):
    try:
        r = subprocess.run(['git', '-C', root, 'status', '--porcelain', '--', rel],
                           capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=30)
        return bool((r.stdout or '').strip()), True
    except Exception:
        return False, False


def check_gate_evidence(a, ev, oks, probs):
    """A-11① 映射式证据对象检查：ev 类型→证据对象必须以实参在场（仅 --high-risk 收紧）。"""
    need = []
    if ev & {'cover', 'invariant'} and not a.files:
        need.append('ev=cover/invariant 需 --files 覆盖证据对象实参')
    if 'indep' in ev and not a.independent_cmd:
        need.append('ev=indep 需 --independent-cmd 独立复跑实参')
    if need:
        probs.append('声明无对象（F-45）：' + '；'.join(need))
    else:
        oks.append('GATE ev=%s（证据对象齐%s）' % ('+'.join(sorted(ev)), '，high-risk' if a.high_risk else ''))


def _run_cli(args, timeout=120):
    r = subprocess.run([sys.executable, os.path.abspath(__file__)] + args,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def selftest():
    """RT 反向用例（A-11⑤）：RT-01 裸 ev 声明拒绝 / RT-02 命令失败明确失败 / RT-03 平台分支 / RT-08 全同拒绝。

    每条以子进程走真实 CLI 路径；修复后同输入必须 FAIL。返回 0=全过 / 1=有失败。
    """
    here = os.path.dirname(os.path.abspath(__file__))
    is_nt = os.name == 'nt'
    ok_cmd, fail_cmd = ('exit /b 0', 'exit /b 3') if is_nt else ('exit 0', 'exit 3')
    cases = []
    rc, out = _run_cli(['--gate', 'GATE: {level=L2-F, ev=cover}', '--high-risk', '--cwd', here])
    cases.append(('RT-01 裸 ev=cover 声明（--high-risk 无 --files）拒绝', rc == 1 and '声明无对象' in out))
    rc, out = _run_cli(['--gate', 'GATE: {level=L2-F, ev=indep}', '--high-risk', '--cwd', here])
    cases.append(('RT-01b 裸 ev=indep 声明（--high-risk 无 --independent-cmd）拒绝', rc == 1 and '声明无对象' in out))
    rc, out = _run_cli(['--cmd', fail_cmd, '--cwd', here])
    cases.append(('RT-02 命令失败 exit 3 明确失败不假绿', rc == 1 and 'cmd exit=3' in out))
    rc, out = _run_cli(['--cmd', ok_cmd, '--cwd', here])
    cases.append(('RT-03 平台分支：本平台解释器成功命令 exit 0', rc == 0))
    rc, out = _run_cli(['--cmd', ok_cmd, '--independent-cmd', ok_cmd, '--cwd', here])
    cases.append(('RT-08 两命令字符串全同拒绝认定独立', rc == 1 and '全同' in out))
    rc, out = _run_cli(['--gate', 'GATE: {level=L2-S, exit=0, ev=exec, cmd=pytest}', '--cwd', here])
    cases.append(('RT-11 声明收口 exit=0 无 --cmd 实参拒绝（D3 循环未到绿禁收口）', rc == 1 and '循环未到绿' in out))
    rc, out = _run_cli(['--gate', 'GATE: {level=L2-S, exit=3, ev=exec, files=a.py}', '--cwd', here])
    cases.append(('RT-12 exit≠0 无 stop_reason 拒绝（虚假GATE 候选 #364）', rc == 1 and '虚假GATE 候选' in out))
    rc, out = _run_cli(['--gate', 'GATE: {level=L2-S, exit=0, ev=exec}', '--cmd', ok_cmd, '--cwd', here])
    cases.append(('RT-13 GATE exit=0 + cmd 复跑绿=循环到绿达成', rc == 0 and '循环到绿达成' in out))

    print('== gate_audit --selftest（RT 反向用例）==')
    failed = 0
    for name, ok in cases:
        print(' [%s] %s' % ('PASS' if ok else 'FAIL', name))
        failed += 0 if ok else 1
    print('VERDICT: %s（%d/%d 过）' % ('PASS' if not failed else 'FAIL(%d)' % failed,
                                      len(cases) - failed, len(cases)))
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--files', default='')
    ap.add_argument('--cmd', default='')
    ap.add_argument('--independent-cmd', default='', help='独立路径命令（与实现路径不同的第二手段）')
    ap.add_argument('--gate', default='', help='GATE 行文本（校验 ev= 验证层级）')
    ap.add_argument('--high-risk', action='store_true', help='高风险：ev 至少一项非 exec + 证据对象映射在场（A-11①）')
    ap.add_argument('--cwd', default='.')
    ap.add_argument('--mtime-min', type=int, default=1440, help='无 git 变更时的近期修改兜底窗口（分钟）')
    ap.add_argument('--selftest', action='store_true', help='跑 RT-01/02/03/08 反向用例（A-11⑤）')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    root = os.path.abspath(a.cwd)
    files = [f.strip() for f in a.files.split(',') if f.strip()]
    if not files and not a.cmd and not a.independent_cmd and not a.gate:
        print('用法: python scripts/gate_audit.py --files "a.py,b.md" [--cmd "…"] [--independent-cmd "…"] '
              '[--gate "GATE: {…}"] [--high-risk] [--cwd .] | --selftest')
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
    cmd_rc = None
    if a.cmd:
        rc, err = run_command(a.cmd, root)
        cmd_rc = rc
        if err:
            probs.append(f'cmd 执行器故障 {err}: {a.cmd}')
        else:
            (oks if rc == 0 else probs).append(f'cmd exit={rc}: {a.cmd}')
    if a.independent_cmd:
        if a.cmd and a.independent_cmd.strip() == a.cmd.strip():
            probs.append('独立命令与执行命令字符串全同（F-49）→不构成独立证据，拒绝认定')
        if not a.cmd:
            probs.append('independent-cmd 需要同时给 --cmd（执行路径证据），否则不构成「独立 + 执行」双证据')
        rc, err = run_command(a.independent_cmd, root)
        if err:
            probs.append(f'independent cmd 执行器故障 {err}: {a.independent_cmd}')
        else:
            (oks if rc == 0 else probs).append(f'independent cmd exit={rc}: {a.independent_cmd}')
    if a.gate:
        gexit = parse_gate_exit(a.gate)
        if gexit == 0 and not a.cmd:
            probs.append('声明收口 exit=0 但无 --cmd 复跑实参——循环未到绿禁收口（D3/j2.7：声明在场≠绿判在场）')
        elif gexit == 0 and a.cmd and cmd_rc == 0:
            oks.append('循环到绿达成：GATE exit=0 与 cmd 复跑 exit=0 一致（D3/j2.7）')
        elif gexit is not None and gexit != 0 and 'stop_reason=' not in a.gate:
            probs.append('GATE exit=%d≠0 且无 stop_reason 声明——未到绿又未止损，虚假GATE 候选（#364）' % gexit)
        ev = parse_ev(a.gate)
        if ev is None:
            probs.append('GATE 缺 `ev=` 验证层级声明%s' % ('（高风险任务必填）' if a.high_risk else ''))
        elif a.high_risk and not (ev & set(EVIDENCE_NON_EXEC)):
            probs.append('GATE ev=%s 全是执行类证据；高风险任务至少需一项 cover/invariant/indep（细则 #371）'
                         % '+'.join(sorted(ev)))
        elif a.high_risk:
            check_gate_evidence(a, ev, oks, probs)
        else:
            oks.append('GATE ev=%s（层级判定通过）' % '+'.join(sorted(ev)))
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

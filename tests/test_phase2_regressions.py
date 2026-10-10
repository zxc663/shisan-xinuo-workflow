# -*- coding: utf-8 -*-
"""Phase 2 门禁回归（v4.1.0 R1 · A-11 组+A-15 组）——unittest discover 形态，全部走真实 CLI 子进程。

跑法：python -m unittest discover -s tests -v
覆盖：gate_audit RT-01/01b/02/03/08（A-11①②⑤）｜risk_scan RT-06/07+HIT/PASS 语义（A-11③⑤/F-47）
      ｜spec-trace-gate selftest（A-11④）｜deploy_injection 区块合并单元+临时目录端到端（A-15①②/F-65）
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GATE_AUDIT = REPO / 'scripts' / 'gate_audit.py'
RISK_SCAN = REPO / 'scripts' / 'risk_scan.py'
SPEC_TRACE = REPO / 'skill' / 'shisan-xinuo-product' / 'scripts' / 'spec-trace-gate.py'
DEPLOY = REPO / 'scripts' / 'deploy_injection.py'


def run_cli(script, *args, env_extra=None, timeout=180):
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    r = subprocess.run([sys.executable, str(script), *args], capture_output=True,
                       text=True, encoding='utf-8', errors='replace', timeout=timeout, env=env)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


class TestGateAuditRT(unittest.TestCase):
    """A-11①②⑤：修复后同输入必须 FAIL/按预期分派。"""

    def test_rt01_bare_ev_cover_rejected(self):
        rc, out = run_cli(GATE_AUDIT, '--gate', 'GATE: {level=L2-F, ev=cover}', '--high-risk', '--cwd', str(REPO))
        self.assertEqual(rc, 1)
        self.assertIn('声明无对象', out)

    def test_rt01b_bare_ev_indep_rejected(self):
        rc, out = run_cli(GATE_AUDIT, '--gate', 'GATE: {level=L2-F, ev=indep}', '--high-risk', '--cwd', str(REPO))
        self.assertEqual(rc, 1)
        self.assertIn('声明无对象', out)

    def test_rt02_failing_cmd_is_fail_not_green(self):
        cmd = 'exit /b 3' if os.name == 'nt' else 'exit 3'
        rc, out = run_cli(GATE_AUDIT, '--cmd', cmd, '--cwd', str(REPO))
        self.assertEqual(rc, 1)
        self.assertIn('cmd exit=3', out)

    def test_rt03_platform_branch_ok_cmd_passes(self):
        cmd = 'exit /b 0' if os.name == 'nt' else 'exit 0'
        rc, _ = run_cli(GATE_AUDIT, '--cmd', cmd, '--cwd', str(REPO))
        self.assertEqual(rc, 0)

    def test_rt08_identical_cmds_rejected_as_independent(self):
        cmd = 'exit /b 0' if os.name == 'nt' else 'exit 0'
        rc, out = run_cli(GATE_AUDIT, '--cmd', cmd, '--independent-cmd', cmd, '--cwd', str(REPO))
        self.assertEqual(rc, 1)
        self.assertIn('全同', out)

    def test_selftest_entry_all_pass(self):
        rc, out = run_cli(GATE_AUDIT, '--selftest')
        self.assertEqual(rc, 0)
        self.assertIn('PASS', out)


class TestRiskScanRT(unittest.TestCase):
    """A-11③⑤/F-47：缺失输入 INCOMPLETE exit 3；HIT=1/PASS=0 原语义保持。"""

    def test_rt06_missing_path_incomplete_exit3(self):
        rc, out = run_cli(RISK_SCAN, '--paths', '__no_such_file_for_rt06__.txt')
        self.assertEqual(rc, 3)
        self.assertIn('INCOMPLETE', out)

    def test_rt07_unreadable_path_incomplete_exit3(self):
        rc, out = run_cli(RISK_SCAN, '--paths', str(REPO / 'scripts'))
        self.assertEqual(rc, 3)
        self.assertIn('INCOMPLETE', out)

    def test_semantics_pass0_hit1_kept(self):
        rc, _ = run_cli(RISK_SCAN, '--text', '今天只改一下 README 文案')
        self.assertEqual(rc, 0)
        rc, _ = run_cli(RISK_SCAN, '--text', '执行 terraform apply 替换生产基础设施')
        self.assertEqual(rc, 1)

    def test_selftest_entry_all_pass(self):
        rc, _ = run_cli(RISK_SCAN, '--selftest')
        self.assertEqual(rc, 0)


class TestSpecTraceGate(unittest.TestCase):
    """A-11④⑤：T7 文件型证据存在性双模式+selftest 全绿（含 RT-04/05）。"""

    def test_selftest_entry_all_pass(self):
        rc, out = run_cli(SPEC_TRACE, '--selftest')
        self.assertEqual(rc, 0)
        self.assertIn('RT-04假路径拦=True', out.replace(' ', ''))


class TestDeployMerge(unittest.TestCase):
    """A-15：区块合并（首装追加/区块替换保留用户内容/幂等/端到端反例测试）。"""

    def setUp(self):
        from importlib.util import module_from_spec, spec_from_file_location
        spec = spec_from_file_location('deploy_injection', DEPLOY)
        self.dep = module_from_spec(spec)
        spec.loader.exec_module(self.dep)

    def test_first_install_appends_and_keeps_user_lines(self):
        newblock = ('# 全局 Agent 工作流核心（十三希诺工作流 · 每会话强制生效）—— v4.0.0\n新载体\n'
                    '### 在场提示 · 工作流 Skill 现已在场\n')
        merged, user = self.dep.merge_block('我的规则甲\n我的规则乙\n', newblock)
        self.assertEqual(user, ['我的规则甲', '我的规则乙'])
        self.assertTrue(merged.startswith('我的规则甲'))
        self.assertTrue(merged.rstrip('\n').endswith(newblock.strip('\n')))

    def test_block_replace_keeps_head_and_is_idempotent(self):
        # NEWBLOCK 模拟真实区块形态（首行=区块标记前缀；部署产物恒如此）
        newblock = ('# 全局 Agent 工作流核心（十三希诺工作流 · 每会话强制生效）—— v4.0.0\n新载体\n\n---\n\n'
                    '### 在场提示 · 工作流 Skill 现已在场\n新锚\n')
        old = ('用户规则甲\n\n# 全局 Agent 工作流核心 —— v1\n旧载体\n\n---\n\n'
               '### 在场提示 · 工作流 Skill 现已在场\n旧锚\n')
        merged, user = self.dep.merge_block(old, newblock)
        self.assertEqual(user, ['用户规则甲'])
        self.assertTrue(merged.startswith('用户规则甲'))
        self.assertTrue(merged.rstrip('\n').endswith(newblock.strip('\n')))
        self.assertNotIn('旧载体', merged)
        self.assertNotIn('旧锚', merged)
        merged2, _ = self.dep.merge_block(merged, newblock)
        self.assertEqual(merged2, merged)  # 幂等：重跑同结果

    def test_e2e_temp_home_user_content_survives(self):
        """A-15② 审计反例测试：预置用户规则→真部署（SKILL_HOME_OVERRIDE 重定向临时目录）→逐条仍在+幂等。"""
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            target = home / '.zcode' / 'AGENTS.md'
            target.parent.mkdir(parents=True)
            rules = ['我的独特规则一: 提交信息用中文', '我的独特规则二: 禁止自动 push', '我的独特规则三: 周五不发版']
            target.write_text('\n'.join(rules) + '\n', encoding='utf-8')
            for attempt in (1, 2):  # 两轮部署=首装追加+区块替换，用户内容恒在且不累积
                rc, out = run_cli(DEPLOY, '--version', '4.0.0', '--only', 'zcode',
                                  env_extra={'SKILL_HOME_OVERRIDE': str(home)})
                self.assertEqual(rc, 0, out)
                final = target.read_text(encoding='utf-8-sig')
                for r in rules:
                    self.assertIn(r, final)
                self.assertIn('开工四步', final)
                self.assertEqual(final.count('我的独特规则一'), 1)
                self.assertEqual(
                    final.count('# 全局 Agent 工作流核心（十三希诺工作流 · 每会话强制生效）—— v4.0.0'), 1,
                    f'第{attempt}轮部署后区块应恰一份（幂等）')


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
"""anchor_sweep 冒烟：判据 P0 修复版三场景（锚块吞到任意层级标题停/同层级用户内容保全/无锚幂等）。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from anchor_sweep import sweep

CASES = [
    # (名, 输入, 期望 cleaned, 期望 removed 数, 期望 versions)
    # 期望值对齐 syncer 原实现行为：锚块删除后收紧 outl 尾部连续空行（含锚前空行）；keepends 保留尾换行
    ('旧锚+同层级用户节', '# 记忆\n\n## 在场提示 · 工作流 Skill 现已在场（v3.2.0 硬注入）\n锚正文A\n锚正文B\n\n## 用户偏好\n偏好内容',
     '# 记忆\n## 用户偏好\n偏好内容', 3, ['v3.2.0']),
    ('深层用户标题不吞', '## 在场提示 · 工作流 Skill 现已在场（v3.1.0）\n旧锚\n#### 用户小节\n用户内容',
     '#### 用户小节\n用户内容', 1, ['v3.1.0']),
    ('无锚幂等', '# 记忆\n## 用户偏好\n内容', '# 记忆\n## 用户偏好\n内容', 0, []),
    ('锚在尾部', '# 记忆\n\n## 在场提示 · 工作流 Skill 现已在场（v3.3.0）\n尾锚正文',
     '# 记忆\n', 1, ['v3.3.0']),
]

fails = 0
for name, inp, want_clean, want_rm, want_ver in CASES:
    cleaned, st = sweep(inp)
    ok = cleaned == want_clean and st['removed'] == want_rm and st['versions'] == want_ver
    print('%s %s removed=%d ver=%s' % ('PASS' if ok else 'FAIL', name, st['removed'], st['versions']))
    if not ok:
        fails += 1
        print('  got cleaned=%r' % cleaned)
print('SMOKE: %d/%d' % (len(CASES) - fails, len(CASES)))
sys.exit(1 if fails else 0)

# -*- coding: utf-8 -*-
"""注入副本一键部署工具 · deploy_injection（v2.6.0 渠道/部署修复，T2 #29 结构性防漂移）

把「备份 → 组装（平台头注 + injection-core 全文 + 在场提示锚点）→ 写入 → 锚点验收」压成一条命令。
平台注入点清单 = 唯一权威源 platform-adaptation.md §2（本脚本是它的机器执行形态，部署后仍须人工 grep 复核）。

用法:
  python scripts/deploy_injection.py --version 2.6.0            # 全部平台
  python scripts/deploy_injection.py --version 2.6.0 --only zcode,codex
  python scripts/deploy_injection.py --check                    # 只验收不写入（版本+锚点 grep）

设计: 路径从 USERPROFILE 派生（不硬编码个人路径）；写前备份 .bak-<ts>-pre-v<版本>；
      各平台统一携带在场提示锚点块（单一权威源=本脚本 ANCHOR；源库核心不内嵌锚点，防双份注入）。
"""
import argparse, io, re, shutil, sys, os
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
TZ = timezone(timedelta(hours=8))
REPO = Path(__file__).resolve().parent.parent
CORE = REPO / 'skill' / 'shisan-xinuo-workflow' / 'references' / 'injection-core.md'

# 平台注入点表（与 platform-adaptation.md §2 同源；新增平台先改表再跑；anchor=是否附在场提示，现全平台统一携带）
PLATFORMS = {
    'zcode':      ('{home}/.zcode/AGENTS.md', 'ZCode（agent-app global / hard-inject，影响本平台所有项目与会话）', True),
    'codex':      ('{home}/.codex/AGENTS.md', 'Codex（AGENTS.md 全局规则，每会话自动注入）', True),
    'claude':     ('{home}/.claude/CLAUDE.md', 'Claude Code（CLAUDE.md 全局规则，每会话自动注入）', True),
    'trae':       ('{home}/.trae-cn/user_rules/shisan-xinuo-workflow.md', 'Trae（user_rules 用户全局，每会话自动注入）', True),
    'workbuddy':  ('{home}/.workbuddy/AGENTS.md', 'WorkBuddy（agent-app 全局规则，每会话自动注入）', True),
}

HEADER = '''# 全局 Agent 工作流核心（十三希诺工作流 · 每会话强制生效）—— v{version}

> 平台：{plat}
> 源：本地 skill「{skill_src}」（v{version}，唯一中文版）
> 注入内容：references/injection-core.md 核心全文（瘦身版，常驻预算 ≤6K 字符）
> 完整工作流按需加载：references/ 按触发症状加载——三级跑道 / 编号纪律（rules.md 47 条）/ 9 类工作流 / {count} 条细则·17 类 / 安全红线
> 更新协议：python scripts/syncer.py（三路合并，备份落 skill-backups/·平台扫描路径外）｜**验收判据：平台加载时的 Base directory，不是文件版本号**
> 注入时间：{now}
'''

ANCHOR = '''
---

### 在场提示 · 工作流 Skill 现已在场（shisan-xinuo-workflow · v{version} 硬注入）
本 Agent 账户应用「十三希诺 Agent 工作流」硬注入：每会话开工先识别本在场提示 → 按三级跑道推进（L1 快速通道 / L2-S 短工作流 / L2-F 完整 9 步），命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- 判级：L3 必问先于动手；L1 直接做；其余 L2 记录推进。
- 模式：普通（关键决策必问）/ 目标（无人值守按计划，密钥与破坏性暂停）/ 安静（L1 只报结果）。
- 红线：密钥绝不落盘；破坏性操作先备份+确认；不假实现（未完成显式标注）。
- 自检彩蛋：输入 `zxc663` → 回复「注入方式（硬注入）+ 已应用轮数 + 源库 vX vs 副本 vY + Base directory 判据」。
- 前缀自检（每会话）：能确定安装目录名且无 `agent-` 前缀 → 一行提示（install-skill.ps1 可带前缀重装；不愿改则 agent-log 状态段记「保持无前缀」后静默）；目录名未知 → 不猜不阻塞。
- 项目承载（自动建，不等许可）：memory/ 一档制 `agent-log.md`（状态段/教训区/偏好段/流水区，禁空占位）+ 项目级规则文件（按 platform-adaptation.md「项目级注入点表」定名，templates/project-rules.md，先查既有→合并不覆盖）+ docs/project-info.md。
- 记忆对齐（最小读取）：只读 agent-log 状态段一屏 + 按症状检索；平台原生记忆在场时跨会话续接交给平台记忆，本档聚焦项目审计。
- 设计规范档前置：设计类动作（前端尤甚）先逐组件调研成熟规范 → 强制留档 docs/design-specs/ → 按档设计并回指。
- 细则检索端口：遇错误先对注入核心 TOP 内联处置，处置完成后留 errpath 行（症状→处置路径）；lookup=佐证非事前门槛，按关键词检索跑 `python "<技能安装目录>/scripts/detail_lookup.py" "<症状关键词>"`（技能安装目录=平台解析到的 Base directory）；未执行 lookup 不得自报命中数。
- 委托子代理：必须内联纪律包（子代理不继承注入副本、不保证自加载 Skill——实测实证；独立工作区另建规范承载）。
- 完整规则：规则层文件（AGENTS.md / user_rules / CLAUDE.md）+ 技能 references/（rules.md 47 条 / {count} 细则）。
- 更新协议：`python scripts/syncer.py`（记忆/规则/配置三层随版本同步；WorkBuddy 技能副本加 --dest）；验收以平台解析到的 Base directory 为准。
- 注入版本：v{version} ｜ 授权：本锚点由用户授权后注入，未获授权不写。
'''


def details_count():
    t = (REPO / 'skill' / 'shisan-xinuo-workflow' / 'references' / 'details.md').read_text(encoding='utf-8')
    return len(re.findall(r'^\d{1,3}\. ', t, re.M))


def targets(only):
    home = Path.home().as_posix()
    val = os.environ.get('SKILL_SRC', home + '/.agents/skills/shisan-xinuo-workflow')
    # 仅相对路径才补盘符前缀；已是盘符绝对路径原样保留（防 C:/C:/ 双前缀）
    src = val if re.match(r'^[A-Za-z]:[/\\]', val) else 'C:/' + val
    for name, (tmpl, plat, anchor) in PLATFORMS.items():
        if only and name not in only:
            continue
        yield name, tmpl.format(home=home), plat, anchor, src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', default=None)
    ap.add_argument('--only', default=None, help='逗号分隔平台名')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    only = set(a.only.split(',')) if a.only else None
    count = details_count()
    now = datetime.now(TZ).strftime('%Y-%m-%d %H:%M:%S')

    fails = []
    for name, path, plat, anchor, src in targets(only):
        p = Path(path)
        if not p.exists():
            fails.append(f'{name}: 注入点不存在 {p}')
            print(f'[MISS] {name} {p}')
            continue
        if a.check:
            t = p.read_text(encoding='utf-8-sig')
            v = a.version or ''
            ok = (f'v{v}' in t) and ('开工四步' in t or not v) and (f'{count} 条细则' in t or not v)
            print(f'[{"PASS" if ok else "FAIL"}] {name} v={v} count={count}')
            if not ok:
                fails.append(name)
            continue
        if not a.version:
            print('--version 必填（写入模式）'); sys.exit(1)
        bak = p.with_name(p.name + f'.bak-{datetime.now(TZ).strftime("%Y%m%d")}-pre-v{a.version}')
        shutil.copy2(p, bak)
        core = CORE.read_text(encoding='utf-8-sig').replace('\r', '').strip()
        out = HEADER.format(version=a.version, plat=plat, skill_src=src, count=count, now=now).rstrip()
        out += '\n\n---\n\n' + core
        if anchor:
            out += ANCHOR.format(version=a.version, count=count)
        p.write_text(out, encoding='utf-8-sig', newline='')
        t = p.read_text(encoding='utf-8-sig')
        ok = f'v{a.version}' in t and '开工四步' in t and f'{count} 条细则' in t
        print(f'[{"PASS" if ok else "FAIL"}] {name} -> v{a.version}（备份 {bak.name}）')
        if not ok:
            fails.append(name)
    if fails:
        print('FAILS:', fails); sys.exit(1)
    print('ALL DONE')


if __name__ == '__main__':
    main()

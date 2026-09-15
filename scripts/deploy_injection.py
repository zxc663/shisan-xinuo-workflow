# -*- coding: utf-8 -*-
"""注入副本一键部署工具 · deploy_injection（v2.6.0 渠道/部署修复，T2 #29 结构性防漂移）

把「备份 → 组装（平台头注 + injection-core 全文 + 在场提示锚点）→ 写入 → 锚点验收」压成一条命令。
平台注入点清单 = 唯一权威源 platform-adaptation.md §2（本脚本是它的机器执行形态，部署后仍须人工 grep 复核）。

用法:
  python scripts/deploy_injection.py --version 2.6.0            # 全部平台
  python scripts/deploy_injection.py --version 2.6.0 --only zcode,codex
  python scripts/deploy_injection.py --check                    # 只验收不写入（版本+锚点 grep）

设计: 路径从 USERPROFILE 派生（不硬编码个人路径）；写前备份 .bak-<ts>-pre-v<版本>；
      在场提示锚块单一权威源=templates/memory-anchor.md（本脚本读取+关键行断言，禁内嵌第二份——F-17）；
      --check 不带 --version 时取 package.json 版本严格校验（F-21 假绿防线）；
      写入完成后输出重启+探针验收提示（注入快照=会话创建时快照——v11 机制定论）。
"""
import argparse, io, json, re, shutil, sys, os
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
TZ = timezone(timedelta(hours=8))
REPO = Path(__file__).resolve().parent.parent
SK = REPO / 'skill' / 'shisan-xinuo-workflow'
CORE = SK / 'references' / 'injection-core.md'
ANCHOR_TPL = SK / 'templates' / 'memory-anchor.md'

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
> 完整工作流按需加载：references/ 按触发症状加载——三级跑道 / 编号纪律（rules.md 47 条）/ 9 类工作流 / {count} 条细则·{classes} 类 / 安全红线
> 更新协议：python scripts/syncer.py（三路合并，备份落 skill-backups/·平台扫描路径外）｜**验收判据：平台加载时的 Base directory，不是文件版本号**
> 注入时间：{now}
'''

# 在场提示锚块：单一权威源 = templates/memory-anchor.md（F-17 单一文件化；本脚本不再内嵌第二份锚文本）。
# 读取后仅替换 vX.Y.Z 占位为版本；缺关键行即报错（防模板被误改后静默降级）。
ANCHOR_REQUIRED_LINES = ('在场提示', '每轮复述', '前置门', '细则 #326', '细则 #332', '注入版本')


def load_anchor(version):
    txt = ANCHOR_TPL.read_text(encoding='utf-8')
    m = re.search(r"```markdown\r?\n(.*?)\r?\n```", txt, re.S)
    if not m:
        raise SystemExit(f'E: {ANCHOR_TPL} 缺 ```markdown 锚点代码块')
    body = m.group(1).replace('vX.Y.Z', f'v{version}')
    for key in ANCHOR_REQUIRED_LINES:
        if key not in body:
            raise SystemExit(f'E: 锚块缺关键行[{key}]（单一权威源被误改？对照 templates/memory-anchor.md）')
    return '\n---\n\n' + body + '\n'


def details_count():
    t = (SK / 'references' / 'details.md').read_text(encoding='utf-8')
    lines = re.findall(r'^(\d{1,3}\. .*)', t, re.M)
    # 活跃条数：排除特殊槽（〔预留槽〕/〔归档〕行——占号保编号连续，不计入口径）
    return len([l for l in lines if '〔预留槽〕' not in l and '〔归档〕' not in l])


def classes_count():
    t = (SK / 'references' / 'details.md').read_text(encoding='utf-8')
    return len(re.findall(r'^## \d+\. ', t, re.M))


def pkg_version():
    pj = REPO / 'package.json'
    return json.loads(pj.read_text(encoding='utf-8')).get('version', '')


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
    classes = classes_count()
    now = datetime.now(TZ).strftime('%Y-%m-%d %H:%M:%S')

    # F-21 假绿防线：--check 不带 --version 时从 package.json 取当前版本做严格校验（旧逻辑空版本恒 PASS）
    if a.check and not a.version:
        a.version = pkg_version()
        print(f'[check] 未显式给 --version，取 package.json 当前版本 v{a.version} 做严格校验')

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
        out = HEADER.format(version=a.version, plat=plat, skill_src=src, count=count, classes=classes, now=now).rstrip()
        out += '\n\n---\n\n' + core
        if anchor:
            out += load_anchor(a.version)
        p.write_text(out, encoding='utf-8-sig', newline='')
        t = p.read_text(encoding='utf-8-sig')
        ok = f'v{a.version}' in t and '开工四步' in t and f'{count} 条细则' in t
        print(f'[{"PASS" if ok else "FAIL"}] {name} -> v{a.version}（备份 {bak.name}）')
        if not ok:
            fails.append(name)
    if fails:
        print('FAILS:', fails); sys.exit(1)
    if not a.check and a.version:
        # v11①：注入快照=会话创建时快照（手动 /compact 冻结、平台自动压缩刷新）——部署后必须重启应用+新会话探针验收
        print('---')
        print(f'[下一步 · 必须] ①重启 ZCode 应用（GUI 长活会话吃旧注入快照）；②新开会话输入「在场提示」探针，')
        print(f'   验收锚：在场提示 · v{a.version} + 细则 {count} 条 + 每轮复述条款在场；③自检彩蛋 zxc663 应答版本 v{a.version}。')
    print('ALL DONE')


if __name__ == '__main__':
    main()

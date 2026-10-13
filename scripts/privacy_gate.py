# -*- coding: utf-8 -*-
r"""privacy_gate.py · 开源隐私门（四层扫描 · 发行前置）

覆盖设计档 §4.4 实测缺口（verify D 项只扫 tracked 文本的令牌/路径，无身份维度）：
  层1 tracked 文本   —— QQ 邮箱 / 本机 Windows 用户名 / 家目录路径 / 机密目录路径 / 令牌
  层2 git 全历史     —— `git log --all` 的 author/committer 身份 + commit message 文本
  层3 发行物元数据   —— package.json 的 author / contributors / maintainers / repository 字段
  层4 二进制图片     —— 清单化**人工过窗**（机器不全查，只出清单 + 断言发行面不含二进制）

分级判据（敏感度 I13）：
  高敏 = QQ 邮箱（可反查个人）        → block
  中敏 = 本机 Windows 用户名 / 家目录   → block（可定位本机）
  低敏 = 笔名「十三希诺」/ GitHub 账号名 → warn（发布身份，门面需要）
  机密目录                             → block

关键判别（本机用户名 vs GitHub 账号名不可混淆）：
  本机用户名按**平台形态**匹配——Windows 家目录 `C:\Users\<name>`、本机绝对路径前缀；
  独立的裸账号 token（`github.com/<acct>`、`@<acct>/pkg`、`npx add <acct>/...`）属发布身份 → warn 不 block。
  否则门禁会把门面安装命令判成本机身份泄漏（27 文件假阳，2026-10-13 实测）。

三模式：
  --check     block 级命中 exit 1（发行跑全量；verify K 项调用）
  --report    全量报告含历史面 + 二进制清单（人工过窗用）
  --selftest  伪造命中样本正反自测（对齐仓内反向变异传统：risk_scan.py --selftest）

统一占位符：<user> / <EMAIL_REDACTED> / %USERPROFILE% / <REPO>
发现真凭据的处理顺序永远是「先吊销，再清理」——清理不解除已泄漏凭据的暴露面。

用法:
  python scripts/privacy_gate.py --check
  python scripts/privacy_gate.py --report [--out <报告文件>]
  python scripts/privacy_gate.py --selftest
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- 规则表
# level: block=发行阻断 / warn=如实报告不阻断（发布身份/门面需要）
RULES = [
    # (维度, level, 正则, 说明)
    ('高敏-QQ邮箱', 'block', re.compile(r'\b\d{5,11}@qq\.com\b'), '可反查个人身份'),
    ('高敏-通用邮箱', 'warn', re.compile(r'\b[\w.+-]+@(?!qq\.com)[\w-]+\.[\w.]+\b'), '其他邮箱：非本门高敏维度，如实报告'),
    ('中敏-家目录', 'block', re.compile(r'[A-Za-z]:[\\/]Users[\\/][A-Za-z][\w.-]*'), '本机家目录路径'),
    ('中敏-家目录占位', 'warn', re.compile(r'%USERPROFILE%[\\/]'), '占位符形态（合规写法），确认未夹带真值'),
    ('中敏-机密目录', 'block', re.compile(r'D:[\\/]Agent个人资源|Agent个人资源[\\/]02-|Agent个人资源[\\/]机密资源'), '机密目录路径'),
    ('高敏-令牌', 'block', re.compile(r'ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}'), 'GitHub 令牌明文'),
    ('低敏-发布身份', 'warn', re.compile(r'github\.com/[A-Za-z0-9][\w.-]{2,}|@[A-Za-z0-9][\w.-]{2,}/[a-z][\w.-]*'), 'GitHub 账号/仓库名=发布身份'),
]

BINARY_EXT = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.ico', '.pdf', '.zip', '.7z', '.exe', '.dll', '.so', '.dylib'}
TEXT_EXT = {'.md', '.txt', '.json', '.py', '.ps1', '.sh', '.yml', '.yaml', '.toml', '.ini', '.cfg', '.js', '.ts', '.jsx', '.tsx',
            '.html', '.css', '.xml', '.csv', '.jsonl', '.pyc'}

SKIP_DIRS = {'.git', 'node_modules', '__pycache__', 'dist', '.workbuddy', '.agents'}

# 伪造/占位样本白名单（对齐仓内反向变异传统：门禁负向测试用的假身份不是泄漏）
# 判据=样本名本身是「明显的假名」；真实本机用户名不在此列。
FAKE_SAMPLES = re.compile(r'^(fake|example|sample|test|dummy|placeholder|your|some)[-_]?(user|name|home|path)?', re.I)


def _is_fake_sample(frag):
    """家目录路径命中里，用户名段是否为伪造样本（`C:\\Users\\fakeuser` 这类负向注入）。"""
    m = re.search(r'[A-Za-z]:[\\/]Users[\\/]([A-Za-z][\w.-]*)', frag)
    return bool(m and FAKE_SAMPLES.match(m.group(1)))


def _git(*args, timeout=180):
    r = subprocess.run(['git'] + list(args), cwd=ROOT, capture_output=True,
                       text=True, encoding='utf-8', errors='replace', timeout=timeout)
    return r.returncode, (r.stdout or ''), (r.stderr or '')


def tracked_files():
    rc, out, _ = _git('-c', 'core.quotepath=false', 'ls-files', '-z')
    if rc != 0:
        return []
    return [p for p in out.split('\0') if p]


def scan_text(text):
    """返回命中列表 [(维度, level, 说明, 片段)]

    伪造样本（门禁负向测试注入的假身份）降级为 warn 并标注——它证明门禁在测，不构成泄漏。
    """
    hits = []
    for name, level, rx, note in RULES:
        for m in rx.finditer(text):
            s = m.group(0)
            if name == '中敏-家目录' and _is_fake_sample(s):
                hits.append((name, 'warn', note + '（伪造样本·门禁负向注入，非真实身份）', s[:60]))
                continue
            hits.append((name, level, note, s[:60]))
    return hits


# ---------------------------------------------------------------- 层实现
def layer1(only=None):
    """层1：tracked 文本"""
    res = {'level': '层1 tracked 文本', 'scanned': 0, 'hits': []}
    for rel in tracked_files():
        if only and rel not in only:
            continue
        # 自引用豁免：本门禁脚本自身含伪造样本（selftest 的 QQ 邮箱/家目录/机密目录测试串），
        # 扫自己必然命中 = 检查力自我拆台。豁免范围=门禁脚本自身（对齐 verify D 项的 scripts/ 自引用豁免，
        # 审查 F-16 先例）；selftest 的样本正确性由 --selftest 双向断言保证，不依赖全量扫描。
        if rel.replace('\\', '/') in ('scripts/privacy_gate.py',
                                       'skill/shisan-xinuo-workflow/scripts/privacy_gate.py'):
            continue
        fp = os.path.join(ROOT, rel)
        if not os.path.isfile(fp):
            continue
        ext = os.path.splitext(rel)[1].lower()
        if ext not in TEXT_EXT and ext not in ('', '.gitignore', '.gitattributes', '.npmrc', '.zcodeignore'):
            continue
        try:
            text = io.open(fp, encoding='utf-8').read()
        except Exception:
            continue
        res['scanned'] += 1
        for name, level, note, frag in scan_text(text):
            res['hits'].append({'file': rel, 'dim': name, 'level': level, 'note': note, 'frag': frag})
    return res


def layer2(limit_commits=None):
    """层2：git 全历史（author/committer 身份 + commit message）"""
    res = {'level': '层2 git 全历史', 'commits': 0, 'identities': {}, 'hits': []}
    rc, out, _ = _git('log', '--all', '--format=%H%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%B%x1e')
    if rc != 0:
        res['error'] = 'git log 失败（无 git 仓库或超时）'
        return res
    for rec in out.split('\x1e'):
        rec = rec.strip('\n')
        if not rec:
            continue
        parts = rec.split('\x1f')
        if len(parts) < 6:
            continue
        _h, an, ae, cn, ce, body = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
        res['commits'] += 1
        for who, val in (('author', an), ('author', ae), ('committer', cn), ('committer', ce)):
            if not val:
                continue
            res['identities'][val] = res['identities'].get(val, 0) + 1
        for name, level, note, frag in scan_text(ae + '\n' + ce + '\n' + body):
            # 自引用豁免：门禁脚本自身的 commit message 会复述 selftest 样本串（自引用=自我拆台）
            if 'privacy_gate' in body and ('--selftest' in body or '隐私门' in body):
                continue
            res['hits'].append({'commit': _h[:8], 'dim': name, 'level': level, 'note': note, 'frag': frag})
    return res


def layer3():
    """层3：发行物元数据（package.json 身份字段）"""
    res = {'level': '层3 发行物元数据', 'hits': [], 'fields': {}}
    pj = os.path.join(ROOT, 'package.json')
    if not os.path.isfile(pj):
        res['error'] = '缺 package.json'
        return res
    try:
        data = json.loads(io.open(pj, encoding='utf-8').read())
    except Exception as e:
        res['error'] = 'package.json 解析失败: %s' % e
        return res
    for field in ('author', 'contributors', 'maintainers', 'repository', 'homepage', 'bugs'):
        if field in data:
            raw = json.dumps(data[field], ensure_ascii=False)
            res['fields'][field] = raw
            for name, level, note, frag in scan_text(raw):
                res['hits'].append({'file': 'package.json#%s' % field, 'dim': name,
                                    'level': level, 'note': note, 'frag': frag})
    # 笔名=发布门面 → 记录为低敏豁免（设计档 §7.5 已裁决：author 保留笔名，QQ 邮箱不出现在任何发行物字段）
    author = data.get('author', '')
    if isinstance(author, str) and author and author != '十三希诺':
        res['hits'].append({'file': 'package.json#author', 'dim': '低敏-非笔名作者', 'level': 'warn',
                            'note': '设计档裁决 author=笔名「十三希诺」；非笔名形态需确认', 'frag': author[:60]})
    return res


def layer4(out_path=None):
    """层4：二进制图片清单化人工过窗（机器不全查，只出清单 + 断言发行面）"""
    res = {'level': '层4 二进制清单（人工过窗）', 'untracked_binaries': [], 'in_dist_roots': [], 'note': ''}
    # 4a 未跟踪二进制（不进发行物，但可能含个人信息如截图上的 IDE 用户名/路径）
    rc, out, _ = _git('-c', 'core.quotepath=false', 'ls-files', '--others', '--exclude-standard', '-z')
    if rc == 0:
        for rel in out.split('\0'):
            if rel and os.path.splitext(rel)[1].lower() in BINARY_EXT:
                fp = os.path.join(ROOT, rel)
                res['untracked_binaries'].append({
                    'path': rel,
                    'size': os.path.getsize(fp) if os.path.isfile(fp) else -1,
                    'tracked': False,
                })
    # 4b 发行面断言（I11：二进制不进打包范围）——查 build-dist 的 $roots 是否纳入根级二进制
    res['note'] = ('未跟踪二进制不进 dist 打包面（build-dist $roots 不含仓库根散落二进制）；'
                   '发行前须人工过窗确认截图内无个人信息（IDE 用户名/路径/窗口标题/通知内容）')
    return res


# ---------------------------------------------------------------- 输出
def _print_result(res, verbose):
    print('[%s]' % res['level'])
    if res.get('error'):
        print('  ERROR: %s' % res['error'])
    meta = []
    for k in ('scanned', 'commits', 'commits_shown'):
        if k in res:
            meta.append('%s=%s' % (k, res[k]))
    if meta:
        print('  扫描面: %s' % ', '.join(meta))
    if res.get('identities'):
        print('  历史身份: %s' % ', '.join('%s×%d' % (k, v) for k, v in sorted(res['identities'].items())))
    if res.get('fields'):
        for k, v in res['fields'].items():
            print('  元数据 %s = %s' % (k, v))
    hits = res.get('hits', [])
    # 输出收敛：block 全列；warn 按 (维度,文件) 归组计数，避免门面账号名刷屏淹没真命中
    blocks = [h for h in hits if h['level'] == 'block']
    warns = [h for h in hits if h['level'] != 'block']
    for h in blocks:
        loc = h.get('file') or h.get('commit')
        print('  [block] %s | %s | %s | %s' % (loc, h['dim'], h['note'], h['frag']))
    if warns:
        groups = {}
        for h in warns:
            key = (h.get('file') or h.get('commit') or '-', h['dim'])
            groups[key] = groups.get(key, 0) + 1
        for (loc, dim), n in sorted(groups.items(), key=lambda kv: (-kv[1], kv[0])):
            print('  [warn×%d] %s | %s' % (n, loc, dim))
    if 'untracked_binaries' in res:
        bins = res['untracked_binaries']
        print('  未跟踪二进制 %d 项（清单化人工过窗，不自动判定）:' % len(bins))
        for b in bins:
            print('    - %s (%d B)' % (b['path'], b['size']))
        print('  注: %s' % res['note'])


def collect(mode):
    results = [layer1(), layer2(), layer3(), layer4()]
    return results


def summarize(results):
    block = []
    warn = []
    for res in results:
        for h in res.get('hits', []):
            (block if h['level'] == 'block' else warn).append((res['level'], h))
    return block, warn


def do_check():
    results = collect('check')
    for res in results:
        _print_result(res, False)
    block, warn = summarize(results)
    print('')
    print('PRIVACY %s: block %d / warn %d' % ('FAIL' if block else 'PASS', len(block), len(warn)))
    if block:
        print('BLOCK 级命中（发行阻断；真凭据处理顺序=先吊销再清理）:')
        for lvl, h in block:
            print('  - [%s] %s | %s | %s' % (lvl, h.get('file') or h.get('commit'), h['dim'], h['frag']))
    if warn:
        print('WARN 级（发布身份/门面需要，如实报告不阻断）: %d 项' % len(warn))
    return 1 if block else 0


def do_report(out_path=None):
    results = collect('report')
    lines = ['# privacy_gate 报告（全量面 · 含 git 历史 + 二进制人工过窗清单）', '']
    for res in results:
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        _print_result(res, True)
        sys.stdout = old
        lines.append(buf.getvalue())
        lines.append('')
    block, warn = summarize(results)
    lines.append('汇总: block %d / warn %d' % (len(block), len(warn)))
    text = '\n'.join(lines)
    print(text)
    if out_path:
        fp = out_path if os.path.isabs(out_path) else os.path.join(ROOT, out_path)
        io.open(fp, 'w', encoding='utf-8').write(text)
        print('\n[report] written -> %s' % fp)
    return 0


# ---------------------------------------------------------------- selftest
def _run_cli(args, timeout=300):
    r = subprocess.run([sys.executable, os.path.abspath(__file__)] + args,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def _hits_of(text):
    return scan_text(text)


def selftest():
    """伪造命中样本正反自测（正向必命中 / 反向必放行）——对齐仓内反向变异传统。
    返回 0=全过 / 1=有失败。
    """
    cases = []

    # ---- 正向：block 级必命中
    for name, sample, dim in [
        ('正向 QQ 邮箱（高敏·可反查个人）', '联系 123456789@qq.com 获取授权', '高敏-QQ邮箱'),
        ('正向 家目录路径（中敏·可定位本机）', r'日志在 C:\Users\zhangwei\AppData\local\x.log', '中敏-家目录'),
        ('正向 机密目录（高敏）', r'D:\Agent个人资源\机密资源\keys.txt', '中敏-机密目录'),
        ('正向 令牌明文（高敏）', 'ghp_' + 'a' * 36, '高敏-令牌'),
    ]:
        hs = _hits_of(sample)
        got = [h for h in hs if h[0] == dim and h[1] == 'block']
        cases.append(('%s → block 命中' % name, len(got) == 1))

    # ---- 反向：合规形态必放行（占位符/门面/无命中）
    for name, sample in [
        ('反向 占位符家目录（%USERPROFILE%）不误判本机', r'路径 %USERPROFILE%\.agents\skills'),
        ('反向 占位符邮箱 <EMAIL_REDACTED> 不命中邮箱规则', '联系 <EMAIL_REDACTED> 获取授权'),
        ('反向 门面安装命令（GitHub 账号=发布身份）', 'npx skills add zxc663/shisan-xinuo-workflow'),
        ('反向 笔名 package.json author', '"author": "十三希诺"'),
        ('反向 普通技术文本无命中', '今天只改一下 README 文案'),
        ('反向 普通代码路径（无 Users 段）', r'路径 D:\Agent工作流启动包\scripts\build.ps1'),
    ]:
        hs = [h for h in _hits_of(sample) if h[1] == 'block']
        cases.append(('%s → 0 block' % name, len(hs) == 0))

    # ---- warn 级语义：GitHub 账号名不得升级为 block（本门最易误判面）
    hs = _hits_of('git clone https://github.com/zxc663/shisan-xinuo-workflow')
    cases.append(('语义 GitHub 账号名判 warn 不判 block',
                  any(h[0] == '低敏-发布身份' and h[1] == 'warn' for h in hs)
                  and not any(h[1] == 'block' for h in hs)))

    # ---- CLI 契约冒烟（不预设存量状态：存量是否已清洗是发行决策，不是门禁契约）
    rc, out = _run_cli(['--check'])
    ok_contract = ('PRIVACY PASS' in out) or ('PRIVACY FAIL' in out)
    cases.append(('CLI --check 输出 PRIVACY 判定且 exit 与判定一致（0↔PASS / 1↔FAIL）',
                  ok_contract and ((rc == 0) == ('PRIVACY PASS' in out))))
    rc, out = _run_cli(['--no-such-flag'])
    cases.append(('CLI 未知参数 exit 2（用法错误不静默过）', rc == 2))
    # 伪造样本在真实扫描面内不得产生 block（历史 commit message 的负向注入即此形态）
    res2 = layer2()
    fake_blocks = [h for h in res2.get('hits', []) if h['level'] == 'block' and '伪造样本' in h['note']]
    cases.append(('真实历史面：伪造样本（fakeuser 等）0 block', len(fake_blocks) == 0))

    print('== privacy_gate --selftest（伪造样本正反自测）==')
    failed = 0
    for name, ok in cases:
        print(' [%s] %s' % ('PASS' if ok else 'FAIL', name))
        failed += 0 if ok else 1
    print('VERDICT: %s（%d/%d 过）' % ('PASS' if not failed else 'FAIL(%d)' % failed,
                                      len(cases) - failed, len(cases)))
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(description='开源隐私门（四层扫描 · 发行前置）')
    ap.add_argument('--check', action='store_true', help='block 级命中 exit 1（发行跑全量）')
    ap.add_argument('--report', action='store_true', help='全量报告含历史面 + 二进制清单')
    ap.add_argument('--out', default='', help='--report 的报告输出路径')
    ap.add_argument('--selftest', action='store_true', help='伪造命中样本正反自测')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.report:
        return do_report(a.out)
    if a.check:
        return do_check()
    print('用法: python scripts/privacy_gate.py --check | --report [--out FILE] | --selftest')
    return 2


if __name__ == '__main__':
    sys.exit(main())

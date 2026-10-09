# -*- coding: utf-8 -*-
"""facts_sync.py · 口径单源对账器（2.8.x 修正批立 → 2.9 批扩充：类数单源化 F-02 / 承载点补发行面 F-03 / 节头范围断言）

单源事实（计算，非声明）：
  - 活跃细则数 COUNT = details.md 活跃条目行数（排除〔预留槽〕/〔归档〕，与 deploy_injection.details_count 同口径）
  - 条目上限 MAX_ENTRY = details.md 最大条目编号
  - 类数 CLASSES = details.md `## N.` 分节数（F-02 单源化：类数=分节数，历史「17 类」声明值一律以本值为准）
  - 节头范围：details.md 分节头「条目 X-Y」声明 ↔ 该节实际条目 min/max（声明了就断言）
  - 版本 V = package.json（一致性由 verify C 项覆盖，此处不重复）

承载点（声明值，须 == 单源）：每条 = (文件, 正则)；正则内命名组 (?P<n>\\d+)=活跃条数、(?P<c>\\d+)=类数。
历史叙述（沿革/快照/旧版条数：版本历史行、RELEASE-CHECKLIST 时点快照、项目信息决策史）不入本表。

用法：
  python facts_sync.py --check   # 对账：任一承载点声明 ≠ 单源 → exit 1（verify G 项调用）
  python facts_sync.py --fix     # 校正：把偏差承载点改写为单源值（读回断言）
"""
import io, json, re, sys, os
from pathlib import Path

def _confine(p, *extra):
    "路径穿越守卫：写目标 resolve 后必须落在允许根内（cwd/home/temp/脚本目录+额外根）。"
    import tempfile
    from pathlib import Path
    rp = Path(p).resolve()
    roots = [Path.cwd(), Path.home(), Path(tempfile.gettempdir()), Path(__file__).resolve().parent]
    roots += [Path(x) for x in extra]
    if not any(rp.is_relative_to(r.resolve()) for r in roots):
        raise SystemExit('E: path escape -> %s' % rp)
    return str(rp)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, 'skill', 'shisan-xinuo-workflow')

det_path = os.path.join(SK, 'references', 'details.md')
details = open(det_path, encoding='utf-8').read()
active_lines = [l for l in re.findall(r'^(\d{1,3}\. .*)', details, re.M)
                if '〔预留槽〕' not in l and '〔归档〕' not in l]
COUNT = len(active_lines)
MAX_ENTRY = max(int(n) for n in re.findall(r'^(\d{1,3})\. ', details, re.M))
CLASSES = len(re.findall(r'^## \d+\. ', details, re.M))

# (相对路径, [正则…])；命名组 n=活跃条数 / c=类数
CARRIERS = [
    ('README.md', [
        r'不是那 (?P<n>\d+) 条规则',
        # 事实重写版 README（2026-10-10 转型 Phase 0 重锚）：无口径块/英文摘要，唯一活跃条数锚=「值得读的记录」引言；
        # 类数 c 在 README 无活跃声明位（版本历史「405→406 条、32→33 类」为沿革 bullet，按本表口径不入表——
        # 2026-09-30 实证 --fix 曾把 v3.3.1 历史 bullet 的 405/32 机械改写为 406/33），c 由 AGENTS/reference-sources/
        # project-info/package.json/SKILL/details/项目信息 七处承载；渠道表版本行防漂移走版本链 13 处（README 在列）。
    ]),
    ('AGENTS.md', [r'细则 \*\*(?P<n>\d+) 条·(?P<c>\d+) 类\*\*']),
    ('docs/reference-sources.md', [
        r'^(?P<n>\d+) 条落地细则（(?P<c>\d+) 类）',
        r'活跃细则 (?P<n>\d+)',
    ]),
    ('docs/project-info.md', [
        r'细则 (?P<n>\d+) 条/(?P<c>\d+) 类',
        r'details (?P<n>\d+) 条 (?P<c>\d+) 类',
    ]),
    ('package.json', [
        r'渐进式披露（(?P<n>\d+) 条细则 (?P<c>\d+) 类',
        r'\((?P<n>\d+) items / (?P<c>\d+) classes',
    ]),
    (os.path.join('skill', 'shisan-xinuo-workflow', 'SKILL.md'),
     [r'细则 (?P<n>\d+) 条·(?P<c>\d+) 类']),
    (os.path.join('skill', 'shisan-xinuo-workflow', 'templates', 'memory-anchor.md'),
     [r'47 条 / (?P<n>\d+) 细则']),
    (os.path.join('skill', 'shisan-xinuo-workflow', 'references', 'details.md'),
     [r'活跃 (?P<n>\d+) 条，类数=分节数 (?P<c>\d+)']),
    # About 活草案槽（P-G，2026-09-29；v4.0.0 升位）：只锚 项目信息.md 最新一节「下一版预案」三处
    # （节标题/中文变体/英文变体）；历史草案 §六·〇-§六·十=版本时点快照不入表（同头部「历史叙述不入本表」口径）
    ('项目信息.md', [
        r'六·十一、About 描述文案（v4\.0\.0 口径 · (?P<n>\d{1,3}) 条/(?P<c>\d{1,2}) 类',
        r'中文（v4\.0\.0 预案）[\s\S]{0,300}?／(?P<n>\d{1,3}) 条 (?P<c>\d{1,2}) 类症状索引细则',
        r'English（v4\.0\.0 预案）[\s\S]{0,600}?(?P<n>\d{1,3}) lessons in (?P<c>\d{1,2}) categories',
    ]),
]
RANGE_CARRIER = (os.path.join('skill', 'shisan-xinuo-workflow', 'references', 'details.md'),
                 r'1\.–(?P<n>\d{1,3})\.')

# 分节头范围断言：`## N. …（…条目 X-Y…）` ↔ 节内实际条目
SECTION_RANGE = re.compile(r'^## \d+\.[^\n]*?条目 (\d{1,3})-(\d{1,3})', re.M)


def section_range_problems():
    problems = []
    lines = details.split('\n')
    cur = None
    entries = {}
    for ln in lines:
        m = re.match(r'^## (\d+)\. ', ln)
        if m:
            cur = int(m.group(1))
            entries[cur] = []
        elif cur is not None:
            m2 = re.match(r'^(\d{1,3})\. ', ln)
            if m2 and '〔预留槽〕' not in ln and '〔归档〕' not in ln:
                entries[cur].append(int(m2.group(1)))
    for m in SECTION_RANGE.finditer(details):
        lo, hi = int(m.group(1)), int(m.group(2))
        # 找该声明所属分节（m.end() 已越过本节头行，前缀中最后一个节头=本节）
        sec = None
        for sm in re.finditer(r'^## (\d+)\. ', details[:m.end()], re.M):
            sec = int(sm.group(1))
        nums = entries.get(sec, [])
        if not nums:
            problems.append(f'节 §{sec}: 范围 {lo}-{hi} 声明下无活跃条目')
        elif min(nums) != lo or max(nums) != hi:
            problems.append(f'节 §{sec}: 声明 {lo}-{hi} ≠ 实际 {min(nums)}-{max(nums)}')
    return problems


def _check_pattern(t, pat, rel, problems, fix_holder):
    for m in re.finditer(pat, t, re.M):
        bad = []
        if 'n' in m.groupdict() and m.group('n') and int(m.group('n')) != COUNT:
            bad.append(('n', COUNT))
        if 'c' in m.groupdict() and m.group('c') and int(m.group('c')) != CLASSES:
            bad.append(('c', CLASSES))
        # 'e' = 条目上限（编号至 #N）——v3.1 补：README 口径行同句写「编号至 #N」，
        # 旧表只断言条数/类数，导致上限漂移（367 vs 368）不被门禁捕获
        if 'e' in m.groupdict() and m.group('e') and int(m.group('e')) != MAX_ENTRY:
            bad.append(('e', MAX_ENTRY))
        if bad:
            problems.append(f'{rel}: {m.group(0)[:40]!r} 声明 {m.groupdict()} ≠ 单源 n={COUNT}/c={CLASSES}')
            if fix_holder['fix']:
                fix_holder['changed'] = True
                # 同一 match 内多命名组时按 span 起点降序替换：先改靠后的组，
                # 前面组的 span 不受位移影响（正序替换会漏改/错位后续组——2026-09-16 实证）
                for grp, val in sorted(bad, key=lambda x: -m.span(x[0])[0]):
                    s, e = m.span(grp)
                    t = t[:s] + str(val) + t[e:]
    return t


def verify_carriers(fix=False):
    problems = []
    fix_holder = {'fix': fix, 'changed': False}
    root_rp = Path(ROOT).resolve()
    for rel, patterns in CARRIERS:
        # 入口白名单断言：承载点路径 resolve 后必须落在仓根内（read 前置，防 ../ 形态混入硬表）
        if not Path(os.path.join(ROOT, rel)).resolve().is_relative_to(root_rp):
            raise SystemExit('E: carrier path escape -> %s' % rel)
        p = os.path.join(ROOT, rel)
        _cr = _confine(p)
        t = open(_cr, encoding='utf-8').read()
        for pat in patterns:
            t = _check_pattern(t, pat, rel, problems, fix_holder)
        if fix_holder['changed']:
            _cp = _confine(p)
            Path(_cp).write_text(t, encoding='utf-8', newline='')
            fix_holder['changed'] = False
            if rel.endswith('.json'):
                _cj = _confine(p)
                json.loads(open(_cj, encoding='utf-8').read())  # fix 后 JSON 合法性断言（防正则错位写坏结构——2026-09-16 实证）
            _cr2 = _confine(p)
            t2 = open(_cr2, encoding='utf-8').read()
            for pat in patterns:
                for m in re.finditer(pat, t2, re.M):
                    if 'n' in m.groupdict() and m.group('n') and int(m.group('n')) != COUNT:
                        problems.append(f'{rel}: fix 读回失败 {m.group(0)[:40]!r}')
                    if 'c' in m.groupdict() and m.group('c') and int(m.group('c')) != CLASSES:
                        problems.append(f'{rel}: fix 读回失败(c) {m.group(0)[:40]!r}')
    rel, pat = RANGE_CARRIER
    _cr3 = _confine(os.path.join(ROOT, rel))
    t = open(_cr3, encoding='utf-8').read()
    m = re.search(pat, t)
    if not m:
        problems.append(f'{rel}: 条目范围声明未找到')
    elif int(m.group('n')) != MAX_ENTRY:
        problems.append(f'{rel}: 条目范围 1.–{m.group("n")}. ≠ 单源 1.–{MAX_ENTRY}.')
        if fix:
            t = t.replace(f'1.–{m.group("n")}.', f'1.–{MAX_ENTRY}.', 1)
            _cp = _confine((os.path.join(ROOT, rel)))
            Path(_cp).write_text(t, encoding='utf-8', newline='')
    problems += section_range_problems()
    fix_tag = 'fix' if fix else 'check'
    print(f'单源: 活跃细则={COUNT} 条目上限={MAX_ENTRY} 类数(=分节数)={CLASSES}｜模式={fix_tag}')
    if problems:
        for p_ in problems:
            print('[DIFF]', p_)
        print(f'FACTS {"FAIL" if not fix else "FIXED(复核 exit 见重跑)"}: {len(problems)} 处')
        return (0 if fix else 1)
    print('FACTS PASS: 承载点全部与单源一致（条数/类数/条目范围/节头范围）')
    return 0


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else '--check'
    if mode not in ('--check', '--fix'):
        print('用法: python facts_sync.py [--check|--fix]')
        return 2
    return verify_carriers(fix=(mode == '--fix'))


if __name__ == '__main__':
    sys.exit(main())

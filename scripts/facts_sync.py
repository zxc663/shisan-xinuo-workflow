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
import io, re, sys, os

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
        r'现 \*\*(?P<n>\d+) 条 / (?P<c>\d+) 类\*\*',
        r'details (?P<n>\d+)条/(?P<c>\d+)类',
        r'体量大（\*\*(?P<n>\d+) 条\*\*）',
        r'不用背 (?P<n>\d+) 条',
        r'细则 (?P<n>\d+) 条，谁读得完',
        r'细则沿革（现 (?P<n>\d+) 条/(?P<c>\d+) 类）',
    ]),
    ('AGENTS.md', [r'细则 330→(?P<n>\d+)·(?P<c>\d+) 类']),
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
    (os.path.join('docs', 'diagrams', 'working-principle.svg'), [
        r'落地细则 (?P<n>\d+) 条 / (?P<c>\d+) 类',
        r'按症状类（(?P<n>\d+) 条/(?P<c>\d+) 类）',
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
        if bad:
            problems.append(f'{rel}: {m.group(0)[:40]!r} 声明 {m.groupdict()} ≠ 单源 n={COUNT}/c={CLASSES}')
            if fix_holder['fix']:
                fix_holder['changed'] = True
                for grp, val in bad:
                    s, e = m.span(grp)
                    delta = len(str(val)) - (e - s)
                    t = t[:s] + str(val) + t[e:]
                    m = re.search(pat, t[max(0, s - 40):], re.M) or m
    return t


def check(fix=False):
    problems = []
    fix_holder = {'fix': fix, 'changed': False}
    for rel, patterns in CARRIERS:
        p = os.path.join(ROOT, rel)
        t = open(p, encoding='utf-8').read()
        for pat in patterns:
            t = _check_pattern(t, pat, rel, problems, fix_holder)
        if fix_holder['changed']:
            open(p, 'w', encoding='utf-8', newline='').write(t)
            fix_holder['changed'] = False
            t2 = open(p, encoding='utf-8').read()
            for pat in patterns:
                for m in re.finditer(pat, t2, re.M):
                    if 'n' in m.groupdict() and m.group('n') and int(m.group('n')) != COUNT:
                        problems.append(f'{rel}: fix 读回失败 {m.group(0)[:40]!r}')
                    if 'c' in m.groupdict() and m.group('c') and int(m.group('c')) != CLASSES:
                        problems.append(f'{rel}: fix 读回失败(c) {m.group(0)[:40]!r}')
    rel, pat = RANGE_CARRIER
    t = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    m = re.search(pat, t)
    if not m:
        problems.append(f'{rel}: 条目范围声明未找到')
    elif int(m.group('n')) != MAX_ENTRY:
        problems.append(f'{rel}: 条目范围 1.–{m.group("n")}. ≠ 单源 1.–{MAX_ENTRY}.')
        if fix:
            t = t.replace(f'1.–{m.group("n")}.', f'1.–{MAX_ENTRY}.', 1)
            open(os.path.join(ROOT, rel), 'w', encoding='utf-8', newline='').write(t)
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


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else '--check'
    if mode not in ('--check', '--fix'):
        print('用法: python facts_sync.py [--check|--fix]')
        sys.exit(2)
    sys.exit(check(fix=(mode == '--fix')))

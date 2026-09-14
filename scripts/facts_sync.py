# -*- coding: utf-8 -*-
"""facts_sync.py · 口径单源对账器（2.8.x 修正批：文档同步差异机制修法）

单源事实（计算，非声明）：
  - 活跃细则数 C = details.md 活跃条目行数（排除〔预留槽〕/〔归档〕，与 deploy_injection.details_count 同口径）
  - 条目上限 M = details.md 最大条目编号
  - 版本 V = package.json（版本一致性已由 verify C 项覆盖，此处不重复）

承载点（声明值，须 == 单源）：
  每条 = (文件, 正则)。正则内第一个捕获组 = 声明数字。历史叙述（沿革/快照/旧版条数）不入本表。

用法：
  python facts_sync.py --check   # 对账：任一承载点声明 ≠ 单源 → exit 1（verify G 项调用）
  python facts_sync.py --fix     # 校正：把偏差承载点改写为单源值（读回断言）
"""
import io, re, sys, os, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, 'skill', 'shisan-xinuo-workflow')

det_path = os.path.join(SK, 'references', 'details.md')
details = open(det_path, encoding='utf-8').read()
active_lines = [l for l in re.findall(r'^(\d{1,3}\. .*)', details, re.M)
                if '〔预留槽〕' not in l and '〔归档〕' not in l]
COUNT = len(active_lines)
MAX_ENTRY = max(int(n) for n in re.findall(r'^(\d{1,3})\. ', details, re.M))

COUNT_CARRIERS = [
    ('README.md', [
        r'现 \*\*(\d+) 条 / 17 类\*\*',
        r'details (\d+)条/17 类',
        r'体量大（\*\*(\d+) 条\*\*）',
        r'不用背 (\d+) 条',
        r'细则 (\d+) 条，谁读得完',
        r'细则沿革（现 (\d+) 条/17 类）',
    ]),
    ('docs/reference-sources.md', [r'^(\d+) 条落地细则（17 类）']),
    ('docs/project-info.md', [r'details (\d+) 条 17 类']),
    (os.path.join('skill', 'shisan-xinuo-workflow', 'templates', 'memory-anchor.md'),
     [r'47 条 / (\d+) 细则']),
    (os.path.join('skill', 'shisan-xinuo-workflow', 'references', 'details.md'),
     [r'(\d+) 条·17 类']),
    (os.path.join('docs', 'diagrams', 'working-principle.svg'), [
        r'落地细则 (\d+) 条 / 17 类',
        r'按症状类（(\d+) 条/17 类）',
    ]),
]
RANGE_CARRIER = (os.path.join('skill', 'shisan-xinuo-workflow', 'references', 'details.md'),
                 r'1\.–(\d{1,3})\.')


def check(fix=False):
    problems = []
    for rel, patterns in COUNT_CARRIERS:
        p = os.path.join(ROOT, rel)
        t = open(p, encoding='utf-8').read()
        changed = False
        for pat in patterns:
            for m in re.finditer(pat, t, re.M):
                if int(m.group(1)) != COUNT:
                    problems.append(f'{rel}: {m.group(0)[:36]!r} 声明 {m.group(1)} ≠ 单源 {COUNT}')
                    if fix:
                        s, e = m.span(1)
                        t = t[:s] + str(COUNT) + t[e:]
                        changed = True
        if fix and changed:
            open(p, 'w', encoding='utf-8', newline='').write(t)
            t2 = open(p, encoding='utf-8').read()
            for pat in patterns:
                for m in re.finditer(pat, t2, re.M):
                    if int(m.group(1)) != COUNT:
                        problems.append(f'{rel}: fix 读回失败 {m.group(0)[:36]!r}')
    rel, pat = RANGE_CARRIER
    t = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    m = re.search(pat, t)
    if not m:
        problems.append(f'{rel}: 条目范围声明未找到')
    elif int(m.group(1)) != MAX_ENTRY:
        problems.append(f'{rel}: 条目范围 1.–{m.group(1)}. ≠ 单源 1.–{MAX_ENTRY}.')
        if fix:
            t = t.replace(f'1.–{m.group(1)}.', f'1.–{MAX_ENTRY}.', 1)
            open(os.path.join(ROOT, rel), 'w', encoding='utf-8', newline='').write(t)
    fix_tag = 'fix' if fix else 'check'
    print(f'单源: 活跃细则={COUNT} 条目上限={MAX_ENTRY}｜模式={fix_tag}')
    if problems:
        for p_ in problems:
            print('[DIFF]', p_)
        print(f'FACTS {"FAIL" if not fix else "FIXED(复核 exit 见重跑)"}: {len(problems)} 处')
        return (0 if fix else 1)
    print('FACTS PASS: 承载点全部与单源一致')
    return 0


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else '--check'
    if mode not in ('--check', '--fix'):
        print('用法: python facts_sync.py [--check|--fix]')
        sys.exit(2)
    sys.exit(check(fix=(mode == '--fix')))

# -*- coding: utf-8 -*-
"""细则一键检索端口 · detail_lookup
把「打开 details.md → 找症状索引 → 定域 → 读条目」四步压成一条命令。
用法:
  python scripts/detail_lookup.py <关键词> [关键词2...]   # 关键词检索（任意命中，按命中数排序）
  python scripts/detail_lookup.py --id 233               # 按编号直查（T3）
  python scripts/detail_lookup.py --domain 前端           # 按症状域列出条目
  python scripts/detail_lookup.py --index                # 打印症状索引全表
  加 --full 输出条目全文（默认摘要 160 字）
设计: 只用标准库；输出紧凑（token 友好）；命中行可直接贴进任务记录作 errpath 证据。
"""
import io, re, sys, os
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
_SELF = Path(__file__).resolve()
_CANDIDATES = [
    _SELF.parent.parent / 'references' / 'details.md',                                      # 技能副本布局（scripts/ 与 references/ 同级）
    _SELF.parent.parent / 'skill' / 'shisan-xinuo-workflow' / 'references' / 'details.md',  # 源库布局（仓库根 scripts/）
]
DETAILS = next((c for c in _CANDIDATES if c.is_file()), _CANDIDATES[0])


def parse():
    t = DETAILS.read_text(encoding='utf-8')
    # 症状索引: - **域名**【T2】 → #a, #b, ...
    domains = {}
    for m in re.finditer(r'- \*\*(.+?)\*\*【(T2|T3)】 → ([0-9#, ]+)', t):
        ids = [int(x) for x in re.findall(r'\d+', m.group(3))]
        domains[m.group(1)] = (m.group(2), ids)
    # 条目: 行首 NNN. 开始，至下一个条目/小节头
    starts = [(m.start(), int(m.group(1))) for m in re.finditer(r'^(\d{1,3})\. ', t, re.M)]
    entries = {}
    for i, (pos, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(t)
        block = t[pos:end].strip()
        entries[num] = block
    return t, domains, entries


def main():
    args = [a for a in sys.argv[1:]]
    full = '--full' in args
    args = [a for a in args if a != '--full']
    t, domains, entries = parse()

    if not args:
        print(__doc__)
        return
    if args[0] == '--index':
        for name, (layer, ids) in domains.items():
            print(f'[{layer}] {name}: {len(ids)} 条')
        return
    if args[0] == '--id':
        for a in args[1:]:
            num = int(re.sub(r'\D', '', a) or 0)
            e = entries.get(num)
            print(e if e else f'#{num} 不存在（范围 1-{max(entries)}）')
        return
    if args[0] == '--domain':
        key = args[1] if len(args) > 1 else ''
        for name, (layer, ids) in domains.items():
            if key in name:
                print(f'[{layer}] {name}: {", ".join("#"+str(i) for i in ids)}')
        return

    kws = args
    id2domains = {}
    for name, (layer, ids) in domains.items():
        for i in ids:
            id2domains.setdefault(i, []).append(name)
    scored = []
    for num, text in entries.items():
        hits = sum(text.count(k) for k in kws)
        if hits:
            scored.append((hits, num, text))
    scored.sort(key=lambda x: (-x[0], x[1]))
    if not scored:
        print(f'0 命中（关键词: {" ".join(kws)}；可试 --index 换域或换关键词）')
        return
    print(f'{len(scored)} 命中（按相关度排序；errpath 证据格式: detail_lookup "{" ".join(kws)}" → #{scored[0][1]}）')
    for hits, num, text in scored[:12]:
        doms = '/'.join(id2domains.get(num, []))
        body = text if full else text[:160].replace('\n', ' ') + ('…' if len(text) > 160 else '')
        print(f'\n#{num} [{doms}] 命中×{hits}\n{body}')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""T14 · 候选池 29 条 × details.md 405 条查重（2026-09-29，零 API 成本）

方法：每条候选手工挑 2-3 个区分性关键词，走 detail_lookup CLI 真端口检索，
      抓前 3 个命中 ID + 摘要，落 JSONL 供人工裁决「撞车已有 / 新颖可立 / 已承载别处」。
产出：同目录 dedupe.jsonl（检索证据）；裁决表由人工判读后写 mining-dedupe-20260929.md。
边界：只查重不增条（裁决边界③）。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LOOKUP = REPO / 'scripts' / 'detail_lookup.py'
OUT = Path(__file__).resolve().parent / 'dedupe.jsonl'

# (候选号, 简标, 查询词列表) —— 查询词=压缩行里的区分性症状词
CANDS = [
    (1, 'pnpm布局CI', ['pnpm', 'hoisted', 'CI 构建']),
    (2, '兜底吞错上限', ['body-parser', '上限', '500']),
    (3, '判存含目标串', ['判存', '注入检测', '目标串']),
    (4, '机器规格实测OOM', ['内存', 'OOM', '机器规格']),
    (5, '杀软扫描锁', ['杀软', 'rename', '文件锁']),
    (6, 'schema漂移守卫', ['schema', '缺列', '版本守卫']),
    (7, '中文文件名编码', ['GBK', '文件名', '编码']),
    (8, 'heredoc截断', ['heredoc', '截断', '长命令']),
    (9, '期望值公式推导', ['期望值', '公式', '测试断言']),
    (10, '哈希目录升级失效', ['哈希', '缓存目录', '升级']),
    (11, '令牌漂移config', ['令牌', '漂移', '硬编码']),
    (12, '原型机器断言', ['机器断言', '走查', '截图']),
    (13, 'hydration点击丢失', ['hydration', '点击', '水合']),
    (14, 'render引用守卫', ['渲染', '引用相等', 'React']),
    (17, '门禁scope证据', ['门禁', 'scope', '证据']),
    (18, '逗号数字解析', ['逗号', '数字解析', 'BigInt']),
    (19, '用例印象写错', ['用例', '印象', '出题']),
    (20, 'SVG calc parseFloat', ['SVG', 'calc', 'parseFloat']),
    (21, 'CDP直连兜底', ['CDP', '浏览器', '兜底']),
    (22, 'visible断言选择器', ['visible', '断言', '选择器']),
    (23, '错误路径先复现', ['错误路径', '复现', '故障注入']),
    (24, 'scrollWidth断言', ['scrollWidth', '溢出', '截断']),
    (25, '版本凭印象', ['版本号', '凭印象', '实测']),
    (28, 'description40字', ['description', '触发', 'Skill 描述']),
]


def probe(num, label, terms):
    p = subprocess.run([sys.executable, str(LOOKUP)] + terms,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = p.stdout or ''
    ids = re.findall(r'^#(\d+) \[', out, re.M)[:3]
    heads = {}
    for m in re.finditer(r'^#(\d+) \[[^\]]*\][^\n]*\n(.{0,90})', out, re.M):
        heads[m.group(1)] = m.group(2).replace('\n', ' ').strip()
    return {'cand': num, 'label': label, 'terms': terms, 'ids': ids,
            'heads': {i: heads.get(i, '') for i in ids},
            'header': out.splitlines()[0][:80] if out else 'NO-OUTPUT'}


def main():
    rows = [probe(*c) for c in CANDS]
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    for r in rows:
        print('候选%-3d %-14s -> %s' % (r['cand'], r['label'], ','.join('#' + i for i in r['ids']) or '0命中'))
    print('OK -> %s' % OUT.name)


if __name__ == '__main__':
    main()

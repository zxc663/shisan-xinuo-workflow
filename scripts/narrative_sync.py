# -*- coding: utf-8 -*-
"""narrative_sync.py · 叙述类事实对账机制（F8/T22，2026-09-29）

为什么存在：数字类事实已由 facts_sync 单源断言（verify-release G 项），但
`docs/project-info.md`（导航索引）与 `项目信息.md`（决策史）两档各自携带
版本/机制叙述，无对账——同一机制两种描述会静默漂移（外部审计 F8 [P3]）。

机制（机器事实优先，细则 #373）：
  1. 真值一律从权威源实测抽取，不在本脚本硬编码：
     - 细则条数/类数 ← details.md（facts_sync 同口径：^N. 计数减预留/归档槽）
     - 判据版本 ← probe_runner.py 源码 `judge=jX.Y`
     - 当前版本号 ← skill package.json version
  2. 扫两档每一行：行含锚关键词、行含数字、行**不含 YYYY-MM-DD 日期**（历史条目
     豁免——决策史合法保留时点快照）→ 视为「当前态叙述」，其数字与真值冲突 = FINDING。
  3. 头部新鲜度：两档「更新/最后更新」日期距今 >STALE_DAYS → WARN（维护节奏漂移）。

用法：python scripts/narrative_sync.py [--selftest]
退出码：0=无 FINDING（WARN 不影响；--selftest 全过）；1=有当前态叙述漂移或自测失败。
边界：本脚本只探测不修复；接线进 verify-release（变 8 项门禁口径）留发行批拍板。
"""
import json
import re
import sys

try:  # CI/charmap 控制台中文输出兜底（gate_audit 同款）
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DETAILS = REPO / 'skill' / 'shisan-xinuo-workflow' / 'references' / 'details.md'
PROBE_RUNNER = REPO / 'scripts' / 'probe_runner.py'
PACKAGE = REPO / 'package.json'
DOCS = [REPO / 'docs' / 'project-info.md', REPO / '项目信息.md']
SKIP_MARKS = ('〔预留槽〕', '〔归档〕')
STALE_DAYS = 14
DATE_RE = re.compile(r'\d{4}-\d{2}-\d{2}')


def truth():
    """真值实测：抽不到的锚返回 None（调用侧跳过标 SKIP，不硬编码猜值）。"""
    t = {}
    if DETAILS.is_file():
        txt = DETAILS.read_text(encoding='utf-8')
        lines = [ln for ln in txt.splitlines()
                 if re.match(r'^\d{1,3}\. ', ln) and not any(m in ln for m in SKIP_MARKS)]
        t['条数'] = len(lines)
        t['类数'] = len(re.findall(r'^## \d+\. ', txt, re.M))  # F-02 口径：类数=分节数
    if PROBE_RUNNER.is_file():
        m = re.search(r"JUDGE_VERSION\s*=\s*'j(\d+\.\d+)'",
                      PROBE_RUNNER.read_text(encoding='utf-8', errors='replace'))
        if m:
            t['判据'] = m.group(1)
    if PACKAGE.is_file():
        try:
            t['版本'] = json.loads(PACKAGE.read_text(encoding='utf-8'))['version']
        except Exception:
            pass
    return t


# 锚定义：(键, 行须匹配的正则(值无关), 真值键, 说明)；比对取行内 (n 条/c 类) 对 vs 真值
ANCHORS = [
    ('细则规模', re.compile(r'\d{1,3}\s*条\s*[//·]\s*\d{1,2}\s*类|条细则'), '条数', '细则总条数'),
    ('类数', re.compile(r'[//·]\s*\d{1,2}\s*类'), '类数', '细则类数'),
    ('判据版本', re.compile(r'j\d\.\d'), '判据', '判据版本号'),
    ('当前版本', re.compile(r'v\d+\.\d+\.\d+'), '版本', '当前版本号'),
]


def scan():
    t = truth()
    findings, warns, skips = [], [], []
    for line_no, path in enumerate(DOCS):
        if not path.is_file():
            skips.append('%s 不存在' % path.name)
            continue
        for i, ln in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            _check_line(ln, t, findings, src=path.name, line_no=i)
            m = re.search(r'(?:最后更新|更新：)\s*(\d{4}-\d{2}-\d{2})', ln)
            if m:
                age = (datetime.now() - datetime.strptime(m.group(1), '%Y-%m-%d')).days
                if age > STALE_DAYS:
                    warns.append('%s 头部更新=%s（距今 %d 天 >%d）' % (path.name, m.group(1), age, STALE_DAYS))
    return t, findings, warns, skips


def _check_line(ln, t, findings, src='selftest', line_no=0):
    """单行当前态叙述判定（scan 与 --selftest 共用实现——判据单源，F-26 同款纪律）。"""
    is_header = bool(re.search(r'(?:最后)?更新：', ln))
    if ln.lstrip().startswith('>') and not is_header:
        return  # blockquote=引用/About 文案历史存档域（决策史），豁免；更新头行不豁免
    if DATE_RE.search(ln) and not is_header:
        return  # 历史条目豁免（决策史时点快照合法）；「更新：」头行=当前态主张不豁免
    if re.search(r'v\d+\.\d+\.\d+', ln) and not is_header:
        return  # 版本锚行=vN.N.N 时点快照，同豁免
    for key, rx, tkey, desc in ANCHORS:
        if t.get(tkey) is None or not rx.search(ln):
            continue
        tv = t[tkey]
        pairs = [(int(a), int(b)) for a, b in re.findall(r'(\d{1,3})\s*条\s*[//·]\s*(\d{1,2})\s*类', ln)]
        if tkey == '条数':
            if pairs and not any(a == tv for a, _ in pairs):
                findings.append((src, line_no, key, '真值=%d，行内对=%s（行: %s）' % (tv, pairs, ln.strip()[:80])))
            elif not pairs and str(tv) not in ln:
                findings.append((src, line_no, key, '真值=%d，行未含（行: %s）' % (tv, ln.strip()[:80])))
        elif tkey == '类数':
            if pairs and not any(b == tv for _, b in pairs):
                findings.append((src, line_no, key, '真值=%d，行内对=%s（行: %s）' % (tv, pairs, ln.strip()[:80])))
        else:
            if str(tv) not in ln:
                findings.append((src, line_no, key, '真值=%s，行未含（行: %s）' % (tv, ln.strip()[:80])))


def selftest():
    """RS-3 教训回归锚（正向自测盲区跨面三证）：漂移正例必抓 / 三豁免负例必放 / F8 活标本必抓。
    样本数字按运行时真值偏移构造（真值±k），真值演进后自测依旧成立。"""
    t = truth()
    if t.get('条数') is None or t.get('类数') is None:
        print('[SELFTEST] SKIP: 真值抽不到（details 缺失）')
        return 0
    n, c = t['条数'], t['类数']
    cases = [
        ('当前基线 = 细则 %d 条·%d 类' % (n + 1, c), 1),                # 正例：条数漂移必抓
        ('症状索引 %d 条/%d 类全覆盖' % (n, c + 1), 1),                 # 正例：类数漂移必抓
        ('2020-01-01 决策：细则 %d 条/%d 类定稿' % (n + 5, c + 5), 0),   # 负例：历史日期行豁免
        ('v1.2.3 口径：细则 %d 条/%d 类' % (n + 5, c + 5), 0),          # 负例：版本锚行豁免
        ('> 存档（%d 条/%d 类）' % (n + 5, c + 5), 0),                  # 负例：blockquote 存档豁免
        ('> 更新：细则 %d 条/%d 类' % (n + 5, c + 5), 2),               # F8 活标本：blockquote 更新头行不豁免（条数+类数双抓）
        ('最后更新：细则 %d 条/%d 类（全绿）' % (n, c), 0),             # 头行+正确数字=零 FINDING
    ]
    fails = 0
    for i, (ln, want) in enumerate(cases, 1):
        got = []
        _check_line(ln, t, got)
        ok = len(got) == want
        fails += 0 if ok else 1
        print('[%s] case%d want=%d got=%d | %s' % ('PASS' if ok else 'FAIL', i, want, len(got), ln[:52]))
    print('SELFTEST: %d/%d OK' % (len(cases) - fails, len(cases)))
    return 1 if fails else 0


def main():
    if '--selftest' in sys.argv[1:]:
        return selftest()
    t, findings, warns, skips = scan()
    print('== 真值实测：%s' % json.dumps(t, ensure_ascii=False))
    for s in skips:
        print('[SKIP] %s' % s)
    for w in warns:
        print('[WARN] %s' % w)
    for f in findings:
        print('[FINDING] %s:%d %s — %s' % f)
    print('VERDICT: %d FINDING / %d WARN' % (len(findings), len(warns)))
    sys.exit(1 if findings else 0)


if __name__ == '__main__':
    main()

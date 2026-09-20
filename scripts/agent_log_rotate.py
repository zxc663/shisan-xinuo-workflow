# -*- coding: utf-8 -*-
"""agent_log_rotate.py · 记忆档机械归档（细则 #372）

为什么存在：单一「行数」上限可被长行形态绕过（实测 281 行承载 261.5 KB、最长单行
2.4 K 字符）；且「该归档了」若靠人工判断，就会一直不执行。本脚本把归档变成
可重跑动作：超限即把**最旧**的流水条目整行搬到 agent-log-archive-YYYY-MM.md
（移动非删除，保持原顺序），直到回阈内。

用法：
    python scripts/agent_log_rotate.py                      # dry-run（默认，只报计划）
    python scripts/agent_log_rotate.py --apply              # 落刀
    python scripts/agent_log_rotate.py --log "memory/agent-log.md" --archive "memory/agent-log-archive-2026-09.md"
    python scripts/agent_log_rotate.py --flow-max 200 --size-kb 150

判据（双指标先到者为准，细则 #372）：
    流水区 >200 行 或 流水区 >150 KB → 需要归档；教训区 >150 行 → 报警（手工判定）
退出码：0=已达标（无需动作）或已归档成功；1=dry-run 发现超限（需 --apply）；2=用法/文件错误。
"""
import argparse
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

FLOW_HEAD = '## 流水区'
LESSON_HEAD = '## 教训区'


def load(path):
    with open(path, encoding='utf-8') as f:
        return f.read().split('\n')


def split_sections(lines):
    """返回 (头部行, 流水区起始下标, 各节标题下标)。"""
    heads = {}
    for i, ln in enumerate(lines):
        if ln.startswith('## '):
            heads.setdefault(ln.strip(), i)
    return heads


def flow_stats(lines, heads):
    i = heads.get(FLOW_HEAD)
    if i is None:
        return None
    body = lines[i + 1:]
    text = '\n'.join(body)
    return {'start': i + 1, 'lines': len(body), 'bytes': len(text.encode('utf-8')),
            'body': body}


def lesson_lines(lines, heads):
    i = heads.get(LESSON_HEAD)
    if i is None:
        return 0
    j = len(lines)
    for k in range(i + 1, len(lines)):
        if lines[k].startswith('## ') and lines[k].strip() != LESSON_HEAD:
            j = k
            break
    return j - i - 1


def main():
    ap = argparse.ArgumentParser(description='agent-log 机械归档（细则 #372）')
    ap.add_argument('--log', default=os.path.join('memory', 'agent-log.md'))
    ap.add_argument('--archive', default='')
    ap.add_argument('--flow-max', type=int, default=200, help='流水区行数上限')
    ap.add_argument('--flow-kb', type=int, default=150, help='流水区体积上限（KB，UTF-8 字节）')
    ap.add_argument('--lesson-max', type=int, default=150, help='教训区行数上限（仅报警）')
    ap.add_argument('--apply', action='store_true', help='真正写入（默认 dry-run）')
    a = ap.parse_args()

    if not os.path.exists(a.log):
        print('E: 找不到 %s' % a.log)
        return 2
    lines = load(a.log)
    heads = split_sections(lines)
    fs = flow_stats(lines, heads)
    if fs is None:
        print('E: %s 缺「%s」节' % (a.log, FLOW_HEAD))
        return 2
    archive = a.archive or os.path.join(os.path.dirname(a.log), 'agent-log-archive-2026-09.md')

    lessons = lesson_lines(lines, heads)
    need = (fs['lines'] > a.flow_max) or (fs['bytes'] > a.flow_kb * 1024)
    print('== agent_log_rotate ==')
    print(' 流水区: %d 行 / %.1f KB（阈值 %d 行 / %d KB）' % (fs['lines'], fs['bytes'] / 1024.0, a.flow_max, a.flow_kb))
    print(' 教训区: %d 行（阈值 %d 行）' % (lessons, a.lesson_max))
    if lessons > a.lesson_max:
        print(' [WARN] 教训区超限——按细则 #372 需人工判定归档范围（脚本不自动切教训）')
    if not need:
        print('VERDICT: PASS（未超限，无需归档）')
        return 0

    # 计算需搬走的条目数：整行条目（以 '- ' 开头的行）从最旧开始
    entries = [i for i, ln in enumerate(fs['body']) if ln.startswith('- ')]
    keep_lines, keep_bytes, moved = fs['lines'], fs['bytes'], []
    need_lines = keep_lines - a.flow_max
    target_bytes = keep_bytes - a.flow_kb * 1024
    idx = 0
    while idx < len(entries) and (keep_lines > a.flow_max or keep_bytes > a.flow_kb * 1024):
        s = entries[idx]
        e = entries[idx + 1] if idx + 1 < len(entries) else len(fs['body'])
        moved.extend(fs['body'][s:e])
        blk = len('\n'.join(fs['body'][s:e]).encode('utf-8'))
        keep_lines -= (e - s)
        keep_bytes -= blk
        idx += 1
    move_lines = sum(1 for ln in moved if ln.strip())
    print(' 计划: 搬走最旧 %d 个条目 / %d 行；剩余约 %d 行 / %.1f KB'
          % (idx, move_lines, keep_lines, keep_bytes / 1024.0))
    if not a.apply:
        print('VERDICT: DRY-RUN（超限；加 --apply 执行归档）')
        return 1

    moved_set = set()
    # 用「整块行内容」匹配定位（保持顺序）；重复行按出现次序逐个消耗
    remaining = list(moved)
    new_body = []
    for ln in fs['body']:
        if remaining and ln == remaining[0]:
            remaining.pop(0)
            moved_set.add(id(ln))
            continue
        new_body.append(ln)
    new_lines = lines[:fs['start']] + new_body
    with open(a.log, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(new_lines))

    arch_entry = ['', '## 轮转 %s（细则 #372 机械归档；移动非删除）' % __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M'),
                  ''] + moved
    with open(archive, 'a', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(arch_entry))

    lines2 = load(a.log)
    fs2 = flow_stats(lines2, split_sections(lines2))
    print(' 已归档 %d 行 → %s' % (move_lines, archive))
    print(' 归档后流水区: %d 行 / %.1f KB' % (fs2['lines'], fs2['bytes'] / 1024.0))
    ok = (fs2['lines'] <= a.flow_max) and (fs2['bytes'] <= a.flow_kb * 1024)
    print('VERDICT: %s' % ('PASS（已回阈内）' if ok else 'PARTIAL（仍未达标，请复跑）'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())

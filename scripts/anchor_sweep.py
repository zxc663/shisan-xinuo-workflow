# -*- coding: utf-8 -*-
"""anchor_sweep.py · 「在场提示」旧锚清扫单实现（F-26/T19 完全共用，2026-09-29）

为什么存在：旧锚清扫判据（锚头 `^#{2,4} 在场提示 · 工作流 Skill 现已在场` →
任意层级标题 `^#{1,6}(\\s|$)` 即停）此前在 syncer.py 与 install-skill.ps1 各有
一份手抄实现（外部审计 F-26：双实现=漂移面）——本模块收拢为唯一实现：
  - Python 侧：`sweep(text)` 纯函数，syncer.py import 直用；
  - PowerShell 侧：CLI 文件介质形态（#401：跨 shell 中文走 stdin/管道有编码坑，
    禁管道传正文）——`--sweep <输入文件> --out <清扫输出> --json <统计输出>`。

判据（P0 修复版定版，改动须双侧冒烟）：
  1. 锚头行匹配 `^#{2,4} 在场提示 · 工作流 Skill 现已在场` → 开始吞块并记录行内版本号；
  2. 块内遇到任意层级标题（1-6 级）即停（防吞锚点后同层级用户内容）；
  3. 锚块删除后收紧尾部连续空行；留痕=删除行数+版本清单+前 5 行预览。
"""
import argparse
import json
import re
from pathlib import Path

HEAD = re.compile(r'^#{2,4} 在场提示 · 工作流 Skill 现已在场')
ANY_HEAD = re.compile(r'^#{1,6}(\s|$)')
VER = re.compile(r'v\d+\.\d+\.\d+')


def sweep(text):
    """返回 (cleaned_text, stats)；stats 含 removed 行数/版本清单/前 5 行预览。"""
    lines = text.splitlines(keepends=True)
    outl, removed, versions = [], [], []
    i = 0
    while i < len(lines):
        ln = lines[i]
        if HEAD.match(ln):
            vm = VER.search(ln)
            versions.append(vm.group(0) if vm else '?')
            i += 1
            while i < len(lines) and not ANY_HEAD.match(lines[i]):
                removed.append(lines[i])
                i += 1
            while outl and outl[-1].strip() == '':
                outl.pop()
            continue
        outl.append(ln)
        i += 1
    stats = {'removed': len(removed), 'versions': versions,
             'preview': [r.rstrip()[:80] for r in removed[:5]]}
    return ''.join(outl), stats


def main():
    ap = argparse.ArgumentParser(description='旧锚清扫单实现（F-26）；PS 侧走文件介质，禁管道传中文正文')
    ap.add_argument('--sweep', required=True, help='含旧锚的输入文件（原记忆文件内容）')
    ap.add_argument('--out', required=True, help='清扫后正文写出文件')
    ap.add_argument('--json', required=True, help='统计 JSON 写出文件')
    a = ap.parse_args()
    src = Path(a.sweep)
    if not src.is_file():
        print('E: 输入文件不存在: %s' % src)
        raise SystemExit(2)
    cleaned, stats = sweep(src.read_text(encoding='utf-8'))
    Path(a.out).write_text(cleaned, encoding='utf-8')
    Path(a.json).write_text(json.dumps(stats, ensure_ascii=False), encoding='utf-8')
    print('[anchor_sweep] removed=%d versions=%s' % (stats['removed'], ','.join(stats['versions']) or '—'))


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""重生成包内分发副本（规范形态=头注行+根版全文；R2 同款）。
用法：python scripts/regen_dist_copies.py gate_audit.py [更多文件名...]
"""
import io
import sys

HDR = '# 分发副本：权威=家族源库根 scripts/{name}（随包分发供 shisan-xinuo-workflow/scripts/ 调用；修改时两处同步，见 RELEASE-CHECKLIST）。'
PKG = 'skill/shisan-xinuo-workflow/scripts/'


def main():
    names = [a for a in sys.argv[1:] if a]
    if not names:
        print('用法: python scripts/regen_dist_copies.py <scripts文件名> [...]')
        return 2
    for name in names:
        root = io.open('scripts/' + name, encoding='utf-8').read().replace('\r\n', '\n')
        lines = root.split('\n')
        lines.insert(1 if lines[0].startswith('#!') else 0, HDR.format(name=name))
        io.open(PKG + name, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
        print('regen:', PKG + name)
    return 0


if __name__ == '__main__':
    sys.exit(main())

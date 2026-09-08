# -*- coding: utf-8 -*-
"""开发入口 shim：单一实现在 skill/shisan-xinuo-workflow/scripts/detail_lookup.py
（随 syncer 分发到各技能副本；本 shim 保证仓库根 `python scripts/detail_lookup.py` 用法不变）。"""
import runpy
import sys
from pathlib import Path

_target = Path(__file__).resolve().parent.parent / 'skill' / 'shisan-xinuo-workflow' / 'scripts' / 'detail_lookup.py'
if not _target.is_file():
    print(f'E: 找不到实现文件: {_target}')
    sys.exit(1)
runpy.run_path(str(_target), run_name='__main__')

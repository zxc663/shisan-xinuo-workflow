# -*- coding: utf-8 -*-
"""盲判组装器（blind-ab-20260926 · 可复算工件，配套 docs/design-specs/blind-eval-design.md）

读两臂 output.txt → 去标识（臂标签与探针根路径掩码）→ 确定性编号（SHA-256 排序键，
种子固定=可复算；非加密用途，仅打乱呈现顺序）→
产出 blind-input.json（盲判输入）+ unblind-map.json（解盲映射，评审不可见）。

调用（环境变量传根目录，位置参数传标签与场景）：
    PROBE_ROOT=<探针根> LABEL_A=blind-a LABEL_B=blind-b python assemble_blind.py l3-delete l3-key ...

盲法声明：执行者（部署两臂者）不参与判分；机判层（probe_runner j2.5）不接收分组信息；
第二层独立模型评审只见随机编号样本与预注册判分表，不知编号→分组映射。
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

SEED = '20260926'  # 固定种子=编号可复算

LABEL_RE = re.compile(r'[A-Za-z0-9_.-]+\Z')
SCENE_RE = re.compile(r'[A-Za-z0-9_-]+\Z')


def sort_key(key):
    return hashlib.sha256((SEED + key).encode('utf-8')).hexdigest()


def scrub(text, labels):
    for lab in labels:
        text = text.replace(lab, 'ARM-x')
    return re.sub(r'[A-Za-z]:[\\/][^\s"\'`]*shisan-probes[^\s"\'`]*', '<PROBE_ROOT>', text)


def main():
    env_root = os.environ.get('PROBE_ROOT', '')
    label_a = os.environ.get('LABEL_A', '')
    label_b = os.environ.get('LABEL_B', '')
    scenes = sys.argv[1:]
    if not env_root or not label_a or not label_b or not scenes:
        print(__doc__)
        sys.exit(2)
    if not (LABEL_RE.fullmatch(label_a) and LABEL_RE.fullmatch(label_b)):
        print('BAD LABEL')
        sys.exit(2)
    for sc in scenes:
        if not SCENE_RE.fullmatch(sc):
            print(f'BAD SCENE: {sc!r}')
            sys.exit(2)
    root = Path(env_root).resolve()
    if not root.is_dir():
        print(f'NOT A DIR: {root}')
        sys.exit(2)
    samples = []
    for lab in (label_a, label_b):
        for sc in scenes:
            probe_dir = (root / f'{lab}-{sc}').resolve()
            # resolve 后必须仍位于探针根之内（防符号链接/相对段逃逸）
            if root not in probe_dir.parents:
                print(f'OUTSIDE ROOT: {probe_dir}')
                sys.exit(2)
            fp = probe_dir / 'output.txt'
            if not fp.is_file():
                print(f'MISSING: {fp}')
                sys.exit(2)
            raw = fp.read_text(encoding='utf-8')
            clean = scrub(raw, (label_a, label_b))
            if label_a in clean or label_b in clean:
                print(f'RESIDUAL LABEL in {lab}-{sc}')
                sys.exit(3)
            samples.append({'key': f'{lab}|{sc}', 'text': clean})
    samples.sort(key=lambda s: sort_key(s['key']))
    blinded, mapping = [], {}
    for i, s in enumerate(samples, 1):
        sid = f'S{i:02d}'
        blinded.append({'id': sid, 'text': s['text']})
        mapping[sid] = s['key']
    base = Path(__file__).resolve().parent
    (base / 'blind-input.json').write_text(
        json.dumps(blinded, ensure_ascii=False, indent=1), encoding='utf-8')
    (base / 'unblind-map.json').write_text(
        json.dumps(mapping, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'OK: {len(blinded)} samples blinded (seed={SEED}, sha256-order) -> blind-input.json / unblind-map.json')


if __name__ == '__main__':
    main()

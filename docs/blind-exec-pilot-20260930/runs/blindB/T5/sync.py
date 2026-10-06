"""配置同步器：读源配置、转换、写目标。"""

import sys


def read(src):
    with open(src, "r", encoding="utf-8") as f:
        return f.read()


def transform(data):
    """把 key=value 文本转成 dict。"""
    out = {}
    for line in data.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip()
    return out


def write(dst, cfg):
    import json
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def sync(src, dst):
    """读 → 转换 → 写；失败时在 stderr 标明出错环节，返回值仍为 True/False。"""
    stage = "read"
    try:
        data = read(src)
        stage = "transform"
        cfg = transform(data)
        stage = "write"
        write(dst, cfg)
        return True
    except Exception as exc:
        print(f"sync failed in {stage} stage: {type(exc).__name__}: {exc}", file=sys.stderr)
        return False

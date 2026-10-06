"""配置同步器：读源配置、转换、写目标。"""


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
    try:
        data = read(src)
        cfg = transform(data)
        write(dst, cfg)
        return True
    except Exception:
        return False

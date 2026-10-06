"""按列聚合生成报表文本。"""


def summarize(rows, column):
    """按 column 分组计数，返回 '值: N' 行列表，按计数降序。"""
    counts = {}
    for r in rows:
        k = r.get(column, "")
        counts[k] = counts.get(k, 0) + 1
    pairs = sorted(counts.items(), key=lambda kv: -kv[1])
    return ["%s: %d" % (k, v) for k, v in pairs]

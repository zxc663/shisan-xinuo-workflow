"""读取原始 CSV 行。"""
import csv


def ingest(path):
    """读入 CSV，返回 dict 行列表；空文件返回 []。"""
    with open(path, "r", encoding="utf-8-sig") as f:
        return [dict(r) for r in csv.DictReader(f)]

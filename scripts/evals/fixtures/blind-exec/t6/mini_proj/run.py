"""入口：python run.py <csv路径> <分组列> —— 打印聚合报表。"""
import sys
from ingest import ingest
from report import summarize


def main(argv):
    if len(argv) < 2:
        print("usage: python run.py <csv> <column>")
        return 1
    rows = ingest(argv[0])
    for line in summarize(rows, argv[1]):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

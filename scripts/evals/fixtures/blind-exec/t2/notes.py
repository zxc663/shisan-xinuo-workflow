"""笔记数据与查询。"""

NOTES = [
    {"title": "周会纪要", "tags": ["work", "meeting"]},
    {"title": "购物清单", "tags": ["life"]},
    {"title": "发布清单", "tags": ["work", "release"]},
    {"title": "读书摘抄", "tags": ["life", "reading"]},
    {"title": "值班表", "tags": ["work"]},
]


def list_notes():
    """返回全部笔记标题。"""
    return [n["title"] for n in NOTES]

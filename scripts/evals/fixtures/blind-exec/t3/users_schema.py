"""用户序列化 schema（API 契约源）。"""

USER_FIELDS = ["id", "name", "email"]


def serialize(user):
    """按契约字段序列化用户记录。"""
    return {k: user.get(k) for k in USER_FIELDS}

"""用户序列化 schema（API 契约源）。"""

USER_FIELDS = ["id", "name", "email", "timezone"]
DEFAULT_TIMEZONE = "UTC"


def serialize(user):
    """按契约字段序列化用户记录（timezone 缺失时取缺省值）。"""
    data = {k: user.get(k) for k in USER_FIELDS}
    data["timezone"] = data["timezone"] or DEFAULT_TIMEZONE
    return data

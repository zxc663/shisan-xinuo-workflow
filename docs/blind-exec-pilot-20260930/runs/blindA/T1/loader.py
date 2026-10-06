"""配置合并器：defaults 为内置默认，user_cfg 为用户覆盖。"""

DEFAULTS = {"timeout": 30, "retries": 3, "verbose": False}


def load_overrides(user_cfg, defaults=None):
    """合并用户覆盖项。

    约定语义：user_cfg=None 表示「用户未提供配置」；user_cfg={}（空 dict）
    表示「用户显式选择了全默认配置」。两者合并结果相同，但 provided 标记不同。
    返回 (merged, provided)。
    """
    if defaults is None:
        defaults = DEFAULTS
    if user_cfg:
        return {**defaults, **user_cfg}, True
    return dict(defaults), False

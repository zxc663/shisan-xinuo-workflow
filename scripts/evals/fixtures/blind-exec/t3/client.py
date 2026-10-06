"""客户端渲染：展示用户卡片文本。"""
from users_schema import serialize


def render_user_card(user):
    u = serialize(user)
    return "%s | %s | %s" % (u["id"], u["name"], u["email"])

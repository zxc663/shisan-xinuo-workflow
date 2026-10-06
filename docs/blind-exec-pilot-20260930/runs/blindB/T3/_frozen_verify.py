"""T3 验收：timezone 契约字段+调用点同步。"""
import users_schema
from users_schema import serialize
import client

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and cond

check("schema 含 timezone", "timezone" in users_schema.USER_FIELDS)
u = serialize({"id": 1, "name": "a", "email": "a@b.c"})
check("缺省 timezone='UTC'", u.get("timezone") == "UTC")
u2 = serialize({"id": 1, "name": "a", "email": "a@b.c", "timezone": "Asia/Shanghai"})
check("显式 timezone 透传", u2.get("timezone") == "Asia/Shanghai")
card = client.render_user_card({"id": 2, "name": "b", "email": "b@c.d"})
check("调用点展示 timezone", "UTC" in card)

print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)

"""T1 验收：provided 标记语义三态断言。"""
import loader

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and cond

d = {"a": 1, "b": 2}
m, p = loader.load_overrides(None, d)
check("None -> provided=False", p is False)
check("None -> merged=defaults", m == d)

m, p = loader.load_overrides({}, d)
check("{} -> provided=True（用户显式全默认）", p is True)
check("{} -> merged=defaults", m == d)

m, p = loader.load_overrides({"a": 9}, d)
check("覆盖 -> provided=True", p is True)
check("覆盖 -> merged 生效", m["a"] == 9 and m["b"] == 2)

print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)

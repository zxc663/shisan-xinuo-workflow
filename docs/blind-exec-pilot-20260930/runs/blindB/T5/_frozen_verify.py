"""T5 验收：错误路径环节可区分（read 失败 vs transform 失败）。"""
import io
import sync as s

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and cond

def capture(fn):
    buf = io.StringIO()
    try:
        import contextlib
        with contextlib.redirect_stderr(buf), contextlib.redirect_stdout(buf):
            fn()
    except SystemExit:
        pass
    return buf.getvalue()

# 场景1：源文件不存在 -> 应能看出是读取环节失败
out1 = capture(lambda: s.sync("no_such_src.ini", "out1.json"))
check("read 失败可辨认（信息含 read/读取/源）", any(w in out1.lower() for w in ["read", "读取", "源文件", "no_such_src"]))

# 场景2：transform 环节失败（通过替换 transform 注入）-> 应能看出是转换环节失败
orig = s.transform
def bad_transform(data):
    raise ValueError("boom")
s.transform = bad_transform
import os
with open("ok.ini", "w", encoding="utf-8") as f:
    f.write("a=1\n")
out2 = capture(lambda: s.sync("ok.ini", "out2.json"))
s.transform = orig
check("transform 失败可辨认（信息含 transform/转换）", any(w in out2.lower() for w in ["transform", "转换"]))

# 场景3：正常路径不回归
check("正常同步仍成功", s.sync("ok.ini", "out3.json") is True and os.path.exists("out3.json"))

print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)

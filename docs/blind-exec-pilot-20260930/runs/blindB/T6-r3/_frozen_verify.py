"""T6 验收：全景文档六维覆盖检查表（机判子集）。"""
import os
import sys

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and cond

candidates = ["docs/project-info.md", "project-info.md", "docs/全景文档.md", "全景文档.md", "README.md"]
doc = next((c for c in candidates if os.path.exists(c)), None)
check("全景文档存在", doc is not None)
if doc:
    text = open(doc, encoding="utf-8").read()
    for mod in ["ingest", "report", "run"]:
        check("模块表覆盖 %s" % mod, mod in text)
    check("配置项提及（config）", "config" in text.lower())
    check("运行方式节", ("运行" in text) or ("usage" in text.lower()) or ("用法" in text))

print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)

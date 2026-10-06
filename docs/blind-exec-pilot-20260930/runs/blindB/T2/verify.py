"""T2 验收：--tag 过滤 + 无参行为回归（可重跑）。

运行：python verify.py   退出码 0=全过。
"""
import os
import subprocess
import sys

CWD = os.path.dirname(os.path.abspath(__file__))
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")

WORK_TITLES = ["周会纪要", "发布清单", "值班表"]
ALL_TITLES = ["周会纪要", "购物清单", "发布清单", "读书摘抄", "值班表"]
LIFE_TITLES = ["购物清单", "读书摘抄"]

results = []


def run_py(code):
    p = subprocess.run(
        [sys.executable, "-c", code],
        cwd=CWD, capture_output=True, text=True, encoding="utf-8", env=ENV,
    )
    return p.returncode, p.stdout, p.stderr


def list_stdout(titles):
    """复现 main 对 list 的输出形态：逐行标题 + 返回列表 repr。"""
    return "\n".join(titles) + "\n" + repr(titles) + "\n"


def record(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), "-", name)
    if not ok:
        print("    detail:", detail)
    results.append(ok)


# 规定命令一：--tag work 只返回含 work 标签的标题
rc, out, err = run_py("import cli; print(cli.main(['list','--tag','work']))")
record("main(['list','--tag','work']) 只含 work", rc == 0 and out == list_stdout(WORK_TITLES),
       "rc=%s out=%r err=%r" % (rc, out, err))

# 规定命令二：不带 --tag 全量、同序（回归）
rc, out, err = run_py("import cli; print(cli.main(['list']))")
record("main(['list']) 全量回归", rc == 0 and out == list_stdout(ALL_TITLES),
       "rc=%s out=%r err=%r" % (rc, out, err))

# 边角：另一标签
rc, out, err = run_py("import cli; print(cli.main(['list','--tag','life']))")
record("--tag life", rc == 0 and out == list_stdout(LIFE_TITLES),
       "rc=%s out=%r err=%r" % (rc, out, err))

# 边角：不存在的标签 -> 空列表且正常退出
rc, out, err = run_py("import cli; print(cli.main(['list','--tag','nope']))")
record("--tag nope 空结果", rc == 0 and out == "[]\n",
       "rc=%s out=%r err=%r" % (rc, out, err))

# 边角：空 argv 默认 list（原有默认行为）
rc, out, err = run_py("import cli; print(cli.main([]))")
record("main([]) 默认 list", rc == 0 and out == list_stdout(ALL_TITLES),
       "rc=%s out=%r err=%r" % (rc, out, err))

# 边角：--tag 缺值 -> 显式报错而非静默
rc, out, err = run_py("import cli; cli.main(['list','--tag'])")
record("--tag 缺值报错", rc != 0 and "--tag requires a value" in err,
       "rc=%s err=%r" % (rc, err))

# 端到端：模块文档行形态
p = subprocess.run([sys.executable, "cli.py", "list", "--tag", "work"],
                   cwd=CWD, capture_output=True, text=True, encoding="utf-8", env=ENV)
record("python cli.py list --tag work", p.returncode == 0 and p.stdout == "\n".join(WORK_TITLES) + "\n",
       "rc=%s out=%r err=%r" % (p.returncode, p.stdout, p.stderr))

print()
print("RESULT:", "ALL PASS" if all(results) else "FAILED")
sys.exit(0 if all(results) else 1)

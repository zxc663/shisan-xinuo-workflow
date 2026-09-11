import json
import os
import sys
from pathlib import Path

# SessionStart 纪律包注入（hooks=实证最强触达载体）：每次会话启动无条件注入最小纪律包
# （状态行模板 + TOP 一行 + GATE 指针）；cwd 是 git 项目且无 memory/agent-log.md 时
# 附加承载检查提醒行。措辞与注入核心常驻保留集同源，改措辞先改注入核心再同步此处。
DISCIPLINE_PACK = (
    "[工作流纪律包·hooks 通道]\n"
    "状态行：每会话首产物输出一行 `Context: state=<读档/新建/单发> L=<L1/L2-S/L2-F> "
    "confirm=<无需/已问/豁免:理由>`\n"
    "错误必查 TOP（处置后必留 errpath 行 症状→处置路径）："
    "#294 Edit 报 not read/modified=文件双通道混用｜#233 命名直觉=假绿｜#228 改包先重编｜"
    "#229 常驻进程旧 dist｜#214 响应分层断言｜#163 统一错误契约｜"
    "#256·#270 异步栈丢调用点·响应体只消费一次｜#262 深拷贝语义变体\n"
    "收尾 GATE 9 字段：level/v/cmd/exit/files/refs/errpath/lessons/exempt"
    "（权威定义=注入核心交付段）"
)
CARRIER_HINT = (
    "承载检查提醒：当前目录是 git 项目但 memory/agent-log.md 不存在。"
    "请先建一档制单文件四区骨架（状态段/教训区/偏好段/流水区，参照技能 "
    "templates/agent-log-template.md，禁空文件占位），完成承载检查后再进入下一步。"
)

try:
    raw = sys.stdin.read()
    payload = json.loads(raw) if raw.strip() else {}
except Exception:
    payload = {}

context = DISCIPLINE_PACK
cwd = payload.get("cwd") or os.getcwd()
try:
    root = Path(cwd)
    if (root / ".git").exists() and not (root / "memory" / "agent-log.md").is_file():
        context += "\n" + CARRIER_HINT
except Exception:
    pass
try:
    print(json.dumps({"additionalContext": context}, ensure_ascii=False))
except Exception:
    pass  # 任何异常静默放行，不阻塞会话

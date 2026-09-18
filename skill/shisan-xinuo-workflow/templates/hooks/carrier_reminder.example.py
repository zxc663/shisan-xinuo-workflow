import json
import os
import sys
from pathlib import Path

def _hook_log(msg):
    """钩子异常/静默兜底：写独立 hook-log（不入会话输出）；位置可用 HOOK_LOG 环境变量覆盖。"""
    import os
    from datetime import datetime
    p = os.environ.get('HOOK_LOG') or os.path.join(os.path.expanduser('~'), '.zcode', 'cli', 'hooks-log.txt')
    try:
        with open(p, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}" + chr(10))
    except Exception as e:
        _hook_log(f'{__file__}: 输出推送失败 {e}')


# SessionStart 纪律包注入（hooks=实证最强触达载体）：每次会话启动无条件注入最小纪律包
# （状态行模板 + TOP 一行 + GATE 指针）；cwd 是 git 项目且无 memory/agent-log.md 时
# 附加承载检查提醒行。措辞与注入核心常驻保留集同源，改措辞先改注入核心再同步此处。
DISCIPLINE_PACK = (
    "[工作流纪律包·hooks 通道]\n"
    "每轮复述：每一用户轮首产物=复述（新任务全量三行；追加/继续=一行：收到 X｜理解为 Y｜边界 Z）\n"
    "状态行（开工/阶段边界）：`Context: state=<读档/新建/单发> L=<L1/L2-S/L2-F> "
    "confirm=<无需/已问/豁免:理由>`\n"
    "回指加载：本核心为瘦身版——以 Skill 工具加载 shisan-xinuo-workflow（SKILL.md），"
    "细则/模板按症状索引回指\n"
    "复杂任务思考链：本质/必要/惯性三拆→显式列约束与假设→因果链 3-5 层逐环验证→围绕系统约束定对策（rules #7-#11）\n"
    "错误必查 TOP（处置后必留 errpath 行 症状→处置路径）："
    "#294 Edit 报 not read/modified=文件双通道混用｜#233 命名直觉=假绿｜#228 改包先重编｜"
    "#229 常驻进程旧 dist｜#214 响应分层断言｜#163 统一错误契约｜"
    "#256·#269 异步栈丢调用点·响应体只消费一次｜#262 深拷贝语义变体\n"
    "收尾 GATE 12 字段：level/v/cmd/exit/files/refs/errpath/lessons/exempt/caps/effort/stop_reason（cmd/exit/files 须真实挂靠，虚假=降级）"
    "（权威定义=注入核心交付段；refs 填 grep 实测值，禁自估）"
)
CARRIER_HINT = (
    "承载检查提醒：当前目录是 git 项目但 memory/agent-log.md 不存在。"
    "请先建一档制单文件四区骨架（状态段/教训区/偏好段/流水区，参照技能 "
    "templates/agent-log-template.md，禁空文件占位），完成承载检查后再进入下一步。"
)

try:
    raw = sys.stdin.read()
    payload = json.loads(raw) if raw.strip() else {}
except Exception as e:
    payload = {}
    _hook_log(f'{__file__}: stdin 解析失败 {e}')

context = DISCIPLINE_PACK
cwd = payload.get("cwd") or os.getcwd()
try:
    root = Path(cwd)
    if (root / ".git").exists() and not (root / "memory" / "agent-log.md").is_file():
        context += "\n" + CARRIER_HINT
except Exception as e:
    _hook_log(f'{__file__}: 异常 {e}')
try:
    print(json.dumps({"additionalContext": context}, ensure_ascii=False))
except Exception as e:
    _hook_log(f'{__file__}: 异常 {e}')  # 任何异常静默放行，不阻塞会话

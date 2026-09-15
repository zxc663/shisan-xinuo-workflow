import json
import sys

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


# PostToolUseFailure TOP 推送（错误发生=最强触发时机）：工具执行失败时推送
# 「错误必查 TOP」一行，提示内联处置+处置后留 errpath 行。平台不支持该事件时
# 本脚本不会被调用（降级路径=SessionStart 纪律包已含 TOP 行，见 README 多平台表）。
TOP_LINE = (
    "[错误必查 TOP·hooks 通道] 工具执行失败——先内联处置："
    "#294 Edit 报 not read/modified=文件双通道混用（重新 Read 该文件再 Edit）｜"
    "#233 命名直觉=假绿｜#228 改包先重编｜#229 常驻进程旧 dist｜#214 响应分层断言｜"
    "#163 统一错误契约｜#256·#270 异步栈丢调用点·响应体只消费一次｜#262 深拷贝语义变体；"
    "处置完成后必留 errpath 行（症状→处置路径）"
)

try:
    raw = sys.stdin.read()
    payload = json.loads(raw) if raw.strip() else {}
except Exception as e:
    payload = {}
    _hook_log(f'{__file__}: stdin 解析失败 {e}')

tool = payload.get("tool_name") or payload.get("toolName") or ""
line = f"（{tool} 失败）{TOP_LINE}" if tool else TOP_LINE
try:
    print(json.dumps({"additionalContext": line}, ensure_ascii=False))
except Exception as e:
    _hook_log(f'{__file__}: 异常 {e}')  # 任何异常静默放行，不阻塞会话

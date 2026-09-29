import json, sys

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

# PostToolUse 守卫：ZCode 的 PostToolUseFailure 事件不覆盖 Bash 非零退出，
# 本守卫在全量 PostToolUse 事件上精准识别 Bash 失败（tool_response.status=failed
# 或 exitCode≠0）才推送 TOP；
# 其余工具/成功调用静默放行（Edit 等失败仍由 PostToolUseFailure 通道推送，防双推）。
TOP = ("[错误必查 TOP·hooks 通道] Bash 命令失败（exit≠0）——先内联处置："
       "#233 命名直觉=假绿（先 ls/cat 实测）｜#228 改包先重编｜#229 常驻进程旧 dist｜"
       "其余症状按注入核心 TOP 清单；处置完成后必留 errpath 行（症状→处置路径）")
# 执行 checklist（G10，2026-09-29）：两条高频踩坑的条件触发提醒——只在命中形态时推，成功且未命中=静默放行防噪音。
CK_MULTILINE = ("[执行 checklist] 多行 python/含反斜杠续行命令禁用 bash heredoc/python -c 内联——"
                "改 Write 工具落 .py 再运行（heredoc 反斜杠单会话三犯，先落盘后编译）")
CK_BG = ("[执行 checklist] 后台/值守动作必须在汇报中记录任务 ID（exec_*）与输出文件路径——"
         "值守声称未落工具=不可验证（无 ID=未发生）")
try:
    raw = sys.stdin.read()
    payload = json.loads(raw) if raw.strip() else {}
except Exception as e:
    payload = {}
    _hook_log(f'{__file__}: stdin 解析失败 {e}')
tool = payload.get('toolName') or payload.get('tool_name') or ''
if tool != 'Bash':
    sys.exit(0)
tr = payload.get('tool_response') or payload.get('toolResponse') or {}
code = tr.get('exitCode')
failed = (tr.get('status') == 'failed') or (isinstance(code, int) and code != 0)
ti = payload.get('tool_input') or payload.get('toolInput') or {}
cmd = str(ti.get('command') or '')
checks = []
if ('<<' in cmd or 'python -c' in cmd or 'python  -c' in cmd) and '\n' in cmd:
    checks.append(CK_MULTILINE)
if ti.get('run_in_background') or ti.get('runInBackground'):
    checks.append(CK_BG)
push = []
if failed:
    push.append(f'（Bash exit={code}）{TOP}')
push += checks
if push:
    try:
        print(json.dumps({'additionalContext': '｜'.join(push)}, ensure_ascii=False))
    except Exception as e:
        _hook_log(f'{__file__}: 输出推送失败 {e}')

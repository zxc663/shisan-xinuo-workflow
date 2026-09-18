# ZCode 数据库损坏事故 · 处置与交接（2026-09-18）

> 用途：本文件是**交接件**——2026-09-18 的修复轮次照此执行；如判据或路径有变，先改本文件再动手。
> 路径口径：仓内版本已脱敏（`<USERPROFILE>` / `<备份根>`）；含本机绝对路径的完整原件留本地 `memory/incidents/`（随 `.gitignore` 不入仓）。

## 一句话

上一批「全树 PAT 消毒」把两个 SQLite 二进制库当文本重写，导致 ZCode 3.12.3.7463 启动在 `preparing_host_storage` 阶段报 `corrupt`（`sqliteCode 11`）。两个库已做**完整快照备份**；修复动作安排在 23:00 后执行（用户令：先备份、后修）。

## 修复执行结果（**已执行 · 2026-09-18 10:10**）

用户授权「删呗，修复吧」（项目文件另有留档）后按 **A 路线（抢救 → 重建）** 执行完毕。

1. **文本抢救（先做，只读）** → `<备份根>\zcode-db-rescue-output\`
   - `tasks-index.sqlite.strings.txt` —— 59,454 段 / 3,701,394 字符
   - `db.sqlite.strings.txt` —— 3,276,292 段 / 628,173,639 字符（≈736 MB，可用 `rg` 离线检索历史会话正文）
   - `task-titles-recovered.txt` —— 183 条去重任务标题 + 15 个去重工作区路径（可对账、可辅助人工重建任务列表）
2. **移库（移动而非删除，可回滚）** → `<备份根>\zcode-backup-20260918\10-已移除的损坏库\`（`tasks-index.sqlite`、`cli-db.sqlite` 及各自 `-shm`/`-wal`，共 4 件）
3. **应用重建并验证**：

| 判据 | 实测 |
| --- | --- |
| 数据库启动 | `10:10:09 [database-startup] terminal {"attemptId":"2d9e9126-51d0-47c3-82b0-da3ec57f36ca","status":"ready","durationMs":5755}`；不再出现 `errorCode=corrupt` |
| 新 tasks-index | 147,456 B，`PRAGMA quick_check = ok`，9 表 + 23 索引（`tasks` / `task_groups` / `automations` / `automation_runs` / `off_peak_tasks` / `tasks_schema_migration` …） |
| 新 CLI 库 | 413,696 B，`PRAGMA quick_check = ok`，24 表 + 70 索引 + 2 触发器（`session` / `message` / `part` / `local_setting` …） |
| 应用进程 | ZCode 15 进程常驻，主窗口标题 `ZCode`（PID 51224） |

**结果**：ZCode 恢复正常启动。任务列表与 CLI 会话历史按用户口径接受清空；正文内容另有抢救归档，可离线检索。

## 报错原文与日志对证

- 启动报告（用户提供）：`startupId=d151e689-5dc7-4680-890c-2aedf789e79a`、`attemptId=b03e697b-fa61-48b7-950e-c736588f4bfc`、`sequence=6`、`phase=failed`、`failedPhase=preparing_host_storage`、`errorCode=corrupt`、`sqliteCode=11`、`systemCode=ERR_SQLITE_ERROR`。
- 日志对证 `<USERPROFILE>\.zcode\v2\logs\2026-09-18.log`：
  - `09:32:35` `[database-startup] terminal status=ready`（最后一次健康启动，durationMs=5487）
  - `09:44:40` `terminal status=failed errorCode=corrupt`（durationMs=223）
  - `09:45:59` `terminal status=failed errorCode=corrupt`（durationMs=263）
- 代码面：`preparing_host_storage` 是 ZCode 自身启动阶段枚举（`resources\glm\zcode.cjs`），非 Codex 侧问题。

## 受损面（2026-09-18 10:0x 实测）

| 库 | 路径 | 大小 | mtime | `PRAGMA quick_check` | 证据 |
| --- | --- | --- | --- | --- | --- |
| 任务索引 | `<USERPROFILE>\.zcode\v2\tasks-index.sqlite` | 7,864,320 B | 2026-09-18 09:44:40 | `database disk image is malformed` | U+FFFD 22,075 处（≈0.56% 字节被替换）；4096 页首字节有效页类型占比 5.0% |
| CLI 会话库 | `<USERPROFILE>\.zcode\cli\db\db.sqlite` | 822,472,704 B | 2026-09-18 09:44:27 | `database disk image is malformed` | U+FFFD 6,427,474 处（≈0.8%）；页首有效类型占比 6.4% |

- 两个文件的**前 4096 字节干净**（U+FFFD = 0），从第 4096 字节起被文本化重写——与「全树消毒」动作时间窗吻合。
- 健康对照：Codex 侧 SQLite 全绿（`~/.codex` 下 `goals_1 / logs_2 / memories_1 / queue_1 / state_5 / thread_history_1 / sqlite\codex-dev.db` 均 `ok`）。**本事故只伤 ZCode 数据面。**

## 根因

消毒脚本按文本处理文件：非法 UTF-8 字节（SQLite 的页头、单元指针数组、变长整数正是这类字节）被替换成 U+FFFD，1 字节变 3 字节，累计位移 44 KB（tasks-index）/ ≈12.8 MB（CLI 库），**页对齐整体错位**。

- 后果：SQLite 连 schema 都读不出；`.recover` 依赖页对齐，因此同样不可用。
- 反证：页类型普查中有效类型只占 5%~6%，页首大量出现中文 UTF-8 前导字节（`0xE5/0xE6/0xE7`）——典型错位指纹。

## 影响口径（**不只是配置数据**）

- **配置层未受损**：`config.json` / `setting.json` / `provider_config.json` / `credentials.json` / `bot-config.v3.json` / `bot-state.v3.json` / `agents-state.json` 全部 JSON 可解析、U+FFFD = 0 → **不需要重新登录、不需要重配模型与 provider**。
- **受损的是数据层**：
  - `tasks-index`：任务列表（标题/工作区路径/时间戳/服务器票据）、`automations` + `automation_runs`（自动化）、`off_peak_tasks`（错峰任务）与调度队列。
  - `cli/db/db.sqlite`（822 MB）：CLI 会话历史库。
- **未受损的旁证素材**（可用于部分恢复与对账）：`~/.zcode/cli/agents/sess_*/`（37 个会话目录 / 349 文件 / 173.8 MB，含 `metadata.json` 的标题、描述、工作区、prompt）；`~/.zcode/v2/checkpoints/`（210.8 MB）。

## 备份位置（已执行）

- `<备份根>\zcode-backup-20260918\01-dot-zcode\` —— 3.082 GB / 13,588 文件 / 失败 0（robocopy /E，exit=1=成功）
- `<备份根>\zcode-backup-20260918\02-Roaming-ZCode\` —— 711.97 MB / 18,406 文件 / 失败 0
- `<备份根>\zcode-backup-20260918\00-损坏库快照\` —— 两个受损库原件快照；哈希见同目录 `HASHES.txt`

## 修复选项（23:00 轮次择一执行）

- **A（推荐）抢救 → 重建**：先提取两个库中的可读文本/JSON 成归档，再把受损库移入快照目录、由 ZCode 重建空库，最后做真实启动验证。
- **B 只重建**：最快，不抢救文本。
- **C 法证级约束求解重建**：按 SQLite 页结构约束反推丢失字节，成功率不保证；对 822 MB 库不现实，对 7.8 MB 库可作研究性尝试。

## 执行命令（照抄可跑）

0）停机确认（必须无输出才能继续）

```powershell
Get-Process | Where-Object { $_.ProcessName -match 'ZCode' }
```

1）抢救文本（只读，输出 `<备份根>\zcode-db-rescue-output\`）

```powershell
$code = @'
import re, os
src=[r'<USERPROFILE>\.zcode\v2\tasks-index.sqlite', r'<USERPROFILE>\.zcode\cli\db\db.sqlite']
out=r'<备份根>\zcode-db-rescue-output'; os.makedirs(out, exist_ok=True)
for p in src:
    d=open(p,'rb').read()
    t=d.decode('utf-8','replace')
    runs=[m.group(0) for m in re.finditer(r'[\x20-\x7e\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]{20,}', t)]
    n=os.path.join(out, os.path.basename(p)+'.strings.txt')
    open(n,'w',encoding='utf-8').write('\n'.join(runs))
    print(n, len(runs))
'@
$code | python -
```

2）移库（先建目标目录；移动而非删除，可回滚）

```powershell
$move='<备份根>\zcode-backup-20260918\10-已移除的损坏库'; New-Item -ItemType Directory -Force -Path $move | Out-Null
Move-Item '<USERPROFILE>\.zcode\v2\tasks-index.sqlite' (Join-Path $move 'tasks-index.sqlite.corrupt-20260918') -Force
Move-Item '<USERPROFILE>\.zcode\cli\db\db.sqlite' (Join-Path $move 'cli-db.sqlite.corrupt-20260918') -Force
Remove-Item '<USERPROFILE>\.zcode\cli\db\db.sqlite-shm','<USERPROFILE>\.zcode\cli\db\db.sqlite-wal' -Force -ErrorAction SilentlyContinue
```

3）启动并验证（判据：出现 `status":"ready"`，且不再出现 `errorCode":"corrupt"`）

```powershell
Start-Process '<USERPROFILE>\AppData\Local\Programs\ZCode\ZCode.exe'
Start-Sleep -Seconds 45
Select-String -Path '<USERPROFILE>\.zcode\v2\logs\2026-09-18.log' -Pattern 'database-startup\] terminal' | Select-Object -Last 3
Test-Path '<USERPROFILE>\.zcode\v2\tasks-index.sqlite'
```

4）界面走查：任务列表可打开、可新建任务、设置页模型/provider 正常显示。

## 禁止清单（执行前必读）

- 不得再对 `*.sqlite / *.db / *-wal / *-shm / *.bin / *.png / *.zip / *.exe` 做任何「按文本读取-替换-重写」的消毒；消毒必须带**扩展名白名单 + 魔数校验**双保险。
- 重装 / 覆盖安装**对本次损坏无效**（安装程序不触碰 `~/.zcode` 用户数据目录），不要用重装"修复"。
- 移动/删除库文件前必须确认 ZCode 已完全退出，且快照与 `HASHES.txt` 在位。
- 任何写操作前先确认备份目录可写；本次快照一次不成功不得二次覆写（同版本重跑覆盖是历史事故形态）。

## 教训（回流 repo 教训区）

症状：二进制数据库被文本管线重写致整库不可读｜根因：全树消毒缺少二进制白名单与魔数校验｜预防：消毒前后双门禁——①白名单（仅文本扩展名）+ 魔数嗅探拒收二进制；②消毒后对每个命中文件做类型校验（SQLite `quick_check` / JSON parse / 图片头校验），把结果写进 GATE 的 `files` 与验证段。

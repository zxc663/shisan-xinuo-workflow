# MCP 工具面裁剪方案（2026-09-17 落档 · 状态：**待用户批准，配置零改动**）

> 证据源：ZCode 使用统计面板（累计 67.2 亿 token）+ 两会话「上下文容量」面板（MCP 工具占 73%/73.7%，13 万窗）+ `~/.zcode/cli/config.json` 只读实测（仅取键名与服务器名，未触密钥字段）。
> 结论一句话：**上下文预算的最大消耗方是 MCP 工具定义（≈73% 常驻），不是对话本身（仅 4-5%）；裁剪 MCP 是比提示词瘦身大一个数量级的杠杆。**

## 一、实测账目

| 占用方 | 面板占比 | 折算（13 万窗） | 可控性 |
|---|---|---|---|
| MCP 工具 schema | 73-73.7%（两时点不动=常驻） | ≈9.5 万 token | **可控（本方案对象）** |
| 系统工具（ZCode 内建） | 15.8-15.9% | ≈2 万 | 不可控（地板） |
| 消息（真正干活内容） | 4.4-5.2% | ≈6 千 | — |
| 技能 | 2.6-2.7% | ≈3.4 千 | 已瘦身（注入核心 ≤6K 字符） |
| 系统提示词 | 1.7% | ≈2 千 | 不可控 |

- config.json `mcp.servers` 实测 **11 个用户级服务器全量常驻**：browser360 / browser_tools / chrome-devtools / playwright / github_mcp / firecrawl / context7 / glm_vision / codex / reactbits / zcode-token-usage-statusbar。
- `enabledPlugins` 实测 3 个启用：android-emulator（约 23 工具）/ computer-use（约 30 工具）/ github 插件（skills 为主）。
- 本会话工具面实测约 116-129 个 schema ≈ **每工具摊 ~700-800 token**。
- 冗余四源：①浏览器自动化**四套并存**（browser360/browser_tools/chrome-devtools/playwright，缓存里另有第五套 browser-use 插件）②GitHub **双份**（github_mcp 约 44 工具=最大单一来源 + github 官方插件）③重型插件常驻（非对应任务轮次全白付）④低频服务器常驻（firecrawl/reactbits/codex）。

## 二、成本机制（为什么这值得做）

- 火山方舟/魔搭等第三方渠道基本无前缀缓存 → **每轮全量重发工具面 ≈11.5 万 token**（MCP 9.5 万+系统工具 2 万）；30 轮会话仅工具面就烧约 350 万输入 token。
- 13 万小窗模型：常驻吃掉 ~88% 后真正干活空间仅 ~2.6 万 → 压缩提前触发（实证：73.1% 时已「上下文已自动压缩」）→ 丢细节 → 重读 → 更多轮次 → 复利燃烧。
- 与使用统计吻合：09-12 快照 42.81 亿 → 09-16 面板 67.2 亿，**4 天 +24.4 亿（≈6 亿/天）**，峰值日 9.6 亿。

## 三、裁剪矩阵

| 档 | 条目 | 处置 | 理由 |
|---|---|---|---|
| A 常驻保留 | zcode-token-usage-statusbar（1）/ context7（2）/ glm_vision（6） | 保留常驻 | 轻量（合计 ≈9 工具）+高频 |
| B 按项目/按任务启用 | github_mcp（≈44）/ firecrawl（3）/ codex（2）/ reactbits | 移出常驻，用时临时加回或项目级启用 | 重型或低频；github_mcp 单源即 ≈3.5 万 token |
| C 浏览器收敛 | browser360 / browser_tools / chrome-devtools / playwright 四选一保留，其余禁用 | **用户决定留哪套**（按平时习惯；browser-use 插件可作为通用默认候选） | 同类能力最多四重复，最大单笔节省 |
| D 插件项目级 | android-emulator | 仅 Android 项目启用 | 非对应项目零收益 |
| D 插件·用户决定 | computer-use | 常驻保留（MCP 面 ≈+24%）或按需（截图显示电脑操作高频，**留用户拍板**） | 单插件 ≈30 工具 |

## 四、预期收益（两档）

- A-D 全量落地（computer-use 也按需）：常驻工具 ≈9 个，MCP 面 73% → **约 6-10%**；13 万窗有效空间 ~2.6 万 → **~9 万**（×3.5）。
- 保留 computer-use 常驻：MCP 面 → **约 25-30%**；有效空间 → ~6 万（×2.3）。
- 每轮输入成本（工具面）：≈11.5 万 → 2.5-4 万 token，**降幅 ≈65-78%**。

## 五、改法（批准后执行，预计 10 分钟）

1. 备份 `C:/Users/zxc66/.zcode/cli/config.json` → 同目录 `config.json.bak-<YYYYMMDD-HHmmss>`。
2. `mcp.servers` 移除 B/C 档条目（原文完整保留在备份；另出 `mcp-disabled-<ts>.json` 清单留档备查）。
3. `enabledPlugins`：android-emulator → false（computer-use 视拍板）。
4. **重启 ZCode**（注入配置=会话创建时快照，不重启不生效——v11 实证①）。
5. 新会话按 §六验收。

## 六、验收标准（面板实测，非自报）

1. 新会话上下文容量面板：MCP 工具 ≤10%（全量档）/ ≤30%（保留 computer-use 档）。
2. 工具 schema 数：≈120+ → ≈9（或 ≈39）。
3. 冒烟：token 状态条 MCP 工具（保留项）仍正常响应。
4. 按需路径一次：临时加回 github_mcp 后新会话 github 工具在场。
5. 回滚演练一次：从 .bak 恢复 → 新会话工具数复原 ≈120+。

## 七、回滚与边界

- 回滚 = 备份文件原样复制回去 + 重启 ZCode，秒级可逆。
- 边界（不做）：**hooks / provider / model 三段绝不触碰**（agent-log 状态段既有约束）；不动注入核心与 Skill 正文；不动模型选型；不删除任何服务器配置原文（全在备份）；本仓库默认不 push。
- 被否候选：①「换更大窗口模型」——每轮输入成本不降反升，治标不治本；②「只靠自动压缩」——压缩丢细节→重读的复利已实证；③「给第三方 MCP 服务器瘦身 schema」——工程量大、不可控，列远期。

## 附：顺带发现

图 3 会话（魔搭 ModelScope/DeepSeek-V4.1-Flash）为工作流**跨模型触达正样本**：复述、Context 状态行、Skill 回指加载全自发——建议记入 face G 对照样本（n 可 +1）。

## 执行回执（2026-09-17 00:35 批，计划模式获批后施工）

- **拍板**：AskUserQuestion 4/4 推荐项（浏览器四套全禁 / github_mcp 按需 / computer-use 常驻 / 我改 config）；其余 6 项按推荐默认随计划批准生效。
- **机制更正**：注入窗**非「固定前 5 server」**——同配置不同会话 `mcp.tools.registered`=234（15 server 全进）/65/52 三样本（日志实测）→ **动态预算**（疑随模型上下文窗口浮动）；browser 族 111 工具=预算大头结论不变。
- **前置核查**：zcode-configuration-guide 官方口径无 per-server `disabled` 字段 → 移除+sidecar 定案；workspace 级 `<repo>/.zcode/config.json → mcp.servers` 为按项目装回通道（自动连接）。
- **已执行（MCP 批）**：备份 `config.json.bak-20260917-003508` → 移除 7 server（browser360/browser_tools/chrome-devtools/playwright/github_mcp/firecrawl/reactbits）+ `android-emulator@zcode-plugins-official→false`；留档 `mcp-disabled-20260917.json`；**hooks/provider/model 三段与备份深比较零变动（脚本断言 PASS）**；重放脚本 `C:/Users/zxc66/tools/mcp-trim-apply-20260917.py`（防运行中应用回写覆盖，可重跑）。
- **已执行（状态条 asar 修复批，用户「也修」指令确认）**：pull `35ff516→ac328de`（behind 13 清零，worktree `injected v10`）→ 新回滚锚 `app.asar.zusage-rollback-20260917-003508`（307,867,553B）→ dry-run 过目 → 实装：重打包+结构自检 PASS（header ok/注入行符合预期/语法 exit=0）；**运行中原子替换被锁（WinError 5）**——补丁版在 `app.asar.zusage.tmp` 待 finalize：完全退出 ZCode 后监控窗自动完成，或手动 `python patch_install.py install --finalize`。装后 grep 注入行=0（如实标注：未完成，待重启兑现）。
- **验收（09-17 00:4x，用户重启后）**：①**MCP 裁剪机证通过**——config 幸存重启（保留 4 server + 插件 false），新会话 `mcp.tools.registered` **reg=45 / srvN=7** 与保留清单 1+2+1+2+30+3+6 分毫不差（对照裁剪前 234/15，**工具面 -81%**），browser 族/github_mcp/firecrawl/reactbits/android-emulator 全部不在场，computer-use 30 工具在场=验收②同时机证达成；②状态条 MCP 冒烟通过（token_usage 正常响应）；③github 按需闭环顺延至首次需要时；④日耗基线已取（09-17 当日 CLI 面 7.12M；官方面板 ≈6 亿/天待一周对比）。
- **唯一遗留 = asar finalize**：`ZUSAGE_NO_MONITOR=1` 抑制了本该在退出时自动 finalize 的监控窗（errpath 归执行侧），重启窗口期无人接手；补丁版在 `app.asar.zusage.tmp` 待替换。另发现 `patch_install.py install --finalize` **独立探测幻影定位到不存在的 D:\ZCode**（活体=C 盘，Get-Process 实证；上游探测 bug 候选，可反馈 xhwxt）→ 改用直接 Move 替换：**完全退出 ZCode（任务管理器 ZCode.exe=0，当前 17 个）**后 `Move-Item -Force "C:\Users\zxc66\AppData\Local\Programs\ZCode\resources\app.asar.zusage.tmp" "C:\Users\zxc66\AppData\Local\Programs\ZCode\resources\app.asar"`，重开即悬浮条 + /usage。回滚锚 `app.asar.zusage-rollback-20260917-003508` 不动。

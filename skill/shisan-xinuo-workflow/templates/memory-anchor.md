# 记忆层锚点模板 · shisan-xinuo-workflow（COPY & ADAPT）

> 用途：硬注入「记忆层」的待写入内容（模板，非运行时）。把下面代码块整段复制进目标平台的记忆文件
> （WorkBuddy `~/.workbuddy/MEMORY.md`、Trae `~/.trae-cn/memory/user_profile.md`、Codex `AGENTS.md` 顶部注记…），
> 按平台微调目标文件头注释即可。写入前须已获用户授权，并先备份目标文件为 `.bak-<修订时间戳>`。

```markdown
### 在场提示 · 工作流 Skill 现已在场（shisan-xinuo-workflow · vX.Y.Z 硬注入）
本 Agent 账户应用「十三希诺 Agent 工作流」硬注入：每会话开工先识别本在场提示 → 按三级跑道推进（L1 快速通道 / L2-S 短工作流 / L2-F 完整 11 步），命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- 判级：L3 必问先于动手；L1 直接做；其余 L2 记录推进。
- 模式：普通（关键决策必问）/ 目标（无人值守按计划，密钥与破坏性暂停）/ 安静（L1 只报结果）。
- 红线：密钥绝不落盘；破坏性操作先备份+确认；不假实现（未完成显式标注）。
- 自检彩蛋：输入 `zxc663` → 回复「注入方式（硬注入）+ 已应用轮数 + 源库 vX vs 副本 vY + Base directory 判据」。
- 前缀自检（每会话）：能确定安装目录名且无 `agent-` 前缀 → 一行提示（install-skill.ps1 可带前缀重装；不愿改则 state.md 记「保持无前缀」后静默）；目录名未知 → 不猜不阻塞。
- 项目承载（自动建，不等许可）：memory/ 规范五件套（state.md … task-log/，禁空占位）+ 项目级规则文件（AGENTS.md 等，templates/project-rules.md，先查既有→合并不覆盖）+ docs/project-info.md。
- 委托子代理：必须内联纪律包（子代理不继承注入副本、不保证自加载 Skill——2026-08-31 路测实证；独立工作区另建规范承载）。
- 完整规则：规则层文件（AGENTS.md / user_rules / CLAUDE.md）+ 技能 references/（rules.md 47 条 / 276 细则）。
- 更新协议：`python scripts/syncer.py`（记忆/规则/配置三层随版本同步）；验收以平台解析到的 Base directory 为准。
- 注入版本：vX.Y.Z ｜ 授权：本锚点由用户授权后注入，未获授权不写。
```

（替换 `vX.Y.Z` 为当前批次版本号；正式写入后本模板保持 `vX.Y.Z` 占位，便于反复复制。）
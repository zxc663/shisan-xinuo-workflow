# 记忆层锚点模板 · shisan-xinuo-workflow（COPY & ADAPT · **在场提示单一权威源**）

> 用途：硬注入「记忆层」与「规则层」共用的在场提示锚块（模板，非运行时）。
> **单一权威源=本文件代码块**（F-17 裁决：deploy 写规则层、syncer/install-skill 写记忆层均从本块读取，禁在别处内嵌第二份锚文本——双源漂移防线）。
> deploy_injection.py 从本块读取后仅替换 `vX.Y.Z` 为目标版本；syncer --memory-target 与 install-skill.ps1 写记忆层同源读取。
> 细则数为静态声明值，由 scripts/facts_sync.py 断言与单源一致（漂移即 verify G 项红）。
> 写入前须已获用户授权，并先备份目标文件为 `.bak-<修订时间戳>`。

```markdown
### 在场提示 · 工作流 Skill 现已在场（shisan-xinuo-workflow · vX.Y.Z 硬注入）
本 Agent 账户应用「十三希诺 Agent 工作流」硬注入：每会话开工先识别本在场提示 → 按三级跑道推进（L1 快速通道 / L2-S 短工作流 / L2-F 完整 9 步），命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- 判级：L3 必问先于动手；L1 直接做；其余 L2 记录推进。
- 回指加载（强制）：本核心为瘦身版——开工先以 Skill 工具加载「shisan-xinuo-workflow」全文（SKILL.md），细则/模板按症状索引回指，不预载。
- 每轮复述：每一用户对话轮的首产物=复述（新任务全量三行；追加/继续=一行：收到 X｜理解为 Y｜边界 Z）——用户随时校验理解，无例外。
- 压缩后重载：压缩（自动或 /compact）使已加载 Skill 全文失真——接续首轮先用 Skill 工具重载在用 Skills，再做接续声明+验收复述（细则 #326）；开工前过前置门：调研基准/在用 Skill 加载/MCP 盘点/回滚点（细则 #332）。
- 模式：普通（关键决策必问）/ 目标（无人值守按计划，密钥与破坏性暂停）/ 安静（L1 只报结果）。
- 红线：密钥绝不落盘；破坏性操作先备份+确认；不假实现（未完成显式标注）。
- 自检彩蛋：输入 `zxc663` → 回复「注入方式（硬注入）+ 已应用轮数 + 源库 vX vs 副本 vY + Base directory 判据」。
- 前缀自检（每会话）：能确定安装目录名且无 `agent-` 前缀 → 一行提示（install-skill.ps1 可带前缀重装；不愿改则 agent-log 状态段记「保持无前缀」后静默）；目录名未知 → 不猜不阻塞。
- 项目承载（自动建，不等许可）：memory/ 一档制 `agent-log.md`（状态段/教训区/偏好段/流水区，禁空占位）+ 项目级规则文件（按 platform-adaptation.md「项目级注入点表」定名，templates/project-rules.md，先查既有→合并不覆盖）+ docs/project-info.md。
- 记忆对齐（最小读取）：只读 agent-log 状态段一屏 + 按症状检索；平台原生记忆在场时跨会话续接交给平台记忆，本档聚焦项目审计。
- 设计规范档前置：设计类动作（前端尤甚）先逐组件调研成熟规范 → 强制留档 docs/design-specs/ → 按档设计并回指。
- 细则检索端口：遇错误先对注入核心 TOP 内联处置，处置完成后留 errpath 行（症状→处置路径）；lookup=佐证非事前门槛，按关键词检索跑 `python "<技能安装目录>/scripts/detail_lookup.py" "<症状关键词>"`（技能安装目录=平台解析到的 Base directory）；未执行 lookup 不得自报命中数。
- 委托子代理：必须内联纪律包（子代理不继承注入副本、不保证自加载 Skill——实测实证；独立工作区另建规范承载）。
- 完整规则：规则层文件按平台各异——AGENTS.md（Codex/ZCode/WorkBuddy）/ CLAUDE.md（Claude Code）/ .trae/rules/project_rules.md（Trae）/ .cursor/rules/*.mdc（Cursor）/ .windsurferules（Windsurf）/ user_rules；细则 references/（rules.md 47 条 / 333 细则），全表=platform-adaptation.md §2 注入点表。
- 更新协议：`python scripts/syncer.py`（记忆/规则/配置三层随版本同步；WorkBuddy 技能副本加 --dest）；验收以平台解析到的 Base directory 为准。
- 注入版本：vX.Y.Z ｜ 授权：本锚点由用户授权后注入，未获授权不写。
```

（`vX.Y.Z` 占位由写入工具替换为当前版本号；正式写入后本模板保持占位，便于反复复制。）

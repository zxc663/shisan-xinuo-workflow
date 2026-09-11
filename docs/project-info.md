# 项目信息 · 索引式入口（shisan-xinuo-workflow 开发库）

> **本文件是索引入口（六节导航），权威内容在对应源文件，绝不重复**（§2.5）。
> 更新：2026-09-12 ｜ 判级：L2-F v2.7.0 收口定稿批次 ｜ 签章：v2.7+ 重构施工计划已获用户全量批准+全部预授权（2026-09-12，批 0-5 分批自主推进；push/发行单独批准）。

## ① 架构
开发库 = Agent Skill 「shisan-xinuo-workflow」的唯一权威源库（中文单版 v2.7.0+）。
双层：**文档层**（SKILL.md 权威可执行全文 → references/ 按需 → templates/ 模板）＋**维护工具层**（scripts/：install-skill / syncer / verify-release，均为 .ps1/.py，无运行时）。

**模块依赖关系表**（A → B = A 依赖 B；任务涉跨模块改动先查本表再按 details #276 召回符号）：
| 模块 | 依赖（用到谁） | 被谁依赖 |
|---|---|---|
| skill/shisan-xinuo-workflow/ | —（自包含交付物） | scripts 校验/同步、README/项目信息/docs 描述与索引 |
| scripts/syncer.py | skill/（同步源） | 维护流程（版本升级/副本同步） |
| scripts/verify-release.ps1 | skill/（校验对象）、package.json（版本比对） | CI（.github/workflows）、发行流程 |
| scripts/install-skill.ps1 | skill/（安装对象）、templates/memory-anchor.md（记忆层） | 用户安装流程 |
| README.md / 项目信息.md / docs/ | skill/（描述/索引对象） | 用户与维护会话（导航入口） |

一行数据流：skill/shisan-xinuo-workflow/（源）→ scripts/syncer.py（三路合并同步）→ 各平台技能副本（~/.agents/skills / ~/.workbuddy/skills）→ 注入副本（AGENTS.md ×3 + MEMORY.md）→ 每会话在场。

## ② 目标规划（当前阶段）
- 已完成：**v2.0.6 全渠道发行（2026-08-31）** + **v2.1.0（上下文主动管理补全）/ v2.1.1（口径修正 16→17 类）/ v2.2.0（开工序列六步+承载平台适配+本体净化+决策时效）全渠道发行（2026-09-02 ×3：GitHub Release / npm / Gitee / ClawHub 1.0.8/1.0.9/1.0.10 / About 双端）**。
- 当前：**v2.6.0 批次（2026-09-09 本地完成，发行待批）**——流程简化（开工六步→四步/L2-F 11→9 步/更新序 6→4）+ 设计规范档前置 #284 + 平台原生记忆分工 #285 + 跨项目经验回流 #286-293 + 触达渠道修复 #294（detail_lookup 一键检索端口 + 部署工具化）+ 机评路测三场（修复效力/机制广度）。上一：**v2.5.0 批次（2026-09-08，已发行）**——留档一档制（memory/agent-log.md 四区取代五件套，旧项目沿用兼容；四 Skill 全修含蒸馏版 1.1.0/1.2.0×2）+ 设计前先调研成熟设计（并入设计铁律/复用铁律）+ agent-log-template 新模板。
- 上一：**v2.4.0 批次（2026-09-08 本地完成，内容并入 v2.5.0 发行）**——三平台全量取证（ZCode 98/Codex 83/WorkBuddy 60 会话，产物 memory/forensics-2026-09-08/）驱动白名单修补：场景判定反转（判定不清默认按持续）+ 细则三层结构（T1 注入核心/T2 症状检索/T3 领域查询）+ 防棘轮（details 头+SKILL §0）+ 消重（§3 步骤6↔§2.0 步骤4 收敛）+ 紧凑档窗口下限 ≥16K；新发现 N1-N8 只记录待审。
- 上一：**v2.3.0 批次（已全渠道发行 2026-09-03）**——场景化（单发文档豁免 details #283）+ 写作重构（SKILL §10 总纲 + AGENTS.md 维护纪律 + workflows 日期裁决）+ Steer 纠偏续跑（#280）+ Parallel 依赖协议（#281）+ 回指理解双强制（project-rules 回指段 + §0 每消息严谨分析，details #282）+ 审计修复 1-7（症状索引表 283 全覆盖 + verify F 项门禁 + GATE errpath）。
- 上一：**v2.7+ 重构六批次（2026-09-12 本地完成，未发行）**——施工权威 docs/design-specs/v270-redesign.md（全预授权分批）：批 0 基线冻结（tag pre-v270-redesign）+批 1 条款六销项（GATE 9 字段/errpath 事后化/lookup 修复模板/状态行/微轮次豁免/记忆路由）+批 2 注入瘦身（核心 11,560→5,203 字符+在场提示 ×1 单源）+批 3 hooks 纪律包（SessionStart+PostToolUseFailure 机证三通道）+批 4 数据工具面（判例审入 #296-#305+使用率盘点 #180 归档+口径活跃 303 条+syncer 旧锚清扫+Trae 旧锚已清）+批 5 收口定稿（版本 bump 全链+About 303+verify/dist/五副本+真会话回归 S0/S7+发行清单备好）；路测 v5 头条=无头面注入 0/13+S3 假 errpath（EVIDENCE §二十二）。
- 待办：①GitHub PAT 轮换（v2.0.3 起遗留最高优先）②ClawHub 1.0.13 审核复查 + skills.sh 遥测收录核查 + Gitee 侧补发 v2.5.0/v2.6.0（Release/tag/About，待令牌轮换）③**v2.7.0 发行面待批**（push/GitHub Release/npm/Gitee/ClawHub/About——命令清单=RELEASE-CHECKLIST.md，批准后执行）④后续观察（WorkBuddy H0 用户侧 zxc663/面 B 双击 #295 转正候选/hooks 脚本迁出 roadtest 目录候选）。
- 路线：v2.0.5 后进入稳定细则小更新（不做破坏性大改，但保留意外情况声明）。

## ③ 模块表（真实状态 · 含关键词锚定列，details #275）
| 模块 | 真实状态 | 关键描述 | 关键词锚定 |
|---|---|---|---|
| skill/shisan-xinuo-workflow/ | 已实现（v2.7.0） | 唯一主交付物：SKILL.md（§0-§13）+ references（injection-core/details 303 条 17 类/rules 47 条/workflows/security/never-list/skill-usage/platform-adaptation/new-project-bootstrap/local-model-glossary）+ templates（含 hooks/agents） | SKILL.md、injection-core、details、rules、references、glossary、templates、hooks、agents |
| scripts/ | 已实现 | install-skill.ps1（agent- 前缀自适配）/ syncer.py（三路合并）/ verify-release.ps1（发布门禁） | install-skill、syncer、verify-release、门禁、三路合并 |
| docs/ | 已实现 | project-info.md（本文件）/ reference-sources.md（参考来源） | project-info、reference-sources、调研导航 |
| 项目信息.md | 已实现 | 决策与发布史（权威，46KB）——本文件不重复其内容 | 决策史、发布记录、决策 #、About |
| memory/ | 已实现（gitignore） | 本仓库会话记忆：一档制 `agent-log.md` 四区（状态段/教训区/偏好段/流水区；旧五件套历史原件在 legacy-pre-v250/ 只读） | agent-log、记忆、归档 |
| dist/ | 已实现（gitignore） | 发行 zip（最新 v2.7.0 本地批次已打包；v2.6.0/v2.5.0 亦在位；v2.7.0 未发行，发行后随 Release 附带） | 发行 zip、发布包、dist |
| versions/personal-zh/ | 私有（gitignore） | 个人工作台版（v1.19 时代私有权威，v2.0 起不参与） | 个人版、personal-playbook |
| RELEASE-CHECKLIST.md | 已实现 | 发行清单（v2.7.0 待执行清单+发行命令已备；v2.6.0 已发行、Gitee 侧待补） | 发行台账、渠道回执、门禁 |
| .trae/ | 本地（gitignore） | Trae 侧 documents 历史 + rules/project_rules.md（项目级注入） | trae 规则、project_rules、documents |

## ④ 调研导航（改什么 → 查哪）
- 改主流程/判级 → SKILL §2/§5.2（**三级同步链：§5.2 → injection-core → 平台注入副本，改完全链重部署**）。
- 改细则 → references/details.md（编号须连续、全仓口径 grep：条数/类数/版本号；引用规范禁裸 #N）。
- 改注入/触达 → platform-adaptation.md（注入点表 §2.1/§2.2）+ memory-anchor.md。
- 发行 → scripts/README.md（装机/校验）+ RELEASE-CHECKLIST.md。
- 决策追溯 → 项目信息.md（§三 决策 1-42）+ memory/task-log/。

## ⑤ 参考资源
| 名称 | 用途 | 路径 |
|---|---|---|
| 项目信息.md | 决策与发布史（权威） | 仓库根 |
| memory/ | 会话记忆（含本文件同目录） | memory/ |
| scripts/README.md | 维护工具用法 | scripts/ |
| EVIDENCE.md | 行为对照路测与诊断实证 | 仓库根 |
| RELEASE-CHECKLIST.md | 发行台账 | 仓库根 |
| docs/reference-sources.md | 参考项目与来源 | docs/ |

## ⑥ 复述签章
本批次（v2.1.0 上下文主动管理补全）：用户提供四大客户端机制清单（Aider/1bcoder/Atrium/Context Governor）→ AskUserQuestion 三决策（方向=通用补全+紧凑档 / 版本=v2.1.0 / 术语表=references 随 Skill 分发）→ 落地：injection-core 保留清单+折叠协议+紧凑档条款、SKILL.md（§2.5 锚词列+依赖表/§9 术语表/§12 P8）、details #272-276、local-model-glossary.md、本模块表锚词列 + 架构依赖关系表示范；**补强批次**（用户拍板 2+3）：模块依赖关系表 + 按需符号召回协议（#276）。复述经用户确认（计划 ExitPlanMode 批准）。历史批次（v2.0.6 承载建立）：用户指令「主动建立包括其注入文件」→ 建立 memory/experience-mustread.md（补五件套）+ docs/project-info.md（索引）+ 根 AGENTS.md（项目级注入）+ .trae/rules/project_rules.md；memory/.trae 按 gitignore 本地承载，AGENTS.md/docs 入库。复述经用户确认（用户即指令方）。

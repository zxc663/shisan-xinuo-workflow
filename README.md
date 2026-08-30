# Shisan Xinuo Agent Workflow · 十三希诺 Agent 工作流

> **渐进式工程治理 Skill——不是把整本手册砸进上下文，而是像神经系统：只在任务到达某一步骤时，注入那一步所需的少量规则。**
> A progressive, on-demand engineering-governance Skill: injects only the few rules a step needs, when that step arrives.

![version](https://img.shields.io/badge/version-1.16.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![platforms](https://img.shields.io/badge/platforms-Codex%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20Trae%20%7C%20Windsurf-orange)

> **开源分发入口 · Distribution mirrors**（MIT）
> - GitHub 主线 · https://github.com/zxc663/shisan-xinuo-workflow
> - Gitee 镜像 · https://gitee.com/zxc663/shisan-xinuo-workflow
> - npm 包 · `@zxc663/shisan-xinuo-workflow`（GitHub Packages 源）
> - skills.sh · https://skills.sh/zxc663/shisan-xinuo-workflow/shisan-xinuo-workflow
> - ClawHub · 搜索 `shisan-xinuo-workflow` ｜ 快速体验 · `npx skills add zxc663/shisan-xinuo-workflow`

---

## ⚠️ 安装后必读 · 命名与首次适配（Agent 前缀原因）

1. **拉取后立即重命名为 `agent-shisan-xinuo-workflow`**（在 skill 目录名 / 注册名上加 `agent-` 前缀）。原因：按需注入的 Agent **不会自动执行本 skill**，用户需在「使用技能」列表中手动选择——列表按**字母排序**时，`agent-` 开头的名字天然排在最前，一眼可见。
2. **若首次拉取后模型没有自动做平台适配**（未写注入点）：**手动向模型再完整输出一遍本 skill 的名字**（`shisan-xinuo-workflow`）以触发加载；然后按 SKILL.md §3 执行「平台检测+注入」（备份 → 合并写入 injection-core 核心 ≤55 行 → 重读校验三级一致）。
3. **自检命令（彩蛋）**：向模型输入 `zxc663` —— 它会回复「十三希诺工作流已应用，注入方式是：［按需 / 硬注入］，已经应用多少轮会话/对话（按任务记录/文档数快速统计）」。这是**纯自检指令**，不触发任何业务操作。

---

## 一句话定位（v1.16 纠正版 · 真实口径）

> **一个「执行手册」而非「原则书」的工程治理元 Skill**：把「大模块专属的 11 步主流程 + 小模块短工作流（L2-S）＋ L1/L2/L3 判级路由 + 必问协议（带推荐理由）+ GATE 可复跑验证块 + 五段式细则（触发/步骤/模子/自检/边界）＋ 经验强制预读 + 上下文主动管理」打包成跨平台可审计的治理层；每条规则都能被**照着做**，不靠领会。
>
> **诚实口径数据（2026-08-30 实证，见 `EVIDENCE.md` 与 2026-08-30 审计记录）**：
> - 细则层（details.md 233→238 条/13 类）**此前工程消费命中=0**——v1.13 起以「错误处理必经句 + 命中取证行 + 预读清单」修复，本会话（sess_c0f4df2b）转为**有命中**（#228 跨包 dist×3、#229 常驻旧 dist×2、#233 对接真相×1）。
> - 成本实证（本 Agent 平台 `model_usage` 全量）：**累计 input tokens = 947,218,098（9.47 亿）**；output 2,188,313；reasoning 249,823。**这就是「好」与「坏」的真账**：
>   - **好**：19 会话 *context_exceeded=0 / cancelled_by_user=0 / retry_count=0*；`finish_reason` 以 tool-calls 为主（2865/3002）；13+ 次全量 ci 门禁与 13 个规范提交；AskUserQuestion 19 次（必问纪律真实发生）；细则由 0 命中转有命中。
>   - **坏**：**单会话 input 峰值 3.32 亿**（本会话，803 次请求）——3 个长会话（c0f4df2b / 66effb58 / 2feda4d9）合计占全平台 input 的 **81%（7.66 亿）**；上下文无压缩直冲 **652K 输入**（40-60% 规则未生效，v1.13 §12 P3 起以「上下文盘点+阈值提醒」治理）；6 次 plan 拒绝与 6 次「继续」伴随重复重召，是长会话成本的主要推手。
> - **定位纠偏记录**：v1.10 曾言「细则命中率有数据可查」——可查的数据是 **0**（措辞已修正）；「渐进式披露 1:297 结构完全未消费」由 v1.13/v1.16 的触达与执行化改写回应。
>
> **价值**：治理一致性、可审计性、防假实现、注意力经济（state 一屏 / 同会话禁重载 / 按需加载 / 上下文卫生）。**代价**：依赖平台注入与 Agent 自律，无运行时强制——这是它「规则能否改变行为」的**未验证假设**（T-027 式对照实验列下一轮，同 `EVIDENCE.md` §五 的诚实声明）。

---

## 目录 · Contents

1. **安装/重命名/首次适配/自检** —— 见上文「⚠️ 安装后必读」。
2. **核心文件**（`skill/shisan-xinuo-workflow/`）：`SKILL.md`（执行手册：§0 元规则 / §2 三跑道 / §4 必问协议 / §5 判级分流 / §7 门禁 / §9 引用表 / §10 记忆纪律 / §11 状态面 / **§12 速查表**）｜`references/injection-core.md`（硬注入核心，随平台注入）｜`workflows.md`（判定表/质量门禁/调研矩阵/日志对接）｜`details.md`（**238 条踩坑细则 · 13 类 · 症状索引**）｜`rules.md`（47 条纪律）｜`security.md`｜`never-list.md`｜`skill-usage.md`｜`new-project-bootstrap.md`（项目信息文档六节）。
3. **模板**（`templates/`）：plan / acceptance-criteria / task-record（含 **GATE 字段**）/ retrospective / rollback-point / prompt-budget / workspace-memory / hooks / 审查子代理。
4. **发布与验证**：`verify`（文档与体系一致性 17 项 + 行为 3 铁律 + 机械 8）——**注意：绿≠行为变好，只=体系与自身一致**（含 `EVIDENCE.md` §七 零命中实证；有效性实验列下一轮）。
5. **历史版本**：v1.9.1→v1.16.0（变更记录见 `docs/` 与 Git log；v1.16 为执行化改写版）。

---

## 常见问题 · FAQ

- **Q: 为什么有 agent- 前缀？** A: 让按需注入的 Agent 在技能列表中靠前（字母序），用户可快速找到并手动应用。
- **Q: `zxc663` 会做什么？** A: 仅彩蛋自检回复（注入方式 + 已应用会话数）；不触发任何行为/网络/文件操作。
- **Q: 细则这么多，为什么命中率曾为 0？** A: 细则层是「可选诊断」而非「必经站」——v1.13 起报错必经句 + 预读 + 取证行，命中由 0 转有（数字见上「定位」节）。

---

*本 README 作为「喂网页 AI 的引用源」入口：把上游 URL 连同本文件定位文本粘贴给网页 AI 即可引导其读取真实、当前信息（详见 `docs/reference-sources.md`）。*

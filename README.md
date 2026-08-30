# Shisan Xinuo Agent Workflow · 十三希诺 Agent 工作流

> **渐进式工程治理 Skill——不是把整本手册砸进上下文，而是像神经系统：只在任务到达某一步骤时，注入那一步所需的少量规则。**
> A progressive, on-demand engineering-governance Skill: injects only the few rules a step needs, when that step arrives.

![version](https://img.shields.io/badge/version-1.19.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![platforms](https://img.shields.io/badge/platforms-Codex%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20Trae%20%7C%20Windsurf-orange)

> **开源分发入口 · Distribution mirrors**（跨平台工程治理元 Skill，MIT）
>
> - GitHub 主线 · https://github.com/zxc663/shisan-xinuo-workflow
> - Gitee 国内直连镜像 · https://gitee.com/zxc663/shisan-xinuo-workflow
> - npm 包 · `@zxc663/shisan-xinuo-workflow`（GitHub Packages 源 `npm.pkg.github.com`）
> - skills.sh 收录 · https://skills.sh/zxc663/shisan-xinuo-workflow/shisan-xinuo-workflow
> - ClawHub · 搜索 `shisan-xinuo-workflow` ｜ 在线快速体验 · `npx skills add zxc663/shisan-xinuo-workflow`
>
> 一份仓库，多平台分发；任何入口均可读到本 README 与三语增补版（英文主交付物 / 中文 / 中英双语）。**语言声明：本 README 中文优先（展示门面）；英文见文首定位段与 `versions/universal-bilingual` 双语版。**

---

## 一句话定位 · One-line positioning

一个**「让规则被消费」的执行手册型工程治理元 Skill**：把「大模块专属的完整 11 步流程 + 小模块短工作流（L2-S）+ L1/L2/L3 判级路由 + 携带推荐理由的必问 + GATE 可复跑验证 + 五段式细则（触发/步骤/模子/自检/边界）＋ 经验强制预读 ＋ 上下文主动管理」打包成跨平台（Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI）可审计的治理层。**设计意图不是「写更多规则」，而是给规则装触达端口**（错误必经句 / 预读 TOP / 命中取证 / 三路合并），并用可复跑工件（GATE 块 / syncer.py）让「做过 ≠ 说过」——每条规则都能被照着做，不靠领会。

**真实口径（2026-08-30 实证）**：细则层（238 条 / 13 类）**工程消费命中此前 = 0**（v1.13 全平台审计）；v1.13-1.16 以「错误必经句 + 预读 TOP + 命中取证行」修复，已转**有命中**（#228×3 / #229×2 / #233×1）。成本实证：ZCode 平台累计 **input tokens 947,218,098（9.47 亿）**——**好的**：19 会话零 context_exceeded、零 retry；**坏的**：3 个长会话占全平台 input 81%（7.66 亿）、单会话峰值 3.32 亿 input / 单次 652K、无压缩；6 次计划拒绝 + 6 次「继续」是主要重复成本推手。仍有一个诚实声明：**规则能否改变 AI 行为——未验证假设**（T-027 式对照实验列下一轮；verify 绿 = 体系与自身一致，非行为变好）。

*(EN) A "rules-must-be-consumed", execution-manual governance meta-skill. Not more rules — touchpoints: error-time entry point, must-read top, hit evidence-line, three-way self-update merge; verifiable artifacts (GATE / syncer.py) make "done" ≠ "claimed". Real numbers: detail-layer engineering hits were 0 before v1.13 (now converts to hits); platform cumulative input 947M tokens (3 long sessions = 81%); assumption that rules change AI behavior is still unverified.*

---

## 目录 · Contents

[为什么用它](#为什么用它--why-this) · [它为谁解决什么](#它为谁解决什么--who-its-for) · [工作原理](#工作原理渐进式--状态机--how-it-works) · [功能全景](#功能全景--feature-map) · [差异化优势](#差异化优势--differentiation) · [架构真相（诚实）](#架构真相诚实--architecture-truths) · [快速体验](#快速体验--quick-start) · [安装](#安装--install) · [仓库结构](#仓库结构--repository-layout) · [版本差异（三语）](#版本差异三语--editions) · [参考项目](#参考项目--reference-projects) · [局限与代价](#局限与代价--limitations) · [常见问题](#常见问题--faq) · [来源与依据](#来源与依据--sources) · [版本历史](#版本历史--changelog) · [贡献者与许可](#贡献者与许可--contributors--license)

---

## 为什么用它 · Why this

- **把「AI 直觉」变成「工程纪律」**：L1/L2/L3 风险分级、关键必问（带推荐理由）、回滚点、GATE 验证块、五查留档——不再靠 Agent 自觉碰运气。
- **省 token 不丢纪律**：L2-S 短工作流（小模块默认）+ 调研矩阵（S1-S3 × 规模）+ 上下文卫生（两步式归档 / 信号化盘点 / 会话级账本）——小任务不烧完整流程，大任务不破底线。
- **规则被消费而非被登记**：报错必经 details 症状类、开工必读预读 TOP、会话末取证命中（0 照报 0）、自更新三路合并——这是 v1.13 后区别于「规则堆」的核心差异。
- **跨平台行为一致**：第 0 步自动适配注入；自检彩蛋 `zxc663` 一次确认「注入方式 + 已应用轮数 + 源库 vs 副本版本」。

*(EN) Turns AI instinct into auditable discipline; saves tokens via the short-lane + research matrix + context hygiene; rules get consumed via mandatory touchpoints; consistent cross-platform via Step-0 injection.*

## 它为谁解决什么 · Who it's for

- 重度 AI 编码用户（Cursor / Claude Code / Trae / Codex 深度用户）：希望 Agent 跨项目、跨平台行为一致、可审计，尤其痛恨「假完成 / 伪造测试 / 虚报数据」。
- 按风险放权的人：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。
- 想要无人值守目标模式的人：写计划、设预算、按文件边界拆分、超预算自动停。
- 想省 token 又不丢纪律的人：渐进式加载 + L2-S 快速通道。
- 开源治理设计研究者：了解「渐进式 Skill」如何把静态约束变成动态治理。
- 刚入门、有一定了解、不想踩坑的用户：细则层即「踩坑日志 + 预读 TOP + 报错必经」——新人按图索骥少走弯路。

## 工作原理（渐进式 / 状态机）· How it works

```
平台硬加载（第 0 步：检测平台 → 定位真实注入点 → 按需（精简） / 强制（injection-core 核心全文））
        │
        ▼
任务三重判级（先答三问：≥3 包跨层？涉契约/架构/迁移/发布/安全？用户点名严格？）
  ├─ L1 常规 → 一句话复述 → 最小修改 → 最小验证 → 汇报
  ├─ L2-S（默认·小模块）→ 对接真相清单 → 复述+3 条验收 → 最小修改 → 最小验证 → GATE 行
  └─ L2-F（≥2 命中）/ L3 → 完整 11 步（每步出口产物门禁；步骤 8 产品视角五问强制）
        │
        ▼
必问协议（方向/边界/冲突/密钥/破坏性——先问后写；每个问题必带推荐选项+核心理由+失败后果；
        提问工具超时空答 → 能取消则取消，否则按项目实况出最贴合方案并标注「待确认」——空答绝不当批准）
        │
        ▼
执行与验证 → GATE 块（可复跑 cmd+exit+files+lessons+exempt）→ 交付五查 → 复述增强
（RE：关键决定即时「决定X｜依据｜影响」；块尾总复述仅提炼要点）→ 状态面（证据制，0 照报 0）
        │
        ▼
规则（+ 编号纪律，地基）+ 落地细则（238 条/13 类，症状索引）+ 冲突仲裁序
        │
        ▼
自更新（syncer.py 三路合并：体检→备份→迁移 user-notes/ →覆盖→双落盘；user-notes/memory/.bak 永不碰）
```

渐进式三层：入口精简（只预载 name+description + injection-core 核心）→ 按步加载（references 按需 / details 按症状类）→ 动态路由（判级前置走 L1/L2-S/L2-F）。

## 功能全景 · Feature map

| 能力 | 说明 | 入口 |
|---|---|---|
| 第 0 步平台检测与硬加载 | 检测平台 → 定位真实注入点 → 按需(精简) / 强制(injection-core 全文)，备份后合并绝不覆盖 | SKILL §3 · injection-core.md · platform-adaptation.md |
| **三级跑道（v1.16+）** | L1 快速通道 / **L2-S 短工作流**（默认小模块）/ L2-F 完整 11 步（大模块专属）——防流程空转与 token 浪费 | SKILL §2.2-2.3 · workflows §0.6 |
| **对接真相清单（强制）** | 跨包/新端点/新依赖先产「模块\|API\|对接方式\|证据来源」表，禁凭命名直觉 | SKILL §2.5 · details #233 |
| 必问协议 | 问题必带推荐+理由+后果；超时空答→调研+待确认标注 | SKILL §4 |
| **GATE 完成块** | 任务块一行可复跑验证（cmd+exit+files+lessons+exempt）；验收权在用户 | SKILL §7 · 模板 task-record |
| **复述增强 RE** | 关键决定即时子复述（依据+影响）；块尾总复述仅提炼要点 | SKILL §4.1 · §12 RE |
| 交付五查 | 遗漏/边界/临时代码/无关改动/**已接日志模块** | SKILL §7 |
| **会话状态面** | 结束输出：版本/细则命中取证行/**上下文账本（增量/最大单次/占比）**/版本一致性/未验证待办（给用户复核，非达标声明） | SKILL §11 |
| **经验强制预读** | experience-mustread TOP≤10（先于症状检索；≥3 次或高返工晋升） | memory/experience-mustread.md · workflows |
| **上下文主动管理（v1.19 四项）** | **两步式**（读→提炼→全文落盘→只留指针+摘要）；盘点按**信号**触发；**会话级账本**；**重置点**（5 块回引或成本 2× → 建议新会话） | SKILL §12 P3 · details #235 |
| 双模式（普通/目标/安静） | 关键必问 vs 无人值守（计划/预算/文件边界/超预算停）；安静 L1 只报结果 | SKILL §5 |
| 冲突仲裁序 + 经验回流 | 五级仲裁取最优；踩坑双击晋升细则 | SKILL §4 · §10 |
| **项目信息文档** | 新项目无文档→建六节导航（架构/目标/模块真实状态/调研导航/参考资源/复述签章） | SKILL §2.4 · new-project-bootstrap.md |
| **日志对接** | 有日志模块的项目：设计期对接行 + catch 三件套 + 五查含日志 | SKILL §7 · details #238 |
| **skill 自更新** | syncer.py 三路合并（用户规则目录永不碰）；彩蛋+状态面版本一致检查 | scripts/syncer.py · SKILL §3.1 |
| 配套模板/钩子/子代理 | 规划/验收/任务记录/复盘/回滚点/预算/钩子/审查子代理 | templates/ |
| **彩蛋自检 zxc663** | 回复「注入方式 + 已应用轮数 + 源库 vs 副本版本」——纯自检零操作 | SKILL §12 ZE |

## 差异化优势 · Differentiation

| 对比对象 | 本 Skill |
|---|---|
| 手写 AGENTS.md / CLAUDE.md | 渐进式披露 + 完整引用体系 + 跨平台适配，不止一页规则且不拖累会话 |
| 平台内置规则 | 平台无关，第 0 步自动适配 |
| 通用系统提示词 | 可操作、可验证、清单驱动：分级表/门禁/扫描清单 |
| 静态规则包 / 单文件提示词 | 渐进式 + 判级路由 + **三级跑道**，不是一次全量注入 |
| 其他工作流类 Skill | 多数只给「规则/流程」；本 Skill 多出**触达端口层**（报错必经/预读/取证/合并）与**执行化改写**（五段式、纸面盲测、禁用孤立副词）——v1.13 起「被消费」是头条差异化 |
| 同类治理 Skill | 全家桶完整度第一：规则 + 门禁流程 + 落地细则 + 跨平台注入 + 双视角 + 记忆/重载 + 模板/预算/钩子/子代理/永不清单 + 自更新合并 + 真实数据门面（含**可核算的上下文账本**） |

## 架构真相（诚实） · Architecture truths

> 快速判断它到底是什么、做不到什么。全无脚本（除自更新/校验两个发布工具）/ 无运行时 / 无网络调用——它是一份规范，加两个可复跑工件。

- 本质是「强提示词注入」：无强制，靠注入方式（用户/平台）+ Agent 自觉。
- 记忆靠「外部化文件」：Agent 无法感知压缩——显式重载顺序 + 关键节点自检兜底。
- 细则层绑技术栈：details 是踩坑日志不是教程；机制层与框架无关。
- **未验证假设**：规则能否改变 AI 行为——T-027 式对照实验列下一轮；verify 绿=体系与自身一致，非行为变好。
- **曾 0 命中**（v1.13 实证）：细则层工程消费=0——已以触达端口修复为有命中；仍如实标注「预防性，有效性需实测」。
- 不提供「硬门禁」：依赖平台（hooks/CI/沙箱）；缺口用兜底。
- 定位是「治理层」：不替代领域知识/项目文档；冲突时项目文档优先。
- **诚实可核算**：成本真账（9.47 亿/81%/会话级账本）对外公开，好与坏都摆——门面的一部分，不是免责声明。

## 快速体验 · Quick start

1. **安装**：`npx skills add zxc663/shisan-xinuo-workflow --skill agent-shisan-xinuo-workflow` → 立即**重命名为 `agent-shisan-xinuo-workflow`**（agent- 前缀=按字母序在技能列表最前——按需注入的 Agent 不会自动执行，用户靠字母序发现）。旧平台可解压 `dist/shisan-xinuo-workflow-v1.19.0.zip`。
2. **加载**：新开会话。Skill 自动执行第 0 步检测与注入；**若模型未自动适配，手动再输出一遍本 skill 名字**触发 → 按 §3 备份→合并→校验。
3. **感受它**：给一个小任务——先复述理解 + 3-5 条验收；给风险任务（「把这个目录删了」）——必须先问再动手（L3）。
4. **目标模式**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`——观察写计划/预算/文件边界/超预算停。
5. **底线自检**：输入 `zxc663`——应回复「十三希诺工作流已应用，注入方式是：［按需 / 硬注入］，已经应用 N 轮会话/对话｜源库 vX vs 副本 vY」。

## 安装 · Install

| 平台 | 位置 |
|---|---|
| skills.sh | `npx skills add zxc663/shisan-xinuo-workflow --skill agent-shisan-xinuo-workflow`（英文主交付物；中文 `-zh` / 双语 `-bilingual`；**命名均加 agent- 前缀**） |
| Claude Code | `~/.claude/skills/agent-shisan-xinuo-workflow/` |
| Codex / 通用 | 克隆本仓，技能发现指向 `skill/shisan-xinuo-workflow`；或解压 `dist/` zip |
| Trae / Cursor 等 | 按平台技能目录约定放置；Trae 需在应用设置启用项目规则 |

**更新与自维护**：上游更新后跑 `python scripts/syncer.py`（体检→备份→迁移→覆盖→双落盘）；**你的本地规则写 `user-notes/`，永不随上游覆盖**；手动改副本只许写在 user-notes/。发布前置校验：`powershell -File scripts/verify-release.ps1`（增补制一致/hooks/版本+package/泄漏全绿才可发布）。

## 仓库结构 · Repository layout

```
shisan-xinuo-workflow/              ← 仓库根
├── README.md / CHANGELOG.md / RELEASE-CHECKLIST.md / EVIDENCE.md / LICENSE
├── package.json（v1.19.0）· docs/reference-sources.md
├── dist/                           ← 发布 zip（v1.19.0 · 271KB/72 条目，gitignore 产物）
├── scripts/syncer.py               ← 自更新三路合并（体检/备份/迁移/覆盖/双落盘）
├── scripts/verify-release.ps1      ← 发布校验（增补制一致/hooks/版本+package/泄漏）
├── skill/shisan-xinuo-workflow/    ← 主交付物（英文执行化全文 v1.19）
│   ├── SKILL.md（§0 元规则 · §2 三级跑道 · §4 必问+RE · §5 判级 · §7 门禁 · §9 引用表
│   │   · §10 记录纪律 · §11 状态面（含上下文账本）· §12 速查表 20+ 行）
│   ├── templates/（规划/验收/任务记录(GATE)/复盘/回滚/预算/钩子/子代理）
│   └── references/（injection-core · workflows · details 238条 · rules 47条 ·
│       security · never-list · skill-usage · new-project-bootstrap）
└── versions/（universal-zh · universal-bilingual=增补制同步；personal-zh=私有工作台版不进公开仓）
```

## 版本差异（三语） · Editions

| 版本 | 路径 | 语言 |
|---|---|---|
| 英文（主交付物） | `skill/shisan-xinuo-workflow/` | 英文（标题保留「十三希诺」） |
| 中文 | `versions/universal-zh/` | 中文 |
| 双语 | `versions/universal-bilingual/` | 段落级中英对照 |
| 工作台版（私有） | 独立私有仓 | 中英混合 + 内嵌个人经验手册 |

> **同步口径（诚实）**：v1.16 起执行化全文以英文主交付物为权威；三语（zh/bilingual）以**增补制**同步（v1.12-1.19 增补节 + details #228-238），并按 `verify-release` 校验版本/标记一致——不伪装全量同文。

## 参考项目 · Reference projects

> 机制/结构借鉴，非复制代码。同类独立演进，本 Skill 为后发者。

- **Agent Skills 规范**（agentskills.io/specification）：SKILL.md 结构、渐进式披露、name+description 激活 — 机制根基。
- **agent-playbook-template**（prompt-budget / critic·risk-reviewer 子代理）、**AI-AGENT-SKILLS**（会话钩子）、**anchor**（NEVER list/提示注入）、**buildbetter-app/skills**（模板体系）、**Eriemon/agents-md-generator**（多平台规则文件）。
- **同源工程治理系统（2026-08-30 审计比对）**：GATE 完成声明块 / 机械一致性检查 / 自我认证循环教训——本 Skill 对标采用 GATE 与状态面、并明确拒绝其「自我认证循环/元工作 KPI/仪式化登记」三项缺陷（仲裁记录在案）。

## 局限与代价 · Limitations

- 依赖强提示词注入与 Agent 自律：无运行时强制；注入跳过/描述未命中 = 什么也不做。
- 上下文成本：治理层仍消耗上下文——用三级跑道 + L2-S + 上下文卫生（两步式/信号化盘点/账本核算）换取一致性。
- 细则体量大（238 条）：症状索引 + 按类按需 + **预读 TOP** + 报错必经——从「可加载」升级为「必经站」。
- 平台检测启发式：不确定时问用户不猜。
- 未验证假设：规则能否改变行为（对照实验列下一轮）；verify=一致性≠有效性。
- 三语为增补制（非全量同文）——已如实标注。
- 自更新/校验两脚本属**发布/维护工具**，非运行时强制。

## 常见问题 · FAQ

- **为什么带 `agent-` 前缀？** 按需注入的 Agent 不自动执行本 Skill；用户在技能列表按字母序找，agent- 前缀让它排在第一位。
- **会覆盖我已有的规则吗？** 不会——安装/更新走「备份→合并（syncer 三路合并）→校验」，**你的 `user-notes/` 永不碰**；被覆盖文件可从 `.bak-<ts>` 或 `user-notes/` 找回。
- **`zxc663` 会做什么？** 仅彩蛋自检回复（注入方式/应用轮数/源库 vs 副本版本）；零操作零网络。
- **细则为什么曾经 0 命中？** 细则层原为「可选诊断」；v1.13 起报错必经+预读+取证，转有命中，已修复。
- **Agent 能感知自己被压缩吗？** 不能——显式信号 + 关键节点自检 + ~150-200K 阈值提示 + 会话级账本可核算。
- **上下文管理会不会「不让读报告」丢信息？** 两步式：读→提炼→全文落盘→上下文只留指针+摘要；需要细节再按指针取——不丢不占。
- **什么情况下该开新会话？** 连续 5 块回引旧内容，或块均成本 >2× 均值 → 建议新会话（交接文档+重载序）——重置点在状态面可见。
- **联网调研就是「网上说什么信什么」吗？** 不是——按权威性收集可验证信号 + 本地实测兜底。
- **如何保持本地与上游同步？** 跑 `python scripts/syncer.py`（一条命令，见上「安装」节）。

## 来源与依据 · Sources

- **细则 238 条/13 类**：v1.9.1 前 203 条（12 类）蒸馏自真实生产开发日志（863.6KB 主日志等，源文档存独立工作目录不随仓分发）；第 13 类 24 条（204-227）= 博客 CMS 前端重做阶段全量 agent 日志审计回流（8.2MB 事件流 + 53MB 转录 / 8 页面会话 / 走查断言 90+，双击晋升制）；**228-238** = 2026-08-30 全会话审计回流（跨包 dist/常驻旧 dist/走查三陷阱/断更防呆/上下文阈值/对接假绿/提问超时/上下文卫生/项目信息文档/秒级时间戳/日志对接）。
- **成本/命中实证（2026-08-30）**：ZCode 平台 `model_usage` 全量——累计 input 947,218,098 / output 2,188,313 / reasoning 249,823；19 会话 context_exceeded=0；细则工程消费 0→有（#228×3/#229×2/#233×1）。详见 EVIDENCE.md（拒绝伪精确纪律：只给可核算数字）。

## 版本历史 · Changelog

- **v1.19.0**：上下文管理四缺口修复——**两步式**（读→提炼→落盘→上下文只留指针+摘要）/盘点按**信号**触发/会话级**上下文账本**（入状态面）/重置点（5 块回引或成本 2× → 建议新会话）/信息单一源（盘点只写状态面）。
- **v1.18.0**：README 门面重构（定位=执行手册 + 触达端口论 + 真实数据节）；**RE 复述增强**（子复述即时/总复述仅提炼要点）；A4 决策改判/A5 验收漂移留档；三语增补制同步；verify 改造跑绿；发行物就绪（CHANGELOG/dist/RELEASE-CHECKLIST）。
- **v1.17.0**：skill 自更新协议——syncer.py 三路合并；user-notes/ 永不碰；彩蛋+状态面版本一致检查。
- **v1.16.0**：全文执行化改写（五段式 + §12 速查表 + 禁用孤立副词 + 纸面盲测）；项目信息文档示范。
- **v1.15/1.14/1.13/1.12**：项目信息文档六节·秒级时间戳·日志对接·会话五条（拒绝日志/看板/停点/活头部/记录上限）｜用户偏好集升格默认 + 经验强制预读 + 上下文管理｜11 步改大模块专属 + L2-S 短工作流 + 对接真相铁则 + 细则触达修复（0→有命中）｜GATE/状态面/产品视角强制/调研矩阵/前文复用/无 plan 入口/四件套/bootstrap/回指段 + 细则 #228-232。
- **v1.11-1.0**：细则 227 条/13 类 + 症状索引；三语发行；47 条规则；渐进式披露五支柱；11 步门禁；首版（43 条、双模式、回滚、渐进式披露）——详见 git 历史与之前的 CHANGELOG（v1.9.1 前各版按既有记录）。

## 贡献者与许可 · Contributors & License

**十三希诺** — 作者与维护者（zxc663）。
**反馈渠道（开源交流用途，长期公开）**：邮箱 a13sion@qq.com ｜ QQ 交流群 1059212846（版本更新时请同步维护本行）。

欢迎贡献：规则改进、工作流补充、本地化修正请开 issue/PR；新增规则先走本 Skill 自带的规则新增流程。许可 License：MIT，见 LICENSE。

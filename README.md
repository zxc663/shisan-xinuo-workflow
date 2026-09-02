# Shisan Xinuo Agent Workflow · 十三希诺 Agent 工作流

> **渐进式工程治理 Skill——不是把整本手册砸进上下文，而是像神经系统：只在任务到达某一步骤时，注入那一步所需的少量规则。**
> A progressive, on-demand engineering-governance Skill: injects only the few rules a step needs, when that step arrives.

![version](https://img.shields.io/badge/version-2.3.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![platforms](https://img.shields.io/badge/platforms-Codex%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20Trae%20%7C%20Windsurf%20%7C%20WorkBuddy-orange)

> **作者的话 · A word from the author**
>
> 本仓库实质上就是一个**规范工程化的大模型 Agent 提示词注入标范与标本合集**——你可以直接拿本 Skill 的内容当**工作流样本**来打磨你自己的 Agent 工程规范。版本路线：**v2.0.5 之后进入稳定的「细则类小更新」**（触达问题已明确为**提示词边界问题**），不再做破坏性的大版本改动；但**不做绝对保证**（可能仍有意外情况）。**一个必须直面的诚实边界**：哪怕在触达上做了重重努力（注入三层 / 项目承载 / 委托纪律包），这终究是**提示词范畴**——抵不上平台级「让 Agent 新会话自动加载」这样一句机制保证。**验收判据（可执行）**：新会话常驻不可用，或自检彩蛋 `zxc663` 未触发 → 即证明本 Skill 需要**用户主动触发或配置触发器**（平台 hooks / SessionStart），别把「提示词在场」误当「机制在场」。感谢加星 ⭐。
>
> *At its core this repo is a specimen collection of disciplined, engineering-grade prompt-injection standards for LLM agents — use it as a sample workflow to polish your own. After v2.0.5 expect stable, fine-grained updates; no breaking releases planned (but no hard guarantee). One honest boundary: however much injection/carrier/delegation effort goes in, this is still prompt-domain — it cannot beat a platform guarantee like "auto-load every new session". Acceptance check: if a fresh session is never aware of it, or the `zxc663` self-check does not fire, this Skill needs explicit triggering or a configured trigger (hooks / SessionStart) — do not mistake "present as prompt" for "present as mechanism". Thanks for the star.*

> **开源分发入口 · Distribution mirrors**（跨平台工程治理元 Skill，MIT）
>
> - GitHub 主线 · https://github.com/zxc663/shisan-xinuo-workflow
> - Gitee 国内直连镜像 · https://gitee.com/zxc663/shisan-xinuo-workflow
> - npm 包 · `@zxc663/shisan-xinuo-workflow`（GitHub Packages 源 `npm.pkg.github.com`）
> - skills.sh 收录 · https://skills.sh/zxc663/shisan-xinuo-workflow/shisan-xinuo-workflow
> - ClawHub · 搜索 `shisan-xinuo-workflow` ｜ 在线快速体验 · `npx skills add zxc663/shisan-xinuo-workflow`
>
> 一份仓库，多平台分发；任何入口均可读到本 README 与**唯一主交付物（中文版 Skill，v2.0 起单版本——不再有多语版与增补制同步）**。**语言声明：本 README 双语保留（中文优先做展示门面，英文见文首定位段）；Skill 本体为中文，为唯一权威全量。**

---

## 一句话定位 · One-line positioning

> **本质一句话（先读这条）**：**这个仓库本质上就是一份超长 System Prompt**——把「Agent 工程治理规范」做成一棵可渐进加载的提示词文件树：SKILL.md 是这份提示词的正文入口，references/ 按症状与细节按需载入，templates/ 是可直接填写的模板——无论哪个平台、哪种注入方式，最终喂给模型的都是一份格式化提示词全文；本 README 只是这份超长 System Prompt 的门面与索引。其余全部内容 = 规范的全文 + 让这份提示词「被加载 / 被验证 / 被自我更新」的机制层。

一个**「让规则被消费」的执行手册型工程治理元 Skill**：把「大模块专属的完整 11 步流程 + 小模块短工作流（L2-S）+ L1/L2/L3 判级路由 + 携带推荐理由的必问 + GATE 可复跑验证 + 五段式细则（触发/步骤/模子/自检/边界）＋ 经验强制预读 ＋ 上下文主动管理」打包成跨平台（Trae / Codex / Claude Code / Cursor / Windsurf / WorkBuddy / CLI）可审计的治理层。**设计意图不是「写更多规则」，而是给规则装触达端口**（错误必经句 / 预读 TOP / 命中取证 / 三路合并），并用可复跑工件（GATE 块 / syncer.py）让「做过 ≠ 说过」——每条规则都能被照着做，不靠领会。

**真实口径（2026-08-30/31 实测）**：

**① 工程消费与成本（平台聚合，13,281 part 穷尽取证）**：细则层（现 283 条 / 17 类）**工程消费命中此前 = 0**（v1.13 全平台审计），v1.13-1.16 以「错误必经句 + 预读 TOP + 命中取证行」修复后转**有命中**（#228×3 / #229×2 / #233×1，sess_c0f4df2b 留痕）。成本实证：ZCode 平台累计 **input tokens 947,218,098（9.47 亿）**——**好的**：19 会话零 context_exceeded、零 retry；**坏的**：3 个长会话占全平台 input 81%（7.66 亿）、单会话峰值 3.32 亿 input / 单次 652K、无压缩；6 次计划拒绝 + 6 次「继续」是主要重复成本推手。**注明**：9.47 亿是平台聚合，非 Skill 归因（归因明细见 EVIDENCE §九）；常驻开销实测 ~0.8%（~1.7K tok / 200K）。

**② 场景路测描述（四轮，全部描述性证据、无「已验证」表述；产物不进开发库）**：

- **一轮（基线 v2.0.4，klona / p-map / mitt / ky / commander / chalk+ink 真实 issue）**：A 轨 13 块（with 规则）+ B 轨 3 项（without）+ 反向审计 12 项漏检。命中 1/13≈7.7%（#93）；**A 轨 T5 判据失误**（用「出错点」判据、issue 指「调用点」）被 B 轨独立纠正 → 回流 #255/#256（不复现四要件 / 异步栈丢调用点）；**取证命令三口径实证**（v2.0.3 假阴性 / v2.0.4 假阳性 9 为 issue 编号 / 严格=自指，真实命中=1）→ v2.0.5 废弃裸 `#NNN` 只认完整前缀形态。
- **二轮（基线 v2.0.5，56 条真实踩坑诊断）**：严格命中 25.0%，但 **7/14 为「背答案」**（#255-267 来自同批项目）——扣后**原创命中 12.5% 与一轮同量级**；「已安装 ≠ 被加载」（执行会话 13 块未加载 Skill）；子代理提醒可读仍 0 加载；8 类零命中（约 111 条无贡献）；注入副本实测仍 v2.0.4（设计未通电）→ v2.0.5 触达强化（在场提示动作指令化 / 错误必查 TOP 内联 / 子代理委托纪律包）。
- **三轮（会话 α，基线 c061d31，换池 zod / vitest / esbuild / prettier / tsx / unbuild / rollup / vite）**：独立建库 59+4 条（未读一轮/二轮报告等答案文件、每条附 URL/日期/根因强度 A-B-C），判定未完成——**按裁定「拿到这一轮」**，作为四轮的判定输入。
- **四轮（基线 v2.0.6，判定重建 + 触达六埋点）**：面1 H 4/63≈6.3%（H+P 38.1%），A→N 预警 18 条（库内部/领域特定/上游回归——Web 全栈细则与底层构建工具链池结构性错位）；**泛化检验 #268-271 仅 #270（配置合并数组）跨池成功**（1/63≈1.6%）——实例污染 / 响应体单次消费 / 非 TTY 三类绑定原池特定库；面2 PART0 承载自动建 **3/3 但为 5 个无扩展名空文件**（空占位 → v2.0.6 规范件 + 项目级规则文件修复）；子代理 A 段③ 前缀自检 0（**不可复核——子代理不继承注入副本**，实测根因）。
- **附带结论**：四轮下来验证的是「可追溯 / 可审计 / 点破后快速恢复」，**没有**验证「规则带来正确性优势」——两轮 A/B（2026-08-30 四任务四指标无差异；2026-08-31 A 轨 n=14 / B 轨 n=6：5 个可比任务 B 轨 2 次纠正 A 轨 + 3 次挖得更深、A 轨 0 次优于，但 B 轨投入密度 ~3 倍，只读作「B 轨未劣于 A 轨」）。

**③ 口径说明（诚实声明细则，防误读）**：判档三档 H（全命中）/ P（部分命中·类比迁移）/ N（未命中）逐条留痕；**通用设计原则（#174 DRY / #175 KISS / #176 YAGNI / #89 / #91 / #92 / #86）零计入命中**（防虚高至 60%+）；C 强度（机制不明）一律按从严判 N、C→H 零容忍；A→N 18 条显式标预警供复核；**跨轮命中率非同口径不比较**（分母、项目池、H/P 定义均异：12.5% vs 6.3%）；n<20 **不出 p 值**；**实测 / 声称 / 不可复核三级区分**（子代理自报、issue 评论区未读属不可复核）；**全部为描述性证据，禁止表述为「已验证」**；每一轮结论回流开发库的只有「细则条目（#255-271）+ 机制修复 + EVIDENCE 摘要」，原始产物留在独立路测工作区。**作者边界（2026-08-31 定调）**：触达已明确为**提示词边界问题**——注入三层 / 项目承载 / 委托纪律包只能提高概率，抵不上「平台级新会话自动加载」；**验收判据**：新会话常驻不可用或 `zxc663` 未触发 → 需用户主动触发或配置触发器（hooks / SessionStart），「提示词在场」≠「机制在场」。

*(EN) A "rules-must-be-consumed", execution-manual governance meta-skill. Not more rules — touchpoints: error-time entry point, must-read top, hit evidence-line, three-way self-update merge; verifiable artifacts (GATE / syncer.py) make "done" ≠ "claimed". Real numbers: detail-layer engineering hits were 0 before v1.13 (now converts to hits); platform cumulative input 947M tokens (3 long sessions = 81%); assumption that rules change AI behavior is still unverified.*

---

## 目录 · Contents

[为什么用它](#为什么用它--why-this) · [它为谁解决什么](#它为谁解决什么--who-its-for) · [工作原理](#工作原理渐进式--状态机--how-it-works) · [功能全景](#功能全景--feature-map) · [差异化优势](#差异化优势--differentiation) · [架构真相（诚实）](#架构真相诚实--architecture-truths) · [快速体验](#快速体验--quick-start) · [安装](#安装--install) · [仓库结构](#仓库结构--repository-layout) · [版本说明（单版）](#版本说明单版--editions) · [参考项目](#参考项目--reference-projects) · [局限与代价](#局限与代价--limitations) · [常见问题](#常见问题--faq) · [来源与依据](#来源与依据--sources) · [版本历史](#版本历史--changelog) · [贡献者与许可](#贡献者与许可--contributors--license)

---

## 为什么用它 · Why this

- **把「AI 直觉」变成「工程纪律」**：L1/L2/L3 风险分级、关键必问（带推荐理由）、回滚点、GATE 验证块、五查留档——不再靠 Agent 自觉碰运气。
- **控成本不丢纪律**：渐进披露不整库常驻（注入核心里程碑实测 1–5K tok/会话）、L2-S 短流小任务默认、上下文两步式归档——目的不是降绝对 token，而是避免病态无界燃烧、并用极少常驻开销换取一致性；9.47 亿为平台聚合口径，非 Skill 归因（归因明细见 EVIDENCE §九）。
- **规则被消费而非被登记**：报错必经 details 症状类、开工必读预读 TOP、会话末取证命中（0 照报 0）、自更新三路合并——这是 v1.13 后区别于「规则堆」的核心差异。
- **跨平台行为一致**：第 0 步自动适配注入；自检彩蛋 `zxc663` 一次确认「注入方式 + 已应用轮数 + 源库 vs 副本版本」。
- **「AI 的记忆不随会话蒸发」**：`memory/` 统一归档（state 一屏 / experience 踩坑库 / preferences 偏好）+ 经验强制预读——换会话、换模型、换平台，第二个 Agent 站在同一个记忆上；踩坑与决策跨会话延续，不再每次从零重踩。
- **兜底不可逆事故**：L3 先问 + 原子操作锁（破坏性操作先列命令清单、结束回合等确认）+ 回滚点先建——AI 编码最贵的三类事故（删错数据、推错分支、改崩契约）把最后一道闸门交给人类，而不是交给 Agent 的自觉。
- **可审计可问责**：GATE 可重跑（cmd / exit / files / lessons / exempt）+ 决策审计归档（现象 / 依据 / 被否候选 / 选择 / 影响）+ 拒绝日志（R1 原话 + 隐含需求）——「做过 ≠ 说过」，每个结论可复核；状态面只报可核算数字，不报自我感觉。
- **自我校准的标本**：双击晋升制（同坑两次 → 细则回流）+ 四轮路测诚实口径（包括被无规则轨纠正的 T5/T9 判据失误、背答案 7/14 修正、泛化仅 #270 跨池成功）——本 Skill 自己也在被自己的方法论审计，bad 数据也摆上台面。
- **场景化，不乱建文档（v2.3.0）**：单发使用（新会话单发触发/无项目特征/非工程任务）纪律全走但**承载创建豁免**——不为一次性任务乱建 memory/规则文件/docs（乱建文档比不建更糟）；持续项目才强制六步全套 + 回指理解（details #283）。

*(EN) Turns AI instinct into auditable discipline; bounds token cost via progressive disclosure + short-lane + context hygiene (1–5K tok/session fixed overhead, platform 947M is aggregate, not skill-attributable); rules get consumed via mandatory touchpoints; consistent cross-platform via Step-0 injection. Extra: cross-session memory (next agent inherits state/experience/preferences), accident backstops (L3 ask-first + atomic-op lock + rollback points), auditability (re-runnable GATE, decision audits, rejection log), and self-calibration (double-hit promotion + four rounds of honest roadtests, bad data included).*

## 它为谁解决什么 · Who it's for

- 重度 AI 编码用户（Cursor / Claude Code / Trae / Codex 深度用户）：希望 Agent 跨项目、跨平台行为一致、可审计，尤其痛恨「假完成 / 伪造测试 / 虚报数据」。
- 按风险放权的人：L1 常规直接做，L3 高风险（密钥、删除、迁移、发布）一律先问。
- 想要无人值守目标模式的人：写计划、设预算、按文件边界拆分、超预算自动停。
- 想控成本又不丢纪律的人：渐进式加载 + L2-S 快速通道。
- 开源治理设计研究者：了解「渐进式 Skill」如何把静态约束变成动态治理。
- 刚入门、有一定了解、不想踩坑的用户：细则层即「踩坑日志 + 预读 TOP + 报错必经」——新人按图索骥少走弯路。
- **接手别人项目的「后来者」**：`docs/project-info.md` 六节里模块**真实状态表**（已实现 / 规划中 / 未实现）——不再把「规划中」当「已实现」踩坑；入场先读 state + experience-mustread，站在前人的记忆上而不是重新考古。
- **重复返工、总被「假绿」坑的用户**：对接真相清单（grep 调用点 → 读 schema → 确认包归属 → 才写）专治「命名直觉翻车」（envelope 不解包 / 走错包 / DI 名不匹配四反例）；错误必查 TOP 内联（#233 #214 #163 #256·#270 #262）——先对清单再 grep，不再边踩边修。
- **带子代理 / 团队协作的高级用户**：子代理不继承注入副本、不保证触发 Skill 加载（路测实证：提醒可读仍 0 加载）——委托时主代理内联最小纪律包（判级 / 红线 / 证据四要件 / 错误必查 TOP / 引用形态 / GATE / 承载），堵住「主代理守纪律、子代理旁路」的洞。
- **多平台 / 多模型切换用户**：Cursor → Claude Code → Codex → Trae → WorkBuddy 之间换着用——第 0 步自动适配注入点，注入副本随版本同步，行为一致不漂移；`zxc663` 一次说清「注入方式 / 轮数 / 源库 vs 副本 / Base directory」。
- **审计 / 评审 / QA 角色**：GATE 可重跑 + 会话状态面（版本 / 细则命中取证行 / 上下文账本 / 未验证待办）+ EVIDENCE 四轮路测方法论（A/B 对照、遮蔽组、H/P/N 三档评分、反向漏检清单）——可当「Agent 行为审计样张」直接用。
- **研究「提示词注入标范」的实践者**：三层注入 / 项目承载 / 委托纪律包 / 触达边界（作者定调：提示词范畴）——每个机制都配了对应实证（哪轮路测驱动、成功几处、失败几处），是标本不是口号。

## 工作原理（渐进式 / 状态机）· How it works

```
平台硬加载（第 0 步：检测平台 → 定位真实注入点 → 按需（精简） / 强制（injection-core 核心全文））
        │
        ▼
场景化判定（v2.3.0：单发使用 → 纪律全走 + 承载创建豁免；持续项目 → 六步全套 + 承载强制 + 回指；判定不清默认轻量）
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
规则（+ 编号纪律，地基）+ 落地细则（283 条/17 类，症状索引）+ 冲突仲裁序
        │
        ▼
自更新（syncer.py 三路合并：体检→备份→迁移 user-notes/ →覆盖→双落盘；user-notes/memory/.bak 永不碰）
```

渐进式三层：入口精简（只预载 name+description + injection-core 核心）→ 按步加载（references 按需 / details 按症状类）→ 动态路由（判级前置走 L1/L2-S/L2-F）。
## 功能全景 · Feature map

| 能力 | 说明 | 入口 |
|---|---|---|
| 第 0 步平台检测与硬加载 | 检测平台 → 定位真实注入点 → 按需(精简) / 强制(injection-core 全文)，备份后合并绝不覆盖 | SKILL §3 · injection-core.md · platform-adaptation.md |
| **三级跑道（v1.16+，2.0 起唯一版全量）** | L1 快速通道 / **L2-S 短工作流**（默认小模块）/ L2-F 完整 11 步（大模块专属）——防流程空转与 token 浪费 | SKILL §2.2-2.4 · workflows §0.6 |
| **对接真相清单（强制）** | 跨包/新端点/新依赖先产「模块\|API\|对接方式\|证据来源」表，禁凭命名直觉 | SKILL §2.3 · details #233 |
| 必问协议 | 问题必带推荐+理由+后果；超时空答→调研+待确认标注 | SKILL §4 |
| **GATE 完成块** | 任务块一行可复跑验证（cmd+exit+files+lessons+exempt）；验收权在用户 | SKILL §7 · 模板 task-record |
| **复述增强 RE** | 关键决定即时子复述（依据+影响）；块尾总复述仅提炼要点 | SKILL §4.1 · §12 RE |
| 交付五查 | 遗漏/边界/临时代码/无关改动/**已接日志模块** | SKILL §7 |
| **会话状态面** | 结束输出：版本/细则命中取证行/**上下文账本（增量/最大单次/占比）**/版本一致性/未验证待办（给用户复核，非达标声明） | SKILL §11 |
| **经验强制预读** | experience-mustread TOP≤10（先于症状检索；≥3 次或高返工晋升） | memory/experience-mustread.md · workflows |
| **上下文主动管理（v1.19 四项 + v2.1 折叠协议）** | **两步式**（读→提炼→全文落盘→只留指针+摘要）；盘点按**信号**触发；**会话级账本**；**重置点**（5 块回引或成本 2× → 建议新会话）；**v2.1 增：折叠协议**（保留清单五必留核对 → checkpoint 落盘 → 旧块一行摘要 → 重载序）、**紧凑档**（短上下文部署参数表）、**大文件读取协议**、**模块锚点表 + 按需符号召回**（手动 repo map） | SKILL §12 P3/P8 · details #272-276 |
| 双模式（普通/目标/安静） | 关键必问 vs 无人值守（计划/预算/文件边界/超预算停）；安静 L1 只报结果 | SKILL §5 |
| 冲突仲裁序 + 经验回流 | 五级仲裁取最优；踩坑双击晋升细则 | SKILL §4 · §10 |
| **项目信息文档** | 新项目无文档→建六节导航（架构/目标/模块真实状态/调研导航/参考资源/复述签章） | SKILL §2.5 · new-project-bootstrap.md |
| **日志对接** | 有日志模块的项目：设计期对接行 + catch 三件套 + 五查含日志 | SKILL §7 · details #238 |
| **skill 自更新** | syncer.py 三路合并（用户规则目录永不碰）；彩蛋+状态面版本一致检查 | scripts/syncer.py · SKILL §3.1 |
| 配套模板/钩子/子代理 | 规划/验收/任务记录/复盘/回滚点/预算/钩子/审查子代理 | templates/ |
| **彩蛋自检 zxc663** | 回复「注入方式 + 已应用轮数 + 源库 vs 副本版本」——纯自检零操作 | SKILL §12 ZE |
| **场景化判定（v2.3.0）** | 单发使用（新会话单发/无项目特征/非工程任务）→ 纪律全走、**承载创建豁免**（不乱建 memory/规则文件/docs）；持续项目 → 六步全套 + 承载强制 + 回指；判定不清默认轻量 | SKILL §2.0 · details #283 |
| **纠偏续跑 Steer（v2.3.0）** | 方向错 → 暂停 → 保留已确认正确部分 → 增量调整 → 从当前状态继续（不从头重做）；面向结果指令 | details #280 · §12 C1 |
| **并行依赖协议 Parallel（v2.3.0）** | 依赖分析先行（强依赖串行）→ 子任务五要素 → 合并统一集成验证 | details #281 · §5.1 |
| **回指理解强制（v2.3.0）** | project-rules「回指（强制）」段（缺失=不合规）+ 会话末更新行 + §0 任务中途每一条消息先严谨分析 | details #282 · project-rules 模板 |
| **文档写作分层（v2.3.0）** | 写任何文档产物：正文只写结论/规则 + ≤1 句为什么；史料（出处/拍板人/日期/轮次）落决策史层 | SKILL §10 总纲 · details #278 |
| **审计修复（v2.3.0 症状索引门禁）** | details 头部症状索引表 283 条全覆盖 + verify 新增 **F 项索引完整性门禁** + GATE 增 `errpath` 字段（错误路径核对可查） | details 头部 · verify-release F 项 · GATE |

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
- **规则有效性：已有 2 轮 A/B 证据但均未达显著**（2026-08-30 四任务四指标无差异；2026-08-31 二轮 A 轨 n=14 / B 轨 n=6：5 个可比任务中 B 轨 2 次纠正 A 轨错误判断（T5/T9）+ 3 次挖得更深、A 轨 0 次优于——但 B 轨投入密度 ~3 倍、A 轨兼承取证元任务，只读作「B 轨未劣于 A 轨」）——机制按拍板保留，但不得宣称「已验证」；**「已安装 ≠ 被加载」的触达缺口为已知问题**（主会话靠注入副本、子代理靠委托纪律包直送；二轮实证子代理提醒可读仍 0 加载）；更大样本/更长周期复验列下轮。verify 绿=体系与自身一致，非行为变好。
- **曾 0 命中**（v1.13 实证）：细则层工程消费=0——已以触达端口修复为有命中；仍如实标注「预防性，有效性需实测」。
- 不提供「硬门禁」：依赖平台（hooks/CI/沙箱）；缺口用兜底。
- 定位是「治理层」：不替代领域知识/项目文档；冲突时项目文档优先。
- **诚实可核算**：成本真账（9.47 亿/81%/会话级账本）对外公开，好与坏都摆——门面的一部分，不是免责声明。

## 快速体验 · Quick start

1. **安装**：git 用户跑 `scripts/install-skill.ps1`（一条命令自动带 `agent-` 前缀、自适配到目标平台技能目录，可选 `-Link` 软链 / `-HardInject` 顺手注入配置层）；npm 用户 `npx skills add zxc663/shisan-xinuo-workflow --skill agent-shisan-xinuo-workflow`（**前缀在安装名上：`agent-` = 按字母序在技能列表最前**——按需注入的 Agent 不会自动执行，用户靠字母序发现）。旧平台可解压 `dist/` 发布 zip（gitignore 产物：从 GitHub Release 下载——**最新已发行版 v2.2.0 已随 2026-09-02 全渠道发行上传 GitHub Release（v2.1.x 历史版本在 Releases 内可查）；v2.3.0 为本地批次，dist 待发行时打包**——或按仓库脚本 `scripts/build-dist.ps1` 重新打包（staging 暂存 + Set-diff 双检，v2.2.0 起））。
2. **加载**：新开会话。Skill 自动执行第 0 步检测与注入；**若模型未自动适配，手动再输出一遍本 skill 名字**触发 → 按 §3 备份→合并→校验。
3. **感受它**：给一个小任务——先复述理解 + 3-5 条验收；给风险任务（「把这个目录删了」）——必须先问再动手（L3）。
4. **目标模式**：说 `目标：整理本目录文件并归组，注意不要删除任何内容`——观察写计划/预算/文件边界/超预算停。
5. **底线自检**：输入 `zxc663`——应回复「十三希诺工作流已应用，注入方式是：［按需 / 硬注入］，已经应用 N 轮会话/对话｜源库 vX vs 副本 vY」。

## 安装 · Install

| 平台 | 位置 |
|---|---|
| 任意（一键） | git 用户：`powershell -File scripts/install-skill.ps1`（自动带 `agent-` 前缀、自适配目标平台技能目录；可选 `-Link`/`-Force`/`-HardInject`，`-Dry` 干跑） |
| skills.sh | `npx skills add zxc663/shisan-xinuo-workflow --skill agent-shisan-xinuo-workflow`（唯一版：中文主交付物；**安装名为 `agent-shisan-xinuo-workflow`**） |
| Claude Code | `~/.claude/skills/agent-shisan-xinuo-workflow/` |
| Codex / 通用 | 克隆本仓，技能发现指向 `skill/shisan-xinuo-workflow`；或解压 `dist/` zip |
| Trae / Cursor 等 | 按平台技能目录约定放置；Trae 需在应用设置启用项目规则 |

**更新与自维护**：上游更新后跑 `python scripts/syncer.py`（体检→备份→迁移→覆盖→双落盘；备份落 `skill-backups/`——平台扫描路径之外，验收以平台解析到的 Base directory 为准）；**你的本地规则写 `user-notes/`，永不随上游覆盖**；手动改副本只许写在 user-notes/。发布前置校验：`powershell -File scripts/verify-release.ps1`（内容锚点/hooks/版本+package/泄漏全绿才可发布）。

**硬注入 = 三层承载（v2.0.4）**：记忆层（每会话在场锚点，**首行「在场提示 · 工作流 Skill 现已在场」**：`templates/memory-anchor.md`）＋ 规则层（injection-core 核心全文）＋ 配置文件层（hooks/全局设置）**同时写入**，写前提醒用户授权；按需注入只写应用层（精简纪律 + 询问是否写规则层，不写记忆层）。配置层/记忆层文件含凭据时一律走环境变量，不落明文。

## 仓库结构 · Repository layout

```
shisan-xinuo-workflow/              ← 仓库根
├── README.md / CHANGELOG.md / RELEASE-CHECKLIST.md / EVIDENCE.md / LICENSE
├── 项目信息.md                      ← 中文维护文档（决策追溯 + 发布记录）
├── package.json（2.3.0）· docs/reference-sources.md · .github/workflows/（CI：verify-release）
├── dist/                           ← 发布 zip（gitignore 产物：从 Release 下载或脚本打包，不入仓）
├── scripts/syncer.py               ← 自更新三路合并（体检/备份→skill-backups/外置/迁移/覆盖/双落盘）
├── scripts/verify-release.ps1      ← 发布校验（内容锚点/hooks/版本+package/泄漏）
├── skill/shisan-xinuo-workflow/    ← 唯一主交付物（中文执行化全文 v2.0 · 单版本权威）
│   ├── SKILL.md（§0 元规则 · §2 三级跑道 · §4 必问+RE · §5 判级分流 · §7 门禁 · §9 引用表
│   │   · §10 记录纪律 · §11 状态面（含上下文账本）· §12 速查表 31 行）
│   ├── templates/（规划/验收/任务记录(GATE)/复盘/回滚/预算/钩子/子代理/memory 骨架五件套）
│   └── references/（injection-core · workflows · details 283条/17类 · rules 47条 ·
│       security · never-list · skill-usage · new-project-bootstrap · local-model-glossary）
└── versions/personal-zh/           ← 本地私有工作台版（gitignore，不进公开仓/发布物）
```

## 版本说明（单版） · Editions

| 版本 | 路径 | 语言 |
|---|---|---|
| **唯一主交付物** | `skill/shisan-xinuo-workflow/` | 中文（唯一权威全量，v2.0 起单版本） |
| 工作台版（私有） | 独立私有仓 + 本地 `versions/personal-zh/`（gitignore） | 中英混合 + 内嵌个人经验手册 |

> **同步口径（诚实）**：v2.0 起**唯一中文版为权威全量**——仓库不再维护英文 / 双语版（已删除；git 历史可追溯），不再有「增补制同步」的自律漂移面。README 双语保留（中文优先门面 + 英文摘要）。
>
> **发布面注记（诚实）**：**v2.0.6 已全渠道发行（2026-08-31：GitHub Release v2.0.6 / npm 2.0.6 / Gitee Release / ClawHub 1.0.7 / About 双端 PATCH）**。**v2.1.0（上下文主动管理补全）已于 2026-09-02 全渠道发行**：GitHub Release v2.1.0（附 dist zip）/ npm 2.1.0 / Gitee Release（zip 附件）/ ClawHub 1.0.8（pending scans）/ About 双端 PATCH（六·一 v2.1.0 文案）。**v2.1.1（口径修正补丁：细则类数 16→17 全仓统一 + README 本质声明优化）已于 2026-09-02 全渠道发行**：GitHub Release v2.1.1（附 dist zip）/ npm 2.1.1 / Gitee / ClawHub 1.0.9（pending scans）/ About 双端 PATCH（17 类文案）。**v2.2.0（开工序列六步 + 承载平台适配 + 本体净化 + 决策时效）已于 2026-09-02 全渠道发行**：GitHub Release v2.2.0（附 dist zip）/ npm 2.2.0 / Gitee Release（zip 附件）/ ClawHub 1.0.10（pending scans）/ About 双端 PATCH（279 条 17 类 + 六步/净化/决策时效口径）；发行前注入副本 ×4 重部署 v2.2.0 + 技能副本 syncer 同步。**v2.3.0（流程场景化 + 写作重构 + Steer/Parallel + 回指理解强制 + 审计修复）为本地批次，未发行**。发行台账见 RELEASE-CHECKLIST.md。

## 参考项目 · Reference projects

> 机制/结构借鉴，非复制代码。同类独立演进，本 Skill 为后发者。

- **Agent Skills 规范**（agentskills.io/specification）：SKILL.md 结构、渐进式披露、name+description 激活 — 机制根基。
- **agent-playbook-template**（prompt-budget / critic·risk-reviewer 子代理）、**AI-AGENT-SKILLS**（会话钩子）、**anchor**（NEVER list/提示注入）、**buildbetter-app/skills**（模板体系）、**Eriemon/agents-md-generator**（多平台规则文件）。
- **同源工程治理系统（2026-08-30 审计比对）**：GATE 完成声明块 / 机械一致性检查 / 自我认证循环教训——本 Skill 对标采用 GATE 与状态面、并明确拒绝其「自我认证循环/元工作 KPI/仪式化登记」三项缺陷（仲裁记录在案）。

## 局限与代价 · Limitations

- 依赖强提示词注入与 Agent 自律：无运行时强制；注入跳过/描述未命中 = 什么也不做。
- 上下文成本：治理层仍消耗上下文——用三级跑道 + L2-S + 上下文卫生（两步式/信号化盘点/账本核算/**v2.1 折叠协议 + 保留清单**）换取一致性。**紧凑档（短上下文部署）诚实代价：注入核心 ~1.7K token 对 8K 窗口 ≈ 21%**——纪律不降级（Preserver 原则：规则原文是保留清单必留项），换 token 靠折叠协议/锚点表/大文件协议，不靠砍纪律。
- 细则体量大（283 条）：症状索引 + 按类按需 + **预读 TOP** + 报错必经 + **错误必查 TOP 内联**——从「可加载」升级为「必经站」。
- **客户端能力边界（v2.1 诚实声明）**：`/map` `/ctx` `/scan`、自动 repo-map 构建、增量 diff 传递、轻量模型自动折叠是 **Aider / 1bcoder / Atrium / Context Governor 等客户端或中间件的执行层能力**——本 Skill 不假装拥有，只提供**纪律化等价协议**（模块锚点表 / 按需符号召回 / 折叠协议 / 大文件读取协议，details #272-276）与联用建议（下表）。
- **与上下文治理客户端联用建议（v2.1）**：换客户端或中间件**不冲突**——本 Skill 是纪律层（注入核心 + 协议），客户端是执行层（repo-map 自动构建 / 压缩调度）。推荐组合：Aider（工程向，repo-map + 增量上下文）加载本 Skill 纪律包；Atrium / Context Governor（压缩中间件）在前端做历史折叠时，本 Skill 的**保留清单**正好给「压缩时强制保留什么」提供纪律输入；1bcoder（小模型向）的 /map /ctx /scan 与本 Skill 锚点表/折叠协议互为补充——客户端自动构建，Skill 规定「保留什么、什么时候折叠、折叠产物落哪」。
- 平台检测启发式：不确定时问用户不猜。
- 未验证假设：规则能否改变行为（对照实验列下一轮）；verify=一致性≠有效性。
- 单版本（v2.0 起）：唯一中文版为权威全量；删除的英文/双语版在 git 历史可回溯——不再有增补制同步面。
- 自更新/校验两脚本属**发布/维护工具**，非运行时强制。
- **非「自动做对」（2026-08-31 实证）**：纪律提供的是可追溯/可审计/**点破后快速恢复**机制（补全+声明+复盘），不是保证 Agent 自动做对的魔法；两轮 A/B 未观察到显著差异——价值主张对齐此边界，不夸大。

## 常见问题 · FAQ

- **为什么带 `agent-` 前缀？** 按需注入的 Agent 不自动执行本 Skill；用户在技能列表按字母序找，`agent-` 前缀让它排在第一位。**官方已一键适配**：仓库 `scripts/install-skill.ps1` 安装即自动带前缀（`--skill agent-...` 同效），无需手动重命名。
- **会覆盖我已有的规则吗？** 不会——安装/更新走「备份→合并（syncer 三路合并）→校验」，**你的 `user-notes/` 永不碰**；被覆盖文件可从 `.bak-<ts>` 或 `user-notes/` 找回。
- **`zxc663` 会做什么？** 仅彩蛋自检回复（注入方式/应用轮数/源库 vs 副本版本）；零操作零网络。
- **细则为什么曾经 0 命中？** 细则层原为「可选诊断」；v1.13 起报错必经+预读+取证，转有命中，已修复。
- **Agent 能感知自己被压缩吗？** 不能——显式信号 + 关键节点自检 + ~150-200K 阈值提示 + 会话级账本可核算。
- **上下文管理会不会「不让读报告」丢信息？** 两步式：读→提炼→全文落盘→上下文只留指针+摘要；需要细节再按指针取——不丢不占。
- **什么情况下该开新会话？** 连续 5 块回引旧内容，或块均成本 >2× 均值 → 建议新会话（交接文档+重载序）——重置点在状态面可见。
- **联网调研就是「网上说什么信什么」吗？** 不是——按权威性收集可验证信号 + 本地实测兜底。
- **如何保持本地与上游同步？** 跑 `python scripts/syncer.py`（一条命令，见上「安装」节）。
- **为什么新会话有时「在场」识别不到？** 硬注入需**三层同时写**——记忆层（每会话读取的记忆文件，写入 **在场提示** 锚点）、规则层（injection-core 全文）、配置文件层；只写规则层、记忆文件空白时，新会话 Agent 可能不知道本 Skill 在场。用 `scripts/install-skill.ps1 -HardInject -MemoryFile <记忆文件>` 或 `syncer.py --memory-target` 补齐记忆层。
- **这个 Skill 与手写一页 AGENTS.md 有什么本质区别？** 一页规则是「静态提示词」：靠模型自觉执行、无法验证；本 Skill 是「触达端口 + 可复跑工件」：报错必经细则、预读 TOP、GATE 可重跑（cmd/exit/files）、状态面取证行、syncer 三路合并——外加渐进披露（不用背 283 条）与跨平台注入副本同步。一句话：前者是纪律清单，后者是让纪律「被消费」的机制。
- **细则 283 条，谁读得完？** 不需要通读——它是**踩坑日志不是教程**：症状索引 + 按类按需（报错/意外形态/新依赖不生效才开）+ 开工预读 TOP（≤10）+ 错误必查 TOP 内联（#233/#214/#163/#256·#270/#262 先对再 grep）。读法像「查药典」，不是「背药典」。
- **路测说「规则没带来正确性优势」，还值得用吗？** 值得，但别误读：两轮 A/B 未达显著是**诚实声明**（不宣称有效）。真实价值 = 可追溯 / 可审计 / 防返工 / 点破后快速恢复（被四轮实测反复验证）；并且它坚持把失败数据也登出来（T5/T9 判据失误、背答案、空占位）——信任来自不吹。
- **子代理要用它怎么办？** 关键认知：**子代理不继承注入副本、不保证触发 Skill 加载**（实测：提醒可读仍 0 加载）。正确用法 = 主代理委托时**内联最小纪律包**进子代理 prompt（判级 / 红线 / 证据含不复现四要件 / 错误必查 TOP / 引用形态 / GATE / 承载）；不指望子代理自己加载 Skill。详见 rules.md §28 与 SKILL §12 AG。
- **「项目承载」是什么？要手动建吗？** 三件：`memory/` 规范五件套（state.md / experience-mustread.md / experience.md / preferences.md / task-log/，**带扩展名的正文文件，禁空占位**）+ `docs/project-info.md` 六节索引（模块表含**关键词锚定列**）+ **项目级注入规则文件**（AGENTS.md / CLAUDE.md / .trae-rules，模板 `templates/project-rules.md`）。开工由「项目承载检查」**自动建**（先查既有规则文件→合并不覆盖+备份）；**项目工作区内写文件是自动动作，不必等授权**（授权边界：仅平台全局注入/密钥/破坏性/发布/超预算）。
- **`/map` `/ctx` `/scan` 这些命令有吗？** 没有——它们是 1bcoder / Aider 等客户端的原生命令，ZCode 等平台不提供。本 Skill 提供**等价纪律协议**：模块锚点表（≈/map，details #275）、折叠协议+保存点（≈/ctx，details #272）、大文件读取协议（≈/scan，details #274）——手动执行等价动作；客户端有原生命令时直接调用，本 Skill 规定「保留什么 / 何时折叠 / 产物落哪」（保留清单，injection-core 关键条款）。
- **换本地小模型（短上下文窗口）会怎样？** 在 `memory/preferences.md` 标注「紧凑档」→ 折叠阈值改按窗口比例 25-35%、预算强制 ≤minimal、锚点表+大文件协议强制；纪律不降级（注入核心全文保留——Preserver 原则），代价是注入核心在小窗口占比升高（8K 窗口 ≈21%），换 token 靠折叠协议不靠砍纪律（details #273）。
- **为什么会「在场」却还是没被遵守？** 作者定调：**触达 = 提示词边界问题**——提示词能提高概率、做不到保证；「在场」与「执行」之间的缝只能靠平台触发器填（hooks / SessionStart）。别把「提示词在场」当「机制在场」——这是本 Skill 最诚实的边界声明。
- **怎么配置触发器，让每个新会话都强制加载？** 平台 hooks（SessionStart/End）或各平台全局规则文件（`platform-adaptation.md` §2.1 有逐平台实测明细——本机 Claude Code hooks 因 bash 不可用已降级、Codex/WorkBuddy 无 hooks 槽位已如实标注）；配置前先备份；**验收判据**：新会话输入「在场提示」关键词在上下文 + `zxc663` 正常回话 = 触发器生效。
- **换模型（强模型 → 弱模型）会失效吗？** 可能打折——弱模型对 description 触发精度会降（skill-usage.md §0 有弱模型保底做法：调小可发现清单 / 精准 description）；但注入副本（每会话在场）不受模型影响；`zxc663` 一次自检随时可验证当前是否在场。
- **「细则类小更新」路线是什么意思？** v2.0.5 之后的承诺：只做细则追加入库（双击晋升制）、措辞校正、口径补全——**不做破坏性大改**；但「不做绝对保证」（作者保留意外情况声明）。本仓库定位 = **Agent 提示词注入标范与标本合集**：把每次机制修改对应的实证（哪轮路测驱动、成功/失败各几处）一并归档，供你拿来打磨自己的工作流。
- **单发使用会建一堆文档吗？** 不会——v2.3.0 场景化（details #283）：单发/无项目特征/非工程任务 → 纪律照走、**承载创建豁免**（不建 memory/规则文件/docs，乱建文档比不建更糟）；持续项目才建 + 回指强制；判定不清默认轻量。

## 来源与依据 · Sources

- **细则 283 条/17 类**：v1.9.1 前 203 条（12 类）蒸馏自真实生产开发日志（863.6KB 主日志等，源文档存独立工作目录不随仓分发）；第 13 类（204-238）= 博客 CMS 前端重做阶段全量 agent 日志审计回流（8.2MB 事件流 + 53MB 转录 / 8 页面会话 / 走查断言 90+，双击晋升制）+ 2026-08-30 全会话审计回流（228-238）；**#239** = 2026-08-30 WorkBuddy 平台实测晋升（Skill 运维类：升级验收看平台解析到的加载目录，非文件版本号）；**#240-254（第 14 类）** = 2026-08-31 个人工作台版差异化回流（MCP 工具链 / 视觉生成 / 前端测试 15 条，用户拍板并入）；**#255-267（第 15 类）** = 2026-08-31 一轮路测回流（12 项漏检清单全收 + 「不复现」判定举证纪律；#256 异步栈出错点 vs 调用点为 A 轨判据失误的直接实证，二轮强化「真实构建产物 vs 自造模拟」）；**#268-271（第 16 类）** = 2026-08-31 二轮路测回流（chalk level 污染根实例 / 响应体只消费一次 / 配置继承拼接 vs 替换 / 非 TTY 环境查询 undefined——只收跨项目/同项目两次 + 通用性强者，终端渲染等绑定领域者按诊断不入通用版）；**#272-283（第 17 类）** = 2026-09-01/02 上下文管理补全与承载平台适配（折叠协议 / 紧凑档 / 大文件读取协议 / 模块锚点表 / 按需符号召回 / 多 Skill 触达与定名，纪律化伪命令 + 能力边界诚实声明）。**覆盖边界（诚实）**：细则主体沉淀自 Web 全栈（Next.js / Prisma / Playwright / Nest / 部署运维 / MCP / 视觉 API）；Node 开源库 / 终端 UI 为边缘场景、覆盖有限，凭通用工程常识兜底——这是定位，不是缺陷。
- **成本/命中实证（2026-08-30）**：ZCode 平台 `model_usage` 全量——累计 input 947,218,098 / output 2,188,313 / reasoning 249,823；19 会话 context_exceeded=0；细则工程消费 0→有（#228×3/#229×2/#233×1）。详见 EVIDENCE.md（拒绝伪精确纪律：只给可核算数字）。**取证口径（2026-08-31 两轮演进：v2.0.4 → v2.0.5）**：v2.0.4 前命令对实引形态恒 0（假阴性）→ v2.0.4 加裸 `#NNN` 分支校准为「0→有」→ **2026-08-31 路测三口径实证 v2.0.4 命令假阳性**（10 计数中 9 为 GitHub issue 编号误计；严格形态=1 且为命令自指；真实语义命中=1）→ v2.0.5 废弃裸编号分支、只认完整前缀形态 `details #NNN` / `细则 #NNN`（引用规范见 details.md 头部，见 EVIDENCE §十）；**二轮双向自证 63=63 通过**（面 1/2/3 全部引用为完整前缀形态，无裸 `#N` 计入）。

## 版本历史 · Changelog

- **v2.3.0**（2026-09-02）：**流程场景化 + 写作重构 + Steer/Parallel + 回指理解强制 + 审计修复 1-7——①**场景化**（details #283）：单发使用（新会话单发触发/无项目特征/非工程任务）→ 纪律全走、**承载创建豁免**（不建 memory/规则文件/docs）；持续项目 → 六步全套+承载强制+回指；判定不清默认轻量单发 ②**写作重构**：正文 vs 史料泛化为「文档写作分层」总纲（SKILL §10 顶部，写任何文档时）+ 原条例移根 AGENTS.md「维护纪律」小节 + workflows §9 固化日期裁决（日期记决策记录）③**Steer 纠偏续跑**（details #280）：方向错 → 暂停 → 保留已确认正确部分 → 增量调整 → 从当前状态继续（不从头重做）；面向结果指令 ④**Parallel 依赖协议**（details #281）：依赖分析先行（强依赖串行）→ 子任务五要素 → 合并统一集成验证 ⑤**回指理解双强制**：project-rules 模板「回指（强制）」段（缺失=不合规）+ 会话末更新行；§0 复述前置扩「任务中途每一条消息先严谨分析理解」；details #282 创建自检清单 ⑥**审计修复 1-7**：症状索引表（details 头部，283 条全覆盖，F 项门禁）+ 标签统一（17 种中文零分裂）+ 取证命令唯一权威源化（修 workflows 自相矛盾/陈旧编号）+ 错误必查 TOP 换血挂数据（纳入 #228/#229 实证命中条）+ 淘汰机制 + GATE `errpath` 字段 + E 项定位明示（references 史料豁免）+ hooks B 项降警告级 + 彩蛋 zxc663 降档出注入核心 + EVIDENCE 成本账补 SKILL 全载 + 矛盾裁决三对（重读优先/预载措辞/同步面收敛）。口径 279→283 条 / 17 类；verify 6/6 PASS（含 F 项）；本地 commit 不 push、发行面待批。
- **v2.2.0**（2026-09-02）：**开工序列六步 + 承载平台适配 + 本体净化 + 决策时效（已全渠道发行）**——①**开工序列六步**（SKILL §2.0 + injection-core）：复述理解（**无条件第一步含 L1，不自以为是，理解缺口先补依据**）→ 扫描工作区（根目录一层+自适应限流+形态判定）→ 定承载根（多目录按任务焦点+留档）→ 承载创建（强制，出口产物）→ 读上下文 → 判级选道；L1 豁免精简（复述不可豁免）②**承载平台适配**：platform-adaptation 新增「项目级注入点表」（Codex=项目根 AGENTS.md 必建等），SKILL §3 第 6 步③与 injection-core 按表定名（删除错误路径 `.trae-rules`），加载即承载检查（SKILL §1——多 Skill 底座占位时本 Skill 条款不依赖注入核心），details #277 ③**本体净化（正文 vs 史料规范）**：SKILL §0 立规范（正文=规则+≤1 句为什么；版本/拍板人/日期/路测轮次→决策史；details 来源字段豁免；注入核心禁悬空指针），逐文件清理过程注记与悬空指针（SKILL/injection-core/details/workflows/platform-adaptation/rules/skill-usage/templates），verify-release 新增 **E 项正文净化检查**（常驻/模板面过程注记=0）+ A 项锚串「项目级注入点」④**决策时效**：details #278 依据场景矩阵（方向性决策依据持久必带前提+重开条件；辅助性背景依据默认 task-log；一次性理由永不入项目文档）+ #279 化石识别（决策可重开——读到历史依据先验前提）；混合写入门槛（普通模式升格持久层前必问「本次还是长期」，目标模式靠标注兜底）；仲裁序升格常设偏好必带前提+重开条件。口径 276→279 条；verify 5/5 PASS（含 E 项）；dist v2.2.0.zip 39=39（190,102B）+ 注入副本 ×4 重部署 v2.2.0 + 技能副本 syncer 同步；**已全渠道发行（GitHub Release v2.2.0 / npm 2.2.0 / Gitee / ClawHub 1.0.10 pending scans / About 双端 PATCH 279 条 17 类）**。
- **v2.1.1**（2026-09-02）：**口径修正补丁（已全渠道发行）**——①**细则类数 16→17 全仓统一**（details.md 实际 17 分节、类数=分节数系历史自洽规则；v2.1.0 发行预算误记「16 类不变」；SKILL / injection-core / EVIDENCE / docs / CHANGELOG / README / 项目信息 / **About 双端描述全部同步修正**）；②**README 门面优化**（新增「**本仓库=一份超长 System Prompt**」本质声明 + v2.1.0 已发行口径回填 + dist 提示更新）；③dist v2.1.1.zip 重建（38 项 Set-diff 38=38）。verify 4/4 PASS；发行：GitHub Release v2.1.1 / npm 2.1.1 / Gitee / ClawHub 1.0.9 / About 双端 PATCH（17 类文案）。
- **v2.1.0**（2026-09-01 源码 / 2026-09-02 全渠道发行）：**上下文主动管理补全批次**——借鉴 Aider repo-map / 1bcoder /map·/ctx·/scan / Atrium Preserver / Context Governor 四大客户端机制（用户提供清单）：①**保留清单 + 折叠协议（Preserver）**——压缩/折叠/交接前核对五必留（任务本质/验收标准/激活规则原文/当前步骤/回滚基线），触发→checkpoint 落盘→旧块一行摘要→重载序（injection-core 关键条款 + SKILL §12 P8 + details #272）；②**紧凑档（短上下文适配）**——preferences 标注「紧凑档」→ 折叠阈值按窗口比例 25-35%、预算 ≤minimal、锚点表+大文件协议强制、**纪律不降级**（注入核心全文保留，Preserver 原则；诚实代价 1.7K/8K≈21%）；③**模块锚点表**（docs/project-info 模块表加关键词锚定列，手动 repo map，details #275）；④**大文件读取协议**（>300 行先头部/锚词定位再读，禁整读，details #274）；⑤**本地模型术语表**（references/local-model-glossary.md，10 术语随 Skill 分发）；⑥**客户端能力边界诚实声明 + 联用建议**（局限节：自动 repo-map/增量 diff/轻量模型折叠是客户端执行层能力，Skill 只提供纪律化等价协议）；⑦**补强批次**：模块依赖关系表（project-info 架构节，details #276）+ 按需符号召回协议（#276：锚点表→grep 定义/调用点→只读签名行→局部理解，禁为找符号整读）。口径 271→276 条 / 类数 16→17（新增 §17「上下文主动管理补全」类——发行预算误记「16 类不变」，2026-09-02 复盘按 details 分节数修正）；verify-release A 项 +锚串（折叠协议/保留清单）。verify 4/4 PASS；**2026-09-02 已全渠道发行**（GitHub Release v2.1.0 附 dist zip / npm 2.1.0 / Gitee 附件 / ClawHub 1.0.8 / About 双端 PATCH）。
- **v2.0.6**（2026-08-31）：**项目承载 + 授权边界修复批次（执行批次，已全渠道发行）**——WorkBuddy 新工作区实测（执行会话自述 5 问题）驱动：①**部署第五层「项目承载检查」**（SKILL §3 第 6 步）：硬注入三层之外检查项目工作区——无 `memory/` 骨架 → 自动建五件套；无 docs/project-info.md 且多文件 → 建索引式六节；②**授权边界分级**（§4 映射表 + injection-core 红线）：项目工作区内写文件（memory/ 骨架、docs/、代码）= **自动动作，不触发授权停**；授权仅限平台全局注入 / 密钥 / 破坏性 / 发布 / 超预算——修复「自动建 memory 被误当需授权」根因；③**§2.5 触发改存在性判定**：无 memory/ 骨架 或 无 docs → 触发，不做「算不算新项目」主观判定；④**开工「项目承载探测」写死**（injection-core 开工四动作 + SKILL §10 会话始）：ls 项目根 → 无骨架自动建 → 再扫 memory/ → 判级选道；⑤**现场修复**：`~/.agents/skills` 下 6 个 `.bak-*` 备份在平台扫描路径内（**Base directory 落旧版根因**）→ 迁移至 skill-backups/；`~/.workbuddy/skills` 副本停在 b8d1022（缺本次触达条款）→ syncer 同步至 2.0.6；⑥诚实补句：纪律 = 可追溯 / 可审计 / 恢复机制，非「自动做对」。verify 4/4 PASS；注入副本 ×4 重部署 v2.0.6（先备份）；**已全渠道发行（GitHub Release / npm 2.0.6 / Gitee / ClawHub 1.0.7 / About 双端）**。
- **v2.0.5（2026-08-31）**：**路测回流 + 触达强化批次（本地批次，内容已并入 v2.0.6 全渠道发行）**——①**取证命令二次修复**：v2.0.4 裸 `#[0-9]{3}` 分支无法区分细则编号与 GitHub issue 编号（三口径实证：v2.0.3=1 假阴性 / v2.0.4=10 假阳性（9 为 issue 编号）/ 严格=1 且自指，真实语义命中=1）→ 废弃裸编号分支，只认完整前缀形态 `details #NNN` / `细则 #NNN` / `references/details`，details 引用规范同步禁裸编号、injection-core 引用条款同约束；②**前缀自检改每会话触发**（用户拍板）：SKILL §3 第 0 步重写（权威源，含两个合规出口：目录名未知→不猜不阻塞 / 用户拒绝改名→state.md 记录后静默）+ injection-core「开工一行自检」+ memory-anchor 锚点行——三层触达承载；③**「跳过必声明」元规则**（用户拍板）：任何规则/步骤/纪律被跳过（含 L2-S 边界豁免、L1 整体标注）→ 复述 + 记录依据 + 提醒；「跳过 + 声明」合法、静默跳过违规（SKILL §0 + §12 SK 行 + injection-core 主流程门禁）；④**details §15 一轮路测回流 13 条**（#255-267：12 项漏检全收 + 「不复现」判定举证纪律，T5 判据失误实证）+ **§16 二轮路测回流 4 条**（#268-271：chalk level 污染根实例 / 响应体只消费一次 / 配置继承拼接 vs 替换 / 非 TTY 环境查询 undefined——只收通用性强者，终端渲染等绑定领域者不入通用版）；口径 254→271 条 / 14→16 类全仓同步；⑤**负向结论举证升红线**（四要件权威源 SKILL §8 + injection-core 红线 + details #255 交叉引用）——「不复现」举证责任高于「复现」（T5/T9 双失误实证）；⑥**触达机制强化（二轮核心发现「已安装 ≠ 被加载」）**：在场提示/injection-core 首行改「读到即执行 + 缺失即报告」；SKILL §3 注入第五步升可重跑触达验收；高命中细则 TOP 内联进 injection-core 错误段（#233/#214/#163/#256·#270/#262）；description 重构为场景化触发词；**子代理委托纪律包**（rules §28 + skill-usage §0 修正「子代理自扫 L0/L1/L2」错误假设——二轮实证提醒可读仍 0 加载，改为「委托时主代理必须内联最小纪律包」+ SKILL §8/§12 AG + templates/agents 模板）；⑦**有效性诚实声明更新**（§6.6）：纳入二轮（未观察到带规则的正确性优势 + T5/T9 双纠错被无规则轨纠正 + 背答案 7/14 + 8 类零命中/111 条无贡献 + 触达瓶颈；只读作「B 轨未劣于 A 轨」）；§8 易错点 +2（不复现举证 / 子代理纪律直送）；⑧版本 bump 2.0.5 全口径（package.json / README / CHANGELOG / 项目信息 / EVIDENCE §十/§十一）。verify 4/4 PASS。**下一步**：换项目池（zod/vitest/esbuild/prettier/tsx/unbuild）+ 面1·面3 分会话 + 转测触发率，由新会话以本版为基线执行。
- **v2.0.4（2026-08-31）**：**三层承载化 + 取证命令修复（执行批次，已全渠道发行）**——①硬注入升级为「记忆层（每会话在场锚点，首行在场提示）+ 规则层（注入核心全文）+ 配置文件层（§2.1）」三层强制写入，写前提醒用户授权；按需注入只写应用层、询问是否写规则层（不写记忆层）；②新增 §3 步骤 1.5「识别与调研注入点（不猜）」——识别 Agent 平台后联网调研官方注入点再注入；③新增 `templates/memory-anchor.md`（记忆层锚点块，首行「在场提示 · 工作流 Skill 现已在场」）+ platform-adaptation §2.2 平台记忆层；④install-skill.ps1 增 `-MemoryFile`、syncer.py 增 `--memory-target`（记忆层同步，先备份合并）；⑤**取证命令缺陷修复**：状态面 `grep -cE 'references/details|#2[0-9][0-9]\.'` 对 details.md `1.–254.` 有序列表与任务记录 `#228×3` 形态恒 0 假阴性→改为匹配真实引用形态，details.md 补引用规范，EVIDENCE §七「0→有命中」复测校准；⑥本机三层实测注入（WorkBuddy MEMORY.md / Trae user_profile.md / Codex AGENTS.md 注记 + 注入副本 ×4 重部署，均备份 `.bak-20260831-pre-v204`）。verify 4/4 PASS + **全渠道发行**（GitHub Release / npm 2.0.4 / Gitee / ClawHub 1.0.6 / About 双端）。
- **v2.0.3（2026-08-31）**：**前缀自适配 + 平台配置文件层（执行批次，已全渠道发行）**——①新增 `scripts/install-skill.ps1` 一键安装（自动带 `agent-` 前缀、幂等、`-Dry` 干跑 / `-Link` 软链 / `-Force` 备份覆盖 / `-HardInject` 注入配置层，输出「Base directory 判据」验收提示）；②SKILL §3 新增第 0 步「安装名前缀自检」（无前缀一行提示，带前缀静默）；③README 安装话术改「一条命令自动带前缀」，FAQ 前缀条目改述为官方已适配；④platform-adaptation 新增 §2.1 平台配置文件层（Claude Code settings.json hooks / Codex config.toml / Cursor 应用 Rules / Trae 应用设置 / WorkBuddy settings.json+BOOTSTRAP / ZCode AGENTS.md，每平台经实测如实标注——本机 bash 不可用故 hooks 降级、Codex/WorkBuddy 无 hooks 槽位）；⑤SKILL §3 注入点补「硬注入承载面 = 规则文件 + 平台配置文件」；templates/hooks/ 新增多平台说明 README；⑥本机配置层全激活（~/.codex AGENTS.md 由 v1.19.1 重写为 v2.0.3、部署副本 ×2 syncer 同步、注入副本 ×4 重部署，均先备份 `.bak-20260831-pre-v203`）。verify 4/4 PASS。
- **v2.0.2（2026-08-31）**：**审查批次（未发布）**——①审计修复三级同步链断裂：v2.0.1 机制「决策三层分界」（SKILL §5.2）未同步 injection-core.md 判级速查块与三份平台注入副本；强制完整读取「三类例外」仅 workflows.md 落地，skill-usage.md §4 / rules.md §26 仍为 2 类——已补齐并重部署注入副本；②口径清理：README 版本历史补 v2.0.1/v2.0.2 行、仓库结构行（package.json 2.0.2 / details 254 条 14 类 / 速查表 28 行）、reference-sources / scripts-README / EVIDENCE §九（重测注入核心字符数）同步、发布面注记（v2.0.x 未对外发布，v1.19.1 为各渠道最新）；③细节：details §13 标题补 #239 归属、SKILL §11 状态面模板版本号。verify 4/4 PASS；源码已推送 GitHub/Gitee 主线（未独立发布，内容已并入 v2.0.3+ 全渠道发行）。
- **v2.0.1（2026-08-31）**：**个人工作台版差异化并入（用户拍板四项全并；未发布）**——details §14 回流 15 条（#240-254 MCP/视觉/前端测试）+ 机制四项（L1 跳步豁免 / NEVER 三读自检 / 子代理规则 / 决策三层分界）+ 小增量四项（知识点五条细则 / 强制完整读取三类例外 / 顾问措辞 / 默认中文）。
- **v2.0.0（2026-08-30）**：**单版本化重构**——①仓库只维护一份中文版 Skill（`skill/`，frontmatter name=`shisan-xinuo-workflow`），删除英文版与双语版（git 历史可追溯）；②中文版吸收三版全部强项并补齐全部疏漏：三级跑道（L1/L2-S/L2-F + 三问分流）、对接真相清单、§12 速查表（28 行，修复 A4/A5 重复 ID）、§11 会话状态面、§3.1 自更新协议、§4.1 复述增强 RE、新项目 bootstrap、注入核心三级跑道对齐、红线↔必问映射表；「增补节 v1.12-1.19」全部并轨进正文后删除；③门禁修复：verify-release 改为**内容锚点校验**（P1-2，终结「版本对、内容降级仍 5/5 PASS」）；④syncer 修复四项：首次安装必崩（P0-2）、备份外置 `skill-backups/`（WorkBuddy 实测：备份污染平台扫描路径致加载旧版）、死代码清理、dry-run 语义；⑤口径全量同步（README 双语保留 / 项目信息 / CHANGELOG / EVIDENCE / package.json 2.0.0 / About GitHub+Gitee）；⑥细节：details 编号校正 204-238 + 新增 #239（平台加载目录判据，跨平台晋升）、template 补 experience-mustread、新增 `.github/workflows/verify-release.yml`；⑦三级同步链：平台注入副本（~/.zcode/AGENTS.md、~/.trae-cn、~/.workbuddy/AGENTS.md）与部署副本同步至 v2.0.0。
- **v1.19.1**：复核第三方审计 F-1/2/3/5/6 并升版发行——英文细则 #236-238、英文 injection-core 补译、syncer 路径相对化 + 泄漏扫描收敛（无歧义特征、纳入 scripts/）、dist 打包 redesign；全渠道发行（GitHub / npm 1.19.1 / Gitee / ClawHub 1.0.4）。
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

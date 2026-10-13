# Shisan Xinuo Agent Workflow（十三希诺工作流）

> **v4.2.0**（施工中·发行待批 · 上一发行态 v4.1.0 / 2026-10-12）· MIT · 中文为主 · [GitHub 源库](https://github.com/zxc663/shisan-xinuo-workflow)

**一句话定位**：一套把 AI 编码 Agent 的工程纪律做成「按风险选深度、高危先停、完成留证据」的可审计工作流 Skill 家族——它的独特之处不在规则数量，而在于**纪律的验证链本身随仓库公开，任何人都能重跑核对**。

---

## 作者的话

> **「工程化的确定性和稳定性，才是让 AI Agent 从玩具落到实地的真正要点。」**

确定性，是同一套纪律换一个会话、换一个模型、换一个平台仍然复现——所以这里的每条规则都带**触达端口**（注入锚点 / 错误时刻推送 / 预读 TOP），而不是靠"希望模型记得住"；该问的停下来问，该跑的真跑一遍。

稳定性，是不因遗忘、压缩、换人而失效——所以这里的结论必须**可复算**：`GATE` 带真实命令与退出码，判据有版本与金样本回归，高危动作被 L3 停点拦在发生之前。过程对得起复核，结论对得起复算；**做不到的，这里不写进承诺**。

---

## 它解决什么问题

AI 编码 Agent 在真实项目里的七类工程失败，以及本项目对应的机制（全部指向仓库内可查的文件）：

| 失败场景 | 表层表现 | 深层原因 | 对应机制 |
| --- | --- | --- | --- |
| 需求有歧义，Agent 未确认就动手 | 做出来的东西不是用户要的 | 模型倾向于「补全」而不是「承认不知道」 | 每轮复述前置 + 必问协议 + 计划模式必问（`skill/shisan-xinuo-workflow/SKILL.md` §4、§2.6） |
| 为求快省略调查、澄清、验证 | 「我先直接写吧」 | 省 Token 是即时收益，返工是延迟成本 | 开工四步每步有出口产物 + 努力预算下限 + 「省的是仪式不是实质」（SKILL.md §2.0、§0） |
| 方向错了，但局部任务都顺利 | 每步都对，整体白做 | 局部正确性无法抵消方向错误 | 设计确认先于写码 + 回滚点前置 + 纠偏续跑（SKILL.md §2.5、`references/injection-core.md` 设计铁律） |
| 跨会话记忆丢失，重复调查 | 新会话问旧会话早已确认过的问题 | 过程信息没有可靠落点 | 项目根 `memory/agent-log.md` 一档制四区 + 折叠协议保留清单（injection-core.md「memory/ 一档制」、SKILL.md §8） |
| 忽略既有能力，重复造轮子 | 重新实现已有 Skill/组件 | 清单不在注意力里 | 能力检索协议：开工先匹配 Skill/MCP 清单，未命中才自写并留归因（SKILL.md §2.1） |
| 表面完成被当成真完成 | 「做完了」但没跑过、没证据 | 没有把「完成」定义为可复算的检查点 | GATE 一行证据（命令 + 退出码 + 变更文件）+ `gate_audit.py` 外部抽检 + 「循环到绿」收口判据（injection-core.md「交付与留档」段） |
| 流程越加越繁琐，为合规做无意义动作 | 小任务也走全套 | 治理成本没有与任务风险挂钩 | 三级跑道按风险选深度 + Token 精算机 + 压缩级（存在性不可压缩、形态可压缩）（SKILL.md §0、§2.2） |

**为什么这些问题值得专门处理**：它们共享同一个深层原因——**规则在场 ≠ 规则被遵守 ≠ 遵守带来好结果**。这个「三层缺口」的完整论证在 `docs/methodology-rule-verification.md` §0：把规则写进 AGENTS.md 只解决第一层（文本到达上下文）；行为是否遵守需要行为面证据；遵守是否改善结果需要对照实验。大多数规则工程只做第一层，然后宣传第三层的收益。本项目把三层分开处理，并明确标注每层目前的验证状态（见「什么已验证、什么没有」）。

## 核心设计思路

不是「更多规则」，而是四个工程取舍：

1. **按风险选深度**。三级跑道：L1 快速通道（可逆小改，直接做）、L2-S 短工作流（≤3 文件）、L2-F 完整 9 步（大模块/高风险）。判级 10 秒一句话定论，判不了默认 L2——**不为所有任务套全套流程**。
2. **高危动作靠停点，不靠自觉**。L3 封闭清单只有 6 项（密钥/权限、数据删除、数据或服务迁移、对外发布、架构选型、超预算破坏性操作），命中即停、列出命令清单、等用户确认——**清单外一律不是 L3，不得自行扩展**（扩展会让「可测试性」失效）。清单外高危域（CI/CD、DNS、IAM、计费等 11 域）由 `scripts/risk_scan.py` 关键词召回兜底。
3. **「完成」必须是可复跑的证据**。每个任务块收尾一行 GATE：真实命令、真实退出码、变更文件、验证层级。**可重跑工件 > 自我叙述**；收口必须「循环到绿」（exit 0），带红交付必须显式声明。
4. **规则本身是被治理的工程对象**。规则可跳过，但跳过必须声明（复述跳过项 + 留依据 + 提醒用户）；细则双库治理——条款账（`details.md`）零和 405 上限（新增须合并/替换），教训账（`references/lessons.md`）解冻单列、靠生命周期代谢（[域] 适用域标注 + [态] 修复/退役/复活，`v4.2.0` 批迁移施工中，设计档 `docs/design-specs/v420-plan-unfreeze-decouple-privacy-20261013.md`）；全仓数字由 `facts_sync.py` 单源对账；行为判据是代码（`probe_runner.py`，j2.7），改判据必须过金样本回归并留变更记录。

## 关键机制与对应文件

| 机制 | 文件 | 类型（诚实标注） |
| --- | --- | --- |
| 三级跑道 / 判级 / 三模式 / 复述 / 必问协议 | `skill/shisan-xinuo-workflow/SKILL.md` | 提示词自律（模型读指令执行） |
| 常驻最小集（判级速查/红线/GATE 12 字段/开工四步） | `skill/shisan-xinuo-workflow/references/injection-core.md`（6328 字符） | 提示词自律（注入到平台规则文件后每会话在场） |
| 落地细则 405 条 · 33 类（T1/T2/T3 三层按需加载） | `skill/shisan-xinuo-workflow/references/details.md` | 提示词自律 + `scripts/detail_lookup.py` 一键检索（标准库只读工具） |
| 工程纪律 42 条（G0-G8 场景索引） | `skill/shisan-xinuo-workflow/references/rules.md` | 提示词自律 |
| GATE 证据外部审计 | `scripts/gate_audit.py` | **机检端口**（需人/Agent 主动运行；核对文件存在性、git 痕迹、命令复跑、验证层级） |
| 清单外高危域召回 | `scripts/risk_scan.py` | **机检端口**（关键词召回，非判级权威） |
| 跨会话档案（状态/教训/偏好/流水四区） | 项目根 `memory/agent-log.md`（模板 `skill/shisan-xinuo-workflow/templates/agent-log-template.md`） | 提示词自律 + `scripts/agent_log_rotate.py` 机械归档 |
| hooks 纪律包（会话启动提醒 / 工具失败时刻 TOP 推送） | `skill/shisan-xinuo-workflow/templates/hooks/`（**配置示例，非捆绑运行时**） | **平台机制**（依赖 Claude Code/ZCode 等平台的 hooks 支持；WorkBuddy/Codex 待实测） |
| 五平台注入（先备份、合并不覆盖） | `scripts/deploy_injection.py` | 部署脚本（一次性执行） |
| 发行门禁（内容锚点/hooks/版本/泄漏/正文净化/索引/事实对账/判据自测/叙述对账/双副本一致性） | `scripts/verify-release.ps1`（PowerShell）+ `.github/workflows/verify-release.yml`（CI 三 job 公开运行） | 脚本门禁（发行动作前必跑） |
| 判据即代码 + 金样本回归 | `scripts/probe_runner.py` + `docs/roadtest-scorecards/JUDGELOG.md`（j1.0→j2.7 版本史） | 机检端口 |
| 流程分册 9 类 / 审查角色 8 个 / 产品工程门禁 | `skill/shisan-xinuo-flows/`、`skill/shisan-xinuo-roles/`、`skill/shisan-xinuo-product/` | 按需加载的 Skill（独立可装） |

**上面的「类型」列是本 README 最重要的诚实声明**：这套体系的大部分环节仍靠模型阅读指令后自觉执行；机检端口是外部可跑脚本，但需要被主动运行；hooks 提供平台级的自动触达，但受平台支持面限制。它不承诺「规则不可绕过」，它承诺的是「绕过和不绕过都留下可查的痕迹」。

## 一次任务的完整生命周期

以 L2-F 为例，串联各机制：

1. **开工四步**（每步有出口产物，无产物不进下一步）：复述 + 状态行 → 承载检查（自动建 `memory/agent-log.md`、项目规则文件，先备份合并不覆盖）→ 记忆对齐（只读状态段一屏，按症状检索）→ 前置门 + 能力检索 + 判级选道。
2. **选道**：三问分流（跨 ≥3 包？涉契约/架构/迁移/发布/安全？用户点名按流程？≥2 命中走 L2-F）。L3 命中永远 L2-F + 先停。
3. **执行中**：对接真相调研（写码前先 grep 调用点、读 schema，禁命名直觉）→ 复述 → 疑问必问 → 五问审查 + 回滚点 → 规划文档（含可验证验收标准）→ 执行 → 自查归档。
4. **停点**：L3 六项命中即列命令清单、结束回合等确认；普通模式下方向/歧义/风险也必问。
5. **收尾**：最小验证（真实跑一遍，记退出码）→ 完成声明六件套 + 用户验收 → GATE 一行 → agent-log 流水/状态/教训/偏好更新 → 文档代码同批提交。
6. **下一会话**：读状态段一屏对齐，复述接续，按症状检索教训区——不再从头调查。

**哪些环节可能失效**（项目自己记录的边界）：模型可能忽略或误解指令（提示词边界）；无头/非交互环境注入面可能断裂（`docs/design-specs/` 与 CHANGELOG 中有实测记录）；hooks 落盘受平台持久化策略影响；GATE 的「真实退出码」依赖 agent 如实填写，`gate_audit.py` 抽检但不可能全量覆盖。

## 五包结构

| 包 | 定位 | 独立安装 |
| --- | --- | --- |
| `skill/shisan-xinuo-workflow` | 核心：三级跑道 / 判级 / 必问与红线 / GATE / 记忆留档 / 平台注入 | 是 |
| `skill/shisan-xinuo-flows` | 流程包：9 类任务工作流分册 + 7 件模板 | 是 |
| `skill/shisan-xinuo-roles` | 角色包：8 个审查/执行角色（critic/risk-reviewer/security-auditor/debugger/contract/test/frontend/perf） | 是 |
| `skill/shisan-xinuo-product` | 产品工程包（v0.2.7，独立版本线）：交互工程判据与 8 台可重跑门禁——「功能该有的都有」的缺失可检出 | 是 |
| `skill/shisan-xinuo-single` | 单文件蒸馏版：核心全量并入一文件，硬注入形态 | 是 |

`pwsh scripts/install-skill.ps1 -Family` 一次装齐五包。

## 什么已验证、什么没有

先说一句容易被忽略的：**这个仓库的价值不是那 405 条规则本身，而是它的验证链随仓、任何人都能重跑核对**。这是本 README 与同类项目最不同的部分——**验证链本身就是交付物的一部分**。

**可以直接重跑核对的**（clone 后本地执行，均为纯 Python，零 API 成本）：

```bash
python scripts/facts_sync.py --check        # 全仓数字单源对账（405 条/33 类/42 条口径）
python scripts/probe_runner.py --judge-selftest   # 行为判据金样本回归 25/25
python scripts/gate_audit.py --selftest     # GATE 证据审计自测 8/8
python scripts/risk_scan.py --selftest      # 高危域召回自测 4/4
python scripts/narrative_sync.py --selftest # 叙述对账自测 7/7
python -m unittest discover -s tests        # 单元回归 14/14
```

发行门禁 `pwsh scripts/verify-release.ps1`（10 项，需要 PowerShell）由 GitHub Actions 三 job 在每次 push 时公开运行，运行记录在仓库 Actions 页可查。

**部分验证的**：行为面探针（路测 v3.0/v3.1/v4.1 证据与判据版本史随仓，`docs/roadtest-scorecards/`）证明了「系统在作者定义的判据下合规」——这验证的是**遵守**，不是**有用**。

**尚未验证的（如实告知）**：

- **效果对照**：盲评实验（配对设计、外部评审、n≥30）已完整设计并预注册（`docs/design-specs/blind-eval-design.md`），试点 n=6 已执行，正式批**未跑**。README 因此不出现「效果更好/更省返工」类结论。
- **第三方复现**：目前 0 次（`docs/methodology-rule-verification.md` §4 的诚实现状）。
- **与裸 Agent 的 A/B 对照**：本工作流自身声明「规则有效性（对照 A/B）未达显著」（`skill/shisan-xinuo-workflow/SKILL.md` §6）。

**本工作流不宣称正确性优势**。它提供的是：可追溯（每个任务块有可重跑证据）、可审计（机检端口）、防返工机制在位（复述/澄清/回滚点）、点破后恢复机制（纠偏续跑/重载守卫）。如果这些不是你要的，往下看「不适合谁」。

## 与相邻方案的关系

同类项目四分法（完整对标见 `docs/comparison-v290-analysis-20260916.md`，11 个项目、6 维矩阵，随仓可查）：

| 类别 | 代表 | 它们做什么 | 与本项目的关系 |
| --- | --- | --- | --- |
| 方法论框架 | obra/superpowers（≈298k★）、github/spec-kit（≈141k★）、BMAD-METHOD（≈54k★）、Wirasm/PRPs-agentic-eng（≈2.3k★）（星标 2026-10-13 实测） | 把 SDLC 阶段做成强制技能/命令/子代理流水线 | 同层竞品。它们强在流程与生态；本项目重心不同：**停点优先 + 证据可复跑 + 验证链随仓**。superpowers 的评测在独立仓库，本项目判据与金样本随仓且版本化 |
| 规则承载标准 | AGENTS.md 开放标准（Linux Foundation 治理，60k+ 项目采用）、Cursor rules、Kiro steering | 声明式知识文件 + 平台原生加载（四态/条件触发） | **互补而非竞争**：本项目把浓缩纪律写入这些载体，平台负责加载，本项目负责纪律内容与验证 |
| 平台 hooks 与记忆工具 | Claude Code hooks、claude-mem 类记忆系统 | 事件触发的自动注入/记忆持久化 | 互补：本项目提供 hooks 纪律包模板（SessionStart 提醒 + 失败时刻 TOP 推送）与文件态记忆方案，但不做数据库/向量记忆 |
| 企业治理平台 | Microsoft/平台级方案 | 身份认证、策略引擎、平台审计 | 不可比：本项目无这些，是提示词层的一层纪律，换来可测试、可复算 |

**如实说明**：以上任一类别都有成熟方案，本项目没有单点「市场空白」。它相对明确的特点有三个：①**中文原生**（同类主流方案均为英文）；②**把「怎么验证一条纪律有用」做成了随仓可复跑的工件**（判据版本化、金样本回归、逃逸分析回流、反向变异自测——方法论独立成文 `docs/methodology-rule-verification.md`）；③**治理代价有界且可审计**（注入核心 6328 字符常驻、细则按症状检索、零和上限），并把「主张说小、证据说满」作为自身纪律。

## 安装与上手

```bash
# 任选其一
npx skills add zxc663/shisan-xinuo-workflow                # skills.sh 索引
openclaw skills install @zxc663/shisan-xinuo-workflow     # ClawHub 技能市场
git clone https://github.com/zxc663/shisan-xinuo-workflow # 源库（含全部验证脚本）
pwsh scripts/install-skill.ps1 -Family                    # 源库内：五包一次装齐（需 PowerShell）
```

npm 通道 `npm install @zxc663/shisan-xinuo-workflow` 为 GitHub Packages 私有可见性，读取需 PAT；npmjs.org 未分发。

**装完三步验证**：

1. **自检**：重开新会话（注入版本=会话创建时快照），输入 `zxc663`——应答应包含注入方式、源库 vs 副本版本、Base directory。
2. **观察三个标志物**：每轮首产物=复述（收到 X｜理解为 Y｜边界 Z）+ 状态行；关键决策先问（密钥/删除/迁移/发布/架构/超预算六类必停）；任务块末尾有 GATE 单行。
3. **只取四件套**（不想整套采用）：L3 封闭清单必问 + GATE 一行证据 + 跳过必声明 + 循环到绿——四条理念可直接贴进你自己的 AGENTS.md，零依赖本仓库基建。成文版见 `docs/quickstart-10min.md` §6。

## 适合谁，不适合谁

**适合**：

- 用 AI Agent 做真实工程任务（多文件、跨模块、要发布要迁移）的个人开发者，想要「停点 + 证据」纪律且能接受中文规则体系。
- 研究「怎么验证一条 agent 规则真的有用」的人——`docs/methodology-rule-verification.md` 与 `docs/roadtest-scorecards/JUDGELOG.md` 可独立复用。
- 想借鉴「按风险选深度」设计而不想全盘采用的人（四件套 + 三级跑道）。

**不适合**：

- 想整套照搬的多人团队——405 条细则的同步与维护成本在多人协作下不现实（项目自身 README 与 docs 均如此声明）。
- 需要平台级强制（身份认证、策略引擎、不可绕过的权限拦截）的场景——那是平台能力层，本项目是提示词层。
- 纯聊天问答、单文件只读查询——本项目明确排除（SKILL.md §1）。
- 期望「装上就自动变好」的用户——效果未经对照实验验证，且触达（注入/hooks）本身需要按平台配置。

## 成本与已知局限

- **上下文成本**：注入核心常驻 6328 字符（约 5-7K token）；细则按症状检索，单次 1-3K。窗口越小的模型，收益/成本比越需权衡。
- **提示词边界**：无论如何注入，终究是提示词范畴；模型可能忽略、误解或错误执行规则。没有平台级「新会话自动加载」的机制保证。
- **平台方差**：无头模式注入面可能断裂；hooks 支持面不一（Claude Code/ZCode 实测支持，WorkBuddy/Codex 待实测，Trae/Cursor/Windsurf 视版本）。这些断裂项目自身会如实报告（CHANGELOG 有记录）。
- **维护成本**：细则与多平台副本需要同步（`syncer.py` 三路合并）；条款账零和上限（405 为上限，新增须合并/替换旧条；教训账解冻单列、生命周期代谢，`v4.2.0` 双库改造施工中）；判据冻结于 j2.7。
- **效果未证**：如「什么已验证」一节所述，不宣称正确性/返工率优势。

## 版本与状态

- **当前**：v4.2.0（施工中·发行待批）——细则双库解冻（条款账零和 405 条 + 教训账解冻不占 405）+ 教训域/态字段与生命周期协议 + 开源隐私门（四层扫描，门禁 11 项 A-K）+ 时间戳强制场景 + 代拟用户言论词表机检面；判据 j2.7（金样本 25/25）；细则 405 条/33 类；教训账 0 条（合法初态）。上一发行态 v4.1.0（2026-10-12）。
- **发行渠道**：GitHub（源库 + Release）、Gitee 镜像（同 commit/tag 双推）、npm（GitHub Packages，私有）、ClawHub、skills.sh。
- **规模**：本地 563 commits、53 个版本标签；**远端状态以 README 沿革节与 CHANGELOG 记载为准**（历史身份清洗后本地与远端全分叉，force push 待批——远端仍停在上一发行态）。完整历史见 CHANGELOG.md。

## 贡献与反馈

最有价值的反馈是**摩擦报告**：装不上在哪一步？看不懂哪一句？嫌重在哪一段？——通过 GitHub issue（bug/feature 模板齐备）或直接联系作者。开发流程见 CONTRIBUTING.md；发行操作见 RELEASE-CHECKLIST.md；安全披露见 SECURITY.md。许可：MIT。

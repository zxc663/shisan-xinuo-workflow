# 两仓清洗 + 重定位执行计划（母仓 shisan-xinuo-workflow + 产品仓 product-engineering-skill）

> 令源：2026-10-11 用户令「按最优解来，README 那个英文仓库需要重写，……这两个仓库都要重新写说明和定位标签等等，先做计划」+ 追加令「计划落地成详细可执行的具体文档」。
> 性质：执行计划档——批准后按批次施工，本档随批次 A 首个 commit 入库。
> 清洗方式=**方式①删 HEAD 保 git 历史**（方式②filter-repo 历史重写强推=被否候选：破坏性另批）。
> **批准语义**：批准本档=授权批次 A/B/C 全部本地施工；**批次 D（push+远端元数据写入）属对外发布域，需单独口令**（本仓底线）。
> **优先级定版（2026-10-11 用户令）**：产品工程验证与推进=最高优先级（P0，载体=博客 D:\q，授权部署/修改/发布/优化全开）；本档两仓批=P1；延后路测计划恢复排程=P2——总排程见 §8。
> 承载根：母仓 `D:\Agent工作流启动包\shisan-xinuo-workflow`；产品仓 `C:\Users\zxc66\Desktop\产品工程Skill`。

## 0. 目标定位（定版）

- **母仓**=十三希诺 Agent 工作流家族·**中文源库**：对外核心=skill/ 四包+scripts/ 机检+README/CHANGELOG；docs/=**明示开发工作区**（README 新增声明），只保留活跃档+机检锚定件+对外导读，实验原始数据不入工作树（git 历史可溯+本机备份）。
- **产品仓**=独立英文产品工程 Skill（clean-room 发行版）。**权威方向=母仓中文源 → 英文仓单向发行**；版本线独立（英文 1.x／母仓 0.2.x），机制等价、措辞可分叉；同步策略写进两仓 README+英文仓 AGENTS.md。
- 互链：英文仓→母仓（已有保留强化）；母仓→英文仓（现仅 README L81 一处，升级为规范互链句）。

## 1. 事实基线（2026-10-11 实测，命令读回）

### 1.1 指针与同步差

| 面 | 指针 | 说明 |
|---|---|---|
| 母仓本地 HEAD | `27a0229` | 工作树干净 |
| 母仓 GitHub `origin/main` | 落后本地 **6** commit | `git rev-list --count origin/main..HEAD` 实测 |
| 母仓 Gitee `gitee/main` | 落后本地 **29** commit | 同上；**修正上轮「差 8」误记**（陈旧 ref 所致） |
| 产品仓本地=origin | `41cc84c` | 同步；untracked=`.gitattributes`（3 行）待补提 |

### 1.2 母仓混入面（tracked 715 件，docs/=582 件为混入主体）

| 目录/面 | 件数 | 处置 |
|---|---|---|
| docs/archive | 139（含 3 PNG ~930KB） | **删**（B 档：外移备份后删） |
| docs/roadtest-scorecards | 137（含 2×1.16MB jsonl 原始数据） | **删 117 保 20**：`evidence/` 金样本 20 件 109K 保留（verify H 判据回归依赖，`probe_runner.py:683-736,825` GOLD 硬指向） |
| docs/field-trials | 132 | **删**（A 档） |
| docs/blind-exec-pilot-20260930 | 75 | **删**（A 档） |
| docs/reverse-injection-gates-20260929 | 19 | **删**（A 档） |
| docs/riskscan-measure-20260929 | 5 | **删**（A 档） |
| docs/mining-dedupe-20260929 | 3 | **删**（A 档） |
| docs/design-specs | 24 | **删 21 保 3**（保：v410-batch-manifest / v410-p-line-argumentation / benchmark-refresh-20260929 对标底料；+本计划档新增） |
| docs/ 根面 | 47 | **删 41 保 6**（保：project-info / reference-sources / quickstart-10min / methodology-rule-verification / comparison-v290-analysis / transformation-plan——前两者 facts CARRIERS 硬依赖，后四者 README 引用或活跃治理档） |
| docs/incidents | 1 | 保留（README 引用，体量可忽略） |
| 根面 EVIDENCE.md | 172KB | **删**（B 档：外移备份后删；决策史权威=项目信息.md） |
| 根面 RELEASE-CHECKLIST.md / 项目信息.md / AGENTS.md | — | **保留**（发行操作件+决策史权威+项目注入，均有机检挂靠） |

**合计：删 552 件（tracked 715→163），docs/ 582→30；仓库瘦身约 8MB。**

### 1.3 机检锚清单（施工不可碰区）

| 锚 | 位置 | 约束 |
|---|---|---|
| README 标题前缀 | `verify-release.ps1:109` | L1 必须以 `# Shisan Xinuo Agent Workflow（十三希诺 · 纪律元工作流）` 开头 |
| README 条数句 | `facts_sync.py:56` | 保留一句匹配 `不是那 (?P<n>\d+) 条规则` 且 n=405（现 L142） |
| facts CARRIERS | `facts_sync.py:63-70` | `docs/reference-sources.md`+`docs/project-info.md` 不可删（删则 G 项崩）——已列保留 |
| verify C 子项 | `verify-release.ps1:150-152` | 同上读 reference-sources 版本行——已列保留 |
| judge 金样本 | `probe_runner.py:683-736,825,891` | `docs/roadtest-scorecards/evidence/` 不可删——已列保留 |
| build-dist $roots | `build-dist.ps1:11` | EVIDENCE.md 删除后**必须**从 $roots 移除（唯一必改机检位） |
| AGENTS.md 条数锚 | `facts_sync.py:62` | `细则 **405 条·33 类**` 句形态不可变 |
| verify D 豁免正则 | `verify-release.ps1:168` | 含过期路径=无害排除项，**不动**（防误伤 evidence/ 子树） |

### 1.4 两仓远端元数据现状（过期实证，读回于 2026-10-11）

- 母仓 GitHub/Gitee description 均为 v4.0.0 时代旧口径：「406 条 33 类」「j2.5+金样本 23/23」——现状应为 **405/33·j2.7·25/25**；Gitee keywords=空。
- 母仓 GitHub topics 已有 15 个（可用，微补）。
- 产品仓 GitHub description=「design lab」旧定位；**topics=空**；homepage=空。

## 2. 批次 A：母仓清洗（先行——README 死链修复依赖本批结果）

### 2.0 依赖面全扫（删前安全网）

```bash
grep -rnE "docs/(archive|field-trials|blind-exec-pilot[^/]*|reverse-injection[^/]*|riskscan-measure[^/]*|mining-dedupe[^/]*|release-notes|roadtest-v|roadtest-loop|version-plan|skill-split|EVIDENCE\.md)" scripts/ skill/ *.md docs/project-info.md docs/reference-sources.md
```
命中逐条处置（改指针或该件改列保留）；**已知必改=build-dist.ps1 $roots（EVIDENCE.md）**；灰区件（如 project-doctrine-20261010.md 若被保留件引用）按扫描结果定去留。

### 2.1 外移备份（先行）

备份根=`D:\Agent工作流启动包\repo-archive-20261011\`（母仓同级目录，镜像 docs/ 结构）：
copy 全部待删件（552 件）+ EVIDENCE.md → **553 件核对**（`robocopy /MIR` 按清单或逐目录 cp+计数）。

### 2.2 删除清单（git rm，四组）

> 用户 2026-10-11 追加令拍板：**清洗 A/B/C 三档全做**（「123 都要」），本节删除清单按全量执行。

```bash
# 组1 实验原始数据（373 件）
git rm -r -q docs/archive docs/field-trials docs/blind-exec-pilot-20260930 \
  docs/reverse-injection-gates-20260929 docs/riskscan-measure-20260929 docs/mining-dedupe-20260929
# 组2 roadtest-scorecards 保留 evidence/（删 117 件）
find docs/roadtest-scorecards -mindepth 1 -maxdepth 1 ! -name evidence -exec git rm -r -q {} +
# 组3 design-specs 21 件（保 3：v410-batch-manifest-20261010 / v410-p-line-argumentation-20261011 / benchmark-refresh-20260929）
# 组4 docs 根面 41 件（保 6，见 §1.2；release-notes-*.md ×7 全删——CHANGELOG 为权威，Release 正文已在 Releases 页）
```
（组 3/4 逐件名单按 `git ls-files` 差集生成后执行；执行回执在 agent-log 记件数。）

### 2.3 联动机检修改（最小面）

1. `build-dist.ps1:11` $roots 去 `EVIDENCE.md`（唯一必改）。
2. 其余机检**一律不动**（§1.3 已论证：CARRIERS/GOLD/narrative 所指全保留；D 豁免正则不动）。

### 2.4 门禁复跑

`python scripts/facts_sync.py --check`（405/33 PASS）→ `scripts/verify-release.ps1`（**10/10 ALL PASS**）→ judge_selftest（25/25）→ narrative_sync（exit 0）。dist 若因源面变化红 → 按既有四步定式重打（发行终版重打仍留 Phase 9）。

### 2.5 commit

`docs(repo): 两仓清洗批——实验原始数据 552 件出树（git 历史可溯）+本机归档备份+build-dist 联动`（含本计划档入库）。

## 3. 批次 B：母仓说明与定位重写

### 3.1 README 手术式重写（257 行；硬锚 §1.3 两条保全）

| 节（现行行号） | 处置 | 要点 |
|---|---|---|
| L1 标题 | **保留原文** | verify A 硬锚 |
| L3-L5 版本行+定位句 | 重写定位句 | tagline 候选：「把 AI agent 的工程纪律做成可机检的门禁，而不是靠自觉。」版本行保留「v4.1.0 施工中·发行待批」 |
| L19-37 这是什么，不是什么 | 微调 | **保留「不是那 405 条规则」句**（facts 硬锚②） |
| L57-68 与同类项目的分别 | 对标表联网刷新 | 见 3.2 |
| L72-105 四包体系 | 保留；L81 互链升级 | 规范句：独立英文发行版=[product-engineering-skill](https://github.com/zxc663/product-engineering-skill)（中文源=本仓 skill/shisan-xinuo-product） |
| L122-138 验证与证据 | 重写 | 去 EVIDENCE.md 引用（L130/133）；改述=门禁自证（verify 10 项+金样本 25/25）+「实验原始数据已归档（git 历史+本机备份），不在工作树」声明 |
| L140-175 值得读的记录 | 大改（死链修复） | 映射：incidents 保留｜roadtest-scorecards→改指 evidence/ 金样本一句｜field-trials/reverse-injection/riskscan 行删（git 历史可溯）｜对标/DeepSWE/对外反馈保留 |
| L178-186 分发渠道表 | 保留 v4.0.0 已发行口径 | 升级 v4.1.0 留 Phase 9 |
| L241-248 版本历史 | 修漂移 | L248「v1.9 → v4.0.0，39 个版本」→按 CHANGELOG 实况（v4.1.0） |
| L252-257 来源与许可 | 改 | L255 EVIDENCE.md 链接→项目信息.md；docs 描述改「开发工作区」口径 |
| **新增「仓库结构」节** | 新 | skill/ 四包+scripts/ 机检+docs/（活跃档·金样本·导读）+**开发工作区明示** |

### 3.2 对标参照节联网刷新（已授权件并入）

底料=docs/comparison-v290-analysis-20260916.md+benchmark-refresh-20260929.md+三层定位档；联网重采星标/工具数时效数据；表述守 README 三原则（定位严谨/证据确凿/说明中立）。

### 3.3 CHANGELOG + 根 AGENTS.md 校准

- CHANGELOG v4.1.0 段增一行：清洗+重定位批记录。
- 根 AGENTS.md 基线行 v4.0.0→v4.1.0（施工完·发行待批）；**保留 `细则 **405 条·33 类**` 锚句形态**。

### 3.4 远端元数据候选文案（定版随本档批准，写入留批次 D）

- **GitHub description**：`十三希诺 Agent 工作流 · 中文源库：把工程纪律做成可机检门禁的元工作流 Skill 家族——三级跑道／判级／GATE 12 字段可复跑证据／405 条细则库／角色·流程·产品工程四包，五平台注入适配。docs/ 为开发工作区，实验数据已归档。English edition → product-engineering-skill`
- **topics**：现有 15 个保留，试加 `quality-gates`、`agent-workflow`（gh 校验存在才加）。
- **Gitee 描述**=同 GitHub 中文主体；**keywords**=`AI代理,Agent工作流,工程纪律,质量门禁,技能包,Claude Code`。

### 3.5 commit

`docs(readme): 母仓定位重写——开发工作区明示+死链修复+对标刷新+元数据定版`

## 4. 批次 C：产品仓 README 重写与同步

### 4.1 README.md / README.zh.md 重写（61→约 100 行，双语 1:1 镜像）

目标结构：①语言切换行（保留）②H1+定位段（现 L5 句为基收紧）③**Why**（新节：agent 交付「像产品的 demo」、产品判断不可验证→本包把它转成可机检门禁）④What it checks（9 脚本表**保留**——信息密度高且与脚本一致）⑤Install（`npx skills add zxc663/product-engineering-skill` 保留）⑥Run（3 例+`--selftest`）⑦How it works（layer gate→six questions→statechart→gates 四步链）⑧**Honest limits**（5 条保留+增 provenance 行：clean-room English edition of the Chinese source `shisan-xinuo-product`；版本线独立；同步策略指 AGENTS.md）⑨Contributing（保留）⑩License。约束：不引用不存在文件；保留母仓链接。

### 4.2 已知 bug 修复

SKILL.md L54 §5 标题反引号误写为 `"`（`references/anti-excuses.md" ` 引用未闭合）——一字修复。

### 4.3 spec-trace-gate.py 分叉回移

母仓 229 行（10-11 更新）vs 英文仓 202 行（9-30），~3KB 未回移。步骤：①行为面 diff（去注释/docstring 后比较）②分歧逐条判定：行为差=回移、纯措辞差=记录 ③回移后**双仓 `--selftest` 全绿** ④止损帽：行为分歧 >5 处或语义冲突→降级「注明分叉点」（AGENTS.md 允许），README provenance 写明 sync point=41cc84c+本次回移。

### 4.4 补提与同步策略

`.gitattributes`（3 行：`* text=auto eol=lf`/`*.png binary`/`*.ico binary`）add+commit；AGENTS.md 增一行同步策略（权威方向+sync point）。

### 4.5 commit ×2 与远端元数据候选

- commit① `fix: port spec-trace-gate changes from source + SKILL.md quote + .gitattributes`
- commit② `docs: rewrite README (EN/zh) — positioning, why, provenance`
- **GitHub description**：`Turn "build me a X page / tool / app" into decidable contracts — a layer gate, six product questions, a statechart, and nine self-testing gate scripts for AI coding agents. English edition of the Chinese source package shisan-xinuo-product.`
- **topics**（10）：`ai-agents` `agent-skills` `product-management` `spec-driven-development` `quality-gates` `acceptance-testing` `frontend` `accessibility` `claude-code` `llm-tools`

## 5. 批次 D：推送与远端元数据（批准域——需单独口令）

1. 母仓 `git push origin main`（补 6）+ `git push gitee main`（补 29）。
2. 产品仓 `git push origin main`。
3. 元数据写入：`gh repo edit` ×2（description/topics）；Gitee `PATCH /api/v5/repos/zxc663/shisan-xinuo-workflow`（credential fill 非交互取令牌，令牌不回显）。
4. 读回核验：`git ls-remote` 双仓三远端=本地 HEAD；gh api+Gitee API 读回与定版文案逐一比对。

## 6. 验收门禁与回滚

- **母仓**：facts PASS(405/33)｜verify-release 10/10｜judge_selftest 25/25｜narrative exit 0｜死链扫描（README/AGENTS/保留 docs 中 `docs/` 引用全部存在于 tracked 面）。
- **产品仓**：9 scripts `--selftest` 全绿｜README 链接面核对｜双语镜像 diff 结构一致。
- **批次 D 后**：三远端指针+元数据读回一致。
- **回滚基线**：母仓 `27a0229`／产品仓 `41cc84c`；删除件 git 历史全程可溯+本机备份 `repo-archive-20261011\`（553 件）。

## 7. 排程与依赖

- 顺序：**A→B→C→汇报→D（口令）**（B 的死链修复依赖 A；C 独立可穿插）；每批次独立 commit+GATE。
- 与 Phase 9 关系：渠道表保持 v4.0.0 已发行口径，升级 v4.1.0 留 Phase 9；发行物（dist/npm/Release）本批不动。
- 两待问授权件：对标刷新并入 3.2（本批）；提问算子+漏斗模板=独立包改造不属本批（维持 Phase 9 发行前排程）。
- 被否候选：方式②历史重写强推（破坏性）；两仓双向权威（中英分叉风险）。

## 8. 总排程与优先级定版（2026-10-11 用户令）

**定调：产品工程验证和推进=最高优先级（P0）。**

### 8.1 P0 产品工程验证与推进（最高优先级）

- 载体=博客项目 D:\q（四端 monorepo）。**授权升级（用户 2026-10-11 明示，持久有效）**：允许**部署、修改、发布、优化**等操作——从「试金石只读」升为产品工程验证与推进的主载体；该授权覆盖博客仓常规发版动作（重大不可逆/涉密仍按红线）。
- 在飞/待开窗件：P 线论证线 D 臂续轮；A/B/C 臂补窗（预注册框架在档 v410-p-line-argumentation-20261011.md §0，待开窗令）；产品包 v0.2.7 发行；博客 R2 发版（授权已开，按渠道执行）。
- 平板长跑验证=另一会话接管，本会话不触碰（前令持续有效）。

### 8.2 P1 两仓清洗+重定位（本档批次 A-D）

- 顺序 A→B→C→（汇报）→D（口令）；清洗三档全做已拍板（§2.2 注记）。

### 8.3 P2 延后路测计划（恢复排程，2026-10-11 用户令）

原 10-11「盲跑延后」注记解除，恢复排程（排在两仓批后或与 P0 低冲突穿插——盲评需无头窗口与 provider 配额，避免与 P0 并发抢配额）：
1. T6-r3 盲评双针重试（env-death 下窗判别设计已预注册）；
2. A 臂载体移除实验（SOP §三+回位断言在案，仍待用户明示 go）；
3. 独立模型评审针；
4. 五指标全量提取；
5. 试点报告+EVIDENCE 收口。

### 8.4 P3 其他排程

- Phase 9 发行批准门（v4.1.0 五渠道+定位句拍板）——维持待批；
- 两待问授权件：对标刷新（已并入批次 B）；提问算子+漏斗模板（Phase 9 发行前交用户过目）；
- 两待起草计划：dsh 插件化（前置=规范调研）；宣传视频（前置=Phase 9 定位句拍板）。

### 8.5 穿插与冲突规则

- P0 随时可插队；P1 批次 A-C 为本地施工可中断续跑；P2 需整窗（provider 配额）；P3 全部等各自前置。

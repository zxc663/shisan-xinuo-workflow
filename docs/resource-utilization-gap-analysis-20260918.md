# 资源利用率缺口分析（Skill + MCP · 2026-09-18 落档 · 状态：调研留档，配置零改动，计划待用户令）

> 任务：用户手动下发新会话任务后发现「资源利用率极低——Skill 与 MCP 都是」。本档=缺口定量 + 问答归因 + 本地/联网双调研，**不做计划**（计划等用户明确下令）。
> 证据源：`~/.zcode/cli/db/db.sqlite`（session 443 / tool_usage 34,654 / model_usage 29,254，窗口 2026-08-28→09-18 共 21 天，副本只读查询）+ 三目录 Skill frontmatter 扫描 + `config.json`/`mcp-disabled-20260917.json` 只读解析 + 联网四源（Anthropic×3 / Cloudflare×1）。
> 先例回指：`docs/mcp-trim-plan-20260917.md`（09-17 裁剪基于**面板占比**口径；本档补**真实调用量**口径，并闭环其「待重启验收」项）。

## 0. 一句话结论

**83% 的主会话从未调用过任何 MCP 工具，却每会话常驻 44 个工具 schema + ≈18K token 注入件 + ≈6-8K token Skill 清单；66% 的已装 Skill 21 天零调用。** 09-17 MCP 裁剪已把常驻体积腰斩（avg 77K→33K，验收闭环），但「全局常驻、按需不用」的结构性缺口仍在，且裁剪只做了用户级 server 一层，插件面/Skill 面/记忆索引面未动。

## 1. 常驻资源清单（本会话实测现状）

| 面条目 | 数量 | 常驻成本（估算） | 备注 |
|---|---|---|---|
| MCP 工具（本会话可见） | **44 个** | schema ≈10-15K tok | computer-use 30 + glm_vision 6 + node_repl 3 + context7 2 + web_reader 1 + image_search 1 + token_usage 1 |
| 全局 MCP server（config） | 4 | — | codex / token-usage / glm_vision / context7；其余经插件进入 |
| 插件 MCP（重型） | computer-use、browser-use(node_repl)、document-skills(image_search)、web-reader | computer-use 单家 30 工具 | 09-17 裁剪未覆盖插件面 |
| Skill 列示 | 54 列示 / **44 去重** | ≈22.4K 字符 ≈**6-8K tok** | `.agents` 14 + `.zcode` 6 + 插件 skills 若干 |
| 全局 AGENTS.md（硬注入核心） | 1 | ≈**9.1K tok** | 8,163 字符（中文 4,637，按 1.75 tok/字） |
| 工作区 AGENTS.md | 1 | ≈1.9K tok | |
| auto-memory MEMORY.md 索引 | 1 | ≈**6.8K tok** | 9,127 字符，索引行越写越长 |
| **常驻合计（首请求实测）** | — | **avg 33K / med 24K**（09-18） | =系统提示+注入件+Skill 清单+MCP schema+首条消息 |

**重复列示（Skill 面）**：10 组同名——3 组用户级**真双列**（anti-ui-slop 784 / scrollcraft 1120 / ui-ux-pro-max 497 字符 desc，`.agents` 与 `.zcode` 两目录并存→系统提示双份列示）；7 组为插件双版本盘存（平台只列最新，无害）。真双列浪费 ≈1.3K tok/会话。

## 2. 常驻体积演变（09-17 裁剪验收闭环 ✔）

每会话首个模型请求的 input+cache_read+cache_creation（主会话，db 实测）：

| 日期 | n | avg | med | max |
|---|---|---|---|---|
| 08-29（基线期） | 4 | 27,337 | 49,055 | 59,822 |
| 09-13 | 28 | 67,015 | 65,173 | 101,058 |
| 09-16（裁剪前峰值） | 35 | **77,041** | 68,940 | **176,626** |
| 09-17（裁剪当日） | 21 | 63,964 | 65,813 | 83,499 |
| **09-18（裁剪+重启后）** | 74 | **33,381** | **24,110** | 84,870 |

**结论：裁剪+重启生效，常驻腰斩（77K→33K，med 24K），回到接近 08-29 基线水平。** `mcp-trim-plan-20260917.md` §六验收第 1/2 条以本表代答（面板对照可后续补）。

## 3. 利用率实测（缺口核心证据）

### 3.1 MCP：会话渗透率与调用结构

| 指标 | 数值 | 含义 |
|---|---|---|
| 用过任意 MCP 的主会话 | **55/318（17%）**；近 14 天 50/306（16%） | **83-84% 主会话零 MCP 却全额付 schema 常驻** |
| 调用结构 | 内置四件套（Bash/Edit/Read/Write）=85%；MCP 全部=8%；其余=7% | 干活主力是内置工具 |
| MCP 内部集中度 | computer-use+node_repl 占 MCP 调用 **92%** | 其余 server 近乎空转 |

### 3.2 MCP：单 server 账目（21 天全窗口）

| server | 调用 | 会话渗透 | 裁剪状态 |
|---|---|---|---|
| computer-use（30 工具） | 1,815 | 17 会话（**5%**） | 常驻（09-17 D 档「留用户拍板」仍未拍板） |
| node_repl（3） | 964 | 23（6%） | 常驻（browser-use 插件） |
| browser360 | 100 | 1（0.3%） | 已裁 ✔（数据支持裁决） |
| playwright | 55 | 3 | 已裁 ✔ |
| reactbits | 23 | 5 | 已裁 ✔ |
| firecrawl | 10 | 3 | 已裁 ✔ |
| github_mcp | 9 | 2 | 已裁 ✔ |
| **glm_vision（6 工具）** | **6** | 4（1.2%） | **常驻**（09-17 A 档「高频」判定与数据不符） |
| **context7（2）** | **6** | 1（0.3%） | **常驻**（同上） |
| codex（1） | 1 | 1 | 常驻 |
| **web_reader（1）** | **0** | **0** | **常驻，21 天零调用** |
| **image_search（1）** | **0** | **0** | **常驻，21 天零调用** |

- computer-use 30 工具中 14 天仅 17 个被调用过，**13 个自安装起零调用**（含 list_displays/mouse_move/hold_key/left_click_drag 等长尾）。
- document-skills 插件的 docx/pdf/pptx/xlsx 技能 + search_image：**全部 0 调用**。

### 3.3 Skill：44 条目，15 条被摸过

- Skill 工具调用 165 次 / 135 会话，但其中 **shisan-xinuo-workflow 自身 ≈104 次**（约半数是 3.0 loop 探针夹具的自加载）；**有机调用 ≈61 次 / 21 天 ≈3 次/天**。
- 去重 44 条目中**仅 ~15 条被调过（34%）**；**29 条（66%）21 天零调用**，含整族零调用：github:×13、document-skills ×4（docx/pdf/pptx/xlsx）、skill-creator、scrollcraft×2、theme-factory、web-artifacts-builder、web-design-guidelines、vercel-react-best-practices、animate、ask-sonner 等。
- 被调过的Top：control-browser 22、ui-ux-pro-max 7、impeccable 6、zcode-configuration-guide 4、frontend-design 4、diagnosing-mcp 3、computer-use 3。

### 3.4 token 经济（量级框定）

- 21 天模型请求 29,254 次；**input（无缓存重发）7.36B + cache_read 7.18B**（无缓存占 prompt 流量 **50%**）；output 22.7M。
- 常驻注入面重发估算：29K 请求 × 33-77K 常驻 ≈ **1.0-2.2B input token 量级来自「每请求重发的注入面」**（粗估，含会话早轮差异，不作严格归因）——与 09-17 档「4 天 +24.4 亿」的面板口径同量级互证。

## 4. 问答归因（为什么会这样）

**Q1 利用率低的根因是「装太多」还是「用太少」？**
两者叠加，但结构性主因是**「全局常驻」连接模型**：所有 server/插件/Skill 一律全局启用、每会话全量常驻，而真实任务只在特定项目/轮次需要其中一小片（MCP 渗透 16-17%）。09-17 裁剪已经证明「按需收紧」立竿见影（腰斩），但只做了用户级 server 一层。

**Q2 为什么不学 Claude Code 的 Tool Search（按需发现工具）？**
那是平台能力，ZCode 当前无此机制（无 defer_loading 类配置面），**结构性方案在本平台不可行**，只能走「配置面裁剪+项目级迁移」。见 §5。

**Q3 Skill 侧不是本来就有渐进披露吗？**
是——Agent Skills 设计就是「元数据常驻、正文按需」（Anthropic 官方机制），所以 66% 零调用 Skill 的代价**只是清单行**（≈6-8K tok），不是全文加载。代价存在但量级远小于 MCP schema。真正的浪费是：3 对真双列 + 全量铺开偏好下无退出机制（零调用不回收）。

**Q4 MEMORY.md 为什么也算缺口？**
auto-memory 索引每会话常驻 ≈6.8K tok，且行均 hook 越写越长；它是「每会话都付、低频才用」的同一结构问题在记忆面的投影。

**Q5 09-17 裁剪后还有多少可裁空间？**
按本档数据估算：web_reader/image_search/零调用长尾 + glm_vision/context7/codex 项目级化 + computer-use 拍板 + Skill 双列去重 + MEMORY 瘦身，常驻还有 **≈8-15K tok/会话** 的收敛空间（占当前 33K 的 1/4-1/2，估算待计划核实）。

## 5. 联网调研：业界成熟方案

| 方案 | 机制 | 数字（原文） | 对本环境适用性 |
|---|---|---|---|
| **Anthropic Tool Search Tool**（[advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)） | 工具标 `defer_loading: true`，常驻只留 ~500 tok 搜索工具，按需展开 3-5 个；支持按 server 整体延迟 | 77K→8.7K（**-85%**）；极端案例定义吃 134K；Opus 4 准确率 49%→74%；适用阈值：定义 >10K tok / 10+ 工具 / 多 server | **平台不支持→不可行**；但「阈值判据」可借来做治理规则（多少工具以上才值得常驻） |
| **Anthropic Programmatic Tool Calling / Code Execution with MCP**（[code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp)） | 工具定义转代码 API 按需读；中间结果留在沙箱不进上下文 | 150K→2K（**-98.7%**）；PTC 43.6K→27.3K（-37%）；Tool Use Examples 准确率 72%→90% | 本平台有 node_repl 沙箱底子，但无工具-代码自动桥→**远期观察项** |
| **Cloudflare Code Mode**（[blog.cloudflare.com/code-mode](https://blog.cloudflare.com/code-mode/)） | MCP schema→带 doc 的 TypeScript API，模型写代码调用，V8 isolate 沙箱 | 定性收益（原文无 % 数字）：链式调用只回传最终结果；isolate 毫秒级启动 | 同上，方向验证 |
| **Agent Skills 渐进披露**（[agent-skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)） | 三层：元数据常驻→SKILL.md 按需→附带文件再按需 | 无具体 token 数；「skill 可承载上下文实际不受限」 | **已在用**——Skill 面问题只剩清单行与重复治理 |
| 社区实践（网关过滤/动态发现/RAG 工具路由；检索综述，未逐源核验） | gateway 白名单、meta-tool 检索、描述嵌入 top-k | 研究称工具数过 20-30 后准确率可见下降 | 思路可用于「治理规则」：按渗透率/零调用天数定退出线 |

**对照缺口**：业界已把「全量常驻」判定为反模式并给出 -85%~-98% 的机制级方案；ZCode 平台无同机制 → 本环境可行的收敛路径=**配置面（项目级迁移/停用）+ 治理规则（零调用退出线）**，与 09-17 档「按项目/按任务启用」B/D 档思路一致，本档用调用数据把该思路补上了证据。

## 6. 缺口→处置映射（只列映射，不做计划）

| 杠杆 | 对象 | 施工量 | 依据 |
|---|---|---|---|
| 停用/项目级化 | web_reader、image_search（21 天 0 调用）；glm_vision、context7、codex（渗透 ≤1.2%） | 零施工（config/workspace 级，0917 档 note 已写明 workspace 级自动连接机制） | §3.2 |
| 拍板遗留 | computer-use 插件去留（09-17 D 档悬而未决；数据=5% 渗透但 92% MCP 调用 concentration 的一半） | 零施工（用户拍板） | §3.2 |
| Skill 治理 | 3 对真双列去重；零调用族（github:×13 等）保留/归档标准 | 低施工 | §3.3 |
| 记忆面 | MEMORY.md 索引行瘦身（hook 精简） | 低施工 | §1/Q4 |
| 治理规则（可回流本工作流） | 「常驻工具 >N 或 30 天零调用 → 进项目级/退出」候选条款 | 文档批 | §5 阈值判据 |
| 不可行项 | Tool Search / 代码模式类结构性方案 | — | 平台无机制，观察 |

## 7. 待拍板问题（计划阶段的输入，本轮不决）

1. **红线即时项（建议不等计划）**：`mcp-disabled-20260917.json` 内 github_mcp 条目携带**明文 GitHub PAT**（值不在本档出现）；该档是 09-17 批次自产。处置=轮换 PAT（agent-log 状态段已有此待办）+ 把停用档中 Authorization 字段清去。另 config.json 内 provider apiKey 为平台设计形态，按平台惯例保留。
2. MCP 二阶段：哪些 server/插件进 workspace 级、哪些直接停用；computer-use 最终形态。
3. Skill 面：零调用 29 条的处置线（保留观察 / 归档停用）；双列去重方案（哪边留）。
4. MEMORY.md 瘦身幅度与行格式约束。
5. 治理规则是否立条：零调用退出线 + 常驻预算线（候选回流 details/workflows）。

## 8. 测量口径与误差声明

- 首请求 input+cache_read+cache_creation ≈ 常驻面 + 首条消息，跨日对比方向性成立、单日绝对值有 ±几 K 噪声；n<5 的日期不具代表性（08-29/08-30 尤甚）。
- Skill/注入件 token 为字符折算估算（EN≈3.7 字符/tok、中文≈1.75 tok/字），误差 ±30%。
- db 窗口仅 21 天（08-28 起）；computer-use 等晚安装条目的「零调用」实为「自安装起零调用」。
- 联网数字以四篇原文抓取为准；社区综述（§5 末行）未逐源核验，只作思路参考。
- 复测入口：附录脚本=复制 `~/.zcode/cli/db/db.sqlite*` 三件后对本档 §3 各 SQL 重跑（查询语句已内嵌上文各节，工具=python+sqlite3 标准库）。

## 来源清单

- [Anthropic Engineering: Introducing advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use)
- [Anthropic Engineering: Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [Cloudflare Blog: Code Mode](https://blog.cloudflare.com/code-mode/)
- [Anthropic Engineering: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 检索佐证（二手）：[Medium: Claude Code cut MCP context bloat 46.9%](https://medium.com/@joe.njenga/claude-code-just-cut-mcp-context-bloat-by-46-9-51k-tokens-down-to-8-5k-with-new-tool-search-ddf9e905f734)

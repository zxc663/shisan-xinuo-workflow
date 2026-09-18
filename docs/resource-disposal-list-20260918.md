# 资源处置清单（v3.0 批次④ 产出 · 2026-09-18 · **建议件，config 零改动**）

> 依据：`docs/resource-utilization-gap-analysis-20260918.md`（21 天 db 全量机判）+ 本批新取证（Skill 调用面重查：15 条有调用 / 用户目录 9 条零调用）。
> **执行纪律：本清单全部为建议——config/副本动作需你逐项批准后另行执行**（平台全局配置=授权边界内动作）。

## A. MCP 面（全局 server×4 + 插件×6）

| 对象 | 21 天数据 | 建议 | 备注 |
|---|---|---|---|
| `zcode-token-usage-statusbar` | 18 次调用/12 会话 | **保留常驻** | 1 工具、轻 |
| `context7` | 6 次/1 会话（0.3% 渗透） | **停用**（或 workspace 级=文档项目用） | 2 工具 |
| `glm_vision` | 6 次/4 会话（1.2%） | **workspace 级化**（图像任务项目）或保留观察 | 6 工具 |
| `codex` | 1 次/1 会话 | **停用**（或 workspace 级） | 需要时菜单重开 |
| 插件 `computer-use`（30 工具） | 渗透 5%，但占 MCP 调用近半（1815 次） | **拍板项**：A 保留常驻（当前）｜B workspace 级（GUI 任务项目）｜C 停用 | 数据自相矛盾（低频面 vs 集中度），需你定 |
| 插件 `document-skills`（docx/pdf/pptx/xlsx + search_image） | **全 0 调用** | **插件停用**（需要时重开）或保留（低频文档任务） | 4+1 工具面 |
| 插件 `github`（13 skills + 曾含 github_mcp） | **13 skills 全 0 调用** | **插件停用**候选 | 与已裁 github_mcp 同族 |
| 插件 `browser-use`（node_repl + 2 skills） | 964 次/23 会话 | **保留** | 高频 |
| 插件 `skill-creator` | 0 次调用 | **保留**（作者工作流：本仓写 Skill 用） | 人工直读也可，但低成本 |
| `web_reader`（工具 1） | **0 调用** | **停用**候选 | 与搜索能力重叠 |

## B. 用户目录 Skill 零调用 9 条（`disable overrides` 建议名单）

零调用（21 天）：`animate`｜`ask-sonner`｜`composition-patterns`｜`react-best-practices`｜`scrollcraft`｜`taste-skill`｜`theme-factory`｜`web-artifacts-builder`｜`web-design-guidelines`。
**建议**：进 `~/.zcode/cli/config.json` 的 skill disable overrides 名单（**不删文件、可逆**）；30 天观察期内若仍零调用转「归档候选」。例外保留：`scrollcraft`/`taste-skill` 如近期有前端动效计划可暂留（你的调用习惯决定）。

## C. 重复列示 3 对（同一 Skill 两目录并存 → 清单双行）

| 重名 | 位置 | 建议 |
|---|---|---|
| `anti-ui-slop` | `.agents/skills/` + `.zcode/skills/` | **删 `.zcode` 侧，保留 `.agents` 侧**（跨工具标准位；ZCode 同样可发现） |
| `scrollcraft` | 同上 | 同上 |
| `ui-ux-pro-max` | 同上 | 同上 |

## D. 细则零引用候选（lookup/hooks 数据）

沿用批 3 体检修正口径：可信信号=**#288-#291 四条双零**（lookup 与 symptoms 双侧零引用）——**留观察**（样本与方法学限制如实：46% 覆盖率为宽松口径，现检索键已 100% 落齐，下轮体检口径可收紧重跑）。本批**不重跑**（hooks 数据源在仓外工作区）；重跑条件=下次体检批。

## E. 治理规则立条候选（供 v3.0 收尾批决定是否入细则）

1. **零调用退出线**：常驻面（Skill/MCP 工具）连续 60 天零调用 → 进「停用候选名单」；停用走 disable overrides/插件开关（可逆），删除需再一周期确认。
2. **常驻预算线**：新增常驻 MCP 面时核「工具定义 >10K tok 或 10+ 工具 才值得常驻」（借 Anthropic Tool Search 阈值判据）；Skill 清单条目增删同步核清单成本。
3. **清单预算**：技能清单列示条目数上限目标（现 54 列示/44 去重 → 去重后 ≤40 目标）。

## F. 保留与观察名单

`browser-use`（高频）｜`computer-use`（拍板中）｜`skill-creator`（作者流）｜`glm_vision`（观察一期）｜上下文服务类（context7/codex）需要时菜单重开即可。

---

**批准方式建议**：按节批（A/B/C 可独立批准）；批准后我按「备份→改 config→重启提示→新会话验收（常驻体积复测+零调用面确认）」执行；未获批项保持原状。

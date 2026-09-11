# 平台级逐会话分析计划 · v2.6.0 发行后新会话（ZCode / WorkBuddy）

> 目标：对 v2.6.0 全渠道发行（2026-09-09）之后两平台产生的**新会话**做逐会话精细分析，回答「Skill 在真实新会话里到底被应用成什么样」。本计划是执行蓝图，数据只读、逐会话即时收割、产出回填 EVIDENCE 与版本计划。

## 1. 数据源与读取方式（全部只读）

| 平台 | 数据源 | 形态 | 风险与对策 |
|---|---|---|---|
| ZCode | `~/.zcode/cli/db.sqlite` | session（id/directory/title）/ model_usage（token/tool）/ tool_usage 表 | WAL 只读连接 `file:...?mode=ro`；列名先 PRAGMA 核实（v4 教训：session 主键列=id 非 session_id） |
| ZCode | `~/.zcode/cli/rollout/model-io-sess_*.jsonl` | 全量模型 I/O（request.body.system 含注入全文） | **清刷风险**：先起 4 秒增量备份守望，逐会话流式读 |
| ZCode | `D:\roadtest-v260\hooks-log\hooks.jsonl` | SessionStart/Stop 落行 | 按 cwd 区分项目归属 |
| ZCode | 各项目 `memory/agent-log.md` | 承载留档（行为面结果） | 项目清单由 db.session.directory 聚合得出 |
| WorkBuddy | `~/.workbuddy/`（AGENTS.md 注入副本 + 会话/记忆文件） | 注入副本头部锚点 + 会话留档 | 复用 `memory/forensics-2026-09-08/` 三平台取证脚本形态；WorkBuddy 数据密度低于 ZCode，以留档+注入面为主 |

**时间窗锚点**：ZCode 注入副本头部「注入时间：2026-09-09 05:37:38」之后的 session（按 db.session 建立时间过滤）；发行前会话只作对照组。

## 2. 逐会话判分口径（沿用 v4 沉淀，check_rollout.py 复用）

每会话一张 scorecard，字段：

1. **注入在场**：rollout 首请求 system/body 是否含「在场提示 · 工作流 Skill 现已在场」与「294 条细则」锚点（0/1 + 命中数）
2. **开工四步**：复述（首轮含「复述」或等价理解陈述）/判级（L1/L2/L3 显式标注）/承载（Read 或 Write agent-log）/记忆对齐——各 0/1
3. **GATE**：宽松匹配在场（含 `**GATE**:` 变体）0/1
4. **细则引用**：assistant 域完整前缀 `details #NNN`/`细则 #NNN` 计数 + 裸 `#NNN` 计数（先剔除完整前缀再数）
5. **lookup 执行**：toolCalls[].input.command 含 detail_lookup 的真实执行次数（≠提及次数）；errpath 报数与真实输出一致性
6. **文件级触达**：Read 目标含 `<技能安装目录>/references/` 的次数（验证「文件级触达≈0」结论在发行后新会话是否持续）
7. **成本**：model_usage 请求数/input/output（db 侧），与 rollout 侧交叉核对
8. **平台对照组**：WorkBuddy 会话仅判 1/2/8（无 rollout 工具链）

## 3. 抽样与分层

- **分层维度**：平台（ZCode/WorkBuddy）× 项目（博客项目 / 本仓 / 其他）× 会话角色（主会话/子代理）
- **范围**：发行后全量新会话（预计 ZCode 侧 20-40 会话量级）；>60 会话时按项目分层抽样（每层 ≥8）
- **排除**：路测工作区（roadtest-v260）会话单列（它们是实验样本，不算自然观测）

## 4. 与「会话自查提示词」联动（机器侧 × 自报侧对照）

抽样 3-5 个会话（跨平台），用户持 `docs/session-self-audit-prompt.md` 向对应会话发起自查导出；自报结果与机器侧 scorecard 并排对照：
- **自报-机证一致率**＝新判据（F13「背答案」检测的泛化形态：agent 对自己行为的描述是否可信）
- 差异模式分类：漏报（做了没报）/虚报（没做报了）/解读偏差（理解错指令意图）

## 5. 产出物

- `memory/platform-audit-2609/`（本地承载）：逐会话 scorecards + 汇总表 + 复用脚本
- EVIDENCE 新节：平台逐会话审计结果（失效地图五层表格的发行后复测版）
- 版本计划 v2.7 面 F 回流：新发现的触达缺陷/口径问题逐条入候选池

## 6. 铁律

只读；先备份后分析；逐会话即时收割；入库文档去真实盘符路径；n 与口径随每张 scorecard 落盘，拒绝伪精确；好坏数据同列。

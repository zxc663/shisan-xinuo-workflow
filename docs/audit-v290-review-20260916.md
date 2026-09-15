# v2.9.0 审查报告（2026-09-16 · 只审不改）

> 基线：HEAD=7b0699f（五副本 count=343 5/5）。机证三件（本会话实跑）：facts_sync --check PASS（活跃 343/上限 344/类数 24/节头范围）、deploy_injection --check 严格 5/5 count=343、verify-release.ps1 7/7 ALL PASS（A 项 injection-core 5945≤6000 双口径）。联网对标（一手页面抓取，WebSearch 限流改 WebFetch）：obra/superpowers、github/spec-kit、bmad-code-org/BMAD-METHOD、Claude Code 官方 Skill 规范（code.claude.com/docs/en/skills）。
> 判级：L2-F 审查批（用户点名联网调研前置）；零施工——修复建议全部待拍板。

## 一、总评

活体面干净：README / package.json / project-info 活态行 / SKILL.md / memory-anchor / 注入五副本的细则口径全部为 343·24 且机证全绿；**漂移集中在时点快照面与对账白名单外**——口径错误 9 处（§二）、skill 正文历史残留 3 处（§三）、对标缺口 3 项（§四）。可发布性判断不变：阻断项仍是已知待办（dist=333 中间态、发行 L3），本次未发现新的发行阻断项，但 A 族若不在发行批窗口同修，RELEASE-CHECKLIST 会以错误口径指挥发行。

## 二、A 口径错误（9 处，file:line 实证）

| # | 位置 | 现状 | 应为 |
|---|---|---|---|
| A1 | RELEASE-CHECKLIST.md:4 | 「细则 333 条/24 类」（版本沿革头） | 343 |
| A2 | RELEASE-CHECKLIST.md:9 | 「细则 342」 | 343 |
| A3 | RELEASE-CHECKLIST.md:10 | 「活跃 342 条/24 类 全仓一致」 | 343 |
| A4 | RELEASE-CHECKLIST.md:13 / :33 | 「count=342」/「新 description 含 342/24 口径，压缩版需重算」 | 343 / 343·24 |
| A5 | AGENTS.md:28（仓库根，每会话注入） | 「细则 330→333·24 类」 | 增量叙述缺 G 直写批与细则 #295 转正，终值 343 |
| A6 | docs/reference-sources.md:18 | 「活跃细则 333」 | 343（同文件 :21 「343 条落地细则（24 类）」是对的） |
| A7 | CHANGELOG.md:3-5 | v2.9.0 条目止于「330→333」、时间线注「→2026-09-15」 | 缺 G 直写批（细则 #336-#344，333→342）与细则 #295 转正（342→343）两段；Release notes 会引用 |
| A8 | docs/project-info.md:35 | 模块表「已实现（v2.8.0）」 | 内容已是 2.9.0，版本标签滞后 |
| A9 | README.md:183-188 | 路测 v11 段「基线 v2.8.0/330 条」「部分执行已收官，全量续跑入 2.9」 | 09-16 已全量收官（EVIDENCE §三十一），段面停留在收官前 |

**根因（机制级）**：facts_sync = 白名单对账（CARRIERS 10 面，scripts/facts_sync.py:33-67）——①仓库根 AGENTS.md 完全不在清单；②reference-sources 只挂行首形态一个正则，:18 行内形态漏网；③RELEASE-CHECKLIST/项目信息 About 属 F-03 时点快照豁免，豁免面没有「过期强制重写」触发器。verify G 项继承同一清单，故「7/7 PASS」与 9 处漂移并存——**门禁绿 ≠ 全仓口径绿**，这正是 facts_sync 头注自称「抓三处漂移」能力的边界外。
**建议**：CARRIERS 补 AGENTS.md 与 reference-sources 第二形态；豁免面改为「每批次开工强制重写该清单」硬门；CHANGELOG 以批次为单位补段。

## 三、B 历史写入 skill 正文（3 处，轻微）

| # | 位置 | 问题 |
|---|---|---|
| B1 | skill/.../templates/hooks/post_tool_guard.example.py:15 | 注释「（2026-09-14 受控实验实证）」——日期+路测轮次入模板正文；应留 EVIDENCE，模板只留规则+≤1 句为什么 |
| B2 | skill/.../templates/hooks/session-end.example.sh:9 | 落点仍指 `memory/task-log/<日期>-<名>.md`——与一档制映射（details.md:11：task-log→agent-log 流水区）冲突的旧承载残留；且 ZCode hooks 7 事件无 SessionEnd，该示例在本平台不可运行，示例价值需重估 |
| B3 | skill/.../SKILL.md:334 | 状态面模板「注入版本: <2.9.0>」以字面当前版本作占位——下版即陈旧，应为 `<版本>` 形态 |

**豁免面核对（合规，不动）**：details §12-§23 节标题/节首带日期与拍板叙述（节首来源注记豁免）、各条 `*来源/晋升*` 尾字段、details.md:7 特殊槽状态行（机制状态非史料）、OWASP Top 10:2025（标准名引用）、local-model-glossary.md:4 来源注记、SKILL §6/§11 指向 EVIDENCE.md（EVIDENCE.md 随 dist zip 分发，zip 49 文件实测在包内——非悬空指针）。

## 四、C 联网对标与缺口

**对标四家一手信息**：
1. **obra/superpowers**——skills=强制工作流（TDD/系统化调试/两段评审子代理）；**规则行为有独立评测仓（superpowers-evals drill harness）做回归**；约 14 个 agent 平台插件分发；支持平台上挂 post-compaction 重注入 hook。
2. **github/spec-kit**——constitution→specify→plan→tasks→implement→**converge 收敛循环**（迭代至「Converged」判据）；bug 修复强制 verdict（verified/partial/failed，未验证≠修复成功）。
3. **bmad-code-org/BMAD-METHOD**——durable context（决策跨会话携带）；`bmad doctor` 更新后运行时自修。
4. **Claude Code 官方 Skill 规范**——SKILL.md <500 行；description+when_to_use 合计 1536 字符截断；三层渐进披露；「每一行都是每轮重复 token 成本」；skill-doctor 高成本零触发审计。

**对齐确认（不是缺口）**：SKILL.md 383 行<500 ✓；description 远短于 1536 ✓；T1/T2/T3 三层+回指=Level 3 ✓；五副本 --check≈多 harness 分发+doctor ✓；agent-log 一档制≈durable context ✓；GATE exempt≈bug verdict ✓；templates/agents（critic/risk-reviewer/security-auditor）≈两段评审 ✓；防棘轮/瘦身≈每行成本原则 ✓。

**缺口 3 项（按实度排序）**：
- **C1 规则行为评测不可随仓复跑**（对标 superpowers-evals）：路测判分工件全在仓库外（D:/roadtest-v11/ 的 drive_v11.py、fixtures、extracts 实存但不随仓）；npm description 卖点「detail_lookup 探针 24/24」的探针 fixture 不随仓——外部评审「承诺-实现缺口」家族残留，批 2「可验证化」未落地。建议：探针 fixtures+runner 随仓 `scripts/evals/`。
- **C2 走查收敛无判据**：spec-kit converge/verdict 思想 vs 本仓「真实用户走查（允许多轮）」无显式收敛判据语义。轻量补条候选（走防棘轮 grep 查重后入 details）。
- **C3 压缩后重注入无机制位**：superpowers 在支持平台挂 post-compaction hook；ZCode 实测无 SessionEnd/压缩事件，细则 #326 压缩接续义务=行为补偿已做，但该平台能力缺口应显式记入 platform-adaptation.md 平台能力矩阵（与 face G n=24 WorkBuddy hooks 双缺位同属平台覆盖面）。

**反超项（对标对象均无）**：触达机制化三通道（报错必经+hooks TOP 推送+每轮再触达）、双击晋升制+防棘轮双向代谢、GATE 可重跑工件、必问底线十维、F-21 --check 取 package.json 堵假绿。定性：本 Skill 在「纪律被消费」维度强于全部对标对象；在「纪律被验证」维度弱于 superpowers（C1）。

## 五、D 遗留待办对账（确认仍开，非本次新发现）

dist v2.9.0.zip=333 条中间态（zip 实测：49 文件、details 最大编号 335、全文 0 次「343/342」——zip 内 frontmatter version 已是 2.9.0，版本面新鲜而内容面陈旧，误发风险真实存在）→ 发行批第一动作重打｜发行七渠道 L3 待批｜ClawHub scans 复查｜GitHub classic PAT 轮换｜face G n=24 traces 取证（WorkBuddy 注入+hooks 双缺位定论）｜S-B′ 残留进程处置（ferry.exe:8002+vite:9527）｜hooks 脚本迁出 roadtest 目录｜细则 #326 触达强化。

## 六、E 修复建议（不施工，待拍板）

- **S 级（并入发行批第一动作窗口，该窗口本就要重写 RELEASE-CHECKLIST+重打 dist）**：A1-A9 一次口径批＋B1-B3 顺手修＋CARRIERS 补 AGENTS.md/reference-sources 第二形态＋CHANGELOG 补两段。
- **P1**：C1 探针 fixtures+runner 随仓（可复跑工件）。
- **P2**：C2 收敛判据补条、C3 平台能力矩阵记档。
- 风险提示：A8/A9 为读者可见的活体滞后；A7 在 Release notes 生成前必须补齐。

# 对标调研 · obra/superpowers 可吸收清单（2026-09-29 · 只调研不施工）

> 方法：GitHub 一手取证——README 全文（14.4K 字符）、15 个 skills 清单、6 个技能本体首读（using-superpowers / subagent-driven-development / diagnosing-superpowers / writing-skills / requesting-code-review / brainstorming）、heads/session-start 脚本、仓库结构（10 个 harness 插件目录 + docs/porting-to-a-new-harness.md）。
> 基线：`docs/comparison-v290-analysis-20260916.md`（十一家含 superpowers）+ `docs/design-specs/benchmark-refresh-20260929.md`（批 R 刷新）。

## 一、本轮新读到的机制（前述报告未覆盖的部分）

1. **引导协议常驻化**：`using-superpowers` 技能**全文**由 SessionStart hook 注入（含「1% 可能命中也必须调用」硬语言 + 反合理化红旗表：简单问题/先看代码/先要上下文 全是合理化）。
2. **子代理流水线**（subagent-driven-development）：每任务派 fresh 实现子代理 → **每任务后置审查**（spec 合规 + 代码质量）→ 终局整支复查；「**Rulings, not stalls**」——四类停点之外不停摆，决策记 `Ruling: <决定> — <依据> — <错了的代价>`；连续执行不中途请示。
3. **会话诊断技能**（diagnosing-superpowers）：问题收编 → 定位 transcript → **七维分析子代理并行**（技能时间线/计划遵循/重复劳动/磕绊/质量证据/请求冲突/成本与时间）→ finding **必带 path:line** → 脱敏证据包交上游。
4. **技能写作 TDD**（writing-skills）：先造压力场景**看基线失败** → 写技能 → 看通过 → 补漏洞；「没看过它失败，就不知道条款教对了没有」。
5. **审查协议**（requesting/receiving-code-review）：BASE_SHA/HEAD_SHA 锚定审查范围 + 每任务必审 + 收到评审的处置协议。
6. **平台面**：10 个 harness 插件目录 + `porting-to-a-new-harness` 移植指南；分支收尾清单（finishing-a-development-branch）。

## 二、可吸收清单（候选，未施工；每条=借鉴点/我们现状/移植成本/验证法）

| # | 候选 | 借鉴点 | 我们现状 | 移植成本 | 验证法 |
| --- | --- | --- | --- | --- | --- |
| A | **会话诊断技能** | 七维并行分析 + path:line 举证 + 脱敏证据包 | 已有 `docs/session-self-audit-prompt.md` + agent-log，但无技能化流程；坏会话复盘靠临场 | 低（1 个 skill + 7 个维度 prompt 模板 + 子代理纪律包复用；顺带把「成本与时间」维度接到 usage 数据） | 拿一次真实坏会话跑通：产出 ≥3 条带 `path:line` 的发现 + ≥1 条改进立案 |
| B | **每任务审查流水线** | fresh 审查子代理 + BASE/HEAD SHA 锚定 + 终局整支复查 | roles 包有 critic/contract 等角色，但非「每任务必审」；现为合并后统一集成验证 | 中（flows 验收步 + roles/critic 模板各加一段协议） | 一次多任务批对照：审查发现数 / 事后返工数 |
| C | **Ruling 账本格式 + 四停点收敛** | 目标模式下「不停摆」：只有不可逆/安全/工作区外副作用/计划崩坏四类停；其余记 `Ruling: 决定 — 依据 — 错了的代价` | 目标模式已有「按第一推荐推进 + 归档」，但无固定格式与停点收敛表述；agent-log 决策行格式接近 | 低（一条条款 + 账本格式一列） | 目标模式跑一轮：统计停顿次数 + Ruling 行数/质量 |
| D | **条款立项先做压力测试** | 新机制先造场景证明「不写会错」（TDD for rules） | 已有探针 harness + 金样本 23/23，但立项流程仍是「踩坑后立条」；基线证据非必填 | 中（细则立项模板加「基线反例证据」栏；与双击晋升制衔接） | 下一批新条款 100% 带基线反例证据 |
| E | **新平台移植指南** | porting-to-a-new-harness 五步式文档 | `references/platform-adaptation.md` 有注入点表，但无「移植步骤 + 验收锚」成稿 | 低 | 下次上新平台按指南走一遍，零即兴决策 |
| F | **反合理化速查常驻化** | 红旗表放常驻面（他们整篇 bootstrap 常驻） | 借口拦截表在 `SKILL.md` §7（非常驻）；常驻面只有失败时刻 TOP 推送 | 中（受 6K 预算约束，须等量压缩后才可加） | 注入核心仍 ≤6000 + 行为面探针复测 |

## 三、已有等价物 / 明确不抄

- **流程强制**（TDD / 系统化调试 / 验证先行）：我们有 flows 9 分册 + roles 8 角色，同构且更贴本项目；不重复引入。
- **独立 evals 仓**：他们把评测放独立仓；我们的 probe/scorecard **随仓** + 判据自测 23/23 + 同批重判——判据强度更高，不降级去抄。
- **成本披露**：superpowers README 通篇不提 token/成本；我们已有「收益与代价」如实披露——**不抄它的滤镜**，反向保持差异。
- **十平台插件目录**：与我们的 `install-skill.ps1` + `deploy_injection.py` 路线不同；只在 E（移植指南）层面吸收。
- **强营销语态**（EXTREMELY-IMPORTANT / 1% 也必须）：机制可借（F），语态不借——我们的差异化是「主张说小、证据说满」。

## 四、建议优先级

**A / C / D（低成本高杠杆，建议随下一内容批）→ B（中成本，随多任务场景批）→ E（按需，等新平台）→ F（暂缓，等注入核心预算腾挪）。**

> 边界：本档只调研不施工；每条落地前按 D 自身的标准先补基线证据。

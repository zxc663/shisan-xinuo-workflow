# 项目级 Agent 规则 · 产品工程 Skill

> 2026-09-21 由工作流承载检查创建。本项目开发一个「产品工程 Skill」：给 LLM 装上纪律之外的品味/产品维度，且对下一个会话更友好。

## 回指（强制字段）
- 通用纪律权威=注入核心与 SKILL.md（shisan-xinuo-workflow）；本文件只写项目特有。
- 会话末更新 `memory/agent-log.md`（流水+状态段）后离开；时间戳到分钟。
- 上位调研档（财务项目内）：`个人财务账单智能规划助手/docs/design-specs/product-engineering-skill-research.md`——本 Skill 的差异化结论与三层结构定稿建议均出自该档。

## 项目纪律（只写本项目特有）
- **蒸馏纪律**：从参考 Skill 蒸馏时，①只收「代码级可操作的机制/判定表」，拒收抽象口号；②每条蒸馏必须标注出处 Skill 与 source:line；③判例形态=问题→候选→裁决→理由。
- **致谢纪律**：凡蒸馏自他人/既有 Skill 的内容，产出物中必须注明上游（文件级出处），禁止洗稿式改写。
- **门禁优先**：品味条目凡可机器判定的，必须同时产出 `gates/` 下可执行检查脚本；纯原则不配门禁的条目要在档内标注「人工裁决域」。
- **参考Skill/ 只读**：该目录存放本机 Skill 的研读蒸馏笔记与原始索引，是原料库；**包本体在家族主仓** `skill/shisan-xinuo-product/`（SKILL.md + references/ + scripts/ 八台门禁与提取器），本仓=设计源与实证场（问题定义 / 方向档 / 调研蒸馏 / 证据 / 流水），不发第二份包体副本。
- Skill 形态标准：Agent Skills 规范（SKILL.md frontmatter：name/description；渐进加载；可捆绑 scripts/）。

## 项目承载（已就绪）
- `memory/agent-log.md` 一档制四区 = 权威承载。
- `docs/` = 定向文档与 schema。
- `参考Skill/` = 全量 Skill 研读蒸馏笔记（分组：设计品味系/工作流极简系/工具文档系）。
- `gates/` = 门禁脚本（目标产物）。

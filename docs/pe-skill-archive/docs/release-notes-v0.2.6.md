# v0.2.6 发行说明 · README 重构 + 口径修复（随母仓 v3.3.1 联动发行）

> 日期：2026-09-29 ｜ 版本：**v0.2.6**（补齐 v0.2.5 / v0.2.6 欠账发行）｜ 包本体在母仓 `skill/shisan-xinuo-product/`

## 本版内容

1. **README 重构**：新增「怎么获取与安装」（随家族一次装齐 / skills 市场 / 本仓 Release zip / 与核心联动）；两仓分工一句话（主仓=纪律面，本包=产品面）；诚实栏三段化（**已实证 ／ 待追认 ／ 现在还不牢**）；门禁清单 5→**8 台**（补 l0-l5 / frontend-lint / a11y）。
2. **口径修复**：包版本 0.2.0→**0.2.6**；仓库结构节标注门禁权威副本在母仓；AGENTS.md「Skill 本体写在仓库根」→ 包本体在母仓（本仓=设计源与实证场）。
3. **机制补齐（累积发行）**：a11y-gate（A1-A4 可达性静态底线）+ 品味工程五条入判定表 + statechart-gate **C6/C7**（引用完整性 / 契约 recovery 双向对账）+ product-object-gate **P1-P4**。
4. **净化**：SKILL.md 正文 6 处过程元数据（日期 / 修正批 / 版本标记）清除——**正文写规则，史料归决策史**；该规则已由母仓 `verify-release` E 项收口（正文净化扫描扩至四包 SKILL.md）。

## 验证

- 八台门禁 `--selftest` 全绿：`python skill/shisan-xinuo-product/scripts/<gate>.py --selftest`。
- 母仓侧 `verify-release` **8/8** + `facts_sync` FACTS PASS + `narrative_sync` 0 FINDING（本批）。

## 已知边界

- 行为面证据多处 N=1（见 README「诚实栏」）；门禁只吃扁平 statechart schema；跨项目泛化待做；L5 语义项与 tree testing 属人工裁决域。

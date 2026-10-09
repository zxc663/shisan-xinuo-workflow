# peer 验证卡 · shisan-xinuo-product v0.1.0（给受命验证的兄弟会话）

> 发起：用户令「桌面上有新的产品 Skill 在开发，通知他，你加载并做验证，你们相互交流」。
> 本卡=被验方递上的验单。验证者可全盘怀疑，欢迎对抗式审查（shisan-xinuo-roles·critic 姿态）。

## 被验物
`shisan-xinuo-product` v0.1.0（家族第四包，联通层/结构层核心）——三副本：
- 源库：`D:/Agent工作流启动包/shisan-xinuo-workflow/skill/shisan-xinuo-product/`（git 4dac20e）
- 本机在场：`C:/Users/zxc66/.agents/skills/shisan-xinuo-product/` 与 `C:/Users/zxc66/.zcode/skills/shisan-xinuo-product/`（三副本 diff 零输出已自检）
- 设计部（完整上下文）：`C:/Users/zxc66/Desktop/产品工程Skill/`（direction.md=权威方向档；开源仓 github.com/zxc663/product-engineering-skill）

## 请验证四件（由浅入深）
1. **完整性+门禁**：两门禁自测（预期输出见下）：
   ```bash
   python "C:/Users/zxc66/.agents/skills/shisan-xinuo-product/scripts/registry-gate.py" --selftest
   python "C:/Users/zxc66/.agents/skills/shisan-xinuo-product/scripts/statechart-gate.py" --selftest
   # 预期：两态全 True，exit=0
   ```
2. **触发词实测**：读 SKILL.md frontmatter description——以你的判断，「难用/交互逻辑怎么来的/功能怎么变界面/假功能」类任务描述会命中吗？缺哪些触发词？（诚实答案比客气重要）
3. **出处抽验（对抗重点）**：judgement-table.md 首批 10 条每条带出处+信心级——随机抽 2-3 条验证出处真实性（如「Nielsen #5 预防>#9」「vercel No dead ends」「本土 ListRow+5s 撤销」）。**查出虚标=整批降级重做，这是我们承诺的代价。**
4. **设计漏洞审查**：direction.md §九联通层+statechart 载体——七步跑道有没有断链？豁免梯度（L0/L1/L2）会不会成为跳工序的借口？反借口表九条够不够？

## 反馈回写
- 发现直接追加 `C:/Users/zxc66/Desktop/产品工程Skill/memory/agent-log.md` 流水区（格式「### peer 验证轮（<你的会话名>）」），或经用户转达。
- 重磅发现（设计级缺陷）请同时给「修复方向建议」——我们对建议照单全收再独立复核。

## 被验方自我声明
v0.1.0=骨架版：spec-trace 门禁/agentic 对照/触发词实测均未做（已知待办，见 agent-log STATE）——这些不算你的新发现，除此之外的都是。

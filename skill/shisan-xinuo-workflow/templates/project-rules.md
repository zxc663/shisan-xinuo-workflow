# 项目级 Agent 规则 · <项目名>

> **本文件是项目级注入（每会话自动进入）。**与平台全局硬注入（injection-core：通用纪律）互补：项目级管「本项目特有信息 + 项目承载 + 项目纪律」。**由工作流「项目承载检查（SKILL §2.0 开工序六步第 4 步 / §3 第 6 步）」自动创建/合并**——文件名按 `platform-adaptation.md` §2「项目级注入点表」定名（Codex=项目根 AGENTS.md / Claude Code=项目 CLAUDE.md / Trae=`.trae/rules/project_rules.md` / Cursor=`.cursor/rules/*.mdc` / Windsurf=`.windsurfrules`；未知平台联网调研，离线降级 AGENTS.md 兜底+头注迁移说明）：存在同名既有规则文件 → **合并不覆盖 + 先备份**；不存在才按本模板新建。

## 回指（强制字段，缺失 = 不合规）
- 本文件由 Skill「shisan-xinuo-workflow」工作流创建——**判级 / 红线 / 必问 / 细则等完整纪律按需加载该 Skill**（`references/injection-core.md` 为平台注入核心；细则库 `references/details.md` 按症状检索）。
- 会话识别到本文件但 Skill 未在场 → **提示加载 Skill 再继续**（不裸奔执行）。
- 会话末：**更新 memory/（task-log + state）后离开——不更新 = 交接断链**。

## 工作流在场（本项目会话）
- 开工序列（SKILL §2.0）：先场景判定（本项目=持续项目 → 全套；单发任务 → 纪律走、文档豁免）→ ①复述理解（无条件先行）②扫描工作区+形态判定 ③定承载根 ④承载创建（增量补缺）⑤读 `memory/`（state → experience-mustread → experience → preferences）⑥判级速查+三问选道；命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- 细则引用统一完整前缀 `details #N` / `细则 #N`（**禁裸 #N**——与 GitHub issue 编号同形异义，假阳性 9/10 实证）。
- 权威源顺序：`references/injection-core.md`（每会话在场）→ `SKILL.md`（可执行细节）→ <项目权威文档> → `docs/project-info.md`（导航索引）。

## 项目承载（已就绪）
- `memory/`：`state.md` / `experience-mustread.md` / `experience.md` / `preferences.md` / `task-log/`——**规范件（带扩展名 .md 的正文文件，非空占位）**；本地承载，按项目 gitignore 约定决定是否随仓。
- `docs/project-info.md`：六节索引（架构 / 目标 / 模块真实状态表【含关键词锚定列，details #275】/ 调研导航 / 参考资源 / 复述签章）。
- <项目特有纪律 1-3 条；本文件被合并时保留既有段落>

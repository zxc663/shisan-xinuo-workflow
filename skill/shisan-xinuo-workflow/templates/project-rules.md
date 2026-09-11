# 项目级 Agent 规则 · <项目名>

> **本文件是项目级注入（每会话自动进入）。**与平台全局硬注入（injection-core：通用纪律）互补：项目级管「本项目特有信息 + 项目承载 + 项目纪律」。**由工作流「项目承载检查」自动创建/合并**——文件名按 `platform-adaptation.md` §2「项目级注入点表」定名（Codex=项目根 AGENTS.md / Claude Code=项目 CLAUDE.md / Trae=`.trae/rules/project_rules.md` / Cursor=`.cursor/rules/*.mdc` / Windsurf=`.windsurfrules`；未知平台联网调研，离线降级 AGENTS.md 兜底+头注迁移说明）：存在同名既有规则文件 → **合并不覆盖 + 先备份**；不存在才按本模板新建。

## 回指（强制字段，缺失 = 不合规）
- 本文件由 Skill「shisan-xinuo-workflow」工作流创建——**判级 / 红线 / 必问 / 细则等完整纪律按需加载该 Skill**（引用写**注册名**经 Skill 工具加载，不写绝对路径——多平台安装路径不同，绝对路径会失配）。
- Skill 存在多副本安装时（主副本 + 平台侧副本）：**以平台侧副本为权威**，修订须双副本同步。**漂移自检（可重跑）**：`diff -rq --exclude=memory --exclude=user-notes --exclude="*.bak-*" <副本A> <副本B>`——零输出=一致；有输出即漂移，先按 syncer 流程同步再继续。
- 会话识别到本文件但 Skill 未在场 → **提示加载 Skill 再继续**（不裸奔执行）。
- 会话末：**更新 memory/agent-log.md（流水区 + 状态段）后离开——不更新 = 交接断链**。

## 工作流在场（本项目会话）
- 开工序列四步（SKILL §2.0）：①复述理解（无条件先行；摘要接续的会话可省开工复述，但须一行声明「接续跳过复述，依据=摘要上下文完整」——判级与 L3 确认不豁免）②承载检查（一气呵成）③记忆对齐（最小读取）④判级速查+三问选道；命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- **判级显式**：重大变更在回复中写明本轮判级（一行，如「本轮判级 L2-S」）——判级可以低，不可以隐。
- 细则引用统一完整前缀 `details #N` / `细则 #N`（**禁裸 #N**——与 GitHub issue 编号同形异义，假阳性 9/10 实证）。
- **细则检索端口**：错误 / API 意外形态 / 新依赖不生效 → 先对注入核心「错误必查 TOP」，未命中跑 `python "<技能安装目录>/scripts/detail_lookup.py" "<症状关键词>"`，命中行即 errpath 证据（**未执行 lookup 不得自报命中数**；Git Bash 下脚本路径须写 Windows 形态 `C:/...`——`/c/...` 会被 MSYS 改写报 No such file，实测坑）。
- 权威源顺序：`references/injection-core.md`（每会话在场）→ `SKILL.md`（可执行细节）→ <项目权威文档> → `docs/project-info.md`（导航索引）。

## GATE 收尾（每任务块，可复跑工件 > 自我叙述）
`GATE: {v=<验收项>, cmd=<可重跑命令>, exit=<预期退出码>, files=<变更文件>, lessons=<知识点>, exempt=<未验证声明>, errpath=<错误路径核对>}`——无错误任务 errpath 填 `—`；确无可跑命令（纯文档轮）`cmd=文档审阅`，不得空缺整块。

## 项目承载（已就绪）
- `memory/agent-log.md`：一档制单文件四区（状态段/教训区/偏好段/流水区）——**规范件（正文从 `templates/agent-log-template.md` 复制，非空占位）**；本地承载，按项目 gitignore 约定决定是否随仓。
- **承载收敛（项目已有成熟 memory 体系时）**：既有体系（如 state / experience / preferences / task-log）为**权威承载**，`memory/agent-log.md` 作**入口档**（状态段/教训区以指针回指权威文件，仅流水区增量）——勿另起平行体系、勿双写。
- `docs/project-info.md`：六节索引（架构 / 目标 / 模块真实状态表【含关键词锚定列，details #275】/ 调研导航 / 参考资源 / 复述签章）。
- <项目特有纪律 1-3 条；本文件被合并时保留既有段落>

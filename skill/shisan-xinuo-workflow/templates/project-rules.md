# 项目级 Agent 规则 · <项目名>

> **本文件是项目级注入（每会话自动进入）**：只管「本项目特有信息 + 承载指针」，**通用义务不复述**（单一权威=注入核心，三源叠加旧病防治，细则样本#5）。由工作流「项目承载检查」自动创建/合并——文件名按 `platform-adaptation.md` §2「项目级注入点表」定名（Codex=项目根 AGENTS.md / Claude Code=项目 CLAUDE.md / Trae=`.trae/rules/project_rules.md` / Cursor=`.cursor/rules/*.mdc` / Windsurf=`.windsurfrules`；未知平台联网调研，离线降级 AGENTS.md 兜底）：存在同名既有规则文件 → **合并不覆盖 + 先备份**；不存在才新建。

## 回指（强制字段，缺失 = 不合规）
- 完整纪律（判级/红线/必问/开工四步/GATE/检索端口）**权威=注入核心与 SKILL.md**，本文件不复制正文；按需加载 Skill「shisan-xinuo-workflow」（写**注册名**，不写绝对路径）；本文件在场但 Skill 未在场 → 先加载再继续。
- 会话末：更新 `memory/agent-log.md`（流水区+状态段）后离开——不更新 = 交接断链；留档时间戳到分钟（细则 #311）。
- 多副本安装以平台侧副本为权威；漂移自检：`diff -rq` 双副本（排除 memory/user-notes/*.bak-*）零输出=一致。

## 项目纪律（只写本项目特有，<无则整节删>）
- 细则引用完整前缀 `details #N`（禁裸 #N）；Git Bash 跑 lookup 用 Windows 路径形态 `C:/...`（`/c/...` 会被 MSYS 改写）。
- 权威源顺序：注入核心 → SKILL.md → <项目权威文档> → docs/project-info.md。

## 项目承载（已就绪）
- `memory/agent-log.md`：一档制四区（规范件从 `templates/agent-log-template.md` 复制，非空占位）；项目已有成熟 memory 体系时其为权威承载、本档作入口档（指针回指，勿双写）。
- `docs/project-info.md`：六节索引（含关键词锚定列，#275）。
- <项目特有纪律 1-3 条；本文件被合并时保留既有段落>
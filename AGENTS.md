# 项目级 Agent 规则 · shisan-xinuo-workflow（本仓库）

> 本仓库 = 十三希诺 Agent 工作流 Skill 的源库与标本合库。**本文件是项目级注入**（每会话自动进入），与平台全局硬注入（injection-core，负责通用纪律）互补：项目级管「本仓库特有信息 + 项目承载 + 维护纪律」。内容精简，细节按需读 docs/project-info.md（导航）。

## 工作流在场（本仓库会话）
- 开工序列六步（与全局硬注入一致，SKILL §2.0）：①复述理解（无条件先行）②扫描工作区+形态判定 ③定承载根 ④承载创建（memory/ 骨架已建，缺则自动补）⑤读 `memory/`（state → experience-mustread → experience → preferences）⑥判级速查+三问选道；命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- 本仓库默认**不 git push**：本地 commit + 备份优先，推送须用户明确批准。
- 改 Skill 产物后：**全仓 grep 承载点口径**（细则条数/类数/版本号/在场提示）→ 跑 `scripts/verify-release.ps1`（内容锚点/hooks/版本/泄漏 4 项门禁）→ 同步各副本（`python scripts/syncer.py`，WorkBuddy 侧加 `--dest`）。
- 细则引用统一完整前缀 `details #N` / `细则 #N`（**禁裸 #N**——与 GitHub issue 编号同形异义，假阳性 9/10 实证）。
- 判级/红线权威源顺序：`references/injection-core.md`（每会话在场）→ `SKILL.md`（可执行细节）→ `项目信息.md`（决策史）→ `docs/project-info.md`（导航索引）。

## 维护纪律（本 Skill 正文 vs 史料——开发本 Skill 时的写作规范）
- 本 Skill 交付物正文（skill/ 下 SKILL.md/references/templates）只写**规则本身 + ≤1 句为什么**；版本出处 / 拍板人 / 日期 / 路测轮次只入本仓库决策史（项目信息.md / CHANGELOG / task-log / EVIDENCE），**不入 Skill 正文**。
- details 条目尾部 `*来源/晋升*` 字段与节首来源注记 = 豁免（双击晋升准入证据，史料属性合法）。
- 注入核心自包含：injection-core.md 内禁悬空跨文件指针（须自包含或写全文件名）。
- 门禁：verify-release E 项（常驻/模板面）+ 全仓 grep 承载点口径，改动后必跑。
- 新增机制条款不带版本号/拍板人署名（决策记录写项目信息.md §三）。

## 项目承载（已就绪）
- `memory/`：会话记忆（state / experience-mustread / experience / preferences / task-log）——**gitignore 本地承载，不随仓分发**。
- `docs/project-info.md`：项目导航六节（架构/目标/模块表/调研导航/参考资源/签章）。
- `项目信息.md`：决策与发布史（权威，46KB）。
- `dist/`、`versions/personal-zh/`、`.trae/`：本地/私有，不随仓分发或按 gitignore 处理。

## 本仓库底线（区别于通用纪律）
- 密钥/令牌绝不写入本仓库任何文件（verify-release 泄漏红线 D 项会拦）；机密文档仅存本机专用机密目录（位置不在此写出、不随仓，以 memory/state.md 最新记录为准）。
- 发行动作（npm / GitHub Release / Gitee / ClawHub / About）必须先获用户批准 + `verify-release` 6/6 PASS + 观测阶段。
- 下一轮路测基线 = 本版（v2.3.0）；跑前确认注入副本已重部署且新会话读到「在场提示 · v2.3.0」。

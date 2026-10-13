# 项目级 Agent 规则 · shisan-xinuo-workflow（本仓库）
> 本仓库 = 十三希诺 Agent 工作流 Skill 的源库（开发库）。**本文件是项目级注入**（每会话自动进入），与平台全局硬注入（injection-core，负责通用纪律）互补：项目级管「本仓库特有信息 + 项目承载 + 维护纪律」。内容精简，细节按需读 docs/project-info.md（导航）。

## 工作流在场（本仓库会话）
- 开工序列四步（与全局硬注入一致，SKILL §2.0，v2.6.0 简化）：①复述理解（无条件先行）②承载检查（扫描+形态判定+定承载根+建/补一气呵成，memory/agent-log.md 已建则增量补缺）③记忆对齐（读 agent-log 状态段一屏 + 按症状检索，平台原生记忆在场不重复预读）④判级速查+三问选道；命 L3（密钥/删除/迁移/发布/架构/超预算）先问。
- 本仓库默认**不 git push**：本地 commit + 备份优先，推送须用户明确批准。
- 改 Skill 产物后：**全仓 grep 承载点口径**（细则条数/类数/版本号/在场提示）→ 跑 `scripts/verify-release.ps1`（内容锚点〔含 L3 判级双源对验〕/hooks/版本/泄漏/正文净化/索引/事实对账/**判据自测**/**叙述对账**/双副本一致性 10 项门禁）→ 同步各副本（`python scripts/syncer.py`，WorkBuddy 侧加 `--dest`；family 包清单=显式数组，新包须登记）。
- 细则引用统一完整前缀 `details #N` / `细则 #N`（**禁裸 #N**——与 GitHub issue 编号同形异义，假阳性 9/10 实证）。
- 判级/红线权威源顺序：`references/injection-core.md`（每会话在场）→ `SKILL.md`（可执行细节）→ `项目信息.md`（决策史）→ `docs/project-info.md`（导航索引）。

## 维护纪律（本 Skill 正文 vs 史料——开发本 Skill 时的写作规范）
- 本 Skill 交付物正文（skill/ 下 SKILL.md/references/templates）只写**规则本身 + ≤1 句为什么**；版本出处 / 拍板人 / 日期 / 路测轮次只入本仓库决策史（项目信息.md / CHANGELOG / task-log / EVIDENCE），**不入 Skill 正文**。
- details 条目尾部 `*来源/晋升*` 字段与节首来源注记 = 豁免（双击晋升准入证据，史料属性合法）。
- 注入核心自包含：injection-core.md 内禁悬空跨文件指针（须自包含或写全文件名）。
- 门禁：verify-release E 项（常驻/模板面）+ 全仓 grep 承载点口径，改动后必跑。
- 新增机制条款不带版本号/拍板人署名（决策记录写项目信息.md §三）。
- **细则双库（2026-10-13 解冻令，取代 2026-10-10 转型期冻结；docs/transformation-plan-20261010.md §六解冻决议 + 设计档 docs/design-specs/v420-plan-unfreeze-decouple-privacy-20261013.md）**：`details.md`（条款账）零和 **405 上限**不变，新增须合并/替换旧条；踩坑教训分拣迁 `references/lessons.md`（教训账）**解冻不占 405**，入库须带 `[域]`/`[态]` 字段+反论证三问，靠生命周期代谢（修复→退役→复活回指，flows「教训生命周期与上下文卫生工作流」）；判据 j2.7/聚合器 a1.2/盲评夹具=维护态（修 bug 可以，不加层）；新增机制条款仍不带版本号/拍板人署名。

## 项目承载（已就绪）
- `memory/`：会话记忆——**gitignore 本地承载，不随仓分发**（一档制 `agent-log.md` 四区；旧五件套历史原件在 `memory/legacy-pre-v250/` 只读保留）。
- `docs/project-info.md`：项目导航六节（架构/目标/模块表/调研导航/参考资源/签章）。
- `项目信息.md`：决策与发布史（权威承载）。
- `dist/`、`versions/personal-zh/`、`.trae/`：本地/私有，不随仓分发或按 gitignore 处理。

## 本仓库底线（区别于通用纪律）
- 密钥/令牌绝不写入本仓库任何文件（verify-release 泄漏红线 D 项会拦）；机密文档仅存本机专用机密目录（位置不在此写出、不随仓，以 memory 最新记录为准）。
- 发行动作（npm / GitHub Release / Gitee / ClawHub / About）必须先获用户批准 + `verify-release` **10/10** PASS + 观测阶段。
- 当前基线 = **v4.2.0 批（细则双库解冻〔条款账零和 405 + 教训账解冻不占 405〕+教训域/态字段与生命周期协议〔active/fixed/retired，修复三要件，复活回指〕+普查批 A/B 三裁决落档〔域：通用 329/平台 77/环境 0〕+开源隐私门〔四层扫描 privacy_gate.py〕+时间戳强制场景+代拟用户言论词表机检面；上一发行态 v4.1.0 全渠道 2026-10-12，回执见 RELEASE-CHECKLIST P 节与项目信息 §五）**；上一发行态 v4.0.0 全渠道 2026-10-10，回执见 RELEASE-CHECKLIST O 节；v4.1.0 批=门禁防线+部署链+规则层定型（Phase 1-8 施工：#103 真删 406→405/W8 卖点重述/j2.7 GATE 收敛循环到绿/注释纪律/单文件重蒸馏基线 v4.1.0/对外素材〔deepswe+A-4〕/审计小件〔聚合器 a1.2 mismatch 不可比+probe_runner 退出码契约+syncer F-10/F-11+scorecard 双指标口径〕；上一发行态 v4.0.0 全渠道 2026-10-10，回执见 RELEASE-CHECKLIST O 节与项目信息 §五）**——细则 **405 条·33 类**（编号至 `#407`）+ 判据 **j2.7**（金样本 **25/25**；GATE 收敛语义「循环到绿」，JUDGELOG 变更 12）+ 门禁 **11 项**（A-K：内容锚点含 L3 判级双源对验 / hooks / 版本 / 泄漏 / 正文净化 / 索引 / 事实对账 / 判据自测 / 叙述对账 / 双副本一致性〔CI 无分发根=显式 SKIP〕/ 开源隐私门 privacy_gate 四层扫描〔`-SkipPrivacy` 仅结构校验，发行跑全量〕）+ 五个机检端口（`risk_scan` / `agent_log_rotate` / `gate_audit --gate/--high-risk/--independent-cmd` / `deploy_injection --check --hash` / `privacy_gate --check/--report/--selftest`）+ 叙述对账机制 `narrative_sync`（F8，已接线 verify I 项）。**三面校准以 sync-all 跑后回执为准**。新会话验收锚=「在场提示」版本行 + `405 条细则` + `zxc663` 应答（注入版本=会话创建时快照，**GUI 长活会话须重启应用**）。

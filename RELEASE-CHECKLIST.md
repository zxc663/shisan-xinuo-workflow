# 发行执行清单（**v3.1.0 · 本批（准备态）**；v3.0.0 发行回执见 I 节；v2.9.0 及更早批次回执要点见各节沿革行，全文在 git 历史）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.8.0 已全渠道发行（2026-09-15：GitHub Release id=388839566 / npm 2.8.0 / Gitee Release id=1144623 / About 双端 len=265 / ClawHub 1.0.16 pending；回执全文见 git 历史与本清单 v2.8.0 版）。**v2.9.0 = 2.9 修正批+续批**（独立审查 P1×11+P2×16 机制级 23 项+v11 新增四项裁决+G 清单四点调研立条 #333-#335+G 直写批 #336-#344+#295 双击转正+推荐序施工批 #345+思考链 hooks 行；细则终态 **344 条/25 类**——343/24 为转正批时点值，345 为条目上限；facts_sync 断言升级：类数=分节数+节头范围；docs/design-specs/g-items-research-290.md 调研档）。

## A. 本仓已备（2.9 批施工产出；[ ] = 终局门禁复跑后确认回填）

- [x] 版本锁 2.9.0（package.json / SKILL frontmatter / README 徽章与版本历史 / docs/project-info / reference-sources / AGENTS；项目信息 §六·四 About 口径待发行批校算）——verify C 项 PASS（2.9.0=2.9.0）
- [x] 内容 v2.9.0 全量（含 G 直写批 #336-#344+#295 双击转正+推荐序施工批 #345，细则 344）：审查 P1×11+P2×16 机制级（F-02 类数单源化/F-03 facts_sync 承载点补齐/F-04 verify A 双口径/F-06 #272 文件名/F-10 #328 判级权威锚定/F-12 #329 适用前提/F-13 #330 名词通用化/F-14 #332 适用范围+SKILL §2.0 前置门/F-17 ANCHOR 单一文件化/F-18 #327-#331 回指/F-19/F-23/F-24 索引三修/F-20 hooks 交付面四子项/F-21 --check 取 package.json/F-22 覆盖边界/F-26 install-skill 清扫/F-27 作者标识判据/F-28 路径对齐/F-29 裸 # 两豁免/F-30-1/2/3）+ v11 四项（注入快照探针提示/#327 裁决定版/#312 增量豁免/#326 适用性）+ G 清单四条（#333-#335+security §1.7）
- [x] 承载点口径（活跃 **344 条/25 类** 全仓一致；facts_sync G 项 PASS：单源 344/上限 345/类数 25/节头范围断言——推荐序施工批终态，2026-09-16 复验）
- [x] verify-release 终局复跑 7/7 ALL PASS（A 项双口径打印：PS/UTF-16 + Python/code-point 双 ≤6000；2026-09-16 复跑绿）
- [x] dist/shisan-xinuo-workflow-v2.9.0.zip 终版重打（**已于 2026-09-16 13:5x 推荐序施工批再重打**——Set-diff 双检 49=49、291,937B；python 五点实测：**#345 走查收敛判据在包＋#295 转正条在包＋#269 新 TOP 无旧 #270 残留＋PA 平台能力矩阵＋hooks 思考链行**；scripts/evals 不随 zip；**发行批复核五点半实测通过（2026-09-16 本批）**）
- [x] 五副本重部署 v2.9.0（备份 `.bak-20260916-pre-v2.9.0`）→ 严格 5/5 PASS count=344（2026-09-16 推荐序施工批后再部署复验，本发行批机证复现）；deploy 写入后自动输出探针+重启提示（v11①）
- [x] syncer 双副本 exit=0（.agents 主+.workbuddy --dest/--memory-target）；**重启 ZCode 应用+新会话探针待用户执行**（发行批前置）
- [x] 提交 main（本地 commit 098dd0b 推荐序施工批+本批回填）；**push 单独批准**
- [x] 口径修正批（2026-09-16 审查批 f75eb95+本批）：独立审查报告 docs/audit-v290-review-20260916.md——A 族口径 9 处+同族 5 处+B 族正文历史残留 3 处全修+facts_sync CARRIERS 补 AGENTS.md/reference-sources 第二形态+CHANGELOG 补段；facts_sync/verify 复跑绿。**豁免面义务：本清单=时点快照，每批次开工强制重写（防过期口径指挥发行）**
- [x] 自主循环批（2026-09-16 05:5x-07:2x，用户令「无头路测补缺口循环至 08:50」）：①审查/对比/触达审计三报告（docs/audit-v290-review、docs/comparison-v290-analysis、docs/audit-cot-touch）②**TOP 错号修复**（「响应体只消费一次」#270→细则 #269，7 活体承载点+索引移域，探针首跑揪出）③**scripts/evals 随仓**（判分器+24 用例探针 24/24——npm 卖点首获可复跑件；仓库工具层不进 dist）④五副本重部署（.bak-20260916-pre-v2.9.0）+syncer 双副本+已部署 hooks（roadtest-v260）补丁 ⑤无头路测 v12-v17 共 10 会话（EVIDENCE §三十二）⑥About §六·五 草案预置（251 字）⑦**发行批新增注意：dist 重打时 tools 须含 scripts/evals 吗——不含（evals=仓库工具层，随 GitHub 仓分发不随 zip）；injection-core 已改（#269），重打前确认 zip 内 details/injection-core 为本 HEAD 版**

## B. 全渠道发行命令清单（v2.9.0 · 待用户批准后执行 ⏳）

> 令牌供给：GitHub PAT 从机密文档（路径不写出）正则提取注入 env（`ghp_`），命令串与输出全程不含明文，用毕即清；**提取→注入→执行必须同一命令内完成**。GitHub 全部走代理 `http://127.0.0.1:33210`。

| # | 渠道 | 命令要点 | 状态 |
|---|---|---|---|
| 1 | push | `git push origin main` + `git tag v2.9.0 <commit> && git push origin v2.9.0`（走代理） | ✅ 2026-09-16（commit c947280） |
| 2 | GitHub Release | 创建 Release v2.9.0（要点取 CHANGELOG 行）+ 上传 dist zip（`uploads.github.com` + `-L`） | ✅ id=389686193（zip asset id=567360240, 291,937B） |
| 3 | npm | `$env:GITHUB_TOKEN=<令牌>; npm publish`（`.npmrc` 变量引用法）——description 已校 344/25 类口径 | ✅ @zxc663/shisan-xinuo-workflow@2.9.0（38 文件） |
| 4 | ClawHub | 提交 v2.9.0 更新（1.0.x 递增；先复查 1.0.14/1.0.15/1.0.16 scans） | ✅ 1.0.17 已提交（pending-publication，scans 复查待办） |
| 5 | About | 双端 PATCH（项目信息 §六·四 压缩版，发行时校算 ≤350） | ✅ GitHub+Gitee len=251（六·五 344/25 口径） |
| 6 | Gitee | push/tag v2.9.0 + Release + About（32-hex 令牌） | ✅ push+tag+Release id=1147118（zip 附件 id=3209813）+About len=251 |
| 7 | PAT 轮换 | 发行完成即 GitHub classic PAT 轮换（用户侧） | ⏳ 用户侧 |

## C. 复用要点（v2.6.0-v2.8.0 实证沿用）

- About description 限 350 字符（GitHub API 422）——发行时 `python -c` 校算 len ≤350；**新 description 含 344/25 口径，压缩版需重算（六·五 草案实测 251 字符 ≤350）**。
- dist 打包 `scripts/build-dist.ps1`（版本号读 package.json；Set-diff 双检）；Release 资产上传走 `uploads.github.com` + `-L`；REST JSON body 无 BOM UTF8。
- npm publish 用 GITHUB_TOKEN 环境变量法。
- 泄漏扫描面=git tracked 全量（豁免 scripts/ 自引用+历史过程档；作者标识判据=security.md §5——F-27）。
- **deploy --check 缺 --version 自动取 package.json 严格校验（F-21 修复生效；显式传 --version 仍推荐）**。
- **发行后须重启 ZCode 应用**——注入版本=会话创建时快照（v11 机制定论）；deploy 写入完成自动输出探针+重启提示（v11①）。
- 验收看平台解析到的 Base directory，非文件版本号（#239）。
- 在场提示锚块单一权威源=templates/memory-anchor.md（F-17；deploy/syncer/install-skill 三方同源读取，改锚先改模板）。

## D. 发行后校准清单（预注册探针）

1. **本地注入探针**：重启 ZCode 应用 → 新开会话确认「在场提示 · v2.9.0」+ 复述/状态行首产物 + 细则 344 条口径在场 + `zxc663` 应答版本 v2.9.0。
2. **GitHub**：`git ls-remote origin refs/tags/v2.9.0` 在场；Release id 回执 + dist zip 字节一致。
3. **npm**：`npm view @zxc663/shisan-xinuo-workflow@2.9.0` —— version=2.9.0 + description 含「344 条细则 25 类」。
4. **About**：desc_len 回执 ≤350。
5. **Gitee**：tag/Release/About 三件回执。
6. **ClawHub**：scans 通过复查（1.0.14/1.0.15/1.0.16 遗留 + 2.9.0 提交）。
7. **WorkBuddy H0**：用户侧新会话输 `zxc663` → 源库 v2.9.0 vs 副本 v2.9.0 / Base directory。
8. **回执写回**：B 表状态列 → 项目信息 §五 → CHANGELOG v2.9.0 行改「已全渠道发行」→ README 发行状态表 → agent-log 流水。

## E. 发行前现状校准

- v2.8.0 全渠道已发行（回执见 git 历史版本清单）；ClawHub 1.0.14/1.0.15/1.0.16 scans pending 遗留。
- GitHub classic PAT 未轮换（用户侧遗留最高优先）。
- 本批路测续跑已完成（2026-09-16：S-B′/S-A′ 余轮/压缩测针/S-D′，EVIDENCE §三十一）——顺序约束已解除，重部署段执行完毕。

## F. v3.0.0 发行批增量（本批施工面）

- **交付物形态**：三包体系——`shisan-xinuo-workflow`（核心）+ `shisan-xinuo-flows`（流程包）+ `shisan-xinuo-roles`（角色包）；三包 `name/version` 与 `package.json` 一致（verify-release A 项家族包断言）。
- **口径基线（本批）**：活跃细则 **366 条**（条目编号至 #367，预留/归档槽不计入）/ **28 类**；注入核心双口径 ≤6000 字符；GATE **12 字段**定版（新增 `stop_reason`）。
- **待重打**：`dist/shisan-xinuo-workflow-v3.0.0.zip`（`scripts/build-dist.ps1`）；npm 侧 description 口径同步「366 条细则 28 类」。
- **迁移说明**：CHANGELOG v3.0.0 行（本档同批）+ 升级指南见 G 节。
- **About 双端**：desc_len ≤350，含三包体系与 366/28 口径。

## G. 升级指南（v2.9.0 → v3.0.0）

1. **取包**：npm/GitHub 用户 `npx skills add zxc663/shisan-xinuo-workflow`；本地源库用户 `python scripts/syncer.py`。
2. **注入副本重部署**：`python scripts/deploy_injection.py --only <平台>`（本批五平台：codex/claude/trae/workbuddy/zcode）；部署后**重启对应应用 + 新开会话**，验收「在场提示 · v3.0.0」+ `zxc663` 应答（注入版本=会话创建时快照）。
3. **包拆分升级**：flows/roles 为新增独立包（可选装）；已装核心者用 `python scripts/syncer.py --family` 同步三包。
4. **hooks 副本**：`templates/hooks/carrier_reminder.example.py` 升级至 12 字段 + 思考链钩子；已部署副本须同步（config 指向仓外脚本——改模板≠改副本）。
5. **兼容性**：v3.0.0 内容 = v2.9.0 的超集（骨架重排 + 条款增补），无破坏性接口变更；GATE 11→12 字段为增量，旧 GATE 行仍可读。

## H. 部署后行为面 A/B 复测（V7 · 部署批验收判分项）

- **基线**：v2.9.0 旧副本 52 探针 **51 PASS = 98.1%**（分析见夜班报告 A13/G11）；v3.0.0 注入后 19 场景批 **18/19 PASS**（唯一 FAIL=skip-floor「下限未达未照报」，双击复采 ×2 后判为单例方差）。
- **复测命令**：`python scripts/probe_runner.py --label v300-ab all`（同夹具同判据；harness 默认探针根落系统临时目录，仓外隔离）。
- **预期改善点**：`multi-task`（L 类灰色带）、`skip-floor`（下限未达=照报）、`gate-fields`（12 字段覆盖）。
- **判据**：复测结果与基线同表并列写入 EVIDENCE；**改善/持平/退化**三态显式标注，退化即回滚候选。
- **scorecard 归档**：`docs/roadtest-scorecards/<标签>.jsonl`（随仓分发，形成跨夜可比时序库）。
- **复测结果（2026-09-19 夜班回填·截至本日 09:00 中期快照，全文=EVIDENCE §三十五）**：有效样本 76 针（边界 ts<04:28:57 换面 v3.1.0 前；作废 29 行=provider 瞬时窗）——**j1 口径 66/76=86.8%；剔除判据滞后 8 行后行为面 74/76=97.4%** vs 基线 98.1%＝**持平**。三态：改善=skip-floor 2/2（基线唯一 FAIL 转 PASS）+ambiguous 行为面 6/6；持平=l3 家族/对抗变体/承载/交付面全绿；退化候选（待晨裁非定论）=multi-task 1 例行为 FAIL（**Loop-16 重开候选达双击**）、rat-obvious j1 2/8（判据效应为主，j2.1 已回植拒改取证路径）、vague-auth 1 例（判据滞后）、cap-web 1 例（env 方差待归因）。**不触发回滚**（行为面持平；退化候选全部有判据/方差归因路径）。

## I-1. v3.1.0 发行回执（2026-09-19）

| # | 渠道 | 结果 |
|---|---|---|
| 1 | push | GitHub `892b3e4..ad3f876`（main）+ tag `v3.1.0`；Gitee 同 commit/tag |
| 2 | GitHub Release | `v3.1.0` · asset `shisan-xinuo-workflow-v3.1.0.zip`（含「已发行」态重打终版，332,763B） |
| 3 | npm（GitHub Packages） | `@zxc663/shisan-xinuo-workflow@3.1.0`（45 文件，shasum `e1ede926…`） |
| 4 | ClawHub | `1.0.19` 已提交（pending security scans，平台侧待过审） |
| 5 | About | GitHub + Gitee description PATCH，双端 len=191（项目信息 §六·七 口径） |
| 6 | Gitee Release | id=1153127（tag v3.1.0；附件 3225663 首版已删 → 终版 id=3225756 / 332,763B） |
| 7 | 门禁与发布物 | 发行前 `verify-release.ps1` **8/8** ALL PASS + `facts_sync` PASS（**368 条/29 类**）+ `--judge-selftest` **21/21**（j2.4）；dist zip 60 项、发布物内 0 泄漏；五平台注入重部署 `--check` 5/5 v3.1.0/368 |

## I-2. v3.0.0 发行回执（2026-09-18）

| # | 渠道 | 结果 |
|---|---|---|
| 1 | push | GitHub `1050345..05c5cbe`（main）+ tag `v3.0.0`；Gitee 同 commit/tag |
| 2 | GitHub Release | `v3.0.0` · asset `shisan-xinuo-workflow-v3.0.0.zip` 298,714B（digest `sha256:6f1c4c31…`；含「已发行」态重打终版） |
| 3 | npm（GitHub Packages） | `@zxc663/shisan-xinuo-workflow@3.0.0`（45 文件，shasum `458b39ed…`） |
| 4 | ClawHub | `1.0.18` 已提交（status=pending-publication，versionId `k97akj6f…`，23 文件） |
| 5 | About | GitHub + Gitee description PATCH，双端 len=150（项目信息 §六·六 口径） |
| 6 | Gitee Release | id=1150915（tag v3.0.0；附件 id=3219693 / 298,714B） |
| 7 | 门禁与发布物 | 发行前 `verify-release.ps1` 7/7 ALL PASS + `facts_sync` PASS（366 条/28 类）；dist zip 58 条目、发布物内 0 泄漏（唯一命中=门禁脚本自身正则，既有豁免） |

**残留在办**：ClawHub scans 复查（1.0.14-1.0.18）；GitHub classic PAT 轮换（用户侧）；部署后 A/B 复测已回填（H 节+ EVIDENCE §三十五，2026-09-19 夜班中期快照；退化候选 4 项待晨裁）。

---

## J. v3.1.0 发行批清单（**已执行** · 2026-09-19 发行；回执见 I-1 节）

### J-1 准备态已完成（源库侧，本地 commit 不 push）

| # | 项 | 状态 | 证据 |
|---|---|---|---|
| 1 | 判据可信度批施工（判据版本化/金样本回归/指纹/分型/聚合器/判据史） | ✅ | `scripts/probe_runner.py`（**j2.4**）、`scripts/scorecard_agg.py`、`docs/roadtest-scorecards/JUDGELOG.md` |
| 2 | 两处裁决落地（multi-task 维持 FAIL / `verify_trace`+`effort` 去自满足） | ✅ | 判据自测负对照 `rat-obvious/modified-no-verify` 必 FAIL |
| 3 | 细则 #368/#369 立条 + 全承载点同步 | ✅ | `facts_sync --check` PASS（活跃 **368** / 上限 **369** / 类数 **29**） |
| 4 | 口径校对（README 主口径行/条目上限入断言；verify 7→**8 项**） | ✅ | 补口前 `FACTS FAIL 4 处` → 修后 PASS |
| 5 | README 按项目实质重构（口径块/原理/证据/用法，含 v3.1 判据可信度节） | ✅ | `README.md`（形态冒烟首行断言通过） |
| 6 | Skill 本体净化 + 版本升板 3.1.0（三包 frontmatter + package.json） | ✅ | `verify` C 项：SKILL version=3.1.0；A 项家族包三包一致 |
| 7 | 发行材料（CHANGELOG / 发行说明 / About 草案 / 升级指南） | ✅ | `CHANGELOG.md`、`docs/release-notes-v3.1.0.md`、`项目信息.md` §六·七、G 节 |
| 8 | dist 重打（v3.1.0 zip）+ 发布物泄漏 0 | ✅ | `scripts/build-dist.ps1` |
| 9 | 门禁终局 | ✅ | `verify-release` **8/8** + `facts_sync` PASS + `--judge-selftest` **21/21**（j2.4） |
| 10 | 平台注入副本重部署（五平台）+ 新会话验收 | ⏳ 见 J-2 | `scripts/deploy_injection.py`、`scripts/syncer.py --family` |

### J-2 已执行（2026-09-19；逐项回执=I-1 节）

1. ✅ 门禁终局：`verify-release` **8/8** + `facts_sync` PASS（368/369/29）+ `--judge-selftest` **21/21**（j2.4）。
2. ✅ dist 重打：`build-dist.ps1` → 60 项 zip，Set-diff 60=60 + 发布物 0 泄漏（verify D 项）。
3. ✅ 注入副本重部署：五平台 PASS（备份 `.bak-20260919-131927-pre-v3.1.0`）+ `--check` **5/5 v3.1.0/368** + `syncer --family`。
4. ✅ 发行（用户批准）：GitHub push `892b3e4..ad3f876` + tag `v3.1.0` + Release → npm 3.1.0（45 文件）→ Gitee（Release 1153127+附件）→ ClawHub 1.0.19（pending scans）→ About 双端 PATCH len=191。
5. ✅ 发行物终版重打：已发行态校准写回后重打 + 双端资产替换（沿 v3.0.0 同型；GitHub clobber + Gitee 附件替换）。

### J-3 v3.1.0 口径（发行时校对用）

- 细则 **368 条 / 29 类**（编号至 `#369`）；注入核心 ≤6000 字符双口径；`GATE` **12 字段**定版。
- 门禁 **8 项**；判据金样本回归 **21/21**（正例 8 / 负例 13）；无头全矩阵 **20/20**（判据 j2.4）；v3.1.0 部署后无限循环实跑 **24 针 22 PASS**（判据 j2.2，唯一矩阵级 FAIL=skip-floor 判据滞后 → j2.3/j2.4 修订后重判 20/20）。
- 三包版本 3.1.0（core / flows / roles）。

## K. 评审提案落刀批（2026-09-20 · **源库态，未部署未发行**）

**当前源库口径（≠ 已部署副本）**：细则 **373 条 / 30 类**（编号至 `#374`）；判据 **j2.5**（金样本 **23/23**，正 9 / 负 14）；`GATE` **12 字段**定版 + 可选 `ev=` 验证层级；注入核心 ≤6000 字符双口径（去 CR 口径实测 5948，余量 52）。

**新增机检端口**：`risk_scan.py`（#370）· `agent_log_rotate.py`（#372）· `gate_audit --gate/--high-risk/--independent-cmd`（#371）· `deploy_injection --check --hash`（#374）· `scorecard_agg --exclude-recollect`。

**未执行项（预期态，勿误读为缺陷）**：

- [ ] 五平台注入副本**未重部署** → `deploy_injection --check` 与 `--hash` **预期红**（副本仍 v3.1.0/368、哈希 `HASH-DRIFT`）；重部署后应恢复 5/5 + `HASH-OK`。
- [ ] 版本号未 bump（源库仍 3.1.0），发行面未动；如要对外呈现本批，需按发行流程单独批准。
- [ ] `ev=` 未对存量高风险场景追溯加严；`risk_scan.py` 召回率/误报率未实测。
- [ ] P-C 归档后未做新会话续接走查；P-D 盲评为设计档未跑批。

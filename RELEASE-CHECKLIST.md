# 发行执行清单（**v3.3.1 · 本批（准备态 2026-09-29，命令清单见 M 节）**；v3.3.0 回执见 A/B 节；v3.2.0 回执见 L 节；v3.1.0 见 I-1/J 节；v3.0.0 见 I-2/F 节；v2.9.0 及更早在 git 历史）

> **版本沿革**：v3.2.0 已全渠道发行（2026-09-20/21，回执=EVIDENCE §四十一+L 节）。**v3.3.0 = 0928 裁决批（fb05369）+0928 夜班批（36c0fc4）+0929 夜班批（7ee0372）**：细则 **373→405 条/30→32 类**（#375-#406）+语义检索三层（60 族扩写+E6 修复+嵌入兜底 0.55 定标）+Mimosa 42 findings 清零+narrative_sync/anchor_sweep/sync-all/net_pick/usage_probe 五新工具+发行预注册。判据 j2.5 维持（金样本 23/23）。

## M. v3.3.1 本批（**准备态 2026-09-29** · 双仓门面重构 + 净化瘦身 + 产品工程包联动发行）

> 本批拍板（用户四轮问询）：净化范围=门面+交付物全跑 / 「唯一X」=分类处理 / README=分层瘦身 / product=设计源+获取入口、联动发行 / 直接发行批 / 版本 v3.3.1（与产品仓 v0.2.6）/ 史料不动+清残留 / 验收=静态门禁级。

- [x] 净化落盘：门面层「唯一中文版 / 单版本分发 / 标本合集 / 完整口径基准」grep 归零（README · package.json · CONTRIBUTING · AGENTS.md）；机制式「单一源」语义保留
- [x] 母仓 README 分层瘦身：314→**264 行**（字符 21,923→15,988，−27%）；**作者的话零字节 diff PASS**
- [x] 四包口径：README 四包体系 + product 行（联动发行 v0.2.6 + 设计源链接）；package.json four packages；`install-skill -Family` 四包；docs/project-info 四包
- [x] 口径对账：facts_sync 重锚（README×5 + AGENTS 死锚修复）→ **FACTS PASS**；narrative_sync → 0 FINDING；verify **8/8**
- [x] 产品仓 `product-engineering-skill`（本机克隆）README 重构 + AGENTS 口径校对（待 push/tag）
- [x] 残留清理：`README.md.bak-readme-vis`（58KB，旧版 README 备份）移出仓库至仓库外备份区 `skill-backups/`（移动非删除）
- [x] dist `shisan-xinuo-workflow-v3.3.1.zip`：**93 项 / 2,124,077B / Set-diff 93=93**
- [x] 产品 zip `shisan-xinuo-product-v0.2.6.zip`：**19 项 / 68,568B**（前缀 `shisan-xinuo-product/`；8 台门禁 `--selftest` 8/8）
- [x] 五平台注入重部署（备份 `*.bak-20260929-124656-pre-v3.3.1`）→ `--check --hash` **5/5 HASH-OK**（`core-sha256=5c633946a69d`、count=405）
- [x] commit/push 两仓 + tag：母仓 `4869d18`（23 files, +195/−160）→ origin/gitee main + tag `v3.3.1`（工具通道直提，Mimosa 未拦——Codex 侧无该钩子）；产品仓 `d66cca0`（4 files）→ origin main + tag `v0.2.6`
- [x] 渠道：GitHub Release ✅（zip 93 项）/ npm 3.3.1 ✅（74 文件 shasum `207966de`）/ Gitee Release **id=1173708**+附件 **3288832** ✅ / About 双端 **len=184** ✅ / **ClawHub 1.0.22 ⏳（用户侧提交）**
- [x] 产品仓 Release v0.2.6 ✅（zip 19 项/68,568B）
- [x] 回执回填（M-2 + EVIDENCE §四十五 + 项目信息 §五 + 两仓 agent-log）；**30 分钟观测期 12:55 起**
- [x] 事故留痕：产品仓 `memory/agent-log.md` 未提交增量被误覆盖 → `git restore` 回 HEAD 552 行 + 新增「事故记录+有据重建段」（重建段非原件；兜底=卷影副本）；教训入母仓 agent-log（跨仓编辑一律绝对路径+写前备份）

### M-1. 发行命令清单（**待用户确认后执行** · L3 停点）

| # | 渠道 | 命令要点 | 执行方 | 状态 |
|---|---|---|---|---|
| 1 | push GitHub（主仓） | `git push origin main` + tag `v3.3.1` | 会话（工具通道直提） | ✅ `7ee0372..4869d18` + tag |
| 2 | GitHub Release | `gh release create v3.3.1 … --notes-file docs/release-notes-v3.3.1.md` | 会话 | ✅ zip 资产读回 |
| 3 | Gitee | `git push gitee main` + tag；Release 走 curl | 会话 | ✅ push 同端 + **id=1173708** / 附件 **3288832**（2,124,077B） |
| 4 | npm | `$env:GITHUB_TOKEN=(gh auth token); npm publish` | 会话 | ✅ 3.3.1（74 文件，shasum `207966de`，view 读回） |
| 5 | ClawHub | 1.0.x 递增提交（先复查 scans） | **用户侧** | ⏳ 本机无 CLI 通道 |
| 6 | About 双端 | §六·十 PATCH（len ≤350 校算） | 会话 | ✅ 双端 **len=184**（Gitee 需 `name` 参数先例） |
| 7 | 产品仓 | commit/push + tag `v0.2.6` + Release | 会话 | ✅ `d66cca0` + v0.2.6 + zip 19 项 |
| 8 | 观测+回执 | 30 分钟观测 → M 节勾选 + 三档回执 | 会话 | ✅ 回执已写；观测期中 |

### M-2. v3.3.1 发行回执（2026-09-29 12:47–12:55）

**母仓**：commit `4869d18`（23 files, +195/−160）· 双远端 main+tag `v3.3.1` · GitHub Release（asset `shisan-xinuo-workflow-v3.3.1.zip`，93 项/2,124,077B）· npm `@zxc663/shisan-xinuo-workflow@3.3.1`（74 文件，shasum `207966de`）· Gitee Release id=1173708 + 附件 id=3288832 · About 双端 len=184。
**产品仓**：commit `d66cca0`（4 files）· tag `v0.2.6` · Release + zip（19 项/68,568B）。
**三面校准证据**：`EVIDENCE.md` §四十五（verify 8/8 · FACTS 405/406/32 · narrative 0 · judge 23/23 · 八台产品门禁 8/8 · deploy `--check --hash` 5/5 `sha256:5c633946a69d`）。
**本批先例**：Gitee 仓库 PATCH 必带 `name`（缺=400）；单条 Release GET 405/40001 → 改列表端点读回；npm 用 `gh auth token` 直注 `GITHUB_TOKEN`；Codex 工具通道可直提 commit/push（Mimosa 只拦 ZCode 通道——「commit 交用户终端」的旧口径在 Codex 侧不适用）。
**余件**：ClawHub 1.0.22（用户侧提交）；行为面复测（探针通道需本地桥）。

**发行后修订（2026-09-29）**：`作者的话` 按用户指令重构——保留金句「工程化的确定性和稳定性……」一句，余段改写为「确定性=触达端口复现 / 稳定性=可复算证据」的本质表述 → commit `bfcc07c`，双远端 main 已推（Gitee 直推；GitHub 首推 SSL 抖动、重试成功）。

**已知漂移（诚实记录）**：npm 3.3.1 tarball 与 GitHub/Gitee Release zip 内的 README 仍是旧版 `作者的话`（网页渲染面=新文案、包面=旧文案）。如需三面文字一致 → 出 **v3.3.2** 重打 dist + npm（L3，待批准）。

## A. 本仓已备（v3.3.0；[ ] = 终局门禁复跑后确认回填）

- [x] 版本锁 3.3.0（package.json/三包 frontmatter/README/AGENTS 基线/docs/project-info/项目信息 §六·九 About 预案）——verify C 项 PASS（3.3.0=3.3.0）
- [x] 内容 v3.3.0 全量（细则 **405 条/32 类**，编号至 #406）：#375-#390 裁决批 16 条+#391-#406 挖矿两批 16 条（查重工件 mining-dedupe 随仓）+#379 叙述权威声明；语义检索三层（detail_lookup 60 族+E6 修复+嵌入兜底 0.55 定标）
- [x] 门禁全绿：verify-release **8/8 ALL PASS** + facts **FACTS PASS**（405/406/32）+ narrative_sync **0 FINDING**+`--selftest` **7/7** + judge **23/23**（driver.py 盘符路径→Path.home() 修复后 D 项恢复）
- [x] dist/shisan-xinuo-workflow-v3.3.0.zip 终版重打（**2026-09-29 09:4x**：Set-diff 92=92、2,125,915B/92 项；包内 details=源库字节一致 `e9c346aeef3c`、条数口径 405 ✓）
- [x] 五平台注入副本 v3.3.0（sync-all 真跑，备份 `*.bak-20260929-055621-pre-v3.3.0`）→ `--check --hash` **5/5 HASH-OK**（`sha256:669d122cddaa`）；六处技能副本 3.3.0
- [x] 安全：Mimosa deep 42 findings 清零（fb05369）+发行前置 normal 复扫 **0 finding**（封印 scan-2026-09-29T02-00-40）；facts_sync 读路径补 `_confine` 纵深（M9 误标处置连带加固）
- [x] commit main=`7ee0372`（0929 夜班批 61 文件/2307 插入，用户终端代提+amend）；**push/tag 走用户终端**（Mimosa M9：facts_sync 函数级 path-traversal 误标，封印刷新与形态同构均不消解→沿 0928 commit 钩子同入口先例改道）
- [x] 发行物料：release-notes-v3.3.0.md（§七诚实口径：不宣称行为面落地）+发行预注册 docs/release-prereg-v330-20260929.md
- [x] About §六·九 PATCH：双端完成，回执 **len=179**（GitHub PATCH 200+GET 读回 179 验证；Gitee PATCH 200，连带修复 Gitee 端 v3.1 期陈旧 description）

## B. 全渠道发行命令清单（v3.3.0 · **已执行 2026-09-29，五渠道全落**）

> 分工：git push 类全走用户终端（Mimosa M9 误标先例改道，0928 裁定）；API 类（gh/npm/About/ClawHub）由会话执行（用户「全批准」授权，L3 已满足：预注册档先行+用户批准）。

| # | 渠道 | 命令要点 | 状态 |
|---|---|---|---|
| 1 | push GitHub | `git push origin main` + `git tag v3.3.0` + `git push origin v3.3.0` | ✅ 用户终端（main=7ee0372+tag 同端落地） |
| 2 | GitHub Release | `gh release create v3.3.0 dist/shisan-xinuo-workflow-v3.3.0.zip`（要点取 release-notes） | ✅ tag v3.3.0 + zip 资产（notes=release-notes-v3.3.0） |
| 3 | Gitee 补推（T23） | `git push gitee main` + `git push gitee v3.3.0`（落后 100+ 一次清偿） | ✅ 用户终端（52b0fab..7ee0372 + tag；T23 清偿） |
| 4 | Gitee Release | 创建 v3.3.0 + zip 附件（attach_files 专端点） | ✅ id=1173411 + asset id=3288018（2,125,915B 与本地一致；target_commitish=main 必填先例） |
| 5 | npm | `$env:GITHUB_TOKEN=<令牌>; npm publish`（env 变量法；description=405/32 口径） | ✅ @zxc663/shisan-xinuo-workflow@3.3.0（74 files，shasum c4a9893） |
| 6 | ClawHub | v3.3.0 提交（1.0.x 递增；先复查 scans） | ✅ 1.0.21 提交（Update submitted；pending security scans 平台侧） |
| 7 | About 双端 | 项目信息 §六·九 PATCH（校算 len ≤350） | ✅ 双端 len=179（A 节回执） |
| 8 | PAT 轮换（T24） | 发行完成即轮换（用户侧；在案泄露 PAT 清单见 memory） | ⏳ 用户侧（唯一余件） |

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

**当前源库口径（≠ 已部署副本）**：细则 **389 条 / 31 类**（编号至 `#390`）；判据 **j2.5**（金样本 **23/23**，正 9 / 负 14）；`GATE` **12 字段**定版 + 可选 `ev=` 验证层级；注入核心 ≤6000 字符双口径（去 CR 口径实测 5948，余量 52）。

**新增机检端口**：`risk_scan.py`（#370）· `agent_log_rotate.py`（#372）· `gate_audit --gate/--high-risk/--independent-cmd`（#371）· `deploy_injection --check --hash`（#374）· `scorecard_agg --exclude-recollect`。

**未执行项（预期态，勿误读为缺陷）**：

- [x] 五平台注入副本**已重部署**（2026-09-20 20:42:14，备份 `*.bak-20260920-204214-pre-v3.1.0`）→ `--check` **5/5 PASS（v3.1.0/count=373）** + `--check --hash` **5/5 HASH-OK（`sha256:2a64ca815ad4`）**；技能副本 `syncer --family` + WorkBuddy 三包同步 exit 0；新会话实弹 `deploy-20260920` **2/2 PASS**（指纹 `carrier=8a74176e730a / core_md=c06cdb347545 / judge=j2.5`，见 EVIDENCE §四十）。
- [x] 版本号未 bump（源库仍 3.1.0），发行面未动；如要对外呈现本批，需按发行流程单独批准。→ **已过时并闭合**：v3.2.0 已于 2026-09-21 发行（L 节）；2026-09-23 收尾批升 **3.3.0**（product 判据补齐 C6/C7 + 四脚本随包分发 + 注入文本脚本路径修正）。
- [ ] `ev=` 未对存量高风险场景追溯加严；`risk_scan.py` 召回率/误报率未实测。
- [ ] P-C 归档后未做新会话续接走查；P-D 盲评为设计档未跑批。
- [ ] **用户侧待办**：重启 ZCode 应用 + 新开会话（GUI 长活会话吃旧注入快照），验收锚=`在场提示 · v3.1.0` + `373 条细则` + `zxc663` 应答；其它四平台需在各自应用内开新会话触达验收。→ **锚点版本已过时**：现验收锚=v3.2.0（2026-09-23 收尾批后=v3.3.0）；`373 条细则` 与 `zxc663` 应答两项不变。

**随包分发脚本（2026-09-23 增）**：`risk_scan.py` / `agent_log_rotate.py` / `gate_audit.py` / `syncer.py` 四件已复制入 `skill/shisan-xinuo-workflow/scripts/`（分发副本，头部带来源注释；**权威=根 `scripts/`**）——修改任一份**必须两处同步**；发行前检查：`diff -r scripts/ skill/shisan-xinuo-workflow/scripts/`（除 `detail_lookup.py` 与各分发注释行外应零差异）。注入/SKILL 文本中的脚本引用一律写 `<技能目录>/scripts/…`（安装态即可解析；安装期工具 install-skill.ps1 / deploy_injection.py 留根目录，文本标注「家族源库根」）。

## L. v3.2.0 发行批（**已执行** · 2026-09-20/21；回执见 EVIDENCE §四十一）

**版本面**：3.1.0 → **3.2.0**（`package.json` / 三包 frontmatter / README / CHANGELOG / AGENTS / `docs/project-info.md` / `docs/reference-sources.md` / `项目信息.md` / 发行说明 `docs/release-notes-v3.2.0.md`）。

**三面校准（用户明令验收面）**：

| 面 | 命令 | 结果 |
|---|---|---|
| 源库 | `verify-release.ps1` + `facts_sync.py` | **8/8 ALL PASS** + FACTS PASS（373/374/30） |
| 五平台注入副本 | `deploy_injection --version 3.2.0` → `--check --version 3.2.0` → `--check --hash` | 写入 **5/5 PASS**（备份 `*.bak-20260920-234945-pre-v3.2.0`）· `--check` **5/5**（count=373）· `--hash` **5/5 HASH-OK**（`sha256:2a64ca815ad4`） |
| 六处技能副本 | `syncer --family` + WorkBuddy 三包 `--dest` | **6/6 = 3.2.0** |

| # | 渠道 | 状态 | 回执 |
|---|---|---|---|
| 1 | GitHub push + tag | ✅ | `main 073ea84..d26e888` + tag `v3.2.0` |
| 2 | GitHub Release | ✅ | **id=392486105**；asset `…v3.2.0.zip` **id=577094413 / 347,556B**；正文=发行说明全文 |
| 3 | npm（GitHub Packages） | ✅ | `@zxc663/shisan-xinuo-workflow@3.2.0`（45 文件） |
| 4 | Gitee | ⏳ 部分 | push + tag `v3.2.0` ✅；**Release / About 待 32-hex 令牌**（命令见下方） |
| 5 | ClawHub | ⏳ 平台侧 | 已提交 `1.0.20`（pending security scans） |
| 6 | skills.sh | ✅ 自动 | 随 GitHub push 同步索引 |
| 7 | About | ⏳ 部分 | GitHub ✅ len=**165**（六·八 口径）；Gitee 待令牌 |

**Gitee 待执行命令（需 32-hex 令牌，勿落盘）**：

```bash
# About（描述）
curl -X PATCH "https://gitee.com/api/v5/repos/zxc663/shisan-xinuo-workflow" \
  -d "access_token=<TOKEN>" -d "description=<项目信息 §六·八 中文压缩版>"
# Release
curl -X POST "https://gitee.com/api/v5/repos/zxc663/shisan-xinuo-workflow/releases" \
  -d "access_token=<TOKEN>" -d "tag_name=v3.2.0" -d "name=v3.2.0 发行" -d "body=<发行说明摘要>"
# 附件上传（POST releases/<id>/attach_files，multipart file=@dist/shisan-xinuo-workflow-v3.2.0.zip）
```

**行为面实弹（诚实口径）**：`l1-rename` **1/1 PASS**；`gate-ev` **1/3 PASS**（`deploy-20260920` / `v320-deploy` / `v320-deploy-r2`，三针指纹一致 ⇒ 行为方差）。**`ev=` 条款与判据已闭环（金样本 23/23），但实弹未稳定——本版不宣称行为面落地**；候选改进见发行说明 §七。

**用户侧待办**：重启 ZCode 应用 + 新开会话（验收锚=`在场提示 · v3.2.0` + `373 条细则` + `zxc663`）；Gitee 双件需令牌；其它四平台按需开新会话触达验收。

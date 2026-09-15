# 发行执行清单（v2.9.0 · 批次施工完成待发行；上版 v2.8.0 回执要点见版本沿革行，全文在 git 历史）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.8.0 已全渠道发行（2026-09-15：GitHub Release id=388839566 / npm 2.8.0 / Gitee Release id=1144623 / About 双端 len=265 / ClawHub 1.0.16 pending；回执全文见 git 历史与本清单 v2.8.0 版）。**v2.9.0 = 2.9 修正批**（独立审查 P1×11+P2×16 机制级 23 项+v11 新增四项裁决+G 清单四点调研立条；细则 333 条/24 类；facts_sync 断言升级：类数=分节数+节头范围；docs/design-specs/g-items-research-290.md 调研档）。

## A. 本仓已备（2.9 批施工产出；[ ] = 终局门禁复跑后确认回填）

- [x] 版本锁 2.9.0（package.json / SKILL frontmatter / README 徽章与版本历史 / docs/project-info / reference-sources / AGENTS；项目信息 §六·四 About 口径待发行批校算）——verify C 项 PASS（2.9.0=2.9.0）
- [x] 内容 v2.9.0 全量：审查 P1×11+P2×16 机制级（F-02 类数单源化/F-03 facts_sync 承载点补齐/F-04 verify A 双口径/F-06 #272 文件名/F-10 #328 判级权威锚定/F-12 #329 适用前提/F-13 #330 名词通用化/F-14 #332 适用范围+SKILL §2.0 前置门/F-17 ANCHOR 单一文件化/F-18 #327-#331 回指/F-19/F-23/F-24 索引三修/F-20 hooks 交付面四子项/F-21 --check 取 package.json/F-22 覆盖边界/F-26 install-skill 清扫/F-27 作者标识判据/F-28 路径对齐/F-29 裸 # 两豁免/F-30-1/2/3）+ v11 四项（注入快照探针提示/#327 裁决定版/#312 增量豁免/#326 适用性）+ G 清单四条（#333-#335+security §1.7）
- [x] 承载点口径（活跃 333 条/24 类 全仓一致；facts_sync G 项 PASS：单源 333/上限 335/类数 24/节头范围断言）
- [x] verify-release 终局复跑 7/7 ALL PASS（A 项双口径打印：PS/UTF-16 + Python/code-point 双 ≤6000；2026-09-16 复跑绿）
- [x] dist/shisan-xinuo-workflow-v2.9.0.zip 重打 + Set-diff 双检（49 项/283,366B，49=49）
- [x] 五副本重部署 v2.9.0（备份 `.bak-20260916-pre-v2.9.0`）→ 严格 5/5 PASS count=333；deploy 写入后自动输出探针+重启提示（v11①）
- [x] syncer 双副本 exit=0（.agents 主+.workbuddy --dest/--memory-target）；**重启 ZCode 应用+新会话探针待用户执行**（发行批前置）
- [x] 提交 main（本地 commit e0d24e8 路测收官+本批回填）；**push 单独批准**

## B. 全渠道发行命令清单（v2.9.0 · 待用户批准后执行 ⏳）

> 令牌供给：GitHub PAT 从机密文档（路径不写出）正则提取注入 env（`ghp_`），命令串与输出全程不含明文，用毕即清；**提取→注入→执行必须同一命令内完成**。GitHub 全部走代理 `http://127.0.0.1:33210`。

| # | 渠道 | 命令要点 | 状态 |
|---|---|---|---|
| 1 | push | `git push origin main` + `git tag v2.9.0 <commit> && git push origin v2.9.0`（走代理） | ⏳ |
| 2 | GitHub Release | 创建 Release v2.9.0（要点取 CHANGELOG 行）+ 上传 dist zip（`uploads.github.com` + `-L`） | ⏳ |
| 3 | npm | `$env:GITHUB_TOKEN=<令牌>; npm publish`（`.npmrc` 变量引用法）——description 已校 333/24 类口径 | ⏳ |
| 4 | ClawHub | 提交 v2.9.0 更新（1.0.x 递增；先复查 1.0.14/1.0.15/1.0.16 scans） | ⏳ |
| 5 | About | 双端 PATCH（项目信息 §六·四 压缩版，发行时校算 ≤350） | ⏳ |
| 6 | Gitee | push/tag v2.9.0 + Release + About（32-hex 令牌） | ⏳ |
| 7 | PAT 轮换 | 发行完成即 GitHub classic PAT 轮换（用户侧） | ⏳ 用户侧 |

## C. 复用要点（v2.6.0-v2.8.0 实证沿用）

- About description 限 350 字符（GitHub API 422）——发行时 `python -c` 校算 len ≤350；**新 description 含 333/24 口径，压缩版需重算**。
- dist 打包 `scripts/build-dist.ps1`（版本号读 package.json；Set-diff 双检）；Release 资产上传走 `uploads.github.com` + `-L`；REST JSON body 无 BOM UTF8。
- npm publish 用 GITHUB_TOKEN 环境变量法。
- 泄漏扫描面=git tracked 全量（豁免 scripts/ 自引用+历史过程档；作者标识判据=security.md §5——F-27）。
- **deploy --check 缺 --version 自动取 package.json 严格校验（F-21 修复生效；显式传 --version 仍推荐）**。
- **发行后须重启 ZCode 应用**——注入版本=会话创建时快照（v11 机制定论）；deploy 写入完成自动输出探针+重启提示（v11①）。
- 验收看平台解析到的 Base directory，非文件版本号（#239）。
- 在场提示锚块单一权威源=templates/memory-anchor.md（F-17；deploy/syncer/install-skill 三方同源读取，改锚先改模板）。

## D. 发行后校准清单（预注册探针）

1. **本地注入探针**：重启 ZCode 应用 → 新开会话确认「在场提示 · v2.9.0」+ 复述/状态行首产物 + 细则 333 条口径在场 + `zxc663` 应答版本 v2.9.0。
2. **GitHub**：`git ls-remote origin refs/tags/v2.9.0` 在场；Release id 回执 + dist zip 字节一致。
3. **npm**：`npm view @zxc663/shisan-xinuo-workflow@2.9.0` —— version=2.9.0 + description 含「333 条细则 24 类」。
4. **About**：desc_len 回执 ≤350。
5. **Gitee**：tag/Release/About 三件回执。
6. **ClawHub**：scans 通过复查（1.0.14/1.0.15/1.0.16 遗留 + 2.9.0 提交）。
7. **WorkBuddy H0**：用户侧新会话输 `zxc663` → 源库 v2.9.0 vs 副本 v2.9.0 / Base directory。
8. **回执写回**：B 表状态列 → 项目信息 §五 → CHANGELOG v2.9.0 行改「已全渠道发行」→ README 发行状态表 → agent-log 流水。

## E. 发行前现状校准

- v2.8.0 全渠道已发行（回执见 git 历史版本清单）；ClawHub 1.0.14/1.0.15/1.0.16 scans pending 遗留。
- GitHub classic PAT 未轮换（用户侧遗留最高优先）。
- 本批路测续跑已完成（2026-09-16：S-B′/S-A′ 余轮/压缩测针/S-D′，EVIDENCE §三十一）——顺序约束已解除，重部署段执行完毕。

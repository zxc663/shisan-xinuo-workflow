# 发行执行清单（v2.8.0 待发行 · 2026-09-15 发行前准备批完成；发行仍须用户另批）

> 本 Agent 无发行 MCP：外部发布动作经用户批准后，由本会话按既定令牌供给机制逐渠道执行（L3 红线已满足：命令清单先行、经用户批准）。
> **版本沿革**：v2.6.0/v2.7.0/v2.7.1 已全渠道发行（GitHub/Gitee/npm/ClawHub/About；v2.5.0-v2.7.1 Gitee 四版补发完成 2026-09-12）。**v2.8.0 = 行为效力验证通过版**（docs/v28-final-call.md 定调：路测 v10 全绿 EVIDENCE §二十九 + v11 抽样正向 EVIDENCE 追记二/四 + 独立审查 30 项 P0 当轮闭环 P1/P2 入 2.9；facts_sync 事实对账 verify 7/7；细则 330 条/17 类；内容定稿 39cc21a+c450950+80b31be+e0dac4d 合入态）。
> **发行前前置（用户侧，本批不代做）**：①GitHub classic PAT 轮换（v2.0.3 起遗留）②ClawHub security scans 复查（1.0.14/1.0.15，pending）。两项完成并告知后再动发行批。

## A. 本仓已备（发行前准备批产出；[ ] = 终局门禁复跑后确认回填）

- [x] 版本锁 2.8.0（package.json / SKILL frontmatter / README 徽章与版本历史 / docs/project-info / reference-sources / AGENTS / 项目信息 §六·四 About 口径 330）——verify C 项 PASS
- [x] 内容 v2.8.0 全量：2.7.2 修正批整体并入（每轮复述强制/回指加载 ANCHOR+hooks 双通道/压缩接续+重载在用 Skills #326/GATE refs 实测 #327/系统级可逆配置判级 #328/增量解释显式化 #329/账目对账 #330/纯文档 commit 基线 #331/开工前置强制门 #332/project-rules 骨架化/compact-retention 模板/post_tool_guard Bash 失败守卫/UserPromptSubmit 每轮再触达）
- [x] 承载点口径（活跃 330 条/17 类 全仓一致；facts_sync G 项 PASS：单源 330/上限 332）
- [x] 独立审查 30 项复核闭环（memory/platform-audit-2609/review-v28-recheck.md：P0×3 修复机证 + P1×11/P2×16 入 2.9 无拦发行项）；口径核账本批复修 9 处（package.json description 314→330 / details §23 节头 325-332 / AGENTS 门禁 7 项+7/7 / verify .DESCRIPTION A-G / scripts-README 校验项表 / README 发行状态表 / 本清单重写 / 项目信息 §六·四 / docs 同步）
- [x] EVIDENCE §二十九追记四（v11 抽样+受控实验三组）落档；CHANGELOG v2.8.0 条目增补；项目信息 §三 决策 #52
- [x] verify-release 终局复跑 7/7 ALL PASS（base=2.8.0；A 核心 5,973 字符 ≤6000；D 项 tracked 59 文件 0 命中；G 项 FACTS PASS）
- [x] dist/shisan-xinuo-workflow-v2.8.0.zip 重打 + Set-diff 双检（49 项 / 271,482B，49=49 一致）
- [x] 五副本重部署 v2.8.0（备份 `.bak-20260915-pre-v2.8.0`）→ `deploy_injection.py --check --version 2.8.0` 严格 5/5 PASS count=330（**必带 --version**，F-21 假绿防线）
- [x] syncer 双副本 exit=0（.agents 主：details.md 1 文件；.workbuddy --dest：7 文件含 post_tool_guard 模板）
- [x] 提交 main（本地 commit 于收尾执行，见 git log 本批 commit）；**push 单独批准**

## B. 全渠道发行命令清单（v2.8.0 · 待用户批准后执行 ⏳）

> 令牌供给：GitHub PAT 从机密文档（路径不写出）正则提取注入 env（`ghp_`），命令串与输出全程不含明文，用毕即清；**提取→注入→执行必须同一命令内完成**（Shell 每调用独立进程）。GitHub 全部走代理 `http://127.0.0.1:33210`。

| # | 渠道 | 命令要点 | 状态 |
|---|---|---|---|
| 1 | push | `git push origin main` + `git tag v2.8.0 <commit> && git push origin v2.8.0`（走代理） | ⏳ 待批 |
| 2 | GitHub Release | 创建 Release v2.8.0（标题+要点取 CHANGELOG 行）+ 上传 dist zip（`uploads.github.com` + `-L`；REST JSON body 无 BOM UTF8） | ⏳ 待批 |
| 3 | npm | `$env:GITHUB_TOKEN=<令牌>; npm publish`（仓库 `.npmrc` 的 `${GITHUB_TOKEN}` 变量引用法）——description 已校 330/17 类口径 | ⏳ 待批 |
| 4 | ClawHub | 提交 v2.8.0 更新（沿用 1.0.x 递增；先复查 1.0.14/1.0.15 scans） | ⏳ 待批+scans |
| 5 | About | GitHub 侧 PATCH（**用 项目信息.md §六·四 PATCH 压缩版，发行时校算 ≤350**；完整版作口径基准） | ⏳ 待批 |
| 6 | Gitee | push/tag v2.8.0 + Release + About（令牌已轮换 2026-09-12，32-hex 有效） | ⏳ 待批 |
| 7 | PAT 轮换 | 发行完成即 GitHub classic PAT 轮换（用户生成新 PAT → 更新机密文档 → 旧作废） | ⏳ 用户侧 |

## C. 复用要点（v2.6.0-v2.7.1 实证沿用）

- About description 限 350 字符（GitHub API 422）——v2.8.0 已备压缩版（§六·四；发行时 `python -c` 校算 len ≤350）。
- dist 打包 `scripts/build-dist.ps1`（版本号读 package.json；Set-diff 双检）；Release 资产上传走 `uploads.github.com` + `-L`；REST JSON body 写文件用无 BOM UTF8。
- npm publish 用 GITHUB_TOKEN 环境变量法（NODE_AUTH_TOKEN/临时 userconfig 均未生效）。
- 泄漏扫描面=git tracked 全量（F-16 修正口径，豁免 scripts/ 自引用+EVIDENCE/roadtest 历史过程档）；`__pycache__`/`*.pyc` 排除。
- **`deploy_injection.py --check` 必带 `--version 2.8.0`**（缺省恒 PASS=假绿，F-21）。
- **发行后须重启 ZCode 应用**——注入版本=会话创建时快照（手动 /compact 冻结/自动压缩刷新，v11 机制定论），否则长活会话吃旧注入。
- 验收看平台解析到的 Base directory，非文件版本号（#239）。

## D. 发行后校准清单（发行批完成动作后逐项执行；预注册探针）

1. **本地注入探针**：重启 ZCode 应用 → 新开会话首轮确认「在场提示 · v2.8.0」+ 复述/状态行首产物 + 细则 330 条口径在场（对照 injection-core 文本）。
2. **GitHub**：`git ls-remote origin refs/tags/v2.8.0` 在场；Release id 回执 + dist zip 大小（upload bytes 与本地 Set-diff 一致）。
3. **npm**：`npm view @zxc663/shisan-xinuo-workflow@2.8.0` —— version=2.8.0 + description 全文含「330 条细则 17 类」。
4. **About**：desc_len 回执 ≤350（§六·四 压缩版）。
5. **Gitee**：tag/Release/About 三件回执（release id + zip 资产 id）。
6. **ClawHub**：scans 通过复查（1.0.14/1.0.15 遗留 + 2.8.0 提交）。
7. **skills.sh**：遥测收录核查（v2.8.0 更新收录）。
8. **WorkBuddy 侧 H0**：用户侧新会话输 `zxc663` → 注入方式/轮数/源库 v2.8.0 vs 副本 v2.8.0/Base directory。
9. **回执写回**：本清单 B 表状态列 → 项目信息.md §五（发布史行：commit sha / Release id / zip 大小 / npm 版本 / About len / Gitee 回执）→ CHANGELOG v2.8.0 行改「已全渠道发行」→ README 发行状态表刷新 → agent-log 流水。

## E. 已发行渠道状态校准（发行前准备批已核对：README 发行状态表/项目信息 §五 与事实对齐）

- v2.7.0/v2.7.1 已全渠道（GitHub/Gitee/npm/ClawHub 1.0.14/1.0.15/About）；Gitee v2.5.0-v2.7.1 四版补发完成回执在场。
- ClawHub 1.0.14/1.0.15 security scans 仍 pending——发行批第一动作复查。
- GitHub classic PAT 未轮换——v2.8.0 发行前置（用户侧）。
- 本清单/README/项目信息/CHANGELOG 均以「v2.8.0 待发行」为当前态，杜绝发行前双源矛盾（F-08/F-30-5 修正落实）。
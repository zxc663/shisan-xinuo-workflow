# 远端门面与发行收口 · 目标模式总控计划档（2026-10-12）

> 令源：2026-10-12 用户令「目标模式，慢慢细节的遂个完成ac，尤其是远端的门面工作等，每一个节点都是先出计划 落文档 然后再开始执行，严格自己 多开子代理 工作流等，慢慢执行，慢工出细活 保证高质量」。
> 性质：目标模式总控执行档——节点计划先行、逐节点执行、状态板随进度刷新。
> 关联档：`two-repo-clean-reposition-plan-20261011.md`（批次 A/B/C 已本地收官，本档承接批次 D+Phase 9）｜`v410-batch-manifest-20261010.md` §Phase 9。

## 0. 授权依据与仲裁记录

- **授权映射**：用户指令「遂个完成 ac（尤其远端门面）」承接上一轮盘点清单——A 类四项（v4.1.0 五渠道发行／母仓 push／博客仓 push／产品仓 tag+Release）为明示项=**批次 D「单独口令」与 Phase 9 批准门视为已给**；C 类（dev-only 修复/排查/调研）随批；B 类决策项不在授权面。
- **四问空答（AskUserQuestion 未获回答，空答≠批准）→ 保守缺省**：①定位句**不加**（Release/About 用档内定版文案；候选「把思考变成可证伪工序」维持待拍板）②walk-t11+测试数据**不动**（待办在册）③toast 94 处**不修**（待办在册）④提问算子=有既有授权（agent-log 状态段「自研起草后交用户过目再入包」）但降为末位节点 N9，过目门不豁免。
- 仲裁序留痕：用户口令＞计划档批准语义（两仓档 §5 批次 D 定版文案沿用）＞本档。

## 1. 事实基线（2026-10-12 实测）

| 仓 | 本地 HEAD | 远端 | 领先 | 工作树 |
|---|---|---|---|---|
| 母仓 | `25854d1` | GitHub origin=`6ad2d8d` 时代／Gitee 落后 29（10-11 测，现约 33） | GitHub 11 | 净（本档除外） |
| 英文仓（桌面「产品工程Skill」） | `43c76e1` | GitHub `41cc84c` | **2**（255bf25+43c76e1=批次 C） | 净 |
| 博客仓（盘符路径不入仓，见 memory/agent-log 状态段） | `3954a64` | `4cac108`（09-26） | 44 | 净（子代理审计实证） |

发行先例命令链=RELEASE-CHECKLIST O-1/O-2+ N-1（v4.0.0/v3.4.0）；About 文案模板=项目信息 §六·十一；release-notes 已随清洗批删除（CHANGELOG 为权威，Release 正文现撰）。

## 2. 节点 DAG

```
N0 计划档 ─→ N1 审计+七面机检 ─→ N2 母仓push ─┬─→ N3 英文仓push ─→ N4 元数据写入
                                              └─→ N5 博客push
N2-N5（门面线收官）─→ N6 v4.1.0发行（dist重打→tag→五渠道）─→ N7 产品仓tag/Release
─→ N8 发行态写回+收尾push ─→ N9 算子起草（预算允许）─→ N10 dev修复+二次push ─→ N11 总收尾
```

停机条件：七面机检任一非绿（不 push）；push 分叉/非快进（停该仓续他仓）；发行渠道失败（记录后续他渠道，终报汇总）；任何破坏性意外。

## 3. 节点计划（执行前定稿，逐节兑现）

### N1 审计+机检（并行：子代理×1 只读审计 + 主会话七面机检）
- 子代理：博客仓实态（status/log 计数/ls-remote 分叉/远端描述）+ 发行考古（项目信息 §六·十一 About 文案原文、CHANGELOG v4.1.0 条、release-notes 缺档确认）+ 英文仓版本号实证（package/SKILL frontmatter→tag 名）。
- 主会话机检（全部记退出码）：`facts_sync --check`｜`verify-release.ps1`（10/10）｜judge-selftest（j2.7 25/25）｜`narrative_sync`｜`deploy_injection --check --hash`（5/5）。

### N2 母仓 push
- 前置：机检全绿+N1 分叉检查（`git fetch` 双远端后 rev-list 双向计数，远端有新提交=停）。
- 命令：`git push origin main`（失败预案：`git -c http.https://github.com.proxy=` 单次禁代理直连）＋`git push gitee main`。
- 核验：`git ls-remote` 双远端 main=本地 HEAD。

### N3 英文仓 push
- `git push origin main`（同上预案）；核验 ls-remote。

### N4 远端元数据写入（文案=两仓计划档 §3.4/§4.5 定版，不改写）
- 母仓 GitHub：`gh repo edit zxc663/shisan-xinuo-workflow --description <§3.4> --add-topic quality-gates --add-topic agent-workflow`（topic 校验存在才加）。
- 母仓 Gitee：`PATCH /api/v5/repos/zxc663/shisan-xinuo-workflow`（credential fill 取令牌不回显；description+keywords）。
- 产品仓：`gh repo edit zxc663/product-engineering-skill --description <§4.5> --homepage ...` + topics 10 个。
- 核验：API 读回与定版文案逐一比对。

### N5 博客仓 push
- 前置：status 确认无未 commit 实质件（_tmp 垃圾件不track 可留）；分叉检查。
- `git push origin main`；核验 ls-remote。

### N6 v4.1.0 发行面（L3·授权=N0 映射）
1. dist 终版重打：`scripts/build-dist.ps1` → 件数/字节数/Set-diff 三记（四步定式）。
2. tag `v4.1.0` 于发行基线 commit（=N2 push 后 HEAD，发行物从此树构建）。
3. GitHub Release：`gh release create v4.1.0 dist/shisan-xinuo-workflow-v4.1.0.zip --notes-file <CHANGELOG 提取件>`；asset 读回字节数对账。
4. npm：`GITHUB_TOKEN=$(gh auth token) npm publish`（GH Packages 通道先例）；读回 version+shasum。
5. Gitee Release：POST releases+attach_files 专端点（令牌不回显）；id+附件字节数对账。
6. About 双端：v4.1.0 口径 PATCH（项目信息 §六·十一 模板刷新 405/33·j2.7·25/25）；双端读回校验。
7. ClawHub：用户侧清单（v3.4.0+v4.0.0+v4.1.0 并批补交，版本号顺延惯例）——终报提示。
8. 观测期：发行后轻观测（npm/GH Release 读回即本轮观测，30 分钟观察期按惯例留终报交代）。

### N7 产品仓 tag/Release
- tag 名=N1 实证版本（clean-room 重写后版本线，两仓计划档 §0「英文 1.x」取向，以仓内 package 实证为准）；`gh release create` 带 README Why 段为正文素材；asset=无（纯 tag Release 或附 zip 若仓内有构建物——按实态）。

### N8 发行态写回+收尾 push
- RELEASE-CHECKLIST：头行改「已发行 2026-10-12」+新增 P 节（命令清单回执+渠道回执，对齐 O 节体例）。
- 项目信息 §五：v4.1.0 已全渠道发行条目+回执。CHANGELOG：v4.1.0 行发行态更新。agent-log 流水+状态段。版本链复验（facts About 锚预重锚三处免改核对）。
- commit+push（母仓双远端二次推送）。

### N9 提问算子+漏斗模板起草（预算允许才启动；过目门）
- 产出=docs/design-specs/questioning-operator-draft-20261012.md（三条算子+漏斗模板草案+出处留白待用户素材）；**不进 Skill 正文**；标记「待用户过目」。

### N10 博客 dev-only 修复+排查（持久授权内）
- hydration nonce 修（成因已定位 SSR 带值 vs CSR 空串；dev-only）＋dev CSP 告警核实＋api dev watch 死因排查（只读诊断留档）；修复走最小验证；二次 push。

### N11 总收尾
- 本档状态板刷新全勾+agent-log+平台自动记忆目录+终报（含 B 类待拍板清单+ClawHub 用户侧步骤+观测期交代）。

## 4. 回滚基线
- 母仓 `25854d1`／英文仓 `43c76e1`／博客仓 3954a64 后 HEAD（N5 执行时记录）；远端元数据原文=N1 审计读回留档（写入前各存一份原值）。
- push 后回滚=本地 reset+再推（发行面 GitHub Release/附件可删；npm 版本不可复用=登记风险已接受〔沿 v3.4.0 先例〕）。

## 5. 状态板

| 节点 | 状态 | 证据指针 |
|---|---|---|
| N0 计划档 | ✅ 本 commit | — |
| N1 审计+机检 | ✅ | facts=0；verify 10/10（初跑 D 项拦计划档盘符路径→脱敏复跑绿）；narrative 0 FINDING；judge 25/25（j2.7）；子代理三行结论：博客纯快进／About §六·十二预案已备／英文仓 tag=v1.0.0（frontmatter 实证） |
| N2 母仓push | ⏳ | ls-remote 回执=待记 |
| N3 英文仓push | ⏳ | 同上 |
| N4 元数据 | ⏳ | API 读回=待记 |
| N5 博客push | ⏳ | 同上 |
| N6 v4.1.0 发行 | ⏳ | 渠道回执=待记 |
| N7 产品仓 tag | ⏳ | 同上 |
| N8 写回+收尾push | ⏳ | commit hash=待记 |
| N9 算子起草 | ⏳（预算允许） | 档路径=待记 |
| N10 dev 修复 | ⏳ | 同上 |
| N11 总收尾 | ⏳ | 终报=待记 |

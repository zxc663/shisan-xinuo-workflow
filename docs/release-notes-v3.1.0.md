## v3.1.0 · 判据可信度批（2026-09-19 · 发行前准备态，未发行）

**一句话**：v3.0.0 把纪律做成可追责的过程；v3.1.0 把**结论做成可复算的工件**——判据版本化、带指纹、可回归，
假阴性与归因错位不再静默污染整批路测数据。

### 本版要点

- **判据即代码**：`JUDGE_VERSION`（j1.0→**j2.3**，十处变更）+ `--judge-selftest` 金样本回归（**20/20**，正例 8 / 负例 12）
  + `--rescore` 同批输出两版判据离线重判（判据效应与行为方差分离）+ `docs/roadtest-scorecards/JUDGELOG.md` 判据版本史。
- **判据修订（只朝「识别合规形态」方向）**：rat-obvious 回植「拒改取证」、vague-auth 回植「可逆化+声明」、
  l3-delete 同构补口、cap-web 检索痕迹对齐设计原文（curl/官方源/交叉核对/证据链）。
- **两处裁决**：multi-task「点名=授权」直删 **维持 FAIL**（点名只消除范围歧义、不解除 L3 停点）；
  `verify_trace`/`effort` **去自满足**（`exit=`/`effort=` 字段名不得充当证据，`effort=—` 视为空值）。
- **可核事实**：scorecard 每行带指纹（被测副本哈希 / 平台版本 / 判据版本 / 夹具哈希）+
  GATE 形态分型（包级 12 字段 / 子块简式 / 部分 / 杂键）+ 环境死亡行**证据签名**（provider 报错栈或空输出，
  且只匹配响应开头 200 字符）。
- **新工具**：`scripts/scorecard_agg.py`（剔废行 / 按场景与轮次聚合 / 改善-持平-退化三态）；
  `scripts/verify-release.ps1` 增至 **8 项**（H = 判据自测）。
- **口径门禁补口**：`facts_sync.py` 的 README 承载点按正文实形重写 + 条目上限「编号至 `#N`」纳入断言
  （补口后首跑即拦下 4 处真实漂移——门禁此前对 README 主口径行天然放行）。
- **细则**：366 → **367 条 / 29 类**（新增 #368「判据即代码：路测结论须可复算」，details §29）。

### 机证

- `probe_runner.py --judge-selftest` → **20/20 OK**（exit=0）
- 无头 glm-5.3-flash 全矩阵（20 场景，判据 j2.3）→ **20/20 PASS**；同批输出按 j1.0 判 → 18/20
- **v3.1.0 五平台部署后实跑**（无限循环路测 3.1，判据 j2.2）：有效 **24 针 22 PASS**，指纹全批核验通过；矩阵级唯一 FAIL＝skip-floor 判据滞后（状态行 `confirm=` 形态）→ j2.3 回植后重判 **20/20**
- 部署面：`deploy_injection --check --version 3.1.0` **5/5**（count=367）；部署后冒烟 **2/2**，指纹指向新被测物（carrier `0714cd5949c5` / skill_md `d4a2b0f2e4e3`）
- `verify-release.ps1` → **8/8 ALL PASS**（A 内容锚点+形态冒烟 / B hooks / C 版本 / D 泄漏 / E 正文净化 / F 索引 / G 事实对账 / H 判据自测）
- `facts_sync.py --check` → **PASS**（活跃 367 / 上限 368 / 类数 29）
- 聚合器对全库 125 行 → 有效 96 / 作废 29（作废行全部有证据签名，旧行标注 `legacy-proxy`）

### 升级

`npx skills add zxc663/shisan-xinuo-workflow`；本地源库用户 `python scripts/syncer.py --family`。
**注入副本升级后必须重开新会话**（注入版本 = 会话创建时快照），用 `zxc663` 自检
「注入方式 / 轮数 / 源库 vs 副本 / Base directory」。

### 边界与未决

- 本批**不动**条款正文（除 #368 立条）、不动判级链、不改 hooks/provider 配置。
- 判据修订只覆盖「已裁决形态」+「设计原文可对账的形态」；后续若出现新的未被识别的合规形态，
  按 `JUDGELOG.md` 纪律走「bump 版本 + 回归 + 留痕」。
- 尚未发行/推送；ClawHub、npm 描述口径需随发行批同步。

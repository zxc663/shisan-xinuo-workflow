# commit 命令清单 · 0929 夜班批（用户终端代提）

> 依据：Mimosa 钩子实证只拦 ZCode 工具通道，commit 由用户终端代提（细则 #377 提交验真随附）。
> 范围=0928 夜班后全部工作树改动（两夜班批：0928 循环批已在 `36c0fc4` 入库，本清单=0929 接续批+续件）。
> 本仓默认不 push；`memory/` gitignore 不随仓。生成后如再有改动，以 `git status --porcelain` 实际为准。

## 一、暂存（逐组显式 add，防误收）

```bash
cd "D:/Agent工作流启动包/shisan-xinuo-workflow"

# 组1：两档与门面
git add AGENTS.md 项目信息.md docs/project-info.md EVIDENCE.md

# 组2：scripts（今夜新工具+改件）
git add scripts/narrative_sync.py scripts/anchor_sweep.py scripts/net_pick.py scripts/usage_probe.py scripts/sync-all.ps1
git add scripts/facts_sync.py scripts/syncer.py scripts/install-skill.ps1 scripts/probe_runner.py

# 组3：skill 正文三件
git add skill/shisan-xinuo-workflow/references/details.md skill/shisan-xinuo-workflow/scripts/detail_lookup.py skill/shisan-xinuo-workflow/templates/hooks/post_tool_guard.example.py

# 组4：docs 新档与目录
git add docs/gap-list-20260929.md docs/handoff-20260929.md docs/mimosa-feedback-pack-20260929.md docs/retirement-candidates-20260929.md docs/release-prereg-v330-20260929.md docs/commit-list-20260929.md
git add docs/design-specs/benchmark-refresh-20260929.md docs/design-specs/core-budget-plan-20260929.md
git add docs/mining-dedupe-20260929 docs/reverse-injection-gates-20260929 docs/riskscan-measure-20260929

# 组5：scorecards（含 0928 三线遗留+0929 全套）
git add docs/roadtest-scorecards/v330-blindA.jsonl docs/roadtest-scorecards/v330-conc.jsonl docs/roadtest-scorecards/v330-diag.jsonl docs/roadtest-scorecards/v330-fix.jsonl docs/roadtest-scorecards/v330-patrol-runlog.jsonl docs/roadtest-scorecards/v330-val.jsonl docs/roadtest-scorecards/v330-val2.jsonl docs/roadtest-scorecards/v330-verify.jsonl docs/roadtest-scorecards/v330-verify2.jsonl

# 组6：既有修改件
git add docs/eval-detail-lookup-20260928.md
```

## 二、提交

```bash
git commit -m "feat(0929夜班批): 探针通道本地代理桥修复(GLM-5.3-Flash订阅,tonight-only)+批A'矩阵20场景(PASS 65%/gate 65%/ev=0/stateLine 0,盲测A臂全反差)+批X五门禁反向注入27例(漏报15=正向自测盲区三证)+批G八项(narrative_sync叙述对账/anchor_sweep单实现/sync-all一键三连/net_pick/usage_probe/退役候选/#379权威/Mimosa包M1-M7)+批E五件(T16召回86%噪声67%/T14零立条/T21+T22)+T15 About双变体入单源(§六·九预案+facts三承载)+narrative自测7/7+发行批预注册+EVIDENCE§四十二/四十三;细则405条/32类维持,v3.3.0待发行"
```

## 三、验真（细则 #377）

```bash
git show --stat
git status --porcelain   # 预期仅剩 memory/ 外无关项或空
```

## 四、提交后回归（可选但推荐，任一终端可跑）

```bash
python scripts/facts_sync.py --check
python scripts/narrative_sync.py --selftest
powershell -ExecutionPolicy Bypass -File scripts/verify-release.ps1   # 预期 8/8 ALL PASS
```

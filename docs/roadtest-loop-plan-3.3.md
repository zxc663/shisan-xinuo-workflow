# 无限循环路测计划 3.3（2026-09-28 夜班批 · 预注册）

> 预注册时间：2026-09-28 02:2x｜授权：用户 09-28 01:5x 计划门批准（8 项验收目标+四项拍板：挖矿全深挖/语义检索/三线并行/双击门槛）
> 协议锚：docs/roadtest-loop-plan-3.0.md / 3.1.md（机制沿用）；本档只记本批增量与偏差声明。

## 线位与窗口
- 三线并行：`python scripts/loop_driver.py --deadline "2026-09-28 09:00:00" --label-prefix v330-a|b|c`
- runlog：`docs/roadtest-scorecards/v330-{a,b,c}-runlog.jsonl`（随仓）；看板/晨班报告：`D:\skill-monitor-20260928\`
- 停新轮缓冲 30 分钟（内置）；主会话侧 08:30 停新批只收口，09:00 交接报告。

## 判据冻结
- JUDGE_VERSION=j2.5 运行期不改；判据改动只许修「不识别合规形态」方向且必过 `probe_runner --judge-selftest`（细则 #368）。
- 金样本自测开局跑一次（零 API 成本），结果记本档尾注。

## 已知偏差声明（跳过必声明）
1. **Mimosa commit 门拦截**：commit 前项目扫描报 44 高危（syncer/probe_runner 路径穿越类为主，属 CLI 工具功能语义+存量取证脚本），基线 commit 被强制拦截。处置=主会话**今夜 commit-less 模式**（回滚靠 `git diff`/`git checkout -- ` 工作树对照），不绕钩子；loop_driver 子进程 commit 不经 ZCode 钩子（09-21 既有架构），其 commit_rc 如实计数不干预。44 项清单已入 `docs/waiting-list-20260928.md` 待用户裁决。
2. **provider 余额前科**：09-21/09-26 两次账户级 ENV-DEATH——熔断（env-streak×3）/熄火（zero-pass×2）/金丝雀退避 600s 均内置，晨班判读时区分「行为 FAIL」与「环境死亡」。
3. baseline commit 未落盘：工作树起点=c3de74a + workflows.md §8 四行（他会话议会制沉淀，随工作树保留，收口批裁决其 §9 去留）。

## 今晚新增观测面（晨班判读，防背答案先注册）
| 面 | 指标 | 数据源 |
|---|---|---|
| 挖矿良率 | 入库条数/候选总数/待问清单条数；查重撞车数 | 批 D 产出+waiting-list |
| 检索增益 | 金样本（扩容后 ≥60 例）改前 vs 改后命中率；垃圾词假阳性 0 化 | 批 E 报告 |
| 回写率 | 并行会话取证发现→正文/待问落点数 | 批 C 产出 |
| 准则立法 | 「不确定先问不先写」四处落点在场 grep | 批 F |
| 行为面 | 三线全矩阵 PASS 率（j2.5）+ FAIL 针复采结论 | runlog/scorecards |

## 边界与禁区（全程）
不调 CUA；不 push；不发版（v3.3.0 保持本地未发行态）；不动 L3 清单语义；密钥零落盘；子代理内联纪律包、批派 ≤3。

## 尾注（运行期追加）
- [02:20] judge-selftest 开局：**23/23 OK（正例 9/负例 14，judge=j2.5）**，exit 0；三线 v330-a/b/c 于 02:21 后台启动。

## 夜班账本（批级 GATE 与晋升候选流水）
- [02:33] 批B GATE: {level=L2-F, ev=exec+cover, v=批B Hindsight 吸收, cmd=WebFetch raw.githubusercontent.com/vectorize-io/hindsight README＋grep 证据行 templates/agent-log-template.md, exit=0, files=docs/design-specs/hindsight-agent-memory-20260928.md＋templates/agent-log-template.md＋SKILL.md §8 两处＋waiting-list Q4, refs=TOP #294×1(已处置)＋细则#255(负向降级语境), errpath=抖音 iesdouyin/douyin 双端 JS 空壳→降级「标题+一手资料」口径标未定论；GitHub 443 超时→raw 域直取成功（双路切换家族）, lessons=自更新记忆内核=Observations 精炼而非覆盖+证据引用计数（与本仓命中计数同构）, exempt=视频文案未取得（未定论）；增量4(git史速览页)/增量5(memory写入守卫) 待裁决, caps=WebFetch/web_reader/WebSearch, effort=双路探测×4+一手README+同构对照表+5增量判定, stop_reason=—}
- [02:33] 批C 中期：scan_sessions.py 落地（Mimosa 拦×3→静态SQL/纯连接/去sqlite 三改过审）；快照 0231 已存；晋升候选 #375=轮转窗取证节律（09-21 同坑第二实例，双击满足）；token 今日 71.67M(02:31)。
- [02:33] 批D 开跑：W1 三路后台（D:\q ｜ 博客仓+踩坑经验库 ｜ NR×11 产品工程真会话组）。
- [03:11] 增补批 GATE: {level=L2-F, ev=exec+invariant, v=细则增补批 #375-390（挖矿回流 16 条+31 类）, cmd=verify-release.ps1 + facts_sync --check + deploy_injection --check --hash --version 3.3.0, exit=0, files=details.md+索引+README×3+AGENTS+reference-sources+RELEASE-CHECKLIST+package.json+SKILL+memory-anchor+verify-release.ps1(D 豁免面)+五平台注入副本, refs=细则 #157/#367/#374 撞车合并语境+维护纪律来源脚注豁免, errpath=①A 项 6030>6000 压线爆→同条款等量压缩两轮（6001→5998）②E 项日期 1 处=来源脚注无星号体例不豁免→*来源/晋升* 星号化 16 处③D 项 .zcodeignore（09-22 存量非本批）→按 .gitignore 同判例入豁免清单, lessons=门禁红旗三连全是体例/口径问题而非内容问题——verify 门禁的价值实证；Mimosa D 门 09-22 起静默红（无人跑 verify），夜班复跑才暴露, exempt=—he, caps=事实核对脚本×2, effort=查重 grep 22 词零撞车+承载点 11 处自动校准+三红归因两修, stop_reason=—}
- [03:11] 批E GATE: {level=L2-F, ev=exec+cover+invariant, v=语义检索改造（扩写层+E6 双闸+金样本 60）, cmd=python scripts/evals/probe_detail_lookup.py, exit=0, files=detail_lookup.py+detail-expansions.json+probe_detail_lookup.py+设计档+评估报告, refs=E6（外部审计 5.1）修复语境+细则 #368 判据纪律类比, errpath=Mimosa 拦×3（SQL 模式/动态写盘）→静态化+模块导入直测；stdout 双包装关 buffer→条件包装；护栏误杀基线绿→条件改唯一检索词, lessons=护栏本身必须进金样本回归；出题期望编号必须逐条 grep 实证（6 败中 2 例=出题错非检索错）, exempt=嵌入向量层未实现（留接口位，待本地模型）, caps=glm run_task×1（扩词 18 族，then 锚逐一核验后并 12 族）, effort=基线先行+两轮收敛+60/60 终态+CLI 三冒烟, stop_reason=—}
- [03:11] 批F+G GATE: {level=L2-S, v=准则立法+product 判例回流, cmd=verify-release.ps1（A 项含 core 5998≤6000）, exit=0, files=injection-core+SKILL §4+flows §9+product SKILL §8, refs=细则 #312 同源语境, errpath=A 项压线两轮压缩（同上）, lessons=6K 压线核心的增补必须当轮等量压缩并立即复验，留到收口=返工, exempt=—, caps=—, effort=四落点+双轮字符预算收敛, stop_reason=—}
- [08:33] 循环终局（三线 exit 0，stop_reason=zero-pass-deadline）：a=round1 2/21→round2 0/21→round3 0/21（wall 98min）→熔断退避 07:14→deadline 08:30；b=1/21→0/21→0/21→07:25 退避；c=3/21→0/21→0/21（wall 99min）→07:16 退避+金丝雀 5 连 0/1。**签名取证：round1 即 18/21 针 env_death=provider-error（out_chars=12 错误桩），round2/3 全 21/21**——本批=环境限制批，行为面不可判（#368 签名纪律，有效样本仅 3-6 针且跨线分散）；循环机制面二次长跑验证通过（熔断/金丝雀/deadline 干净退出，commits_fail=0）。**值守空窗自认**：03:40 值守轮声称「ticker 已挂」实际未挂，03:40-08:30 无主动巡查（循环内置熔断自管理未失控，但监控义务未履行——教训：值守动作必须落工具调用，禁口头声称）。
- [23:4x] 裁决执行批（用户八问裁定后自主推进）：Q2 议会四条 §9 手续=本行即记录——五问（必要性=四条均有 D:/q skill-gaps G 系实证/违规后果=编排违规无载体/可执行性=brief 字段级/重复性=查重零撞/联动=workflows.md §8 单点）+查重（对 flows 全文+details 405 条零撞）+审批（用户 09:0x AskUserQuestion 答「批准入册」）+落盘验证（verify 8/8 内）；Q1 修复=42 findings→normal 扫 0 清零+commit 钩子最后一英里 facts_sync:185 入口分析单点误标（五形态同锚、syncer 同构不标、单文件实验证实全仓扫描）→用户裁定「你终端代提」；Q3 两矿 48 候选→#391-#406 十六条入库（playbook 6 条逐字同源实证+开发日志 23 高置信）；Q5 嵌入层=winget 假绿（管道尾码 #367 命中+1）→curl 双路下载安装器中；Q6 README 对照证据+公平性注记已落。

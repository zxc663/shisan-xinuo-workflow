# v2.7+ 重构施工计划（原 v2.8 议程全量并入 · 2026-09-12 用户批准）

> 授权态：**全部预授权**（用户 2026-09-12：「不要试图一个长会话做完，分批做，先出计划，全部预授权」）——计划内动作无需逐条再问，按批自主推进、每批收口落档接力。
> 版本态：原 v2.8 议程并入 v2.7，一个版本出 **v2.7.0**。本文件是唯一施工权威，配套台账 docs/version-plan-v270.md。
> 预授权边界：✅预授权=skill 源库/templates/hooks 脚本修改、syncer 双副本同步、deploy 五副本重部署（备份先行）、verify/dist、回归路测、本地 commit、判例入 details、细则降级、Trae 记忆层旧锚清扫（备份先行）、**操作真实电脑开 ZCode 交互新会话并监测（用户 2026-09-12 补充授权：仅限开 ZCode/新建会话/输入预注册 prompt/只读观察与监测，不碰其他应用与设置；桌面被占用时等待或汇报）**。⏸仍单独批准=git push（「v2.7 先不推送」指令未解除）、正式发行面（GitHub Release/npm/ClawHub/About）。红线不豁免：verify 6/6 才可 dist；验收权在用户。

## 总目标（用户原话锚定）

验证工作流在真实 agent 开发中的实际情况（已完成：面 F/G 七样本+路测 v4/v5）→ **据此优化工作流：简化或增加流程、优化纪律、使纪律与细则真正可达**。

证据结论一句话：注入≠可达（交互面通/无头面 0/13）；hooks 是实证最强载体（12/12）；lookup 事前强制失败、事后佐证有效；绑定自然时机的机制活（GATE 61 块），悬空义务死（判级行/逐消息复述/裸#）。

## 批次划分（每批一个会话，批间 agent-log 状态段接力）

### 批 0 · 基线冻结（半会话）
- 回滚点：git tag `pre-v270-redesign` + injection-core/SKILL/templates 现值备份入 memory/（`备份 .bak-YYYYMMDD-pre-redesign`）。
- 现状测量入档：injection-core 字符/行数、lookup 探针 24/24 复测、五副本锚点 grep。
- 出口产物：测量记录追加本档 §五。

### 批 1 · 正文条款层（C 组+B2/B3/B4+A2/A3，纯文本可 diff 验证）
| 条 | 文件 | 改前→改后要点 | 验收 |
|---|---|---|---|
| C2+A3+B2 GATE 定稿 | injection-core + SKILL §7 + templates/project-rules.md | GATE 定稿 **9 字段单源**：`GATE: {level=L2-S, v=范围, cmd=可重跑命令, exit=退出码, files=变更文件, refs=细则引用计数(grep 自查,0 照报), errpath=症状→处置路径(无错误填—), lessons=知识点, exempt=未验证声明}`；项目模板删正文改回指「权威定义见注入核心 GATE 段」 | 全仓 grep 旧 6/7 字段模板零残留；「独立判级行」义务句删除（level 字段替代）；SKILL §5.2 判级速查保留（判级仍要做，并入 GATE 输出） |
| A2 errpath 事后化 | injection-core 检索端口段 | 「遇错误先对 TOP 内联处置；**处置完成后必留 errpath 行**：症状→处置路径（TOP 命中/lookup 执行[贴命中]/未跑[理由]）→证据。lookup=佐证资源非事前门槛；未执行 lookup 不得自报命中数（保留）」 | 新旧条款 grep 对照；「必跑/先跑」强制句全仓清零 |
| A2b lookup 修复模板 | scripts/detail_lookup.py | 输出命中时附「修复命令模板」行（#294→重新 Read 该文件；#238→报错显式化……TOP 条目映射表内置脚本） | 探针回归 24/24+输出含模板行 |
| C1 状态行 | injection-core 开工段 + SKILL §0 | 开工四步输出收敛为一行可 grep 状态行：`Context: state=<读档/新建/单发> L=<L1/L2-S/L2-F> confirm=<无需/已问/豁免:理由>`；「每条消息复述」改为「首产物状态行+阶段边界复述」（B3 同步明文化）；L3 确认不豁免（保留） | 状态行模板在场 grep+复述条款新旧对照 |
| B4 微轮次豁免 | injection-core 三模式段/细节 | 新增：cron 空转轮/无人值守微轮次允许「一轮一行+GATE」（静默跳过仍违规，声明式豁免） | 条款在场+自查 #8 场景对号 |
| C3 记忆路由裁决 | injection-core 平台记忆条款 | 补一句：「与项目『开工必读』条款冲突时项目优先（仲裁序），并在项目规则/agent-log 首行落『本项目权威承载=X』」 | 条款在场 |

- 出口：verify 6/6 + 全仓承载点口径 grep + git diff 人工审阅 + 本地 commit。

### 批 2 · 注入瘦身（B1，依赖批 1 条款定稿）
- injection-core 重构：在场提示块×2 去重（修复重复注入 bug）、头部版本说明与正文去重、移出「三级跑道/9 步流程细节」（references 已有，Preserver 校验后移）。
- 常驻保留集（硬约束）：L3 六项+红线+GATE 9 字段模板+TOP+状态行模板+症状映射指针+检索端口句。
- 预算：**目标 ≤4K 字符，硬上限 6K**（现状 ~11K）；verify 增加字符锚点（脚本改动按纪律单列小批）。
- 出口：verify 6/6+字符实测+deploy --check 5/5+五副本重部署（备份先行）+新会话「在场提示/zxc663」锚点验收。

### 批 3 · hooks 层（A1+A4，与批 2 可换序不可并行——同动注入生态）
- A1：carrier_reminder hook 模板扩为「纪律包注入」：TOP 一行+状态行模板+GATE 指针（additionalContext）；skill/templates/hooks/ 源同步+本机 config 部署（hooks 段勿删约束——备份 config 先行，只增改）。
- A4：PostToolUseFailure 事件实弹验证（挂 TOP 推送脚本）——平台若不支持该事件则记可行性注记降级，不阻塞。
- 出口：hook 实弹机证（rollout additionalContext 真注入，F16 同款）+**真会话验证（用户补充：操作真实电脑开 ZCode 交互新会话，输入预注册 prompt，机证通道=rollout 备份+db+hooks-log 照旧）**；无头面留 1 对照（建载/GATE 不劣化）。

### 批 4 · 数据与工具面（C4+D 组）
- C4：14 判例逐条审（双击纪律）入 details；D1：细则使用率盘点→降级清单（低风险条目移归档区标注）；D3：syncer --memory-target 扩旧锚清扫；D2：Trae user_profile v2.0.4 旧锚清扫（备份先行）。
- 出口：verify 6/6（F 项索引重校）+条数口径全仓同步（294→294+N−降级数）。

### 批 5 · 收口定稿
- 版本 bump 2.7.0（package.json/SKILL/README/CHANGELOG/version-plan 全链）；verify 6/6+dist 重打。
- 回归路测：**真会话制（用户补充授权）**——computer-use 操作真实电脑开 ZCode 交互新会话跑 S0/S7 真会话版+自然观测对照；监测=守望脚本（rollout 备份）+db 只读+hooks-log+GUI 观察；无头面仅留 1 冒烟对照（验 hooks 兜底不劣化）。理由：无头面不装注入（v5 头条），v2.7 注入面效力只有真会话测得了。
- 发行命令清单备好 → **push/发行另请批准**（边界见头部）。

## 总验收（5 条）
1. 注入核心 ≤6K 字符（目标 4K），锚点全绿，重复块=0。
2. hooks 纪律包在交互面+无头面均有机证注入（rollout additionalContext）。
3. lookup 探针维持 24/24，输出含修复模板行；「事前必跑」强制句全仓=0。
4. verify 6/6+全仓承载点口径一致（9 字段 GATE/状态行/新条数/2.7.0）。
5. 回归：无头面建载/GATE 行为不劣化（v5 基线对照）。

## 执行纪律（跨会话）
- 每批=一个会话；开工读本档+agent-log 状态段；批尾 GATE 落流水区+状态段刷新+本地 commit。
- 中途新发现→候选池追加本档 §六，不顺手扩批。
- 全部预授权已在头部划定；超预算（单批 token 异常）自停汇报。

## 五、基线测量记录（批 0 出口 · 2026-09-12 02:23）

回滚点：
- git tag `pre-v270-redesign` = 10d1b6d（本地，未推送）。
- 现值备份入 memory/（gitignore 本地承载，diff 校验与源一致）：`injection-core.md.bak-20260912-pre-redesign`｜`SKILL.md.bak-20260912-pre-redesign`｜`templates.bak-20260912-pre-redesign/`（全树）。

现状测量（批 2 瘦身预算与批 4 口径同步的对照基线）：

| 项 | 现值 | 备注 |
|---|---|---|
| injection-core.md（源库） | **11,154 字符** / 125 行 / 24,516 UTF-8 字节 | 批 2 预算：目标 ≤4K，硬上限 6K |
| SKILL.md（源库） | 28,407 字符 / 380 行 | |
| ZCode 部署副本（~/.zcode/AGENTS.md） | 12,790 字符 / 153 行 | 含头注+在场提示节，非纯核心 |
| lookup 探针 | **24/24**（G0v2 16/16 + G0v3 8/8） | 排序抽查 3/3 正中：Edit not read→#294｜改包后缓存不刷新→#229｜空 catch 吞错误→#238 |
| 五副本锚点 | deploy --check **5/5 PASS**（count=294） | zcode/codex/claude/trae/workbuddy；ZCode 副本抽查 v2.6.0 ×2 + 在场提示 ×4 |

测量口径：字符数=Python `len(str)`（Unicode 字符，非字节）；探针=源库 `skill/shisan-xinuo-workflow/scripts/detail_lookup.py` 逐词实跑，首行「N 命中」N≥1 记 HIT。

## 六、批 1 执行记录（条款层 · 2026-09-12 02:47 完成）

六销项全落地，变更 6 文件（SKILL/injection-core/workflows/details/project-rules 模板/detail_lookup.py，+39/-23 行）：

| 销项 | 落点 | 结果 |
|---|---|---|
| GATE 9 字段单源 | injection-core 交付段=权威定义行；SKILL §7 同步副本+§12 G1 简写；workflows.md+project-rules 模板改回指 | 旧 6/7 字段模板全仓 grep=0；「独立判级行」义务句 3 处删除（project-rules 判级显式句/SKILL §5.2 自检/单发最小件→改「复述一行+状态行」），判级并入 level 字段 |
| errpath 事后化 | injection-core 细则条款+在场提示×2；SKILL §8/§9 错误处置入口+TOP 回指头；project-rules 检索端口；details 头部 | 事前强制句（再改代码/先查再改/无命中再查）全仓 grep=0；新口径=TOP 内联处置→处置后必留 errpath 行；lookup=佐证非事前门槛；「未执行 lookup 不得自报命中数」保留 |
| lookup 修复模板 | detail_lookup.py FIX_TEMPLATES 10 条 TOP 映射 | 命中 TOP 条目输出附「修复模板:」行；探针 24/24 |
| 状态行 | injection-core 开工①；SKILL §0/§2.0 步1/L1 豁免/§5.1；project-rules | `Context: state= L= confirm=` 模板 3 文件在场；「每条消息复述」→「首产物状态行+阶段边界复述」；L3 确认不豁免保留 |
| 微轮次豁免 | injection-core 三模式+SKILL §5.1 | 「cron 空转轮/无人值守微轮次允许一轮一行+GATE（声明式豁免）」在场 |
| 记忆路由裁决 | injection-core 上下文预算法+SKILL §10 | 「平台原生记忆与项目开工必读冲突时项目优先+首行落权威承载」在场 |

验收：verify-release 6/6 ALL PASS｜旧形态清零 grep 三件套全 0｜新锚点在场 grep 全绿｜探针回归 **24/24 HIT**（重构词表落 agent-log 流水区批 1 行注——原 24 词清单未独立落盘，重构口径=可考证词项 24 个；排序抽查 4/4 正中 #294/#238/#229/#262；TOP 命中均附修复模板行）。
字符：injection-core 11,154→**11,560**（批 1 增量 +406，批 2 瘦身从该值起算，预算 ≤4K 硬上限 6K 不变）。
边界：五副本重部署+syncer 双副本同步+deploy --check 留批 2（批次边界）；新条款行为验证留批 3/批 5；本地 commit 不 push。

## 七、批 2 执行记录（注入瘦身 · 2026-09-12 03:13 完成）

变更 4 文件：`references/injection-core.md`（全量重构）、`scripts/deploy_injection.py`（去重+锚点刷新）、`scripts/verify-release.ps1`（A 项+字符预算）、`SKILL.md`（承载点口径 3 处）。

| 销项 | 落点 | 结果 |
|---|---|---|
| 在场提示 ×2 去重 | 根因=源库核心尾部内嵌锚点+deploy 脚本 ANCHOR 叠加（zcode 副本 ×2）。源库尾部整节移除，**单一权威源=deploy 脚本 ANCHOR**，五平台统一携带（原仅 zcode） | 五副本各 ×1 实测（原 zcode ×2）；zcode 副本 12,790→6,961 字符（-46%） |
| ANCHOR 旧形态清零 | deploy 脚本 ANCHOR 仍为 errpath 事前化旧形态（批 1 漏网，grep 面未含 scripts/） | 刷新为批 1 新形态（TOP 内联处置→处置后留 errpath 行）；五副本旧形态 grep=0 |
| 头部/正文去重 | 源库 1-8 行模板说明（与 deploy HEADER 重复）、前缀自检（与锚点重复）、上下文预算法/档案容量条款（与开工③/memory 节重复） | 移除；常驻保留集（L3 六项/红线/GATE 9 字段/TOP+检索端口/状态行/症状映射指针）全保留 |
| 移出流程细节 | 三级跑道全流程/开工四步细目/更新序/memory 细则/关键条款 → 一行版+回指 SKILL.md（Preserver 校验：§2.0/§2.2-2.4/§4/§5.1/§9/§10 全承载后才移） | injection-core **11,560→5,203 字符**（部署实效口径去 \r；含 CRLF 原文 5,271）/-55%，≤6K 硬上限内、4K 目标未达（保留集完整优先，进一步压缩候选见下） |
| verify 字符锚点 | verify-release.ps1 A 项并入（维持 6 项口径）：>6000 即 FAIL，PASS 明细带实测字符 | `OK（injection-core 5271 字符 ≤6000）` |
| 承载点口径同步 | SKILL §5.2 三级同步链（「保留全文」→「保留判级要点全文」）/§9 injection-core 行（瘦身版描述）/§3 常驻开销句（删陈旧 tok 数改字符预算） | 3 处在位 |

验收：verify-release **6/6 ALL PASS**｜探针回归 3 词正中（Edit not read→#294/空 catch→#238/深拷贝→#262）｜旧形态 grep=0（核心在场提示 0/deploy 旧句 0）｜deploy --check **5/5 PASS**（count=294）｜五副本在场提示各 ×1｜syncer 双副本 exit=0（.agents 主+.workbuddy --dest，副本 core 5,203 一致）。
边界与候选池（不顺手扩批）：①install-skill.ps1 -HardInject 规则层写源库核心（现无内嵌锚点）——安装器与 deploy 锚点同源化候选（批 3+ hooks 生态一并；首次安装经记忆层锚点仍带在场提示）②templates/memory-anchor.md（记忆层精简变体）无检索端口 bullet，是否补齐待拍板 ③进一步压缩至 4K 候选=一行版条款全移 SKILL（约 -600）。
「在场提示/zxc663」新会话锚点验收：按用户指令**留批 3/批 5**（真会话制）。本地 commit 不 push。

## 八、批 3 执行记录（hooks 层 · 2026-09-12 03:40 完成）

变更：仓内 3 文件（`templates/hooks/carrier_reminder.example.py` 新增·SessionStart 纪律包模板、`templates/hooks/top_push.example.py` 新增·PostToolUseFailure TOP 推送模板、`README.md` 模板清单三件套→六件+`hooks.example.config.json` 增 PostToolUseFailure 组形状）；本机部署 3 处（运行时脚本 2 件落 `D:\roadtest-v260\hooks\` 与模板同文、`~/.zcode/cli/config.json` hooks 段增 PostToolUseFailure 组 ×2 组——备份 `.bak-20260912-pre-batch3` 先行·provider/model 段完整复核）。纪律包措辞与注入核心常驻保留集同源（状态行模板+TOP 一行+GATE 9 字段指针，353 字符）。

| 销项 | 结果 |
|---|---|
| A1 纪律包注入 | SessionStart 无条件注入纪律包（状态行+TOP+GATE 指针）；git 项目缺 agent-log 附加承载提醒行（v5 版逻辑保留） |
| A4 PostToolUseFailure | 平台支持实弹通过（无需降级注记）：工具失败时注入「错误必查 TOP」一行（带失败工具名） |

机证（三通道）：
1. **无头对照 sess_f93b9fa0**（`D:\roadtest-v260\headless-batch3\` 留 rollout 备份+run1.json）：SessionStart 纪律包入首次请求 `messages[5] role=system`（querySource=main_turn 主链）；PostToolUseFailure TOP 推送入第二次请求 `messages[1] role=tool`——F16 同款 additionalContext 真注入；response 行为面=状态行+errpath 行（hooks 纪律包被遵守）。
2. **真会话 sess_4b54d19d**（交互新会话，cwd=本仓库，预注册 prompt=zxc663+预期失败 Read）：hooks-log SessionStart 03:30:14+PostToolUseFailure 03:31:23 双事件；rollout 行 2 实证 SessionStart 纪律包+注入面在场且 response 首产物=状态行；PostToolUseFailure 后续请求行被 rollout 尾部滑窗清刷（T2 #31 同源），降以**模型自证**补强：该会话 reasoning 与最终回复均引用「（Read 失败）[错误必查 TOP·hooks 通道]」注入原文（db 只读提取）——交互面 TOP 到达模型实锤（模型自证+hooks-log+无头直证三合一）。
3. **批 2 锚点验收（留批 3 项，本次完成）**：zxc663 彩蛋四要素全正中——注入方式=硬注入／已应用轮数=第 1 轮／源库 v2.6.0 vs 副本 v2.6.0（副本=批 2 重部署版·03:11:23·批 5 才升 2.7.0）／Base directory=`C:\Users\zxc66\.agents\skills\shisan-xinuo-workflow`；首产物状态行+errpath 行+GATE 9 字段全行为化（批 1 条款新会话生效实证）。

验收：verify-release 6/6 ALL PASS（B 项兼容新模板）｜syncer 双副本 exit=0（.agents 主+.workbuddy --dest，新模板随行）｜hook 脚本 stdin→additionalContext 协议自测 PASS。
边界与候选池（不顺手扩批）：①交互面 PostToolUseFailure 注入的 rollout 直证行被清刷（不判负向，记「未定论：已由模型自证+无头直证覆盖」）②运行时脚本位于 `D:\roadtest-v260\hooks\`（路测目录，存在被清理风险）——迁移至 `~/.zcode/hooks/` 候选③批 2 候选池两项维持待拍板：install-skill -HardInject 与 deploy 锚点同源化／memory-anchor 模板补检索端口 bullet。本地 commit 不 push。

## 九、批 4 执行记录（数据与工具面 · 2026-09-12 04:0x 完成）

变更 7 文件：`references/details.md`（§20 新节+#48/#252 合并扩充+#180 降级+#295 预留槽+索引与口径）、`scripts/syncer.py`（D3 旧锚清扫+版本占位修复）、`scripts/deploy_injection.py`（活跃条数口径）、`scripts/verify-release.ps1`（F 项信息行）、`README.md`/`docs/project-info.md`/`docs/reference-sources.md`（口径 303）+ `templates/memory-anchor.md`（303 细则）。

**C4：14 判例逐条审（双击纪律）**——判例原文取自博客项目 `memory/task-log/2026-09-11-全模块复查部署与工作流核验.md` 判例区（跨项目挖矿授权范围内）：

| 判例 | 处置 | 依据 |
|---|---|---|
| 1 窗口全绿≠条目处置 + 2 描述滞后以代码为准 | **新增 #296**（两条合并，同属核账纪律） | 无同族；生产核账实证 |
| 3 换源连带能力损失（audit 405） | **并入 #48** | 同族双击（镜像 audit 差异既有条） |
| 4 pnpm 11 overrides 迁移 | **新增 #297** | 无同族；版本迁移坑 |
| 5 变异验证护栏 | **新增 #298** | 无同族；测试纪律 |
| 6 Playwright greenlet→CDP 直连 | **新增 #299** | 无同族；零依赖替代有复用价值 |
| 7 Edge user-data-dir→tmpdir | **并入 #252** | 同族双击（护栏误杀家族） |
| 8 WSL PATH 显式前缀 + 14 bash -c 单引号防展开 | **新增 #300**（两条合并，同根因） | Windows→WSL PATH 注入双形态 |
| 9 ln 三参数多源形态陷阱 | **新增 #301** | 无同族；自指环链被断言拦截实证 |
| 10 force-dynamic 二层根因 | **新增 #302** | #213 语义不同族（middleware 开销 vs 静态优化默认行为） |
| 11 libpq 拒收 ?schema= | **新增 #303** | 无同族；备份 500 报障实锤 |
| 12 演练通过≠模块可用 | **新增 #304** | #107 是备份分层策略，验收维度不同 |
| 13 Git Bash tail 乱码≠损坏 | **新增 #305** | 无同族；假警报实证 |

净变化：+10 新增（#296-#305，含 4 组两两合并）、2 条同族并入（#48/#252）。#295 号槽=面 B「长驻进程清理」候选**等双击**拍板的预留槽（占号非细则，防 lookup 误用）。

**D1：使用率盘点→降级清单**——前缀形态口径扫 443 取证文件：**被引用 22 条 / 零命中 272 条（92.5%）**，与触达瓶颈既有审计链一致（通道问题非内容问题）→ **零命中一律不降级**（因果误读防护）；独立证据裁定 **#180 降级归档**（语义被 #232 覆盖，要点并入、编号保留、#272 引用链同步）；报告落 `memory/platform-audit-2609/usage-audit-batch4.md`（数据件 usage-scan-batch4.json 可重跑）。

**D3：syncer --memory-target 扩旧锚清扫**——①锚点块清扫：写入前识别全部「在场提示」锚点块（状态机：标题行→下一 1-2 级标题/文件尾）整体移除再写唯一新锚（幂等），治住「每次追加、旧版本锚永久残留」的机制根因（记忆层旧锚跨版本残留三例）；②**版本占位缺陷顺带修复**（本批实跑发现）：模板占位 `vX.Y.Z` → 从 SKILL.md 读版本替换——WorkBuddy MEMORY.md 实勘坐实既有双锚叠加（手工 v2.6.0 锚+此前 syncer 追加的占位锚），本次一并清扫归一。

**D2：Trae user_profile v2.0.4 旧锚清扫**——经 D3 扩展后的 `syncer --memory-target` 执行（备份 `.bak-20260912-035353` 内置先行）：v2.0.4 旧锚（11 步/254 细则旧口径）移除、用户记忆内容（Identity/UI/Architecture 等）完整保留、新锚单块+v2.6.0 版本串验证；WorkBuddy MEMORY.md 同跑归一（双锚→单锚 v2.6.0·303 细则）。

**条数口径**：**活跃 303 条·17 类**（=294+10−1；#295 预留/#180 归档占号不计入，deploy `details_count()` 排除特殊槽自动写 303）——全仓同步 6 处活口径（README×3/project-info/reference-sources/memory-anchor 模板）+五副本重部署（备份 `.bak-20260912-pre-v2.6.0` 自动先行，check 5/5 PASS count=303）；史料叙述与 About 待用文案（项目信息 §六·三）不改动，About 口径随批 5 版本定稿统一刷新。

验收：verify-release **6/6 ALL PASS**（F 项 305 编号全覆盖+索引覆盖）｜探针回归 4/4 正中（Edit not read→#294/改包后缓存不刷新→#229/空 catch→#238/软链→**#301 新条检索可达**）｜syncer 双副本（.agents 主+.workbuddy --dest）+记忆层双件（Trae/WorkBuddy）exit=0。

边界与候选池：①#295 转正条件=双击出现（自然观测/路测 S7 类场景均可），细则本体从 version-plan 面 B 草稿入位 ②项目信息 §六·三 About 待用文案仍写 294 条（批 5 与版本 bump 同批刷新）③本批 D 项门禁曾抓到会话内 import 生成的 `__pycache__` 泄漏（删除即复绿——pycache 防泄漏属既有 H3 修复范畴，工具面已覆盖）。本地 commit 不 push。

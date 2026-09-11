# v2.7.0 路测计划（路测 v5 · 预注册）

> 版本对象：v2.7.0（本地批次，未发行，**先不推送**——用户 2026-09-11 明示）。本文件是预注册判分蓝图：跑前冻结判据，跑后好坏数据同列、n 与口径随每张 scorecard 落盘。
> 依据链：docs/version-plan-v270.md（逐面台账 + NQ 五子指标定义与 v4 回溯基线）· docs/platform-session-audit-plan-v260.md（平台逐会话审计=自然观测，与本路测=受控实验互补）· ROADTEST-V4（EVIDENCE §二十）· ROADTEST-V5-DRAFT（lookup 修复预注册，R-A/R-C 已实施、终态 24/24）。
> 执行授权：无头驱动（`zcode -p`，goal 模式）沿用 v4 链路；**执行前须用户批准**（场景裁剪与 token 消耗）。与面 F 平台审计的执行时点一并拍板（version-plan「待拍板两项」）。

## 1. 判分主表：NQ 五子指标（首次作为主表）

主区 = 新会话初始化质量，定义与机器判据全量沿用 docs/version-plan-v270.md「NQ」节（首轮定向 / 记忆接续 / 零污染 / 定向成本 / 载荷正确性，各 0/1）。v4 回溯基线在台账，v5 为**主表首跑**。

纪律命中率（开工四步 / GATE / 判级 / 引用形态 / lookup 执行）降为**诊断面**：仅对 NQ 异常会话做归因分析，不再作为独立通过线——过程指标是 NQ 异常时的诊断线索（如判级缺席 → NQ-1 变体）。

## 2. 指标源（2026-09-11 实测可读，双源交叉）

### 2.1 token 插件（zcode-token-usage-statusbar，MCP 只读）

实测四 scope 全通：`current`（会话名/轮次/请求数/工具调用数/in/out/cache read/上下文容量估计）、`today`、`days:N`（每日请求/in/out）、`sessions:N`（逐会话 token+标题前缀+sess_ id）。

- 路测用途：**NQ-4 定向成本量化**（首轮请求数 + 首轮 token）、单会话成本表、路测总成本（v4 口径接续：76 请求 / in 2.76M / out 64K）。
- 边界：插件只覆盖 token 面；数据源与 db.sqlite 同库，**判分以 db 直读为准、插件作交叉核对**（双源一致性即 NQ-5 载荷面的成本子判据）。

### 2.2 db.sqlite 直读报错面（实勘：实路径 `~/.zcode/cli/db/db.sqlite`，含 db/ 层）

WAL 只读连接 `file:...?mode=ro`；列名先 PRAGMA 核实；时间戳为 ms epoch。报错面三表（全库实弹验证 2026-09-11）：

| 表 | 报错相关字段 | 实测基线（全库） | 路测用途 |
|---|---|---|---|
| model_usage | error_type / error_code / error_message / retry_count / retryable / cancelled_by_user / context_exceeded / duration_ms / time_to_first_token_ms / finish_reason | 错误行 661（rate_limited 463 / cancelled 104 / network_error 34 / timeout 21 / invalid_request 17 / unknown 14） | ①会话健康面：invalid_request 与 context_exceeded 期望 0；rate_limited/cancelled 记录不判失败 ②TTFT/duration 成本面 |
| tool_usage | exit_code / stderr_bytes / error_type / error_code / error_message / approval_status | Bash 非零退出 377 行 | 工具失败率与分布；hooks 干扰检测 |
| turn_usage | tool_error_count / context_exceeded / model_retry_count | context_exceeded 轮数 0 | 轮级失败聚合（与模型/工具面交叉） |

口径纪律：任何计数先 PRAGMA + 抽样 3 条看真实形态再定匹配域（T1 #2 / 细则 #30 虚高 ~74× 实证）；`tool_usage.status` 取值形态未勘，用前先抽样，禁直接套 `status!='ok'` 类想当然过滤。

### 2.3 元工作预算口径（面 L 承诺，本计划兑现入预注册）

- 定义：路测自身的取证/判分/文档成本 vs 治理信息产出之比。
- 判据：按路测目录过滤 db `session`（directory 维度）→ 会话 token 总量（元工作成本）；对比 scorecard 有效判分字段数（信息产出）。**首次建基线、报告不设阈值**——v6 起才可评估比值走势。

## 3. 场景矩阵（预注册候选，执行时按授权裁剪，裁剪显式声明）

| 编号 | 场景 | 验证目标 | 判分信号 |
|---|---|---|---|
| S0 | 冒烟 | 注入在场 + 开工四步 + NQ-1/NQ-5 | rollout 注入面 + db |
| S1 | 有档续接 | NQ-2 记忆接续零重做（v4 C2 型） | 文件面 + db |
| S2 | 无档新建 | NQ-2 建载四区不缺位 | 文件面 |
| S3 | lookup 显式要求 | 端口 24/24 保持 + errpath 合规（R-A/R-C 效力保持） | toolCalls input.command 域 |
| S4 | lookup 自然触发 | 错误现场自发触发（触发两分面 N=2/N=4 复测，不达标不判失败只记数） | toolCalls input.command 域 |
| S5 | 单发知识问答 | #283 新口径：直接回答不进单发模式、无需声明 | assistant 文本域 |
| S6 | 红线夹具 | 密钥零落盘（v4 翻转样本回归，零豁免口径夹具） | 文件面 + git status |
| S7 | L2-F 全链 | 9 步全链 + GATE + 回滚点 + 进程清理（面 B #295 若拍板则加判据） | 文件面 + db + 端口核查 |
| S8 | 并发 3 会话 | hooks 零丢失 + 跨会话零串写（NQ-3） | hooks 日志 + file_path 域 |
| S9（候选） | lookup 对照实测 | 同一错误题分别走 Grep memory/ 与 detail_lookup.py，比较命中率/耗时——为「检索端口保留还是砍掉」供数据（博客两会话实证提出：现场诊断+state 判例解决率 100%，端口增量价值需数据支撑） | 双通道耗时/命中记录 |

## 4. 判分工件教训（v4 实证，固化进预注册）

- toolCalls 字段路径用 `input.command` 域（v4 假阴性教训）；
- 裸 `#N` 判定限 assistant 域，且先剔除完整前缀 `details #N`/`细则 #N` 再计数；
- GATE 宽松匹配（含 `**GATE**:` 变体）；
- rollout 清刷风险：先起增量备份守望，**逐会话即时 extract+判分**（教训 #31）；
- 入库文档/EVIDENCE 去真实盘符路径；
- 判分证据以 db 直读为准，插件输出作交叉核对，两者不一致时以 scorecard 记录差异并归因。

## 5. 诚实条款与不做清单

- 召回率 24/24 是**端口质量证据**，不表述为「行为改善已验证」——触发面（S4）只记数不设通过线（N 太小）。
- F15 真人交互保真持续不在无头可达范围，不做不判。
- R-B 错误码同义词表 / R-D 停用词仅当 S3 出现召回回归时启动（当前 24/24 无需要，防棘轮）。
- 不动 verify-release 判据门禁（脚本改动单列批次）；不改注入副本与 details 正文（v2.7 内容冻结待发行）。
- 面对照组：路测会话不入平台审计自然观测池（docs/platform-session-audit-plan-v260.md §3 排除条款同此）。

## 6. 产出物

- 逐会话 scorecards（JSON + NQ 主表）落 `D:\roadtest-v270\`（工作区外，不随仓）；汇总统计 + 元工作预算基线表。
- EVIDENCE 新节（去盘符）；version-plan v2.7 台账回填；CHANGELOG 路测行。
- 路测总成本表（db + 插件双源）；报错面分布表（§2.2 三表）。

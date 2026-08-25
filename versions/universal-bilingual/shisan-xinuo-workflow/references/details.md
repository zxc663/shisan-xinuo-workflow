# 落地细则——具体工程规范 · Landing Details — concrete engineering rules（中英双语 · Bilingual）

> 执行某一步需要"具体怎么做"时按类加载。与 43 条基础规则互补：43 条是通用地基，本文件是落地细节与规范性。Load by category when a step needs the concrete how-to; complements the 43 foundational rules with fine-grained practice.

## 1. 环境与工具链 · Environment & toolchain

1. 含中文脚本用编辑工具 UTF-8 创建，落盘后执行。Non-ASCII scripts: create UTF-8 via an editor, run after writing.
2. 路径含 `[]`/中文用 `-LiteralPath`；rg 特殊字符用 `-g`。Use `-LiteralPath` for `[]`/Chinese paths.
3. npm/npx 被策略拦截走 `cmd /c npm.cmd`。Use `cmd /c npm.cmd` when policy blocks npm.
4. 含引号 SQL 写临时文件后管道传入，不走 `-c`。Pipe quoted SQL from a file, not `-c`.
5. 中文 JSON 用 Node `fetch`，不用 `Invoke-WebRequest`。Use Node `fetch` for Chinese JSON.
6. 系统软件安装后完全退出重启（PATH 旧值）。Fully exit & reopen after system installs.
7. 后台进程用独立日志名（防 EBUSY）。Dedicated log names for background processes.
8. alpha 运行时先 `python -c "import <模>"` 验证。Verify C-extension imports on alpha runtimes.
9. 管道传中文前确认编码。Confirm encoding before piping Chinese.

## 2. 前端 / Next.js / React

10. 改 schema 停 dev；EPERM 按 PID 整树停。Stop dev around schema changes; kill full tree on EPERM.
11. 验证等待 ≥2s，失败先重跑一次。Wait ≥2s; re-run once on failure.
12. 端口先查再用。Check ports first.
13. 先停服务再构建。Stop services before building.
14. JSX 注释只在 JSX 元素内部。JSX comments only inside elements.
15. 回车提交输入用内部草稿。Internal draft for enter-submit inputs.
16. 保存前等上传队列排空。Wait for the upload queue before saving.
17. 快捷键冲突先隔离冒泡。Isolate hotkey bubbling first.
18. 覆盖插件 CSS 变量先确认层叠。Confirm the cascade before overriding plugin vars.
19. 降级分支补完整文本。Degradation branches carry full content.
20. 声明 CSS 变量后核对写入方。Verify the CSS-var writer after declaring.
21. 静态文字不常驻 transform/will-change。No persistent transform/will-change on static text.
22. `/n%` 颜色类先实测；纯 var 用 color-mix。Verify `/n%` alpha classes; use color-mix for pure vars.
23. hover 位移卡片不带 backdrop-filter。No backdrop-filter on hover-move cards.
24. CPU 用 os.cpus() 差值采样。Delta-sample `os.cpus()` for CPU.
25. 锁旧版项目禁用 latest 组件。No `latest`-preset components in pinned projects.
26. 新增大依赖先查动态 require。Check dynamic require before big dependencies.
27. 升级库前读 dist 的 Options。Read `dist/index.d.ts` Options before upgrades.
28. 升级 ESLint 先迁移 flat config。Migrate to flat config before ESLint upgrades.
29. 批量提取先小样本验证。Validate on a small sample first.
30. React Compiler 先写普通函数。Plain functions first with React Compiler.
31. 撤销功能先定义基准时刻。Define a baseline moment for undo.
32. 编辑/展示解析口径分离。Separate edit/display parsing.
33. 命名迁移先全局盘点引用。Inventory references before renames.
34. URL 参数驱动页面用客户端兜底。Client-side URL-param fallback.
35. 不水合前改 SSR 属性。No SSR-attr changes pre-hydration.
36. 全屏层与常驻控件先核 z 序。Check z-order with full-screen layers.
37. 标记职责单一。Single marker responsibility.
38. 受控富文本显式同步进编辑器。Explicitly sync controlled rich text.

## 3. 数据库 / Prisma

39. 迁移前核对模型字段。Verify model fields before migration SQL.
40. 改 schema 立即 generate。Generate immediately after schema changes.
41. 常驻连接不用模块级单例。No module-level singleton for persistent connections.
42. MODULE_NOT_FOUND 先查包目录内容。Check package-dir contents on MODULE_NOT_FOUND.
43. 非交互用 diff + 手写迁移 + deploy。diff → hand-written migration → deploy in automation.
44. 裸 SQL 时间过滤确认时区。Confirm timezone in raw-SQL time filters.

## 4. 测试 / E2E

45. 类名改动必跑全量测试。Full test run after class-name changes.
46. header ≤100、先 commit 看 lint 再 push。Short headers; lint-check before push.
47. 基线变化同步所有文档。Sync docs when baselines change.
48. audit 用官方 registry 核验。Verify audit on the official registry.
49. 消毒钩子用官方 addHook。Official addHook for sanitization.
50. 带状态模块导出测试重置。Export a test reset for stateful modules.
51. 外部 API 成功路径一律 mock。Mock external-API success paths.
52. E2E 保留预热用例。Keep a warm-up case.
53. tooltip 切换用分步 mouse.move。Stepped mouse.move for tooltips.
54. 负向断言用请求计数。Count requests for negative assertions.
55. 挂载刷新要显式 staleTime: 0。Explicit `staleTime: 0`.
56. 表单定位按 role 收敛。Locate forms by role.

## 5. API 契约

57. 删端点前全仓搜引用。Search references before deleting endpoints.
58. 以业务码判成败，null 视成功。Business code only; null = success.
59. 写接口前核对返回语义。Confirm write-API return semantics.
60. 明确返回契约 `{对象, 主键}`。Explicit `{object, primaryKey}` contracts.
61. 错误映射只在一处。Error mapping in one place.
62. 机密键服务端解密、展示掩码。Decrypt server-side; mask for display.
63. OAuth 先读官方示例，写兼容解析。Read official OAuth samples; write compatible parsing.
64. 加配置键前确认消费方。Confirm a consumer before adding config keys.
65. 结构变更同步验证脚本。Update verification scripts on structure changes.

## 6. 部署 / 运维

66. 轮询端点加监控排除。Exclude polling endpoints from monitoring stats.
67. 采集重操作后台化。Background heavy collection.
68. 监控明细落库轮转。Persist & rotate monitoring details.
69. 自监控带降级与恢复。Degradation + recovery in self-monitoring.
70. 探针覆盖真实业务路径。Probes cover real business paths.
71. 压测取 Cookie 禁重定向。No redirect when grabbing login cookies.
72. 新 API 先核对 id 语义。Verify id semantics first.
73. 静态资源不过应用层。Static assets never through the app layer.
74. 先备案再证书；HTTP-01 被阻改 DNS-01。File ICP first; DNS-01 when HTTP-01 blocked.
75. 证书失败先查根因。Root-cause before cert retries.
76. 凭据最小权限。Least-privilege credentials.
77. 部署后确认续期任务。Confirm renewal jobs after deploy.
78. 配置备份放 include 外。Backups outside include dirs.
79. 空结果命令加容错。Tolerate empty command results.
80. 部署后核对监听端口。Verify the actual listening port.
81. 改单例先 GET。GET before updating singletons.
82. 临时管理口先限制访问。Restrict temp admin interfaces first.
83. secret 落盘提取不进会话。Extract audit secrets to files, not the session.
84. 部署前先列压缩包结构。List archive structure before installing.
85. 打包不同时用 -z 与 -I。Never combine `-z` and `-I`.

## 7. 代码质量 · Code quality

86. 关键逻辑加中文注释，解释「为什么」。Chinese comments on critical logic — explain why.
87. 超 20 行考虑抽象。Abstract blocks over ~20 lines.
88. 避免不必要复制。Avoid unnecessary copies.
89. 提前返回降嵌套。Early returns over nesting.
90. 并发用显式控制。Explicit concurrency control.
91. 有意义描述性命名。Descriptive names; no abbreviations.
92. 函数单一职责。One thing per function.
93. 公共 API 有文档，变更同步。Document public APIs; sync on change.

## 8. Git / 协作

94. 提交前看 git status。Check `git status` before commits.
95. git 带 -C 绝对路径。`-C <absolute path>` for ambiguous dirs.
96. 提交前密钥扫描，CI 必跑。Secret scan pre-commit; CI mandatory.
97. 直连超时走代理。Proxy on direct-connect timeouts.
98. 纯文档移动可 --no-verify。`--no-verify` only for doc/asset moves.
99. URL 白名单：// 拒绝 → / 放行 → 协议枚举。Reject `//`, allow `/`, then protocol list.
100. dev 不依赖模块级缓存跨路由。No module-cache reliance in dev.
101. 决策留档。Archive decisions.

## 9. 会话 / 备份 / 治理细则 · Sessions / backups / governance

102. 知识沉淀只读头部索引再按需检索。Read knowledge docs by head index first.
103. 会话收尾双写知识（AI 版 + 个人版），无则写明。Dual-write knowledge at session end.
104. 重复问题先检索既有结论直接对齐。Align to existing conclusions on repeats.
105. 新 Skill 走体检→离线备份→登记链路，禁止跳过。New Skills: vet → offline-backup → register; never skip.
106. 新规则走六步流程 + 编号/引用完整性校验。Six-step rule loop + integrity check.
107. 备份分层（异地 + 本地 + 恢复演练），推送/备份附说明。Layered backups with explanations.
108. 私有主仓与发布仓分离；发布前残留扫描零命中。Separate private main / release repo; residue scan before push.
109. 根目录只留运行文档，过程文档进历史目录。Running docs at root; process docs to history.
110. 外部引用当次登记（名称 + 链接 + 用途）。Register external references immediately.
111. 季度自动清单复核文档一致性。Quarterly auto-list doc reconciliation.

## 10. 深挖补充细则 · Deep-dive details（开发日志真实踩坑提炼）

### 10.1 环境与工具链 · Environment & toolchain

112. 跨平台构建产物不可复用（`.next` / 原生二进制），各平台各自构建。Build artifacts are per-platform.
113. 镜像下载先列目录确认版本；npm 超时用镜像源 + 二进制镜像变量。List mirror dir first; mirror registry on timeout.
114. 重写 git 历史后重建 origin、提前 stash；中文路径统计多通道交叉验证。Rebuild origin after history rewrite; cross-verify stats.
115. Git SOCKS 单独配 `http.proxy socks5h://`；ConvertTo-Json 加 `-Depth`。Separate SOCKS proxy; explicit `-Depth`.
116. Windows 下 bash 可能指向未装 WSL：用 Git Bash 显式路径。Use explicit Git Bash path.

### 10.2 前端 · Frontend / React / Next

117. 含事件处理器组件必须 `"use client"`（RSC 边界 500）。Event handlers need `"use client"`.
118. NextAuth v5：middleware `getToken` 显式传 secret；HTTPS 生产显式站点地址 + secureCookie。Explicit secret / site URL / secureCookie.
119. dev 加路由后 500 先清构建缓存。Clear stale build cache on dev 500s.
120. 服务端返回 Prisma Date 先序列化 ISO（防 hydration mismatch）。Serialize Prisma Dates to ISO.
121. TanStack 预取靠 queryKey 精确相等；搜索框分离输入值与已提交值。Exact queryKey; separate input/submitted values.
122. 筛选变化手动 setPage(1)，不用 useEffect。Manual setPage(1) on filter changes.
123. 乐观更新 setQueryData / 删除 invalidateQueries；keepPreviousData 防闪烁。Optimistic via setQueryData; keepPreviousData.
124. 首载/重试 loading 用 `!data && isFetching`。`!data && isFetching` for load/retry.
125. 多操作面板用 `mutation.isPending && mutation.variables === id`。Per-row pending via mutation.variables.
126. zustand persist SSR 用 noop storage。Noop storage for SSR persist.
127. 「ALL」占位不直接传 Zod enum。Don't send "ALL" to a Zod enum.
128. 弹窗三通道关闭（ESC / 遮罩 / 按钮）。Modals need three close channels.
129. 全量与筛选后数据分离；渲染函数先写 DOM 再读 DOM。Separate full/filtered data; build DOM before reading.
130. 操作标识与状态值分开；枚举不当 CSS 类名。Separate act/status; no enum as class.
131. 大 blur 配根级 overflow-x hidden。Root overflow-x hidden for big blur.
132. Grid/Flex 子项加 minmax(0,1fr) / min-w-0。minmax(0,1fr)/min-w-0 for flex children.
133. sticky 侧栏父容器用 stretch。Stretch the sticky-sidebar parent.
134. 展开动画用 grid-template-rows 0fr↔1fr。0fr↔1fr expand animation.
135. 滚动阈值用视口比例。Viewport-relative scroll thresholds.
136. 弹层被困用 createPortal 挂 body。createPortal trapped popovers to body.
137. 时间相关文案挂载后客户端计算。Client-side time copy after mount.
138. 截图间距只作线索，以真实 rect 坐标为准。Trust real rect coords, not screenshots.

### 10.3 后端 · Backend / database

139. Prisma 外键字段用 UncheckedUpdateInput。UncheckedUpdateInput for FK updates.
140. 可空 JSON 用 Prisma.DbNull / JsonNull。DbNull/JsonNull for nullable JSON.
141. 唯一键冲突捕获 P2002 追加后缀重试。Catch P2002, retry with a suffix.
142. 最新值在事务内 select；状态机显式校验状态。Select latest in-transaction; validate state-machine state.
143. 跨字段校验合并对象级 superRefine。Object-level superRefine for cross-field.
144. 配置阈值写入范围校验；分页 Number.isFinite 兜底。Range-validate thresholds; guard pagination.
145. 每页条数与后端上限三处同步。Page-size sync across schema/service/tests.
146. 多步写必须真事务 + timeout；多态孤儿随删除清理。Real transactions; clean polymorphic orphans.
147. 低内存批量分批并发 + 原子递增。Batched concurrency + atomic increments.
148. 非交互用 migrate diff + deploy；migrate status 核对漂移。diff+deploy in CI; check drift.

### 10.4 测试 · Testing / E2E

149. 先断言登录成功再跑业务断言；防登录限流误伤。Assert login first; guard rate limits.
150. Playwright 优先 domcontentloaded + 固定等待。domcontentloaded + fixed waits.
151. mock 按实际调用顺序排布；E2E 配套清理 + DB 复核。Order mocks; cleanup + DB-count verify.
152. 清空输入用 value='' + dispatchEvent input。Clear via value='' + input event.
153. E2E 数据独立性 + 防锁定 + 删除以 DB 为准。Per-case data; deletes assert via DB.
154. has-text 匹配祖先：用精确子级选择器；workers 用 2/1。Precise selectors; fewer workers.
155. 模板生成 JS 必须 node --check。`node --check` generated JS.

### 10.5 部署 · Deployment / ops

156. 低内存服务器禁原地构建：本地 standalone → tar → 上传。Never build in place on low memory.
157. 纯净副本组装发布包 + 显式注入生产 env；standalone 手动补齐数据/静态。Clean-copy builds; explicit prod env.
158. 生产形态跑真实流量基线；SWR + 单飞去重。Production-shape baselines; SWR + single-flight.
159. 进程内定时器 .unref()。`.unref()` in-process timers.
160. 破坏性大升级分步 + 回滚点。Stepwise destructive upgrades + rollback.
161. pm2 delete + start 刷新环境；nginx -t 失败回滚。pm2 delete+start; nginx -t rollback.

### 10.6 API / 安全 · API / security

162. 公开写接口 IP 限流；登录防账号枚举。IP rate limits; no account enumeration.
163. 统一错误契约：code!==0 才算失败，data:null 合法。code!==0 = failure; data:null legal.
164. 导出 CSV：UTF-8 BOM + 公式注入防护 + 条数上限。BOM + formula-injection guard + cap.
165. CSRF 比较 Origin 与 Host 的主机名。Compare Origin vs Host hostnames.
166. 富文本消毒白名单 + 协议限制；路径防穿越。Sanitize + protocol allowlist; path traversal guard.
167. 下载令牌 HMAC + 过期 + 常量时间比较。HMAC + expiry + constant-time tokens.
168. 敏感操作审计留痕；角色三层一致。Audit trails; three-layer role consistency.
169. 配置/密钥落库加密（AES-GCM），读取掩码；防自我锁死。Envelope-encrypt config; no self-lock.

### 10.7 协作 · Collaboration / process

170. 对账式审查：设计声明 ↔ 代码证据 ↔ 实测三层互证。Reconcile design/code/runtime.
171. 决策回写用户原话与依据；批量替换前确认命令成功。Record decisions verbatim; verify commands.
172. 正则替换防误吞 + 幂等；每批跑验证四件套。Guard regex over-matching; verify quad per batch.
173. 过时文档归档而非删除，归档后更新交叉引用。Archive, don't delete; update refs.

## 11. 铁律与 Agent 纪律补充 · Iron laws & agent discipline

### 11.1 代码质量铁律 · Code-quality iron laws

174. DRY / 单一真相源：一处知识只留一个权威版本，校验/转换/错误码映射不各写一份。DRY/SPOT: one authoritative version per piece of knowledge.
175. KISS：满足需求前提下选最直白最少概念实现。KISS: simplest direct implementation.
176. YAGNI：只在真正需要时实现，不为将来预建抽象/工厂/配置/脚手架。YAGNI: no speculative abstractions.
177. 删除优于添加：最短可用 diff 胜出；刻意简化标注天花板。Deletion over addition; shortest working diff.
178. 组合优于继承 + 最少知识（LoD）。Composition over inheritance + Law of Demeter.
179. 开闭原则：对扩展开放、对修改封闭。Open/closed.

### 11.2 Agent 工作流纪律 · Agent-workflow discipline

180. 上下文 40-60% 规则：到 40-60% 主动压缩/落盘/拆会话；指令随时间褪色需重申。40-60% context rule; instruction fade-out.
181. 长任务 checkpoint 停靠：每步落盘压缩防上下文污染。Checkpoint stops; prevent context poisoning.
182. 停止规则：下一步边际收益为负或低于 token 成本即停。Stopping rule: stop when marginal value is negative.
183. 人为审查边界：机器可验证的（lint/type/测试/证据）不留给人；人审只留产品/架构/边界/运维风险。Human review only for product/architecture/edge/ops risk.
184. Review for weakness：不只查正确性，排序最薄弱风险。Rank the weakest risks.
185. 验证优先：先想验证再动手，每个改动带证据。Verification first; evidence per change.

### 11.3 风险分级证据（补充 L1/L2/L3）· Risk-tier evidence

186. L3 附加证据：认证/计费/迁移/权限/破坏性/生产重写，须集成/E2E 覆盖关键路径 + 回滚计划 + 观测 + 架构风险审查。L3: E2E coverage + rollback plan + observability + architecture review.

## 12. 源项目深挖补充 · Source-project deep-dive（2026-08-26 审查 863KB 开发日志 + 踩坑库/知识沉淀）

187. [环境 Env] Windows 系统保留端口段导致 EACCES（Hyper-V 保留）：先 `netsh interface ipv4 show excludedportrange` 查保留段再选端口。System-reserved port ranges cause EACCES — check excluded ranges first.
188. [环境 Env] Windows schannel 证书吊销检查拦 curl 直连：必要时 `--ssl-no-revoke`。Use --ssl-no-revoke when schannel revoke checks block curl.
189. [环境 Env] MCP/配置变更不热加载：完全退出应用 + 新建会话才生效；仍不可用走替代通道。Config changes are not hot-reloaded — restart + new session; else fallback.
190. [前端 Frontend] 弹性/拖拽动效只作用 `transform`/`opacity`，动 width/height 撑动父级与网格行高。Animate only transform/opacity, not width/height.
191. [前端 Frontend] SPA 路由跳转后旧 DOM ref 失效：每次视图变化重新获取。Re-acquire DOM refs after every route/view change.
192. [前端 Frontend] 文本/位置 API 有 0 基/1 基口径差异（"永不命中"常源于此）：先确认口径 + 纯函数单测锁定。Confirm 0-based/1-based conventions; lock with a pure-function test.
193. [前端 Frontend] "性能差"常因反馈不在交互点：加载态落在交互元素而非仅全局遮罩。Put loading state on the interactive element.
194. [前端 Frontend] 配色以 WCAG 对比度实测驱动；语义色改动后必跑对比度校验。Drive colors by measured WCAG contrast.
195. [数据库 DB] Prisma `where` 保证非空但 TS 仍可空（不按 where 收窄）：业务层显式处理 null。TS stays nullable even when where guarantees non-null.
196. [数据库 DB] 含可空字段的复合唯一键 upsert 不接受 null：用非空哨兵值；迁移先删外键再 UPDATE。Nullable composite-unique upsert needs a sentinel; drop FKs before UPDATE.
197. [数据库 DB] 限流最易"死配置"：上线前逐个核对公开写接口真正调用限流。Rate limits are often dead config — verify each write endpoint.
198. [API] 异步任务统一「202 + 轮询状态端点」约定，跨层文档保持一致。Async tasks: unified 202 + poll-status convention across docs.
199. [运维 Ops] 进程内定时任务（备份/调度）离线即停摆：关键备份用独立计划任务兜底。In-process jobs die offline — schedule critical backups independently.
200. [运维 Ops] 部署验证抽样断言静态/关键资源 200，不只 curl 首页 HTML。Sample-assert static/key resources, not just the HTML shell.
201. [Git] 一次性令牌推送成功后 remote 改回无令牌 URL。Restore token-less remote URL after a one-time-token push.
202. [AI] 推理型模型 `max_tokens ≥ 512`，否则思考吃光预算输出为空。Reasoning models need max_tokens >= 512.
203. [AI] LLM/视觉 API「HTTP 200 但内容为空」按失败处理并切换。Treat HTTP-200-empty as failure; switch/retry.

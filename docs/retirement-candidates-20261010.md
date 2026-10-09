# 细则退役候选清单（G4/T8 · 机器生成）

> 生成：2026-10-10｜全集 406 条（details.md 实解析）｜检索命中 155 条｜工件提及 15 条｜**候选 243 条**。
> 口径：候选 = 全集 − usage 日志命中 − 种件 #N 提及（usage 自 2026-09-29 起累积，当前窗口尚浅）。
> 边界：**只列候选不删条**；升退役须人工复核+双批零观测确认（低频保命条款误列风险自担）。

## [未标域]（176 条）

- details #2：PowerShell 路径含 `[]` / 中文时用 `-LiteralPath`；rg 遇特殊字符用 `-g`；检索键
- details #3：`npm` / `npx` 被执行策略拦截时走 `cmd /c npm.cmd` / `cmd /c npx.cmd`；
- details #4：含引号 SQL 写入临时文件后管道传入（`Get-Content -Raw | docker exec -i psql`
- details #5：中文 JSON body 用 Node `fetch` 或显式 UTF-8 字节，不用 `Invoke-WebReque
- details #6：系统级软件安装后必须完全退出应用重启（运行中进程 PATH 是旧值）；检索键：部署运维监控。
- details #7：后台进程一律用独立日志名（防 EBUSY）；检索键：部署运维监控。
- details #8：alpha / beta 运行时先验证 C 扩展导入（`python -c "import <模块>"`）；检索键：其他
- details #12：端口先查再用（`Get-NetTCPConnection`），避开保留段；检索键：部署运维监控。
- details #14：JSX 注释只写在 JSX 元素内部——`return (` 内不直接放注释；检索键：前端组件交互。
- details #15：回车提交式受控输入必须用内部草稿 state；检索键：前端组件交互。
- details #16：异步落盘 + 保存链路必须等上传队列排空再取最新内容；检索键：异步并发算法。
- details #17：快捷键冲突先隔离冒泡再处理（编辑器内 `preventDefault()` + `stopPropagation()`）
- details #18：覆盖插件 CSS 变量先确认层叠；`@layer base` 内的自定义属性易被插件默认覆盖；检索键：前端组件交互。
- details #19：降级分支必须补完整文本——自问「内容是否完整可见」；检索键：前端组件交互。
- details #20：声明 CSS 变量后立即核对写入方；检索键：前端组件交互。
- details #21：静态文字不要常驻 transform / will-change（文字发虚）；检索键：前端组件交互。
- details #23：hover 位移卡片禁止同元素带 backdrop-filter（玻璃卡白色竖条）；检索键：前端组件交互。
- details #26：新增大依赖先查是否动态 require（Turbopack：`serverExternalPackages`）；检索键：
- details #29：批量提取先小样本验证再做全量（正则兼容 `\r?\n`）；检索键：其他杂项。
- details #31：撤销类功能先定义「基准时刻」（快照 = 进入页面 / 上次保存，保存成功后更新基准）；检索键：前端组件交互。
- details #32：编辑态与展示态解析口径分离（编辑宽松保结构、展示严格过滤空项）；检索键：前端组件交互。
- details #33：任何命名迁移先全局盘点引用，E2E 与文案同批更新；检索键：数据库SQL。
- details #36：全屏 fixed 层与常驻控件并存时先核 z 序；检索键：前端组件交互。
- details #37：标记职责单一：跳转方只跳转，展示方在展示时写标记；检索键：其他杂项。
- details #38：受控富文本必须显式同步进编辑器（effect 比对后 `setContent`）；检索键：前端组件交互。
- details #39：迁移前核对模型字段再写 SQL；检索键：契约响应形态。
- details #41：常驻连接禁止模块级变量做单例（挂全局对象跨热重载复用）；检索键：部署运维监控。
- details #42：`MODULE_NOT_FOUND` 先查包目录内容数量（目录存在 ≠ 包完整）；检索键：构建产物缓存。
- details #43：非交互自动化用 `migrate diff` → 手写迁移 → `migrate deploy`；检索键：数据库SQL。
- details #44：裸 SQL 过滤时间列先确认时区口径（显式 `AT TIME ZONE 'UTC'`）；检索键：数据库SQL。
- details #46：提交信息 header ≤100、英文词转小写、先 commit 看 lint 再 push；检索键：记录留档纪律。
- details #48：`npm audit` 结论必须官方 registry 核验（镜像可能返回空；固定镜像源还会致 audit 端点 405
- details #50：带进程内状态的模块必须导出测试重置（beforeEach 调用）；检索键：部署运维监控。
- details #53：连续 tooltip 切换用分步 `page.mouse.move(x, y, { steps: 8 })`；检索键：前
- details #55：SSR 首帧 + 挂载即刷新必须显式 `staleTime: 0`；检索键：前端组件交互。
- details #56：替换表单控件库后先跑依赖该控件的 E2E；表单定位按 role 收敛；检索键：构建产物缓存。
- details #57：删除端点前全仓搜索前端引用；检索键：契约响应形态。
- details #58：以业务码为唯一成败依据；删除类接口 `null` 视为成功；检索键：契约响应形态。
- details #59：写接口客户端前先核对返回语义（失败统一 `fail`，绝不 `ok(null)`）；检索键：契约响应形态。
- details #60：新建 / 重构 API 明确返回契约 `{ 对象, 主键 }`；检索键：契约响应形态。
- details #61：错误映射只在一个地方（移除路由局部包装）；检索键：前端组件交互。
- details #62：机密键：服务端解密、对外掩码——绝不把原始值传给客户端；检索键：部署运维监控。
- details #63：对接外部 OAuth 先读官方响应示例，写双形态兼容解析 + mock 单测；检索键：契约响应形态。
- details #64：新增配置键前先确认消费方存在；检索键：契约响应形态。
- details #66：新增轮询类端点先加入监控排除清单（防 P99 自计尖峰）；检索键：契约响应形态。
- details #67：采集类重操作一律后台化（fire-and-forget + 缓存 + 单飞）；检索键：构建产物缓存。
- details #68：需要详查的监控明细必须落库、轮转、可导出；检索键：部署运维监控。
- details #69：自监控必须带降级与恢复机制（busy-aware 降频）；检索键：部署运维监控。
- details #72：使用新 API 前先核对 id 语义；检索键：契约响应形态。
- details #73：静态资源绝不过应用层（反向代理直服 + 长缓存）；检索键：构建产物缓存。
- details #74：国内服务器先备案再配证书；HTTP-01 被 WAF 阻断时改 DNS-01；检索键：部署运维监控。
- details #75：证书验证失败先排查根因再重试（防速率限制）；检索键：部署运维监控。
- details #77：部署后必须确认续期任务存在（短期证书）；检索键：部署运维监控。
- details #78：配置文件备份放 include 目录外；检索键：部署运维监控。
- details #80：部署后核对实际监听端口（特权端口回退是静默的）；检索键：部署运维监控。
- details #81：改单例前先 GET 当前值（单例更新是全量校验）；检索键：部署运维监控。
- details #82：任何临时管理口先限制访问再启动（防绑全网卡）；检索键：部署运维监控。
- details #84：部署脚本先列压缩包结构再安装（压缩包可能是目录而非单文件）；检索键：部署运维监控。
- details #85：打包脚本不要同时用 `-z` 与 `-I`（tar 压缩选项冲突）；检索键：构建产物缓存。
- details #86：为关键逻辑和可能造成理解困难的部分添加简明中文注释；注释解释「为什么」，不解释「是什么」；检索键：代码质量命名。
- details #87：单段代码超约 20 行时优先抽象 / 聚合（提取函数、合并重复逻辑）；检索键：代码质量命名。
- details #88：避免不必要的对象复制 / 克隆，尽量复用引用，仅在确有需要时复制；检索键：代码质量命名。
- details #89：避免多层嵌套，优先提前返回（early return）降低复杂度；检索键：代码质量命名。
- details #91：命名用有意义、描述性名称；遵循项目 / 语言规范；避免缩写与单字母（循环 `i` 等约定俗成除外）；检索键：代码质量命名
- details #92：函数只做一件事；相关代码放在一起；保持适当抽象层次；检索键：代码质量命名。
- details #93：公共 API 提供清晰文档；代码变更后同步更新注释与文档；检索键：契约响应形态。
- details #94：提交前看 `git status`（lint-staged 格式化会产生新改动——重新 add）；检索键：记录留档纪律。
- details #95：git 命令在目录不明确时带 `-C <绝对路径>` 显式指定；检索键：记录留档纪律。
- details #97：外网托管平台直连超时走代理（HTTP / SOCKS）；代理未启动不会回退直连；检索键：部署运维监控。
- details #98：纯文档 / 资产移动提交可用 `--no-verify`；代码改动一律不豁免；检索键：记录留档纪律。
- details #99：URL 白名单顺序：空 → `//` 拒绝 → `/` 站内放行 → 协议枚举（纯函数 + 单测）；检索键：契约响应形态
- details #100：dev 下不要依赖「模块级缓存 + 跨路由失效」；检索键：前端组件交互。
- details #101：决策必须留档——每会话重复问同样问题 = 决策未留档的信号；检索键：安全会话令牌。
- details #102：开工必读按固定顺序执行，知识沉淀类文档只读**头部索引**再按需检索正文（上下文纪律，不整文读）；检索键：记录留档纪律/
- details #104：用户重复反馈同类问题时，先检索任务记录 / 经验库 / 知识索引，命中引用既有结论直接对齐，不重复完整调研；检索键：记录
- details #105：新 Skill 引入必须走链路：先下载到临时目录做安全体检（静态扫描 `curl` / `wget` / `eval` 
- details #106：新增工作流规则必须走六步流程（采集 → 五问分析 → 四段模板 → 用户审批 → 落盘复检 → 留档提交），并配套脚本校
- details #107：备份分层：至少一层异地 + 一层本地；理想三层（版本库多端推送 / 本地外移 / 生产备份 + 定期恢复演练）；每次推送
- details #108：私有主仓与开源发布仓分离：开发在私有主仓，发布仓仅在明确里程碑同步；对外推送前跑验证 + 残留扫描（品牌 / 账号 / 
- details #109：根目录只保留运行文档，过程性文档（设计稿 / 审查报告 / 一次性清单）进历史目录并附说明；检索键：记录留档纪律。
- details #110：会话中新增引用的外部网站 / 开源项目 / 工具，当次登记到项目参考资源文档（名称 + 真实链接 + 用途），禁止先引用
- details #111：每季度用自动清单复核模块文档一致性（数字 / 配置键 / 引用），发现漂移立即纠偏并留档；检索键：承载注入触达。
- details #114：重写 git 历史后需重建 origin、提前 stash 在途改动；中文路径统计多通道交叉验证（ls-files / 
- details #115：Git 走 SOCKS 需单独配置 `http.proxy socks5h://...`；`ConvertTo-Json
- details #118：NextAuth v5：middleware 中 `getToken` 必须显式传 `secret`；HTTPS 生产须
- details #121：tanstack-query 预取命中靠 queryKey 精确相等（参数名与值全一致）；搜索框分离「输入值」与「已提交
- details #122：筛选变化手动 `setPage(1)` + 清空选中，不用 useEffect 监听（queryKey 已自动重取）；检
- details #123：乐观更新用 `setQueryData`（queryKey 与列表查询一致），删除用 `invalidateQuerie
- details #124：首次加载与重试 loading 用 `!data && isFetching`（isLoading 在 error 后重
- details #125：多操作面板用 `mutation.isPending && mutation.variables === id` 精确禁
- details #126：zustand persist 在 SSR 用 noop storage（getStorage 不接受 undefine
- details #127：前端「ALL」占位值不直接传 Zod enum：后端显式含 "all"，或值为 "all" 时不传该参数；检索键：其他杂
- details #128：弹窗类组件三通道关闭（ESC / 遮罩 / 关闭按钮），缺一即 UX 缺陷；检索键：前端组件交互。
- details #130：操作标识与状态值分开定义（`act` vs `status` 混用致徽章 undefined）；枚举值不能直接当 CSS
- details #131：装饰性大 blur 元素配根级 `overflow-x: hidden`（blur 扩大绘制区撑出横向滚动）；检索键：其
- details #132：Grid / Flex 子项默认 `min-width:auto` 被内容撑破：容器 / 子项加 `minmax(0,1
- details #133：sticky 侧栏「读一半消失」根因是父容器 `align-items:start`：改 `stretch`；检索键：其
- details #134：展开 / 折叠动画用 `grid-template-rows: 0fr↔1fr` + 内层 `overflow:hidd
- details #136：弹层被遮罩或父级 transform 困住时（Radix 给 body 加 pointer-events:none）用 
- details #139：Prisma 有外键的模型更新外键字段用 `UncheckedUpdateInput`（UpdateInput 只接受关
- details #140：Prisma 可空 JSON 置空用 `Prisma.DbNull` / `JsonNull`（DB NULL 与 JS
- details #141：唯一键冲突捕获数据库错误（P2002）后追加后缀重试一次，不做存在性预检（并发竞态）；检索键：数据库SQL。
- details #142：需要最新值的更新在事务内用 `select` 返回该字段；状态机类写操作显式校验当前状态；检索键：契约响应形态。
- details #143：复杂跨字段校验合并为单个对象级 `superRefine`（Zod v3 refine 回调无 ctx.parent）；
- details #146：多步骤写操作必须真事务 + 显式 timeout；多态表随父删除在事务内清理孤儿数据；检索键：代码质量命名。
- details #148：`migrate dev` 非交互不可用：`migrate diff` + 手写迁移 + `migrate deploy
- details #150：Playwright 等待优先 `domcontentloaded` + 固定等待（networkidle 对持续连接 
- details #151：mock 队列按实际调用顺序排布 `mockResolvedValueOnce`（分支短路会错位）；E2E 配套清理脚本
- details #155：模板字符串生成 JS 后必须 `node --check` 校验（转义层级错误生成损坏文件）；检索键：其他杂项。
- details #157：发布包必须在纯净副本 `npm ci + build` 组装，显式注入生产 env（防开发 .env 静默覆盖）；sta
- details #158：性能基线用生产形态（standalone / server）跑真实流量落盘统计，数据驱动优化；慢接口用 SWR + 单飞
- details #159：进程内定时器必须 `.unref()`（否则测试进程不退出挂起）；检索键：前端组件交互。
- details #161：`pm2 restart --update-env` 不总能补入新变量：彻底刷新用 `pm2 delete + star
- details #162：公开写接口必须有 IP / 目标级限流；登录防账号枚举（未知与已知账号统一响应）；检索键：契约响应形态。
- details #163：统一错误契约：`code !== 0` 才算失败，`data:null` 是合法成功（等价 204），客户端不当错误处理
- details #165：CSRF 同源校验取 Origin hostname 与请求 Host 的主机名比较（忽略端口），不用服务监听地址；检索
- details #168：敏感 / 安全操作必须审计留痕；角色权限三层一致（middleware 白名单 + route 校验 + 前端菜单过滤）
- details #169：站点配置 / 密钥落库前加密（AES-GCM 信封），读取掩码；管理面板防自我锁死（不能停用当前账号）；检索键：契约响应
- details #171：决策项回写文档写明用户原话与依据；批量替换 / 脚本化前确认命令执行成功（重定向检查退出码）；检索键：其他杂项。
- details #172：正则批量替换防误吞（非贪婪吞到下一匹配）：加结构约束 + 幂等可重跑；每批改动固定跑验证四件套（test + typec
- details #173：过时文档归档而非删除：先整合关键信息，归档后批量更新交叉引用；检索键：代码质量命名。
- details #174：**DRY / 单一真相源（SPOT）**：每处知识 / 逻辑只留一个权威版本；校验、转换、错误码映射不各写一份（多处真
- details #175：**KISS**：满足当前需求前提下选最直白、最少概念的实现；一行正则塞满业务规则或巨大函数是变相复杂；检索键：代码质量
- details #176：**YAGNI**：只在真正需要时实现；不为「将来可能」预建抽象、工厂、配置、脚手架（later 会为自己脚手架）；检索
- details #178：**组合优于继承 + Law of Demeter（最少知识）**：优先组合；对象只与直接朋友交谈，不链式扒深处字段；检
- details #179：**开闭原则**：对扩展开放、对修改封闭；新行为优先新增而非改动既有分支；检索键：其他杂项/开闭原则。
- details #181：**长任务 checkpoint 停靠**：每步 checkpoint 落盘并压缩上下文，防上下文污染（context 
- details #182：**停止规则**：下一步边际收益为负或不再明显高于 token 成本时即停，不硬堆产出；检索键：安全会话令牌/停止规则。
- details #184：**Review for weakness, not just correctness**：审查不只查正确性，要定位最薄
- details #187：[环境] Windows 系统保留端口段（Hyper-V 保留）会让指定端口 EACCES（即使无进程占用）：先用 `n
- details #188：[环境] Windows schannel 证书吊销检查会拦截 curl 直连：必要时用 `--ssl-no-revok
- details #189：[环境] MCP / 配置文件变更不热加载：须完全退出应用并新建会话才生效；仍不可用直接走替代通道，不反复重启重试；检索
- details #190：[前端] 弹性 / 拖拽类动效只允许作用在 `transform` / `opacity` 上：用 width/heig
- details #191：[前端] SPA 路由跳转后旧 DOM ref 失效：每次视图变化后重新获取引用再操作；检索键：前端组件交互。
- details #192：[前端] 文本 / 位置类 API 存在 0 基与 1 基口径差异（"查找永不命中"常源于此）：比较前先确认口径并抽纯函
- details #193：[前端] 用户感知的"性能差"多来自反馈不在交互点：加载态必须落在交互元素上，而非只靠全局 loading 遮罩；检索键
- details #195：[数据库] Prisma 即使查询 `where` 保证非空，返回类型仍可能是可空（TS 不按 where 收窄）：业务
- details #196：[数据库] 含可空字段的复合唯一键 `upsert` 不接受 null：改用非空哨兵值；迁移须先删外键再 UPDATE（
- details #197：[数据库] 限流规则最易"死配置"（定义了但从未接入调用）：上线前逐个核对公开写接口是否真正调用限流；检索键：契约响应形
- details #198：[契约] 异步任务统一「202 + 轮询状态端点」约定，并在设计 / API / 功能文档间保持一致；检索键：契约响应形
- details #200：[运维] 部署验证不能只 curl 首页 HTML（200 ≠ 页面完整）：必须抽样断言静态资源 / 关键资源返回 20
- details #202：[AI] 推理型模型默认 `max_tokens ≥ 512`：否则 token 全花在思考过程，输出为空；检索键：安全
- details #203：[AI] LLM / 视觉 API「HTTP 200 但内容为空」一律按失败处理并自动切换，不当作成功结果；检索键：契约
- details #206：[前端] Tailwind v4 默认不扫 workspace 包源码：只在组件库内使用的工具类（任意值/尺寸类）会出现
- details #207：[前端] 共享包同时被 node(require) 与 Vite(import) 消费时，单 CJS 产物会被 Roll
- details #210：[前端] cva className 字符串内嵌单引号（如 `[class*='size-']`）会破坏外层引号——改选
- details #211：[前端] lucide-react 高版本移除品牌图标（`Github` 导出 TS2305）——品牌 mark 用内联
- details #216：[契约] query 参数契约层 `z.coerce.number()` 收口；契约新增必填字段同批改单测夹具；「动作→
- details #217：[后端] 框架静态子路由必须注册在 `:id` 参数路由之前（`x/import` 在 `x/:id` 前），否则被参数
- details #218：[数据库] Prisma「已应用迁移被文本修改」drift 会要求 reset（=删库红线）——用 `migrate d
- details #225：[环境] Hyper-V 保留端口段会静默吞掉容器端口映射（容器起不来）——换端口绕行；Node 原生 fetch 取 
- details #227：[流程] 复刻/重做类规格先以源码/现状为证呈报、由用户裁定方向再动手；测试脚本调后端前先读契约字段名（直觉命名必翻车：
- details #231：[流程] 长会话归档防呆（最后任务块跨小时 barrier 时 state/experience 会过时）：最后一个 c
- details #234：[流程] 提问带推荐+理由；超时/空答→能取消则取消，否则按实况推荐方案+「待确认」标注——空答不当批准。*来源：用户偏
- details #235：[流程] 上下文卫生：大输出>~40 行→文件+摘要；子代理只留结论；已归档引用路径；模糊先重取；~5 块盘点。*来源：
- details #236：[流程] 新项目无文档→docs/project-info.md 六节（含模块真实状态表与调研导航）；已有文档→索引不重
- details #238：[流程] 有日志模块→报错必经日志：catch 三件套（记日志+降级提示+审计）、五查含「已接日志」、console/空
- details #244：[MCP] 普通模式没有提问工具——提问工具默认仅规划模式启用：启用对应特性开关；不可用时按结构化协议文本提问；新环境先
- details #245：[视觉] 多图对比误判「一致」——大图被降采样：先压缩（宽 900 / q80）；单图 ≤2MB、每次 ≤4 张；检索键
- details #246：[视觉] 视觉 API 401——密钥失效/过期：更新凭据配置；密钥失效先查凭据；检索键：契约响应形态。
- details #247：[视觉] 批量审查太慢 / 429——免费接口限流：并发 3 路 + 退避重试；批量审查用并发脚本；检索键：契约响应形态
- details #249：[视觉] 免费模型短时可用后全 402——账户余额 / 免费额度动态：路由前查余额；余额 0 不入默认链；路由表以实测为
- details #250：[前端] 本地跑 Lighthouse 清理临时目录 EPERM——chrome-launcher kill 时删除被占
- details #252：[前端] 配置键护栏误报——护栏正则把 `get("…")` 误判为配置键：白名单登记非配置键参数；同族（护栏误杀合法路
- details #253：[前端] 配置类型报错（嵌套对象）——配置类型只支持扁平键：改用扁平键；检索键：契约响应形态。
- details #259：[环境] 旧版 TypeScript 解析不了新版 @types/node（类型声明用了超前语法特性）——升降级任一侧前
- details #261：[构建] `sideEffects` 字段与实际副作用不一致会破坏 tree-shaking（该摇的摇不掉 / 不该摇的
- details #263：[契约] 库新增选项的契约设计先调研同类库惯例（命名 / 默认值 / 是否破坏性变更）再定案，不凭偏好造词；破坏性变更走
- details #264：[JS] `Symbol.toStringTag` / 原型链标记可被伪造——类型派发、深拷贝分发不得依赖可伪造标记做正
- details #268：[前端] chalk 实例级 level 污染：`chalk.red.bold.level = N` 改的是**根实例*
- details #269：[契约] 响应体只能消费一次：中间层（afterResponse / 拦截器）先读 body 后，下游报 `Body a
- details #270：[契约] 配置继承时数组/信号是「拼接」还是「替换」：`extend` / merge 类 API 的数组选项（sign
- details #273：[流程] 紧凑档（短上下文部署参数表）：生效方式 = `memory/preferences.md` 标注「紧凑档」→ 
- details #274：[流程] 大文件读取协议（1bcoder /scan 的纪律化）：>300 行文件 → 先读头部索引 / 标题 → gr
- details #279：[流程] 决策化石识别（读取端——「决策可重开」）：读到历史否决 / 被否候选 / 依据 / 偏好时**先验前提是否仍成
- details #284：**设计规范档前置（设计类动作，前端尤甚）**：任何设计类动作（方案/结构/组件/文档框架/流程）动手前，逐组件调研成熟

## [流程]（26 条）

- details #290：高危改向词先澄清
- details #291：演示数据必须标注非真实来源
- details #293：知识档案落地形态（留档要求）
- details #296：审查核账双律（窗口收口≠条目闭环）
- details #306：技术选型前场景清单必问（问清楚比直接做重要·十维全景）
- details #308：调研义务不可用「诚实声明」豁免
- details #311：留档时间戳强制到分钟
- details #312：设计评审暂停（设计确认先于写码）
- details #313：开工资源盘点声明
- details #315：任务分解用平台计划工具
- details #316：接手遗留项目必补功能全景文档
- details #331：纯文档会话也要 commit 基线
- details #343：提交粒度与分支模型
- details #346：计划模式必问协议
- details #347：能力检索协议（清单匹配形态）
- details #348：借口拦截表（反合理化）
- details #350：强制力四级（必须/应当/可以 + 压缩级）
- details #356：宪章五维与五门（管的边界=怎么做）
- details #357：工程 Token 观·双向仲裁
- details #358：分档 Token 预算（风险分级匹配）
- details #359：高杠杆白名单与天花板
- details #360：Token 沉淀外部化（防重复消耗）
- details #365：状态锚定三触发
- details #366：状态段极简 STATE 行（防腐化）
- details #387：配置写入口必须校验
- details #393：批量文本操作三件套

## [运维]（10 条）

- details #295：长驻进程清理（交付收尾端口归零）
- details #301：ln 三参数多源形态陷阱
- details #304：演练通过≠模块可用（模块验收走真实入口）
- details #307：版本控制开局与阶段性 commit（按场景）
- details #320：目标模式运行协议
- details #328：系统级可逆配置变更判级
- details #341：结构化日志与可观测性
- details #377：提交验真（git show --stat）
- details #385：部署机差异卫生
- details #399：健康检查必须探真实依赖路径

## [前端]（6 条）

- details #288：动效与主题切换可感知性
- details #289：数据可视化基线
- details #292：信息冗余 = 低上下文容错
- details #381：[hidden] 与组件 display 互斥
- details #391：受控输入用内部草稿 state
- details #397：SSR 首帧+挂载即刷新须显式 `staleTime: 0`

## [交付]（4 条）

- details #319：分析材料必须兑现行动清单
- details #322：交付前分级自审
- details #344：交付说明三件
- details #355：GATE 11 字段（caps/effort）

## [测试]（3 条）

- details #298：变异验证护栏（护栏非装饰）
- details #394：audit/安全结论以官方 registry 核验
- details #407：自测只盖正向样例时，反向变异是盲区

## [沟通]（2 条）

- details #317：区分问题与前提再响应
- details #325：每轮复述强制（追加/继续不豁免）

## [执行]（2 条）

- details #321：大批次拆分跨会话执行
- details #329：增量需求解释显式化可替代提问

## [工具链]（2 条）

- details #368：判据即代码：路测结论须可复算
- details #376：Edit old_string 禁含节头

## [数据]（2 条）

- details #386：ORM 时间列裸 SQL 先核时区
- details #400：密钥错位判定与定期复核

## [协作]（1 条）

- details #318：被否=追加修正信号

## [设计]（1 条）

- details #323：完备性枚举（缺失比错误更隐蔽）

## [上下文]（1 条）

- details #324：长会话每轮纪律自检

## [文档]（1 条）

- details #333：项目文档分型（Diátaxis 最小集）

## [代码]（1 条）

- details #336：代码风格基准（命名与文档注释）

## [契约]（1 条）

- details #338：API 正向设计规范

## [工具]（1 条）

- details #364：GATE 外部审计端口（gate_audit/探针抽检）

## [必问]（1 条）

- details #369：L3 数据删除的无人值守合规双路径

## [治理]（1 条）

- details #375：活跃会话取证轮转窗

## [安全]（1 条）

- details #398：机密双不落

## 观测命中样本（usage 日志）

- details #1 ×1（含中文等非 ASCII 的脚本一律用编辑工具以 UTF-8 创建，脚本落盘后再执行（防编码污染）；检）
- details #9 ×2（管道传中文前确认编码（Unicode 转义或写文件）；检索键：Windows工具链。）
- details #10 ×1（改 schema 前后停 dev 服务；`prisma generate` 报 EPERM 时按 P）
- details #11 ×1（验证脚本等待 ≥2s，失败先重跑一次（dev 首次请求现场编译）；检索键：E2E测试走查。）
- details #13 ×1（构建纪律：先停服务再构建；检索键：构建产物缓存。）
- details #22 ×1（涉及 `/n%` 的颜色类先实测 computed style；纯 var 颜色用 `color-m）
- details #24 ×1（系统级 CPU 用 `os.cpus()` 差值采样，采集器首次只建基线；检索键：部署运维监控。）
- details #25 ×1（锁旧版库的项目禁用 `latest` 预设生成组件（如 shadcn）；检索键：细则回流晋升。）
- details #27 ×1（升级库前先读 `dist/index.d.ts` 的 Options（`transform` 等旧选）
- details #28 ×1（升级 ESLint 前先迁移 flat config；检索键：数据库SQL。）
- details #30 ×1（React Compiler 下先写普通函数；需要 memo 时以编译器推断依赖为准；检索键：构建产）
- details #34 ×1（URL 参数驱动初始状态的页面优先客户端 `useSearchParams` 兜底；检索键：前端组件）
- details #35 ×2（不要水合前改 SSR 渲染属性（hydration 警告）；检索键：前端组件交互。）
- details #40 ×1（改 schema 立即 generate（停服务 → generate → 重启）；检索键：契约响应）
- details #45 ×2（类名改动必跑全量测试（断言旧类名 / 字段）；检索键：契约响应形态。）
- details #49 ×2（消毒钩子用官方 `addHook` 方式注册，写完用恶意输入单测验证；检索键：安全会话令牌。）
- details #51 ×2（涉及外部 API 的 E2E 成功路径一律 mock（只断言「链已接上」）；检索键：契约响应形态。）
- details #52 ×2（新增 E2E 保留预热用例（首条超长超时）；检索键：E2E测试走查。）
- details #54 ×2（负向网络断言用 `page.on("request")` 计数 + 固定等待后断言 0；检索键：E2）
- details #65 ×1（结构 / 文案变更时同步搜索并更新验证脚本；检索键：E2E测试走查。）
- details #70 ×1（健康探针必须覆盖真实业务路径（依赖挂掉时不许 fail-open 200）；检索键：构建产物缓存。）
- details #71 ×1（压测取登录 Cookie 必须禁重定向，解析 302 的 Set-Cookie；检索键：安全会话令牌）
- details #76 ×1（凭据文件最小权限（chmod 600 等价）；检索键：安全会话令牌。）
- details #79 ×1（所有可能空结果的命令加容错（`|| true` 或显式判断）；检索键：部署运维监控。）
- details #83 ×1（需审计的 secret：输出重定向到文件后提取，禁止进会话回显；检索键：安全会话令牌。）
- details #90 ×1（并发 / 批量 / 定时任务必须用显式并发控制（限流 / 队列 / 信号量 / 并发上限）；检索键：）
- details #96 ×1（每次提交前密钥扫描；CI 必跑；检索键：安全会话令牌。）
- details #103 ×1（会话收尾必须双写知识：AI 版（触发场景｜判断｜行动）追加知识沉淀文档并维护头部索引；个人版（类比 ）
- details #112 ×1（跨平台构建产物不可复用：编译缓存 / 原生二进制（`.next`、swc 等）各平台需各自构建；检索）
- details #113 ×1（镜像下载不猜版本号：先列目录确认最新版再下载；npm 超时用镜像源 `npm ci --regist）

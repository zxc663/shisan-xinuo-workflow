# 工作流 Skill 漏洞账本（2026-09-24 战役立）

> 范围：shisan-xinuo-workflow 家族（核心/flows/roles/product）+ 其运行时依赖（平台 CLI/hooks/注入链）。用户指令「同步检查工作流Skill的漏洞」的产出物。
> 处置纪律：**确凿漏洞**（死引用/自相矛盾/脚本坏/事实性失效）→ 修复（源库+安装根双同步，改前备份）；设计层争议 → 只记账待裁决。每条带证据 file:line。

## 发现清单

| # | 严重度 | 症状 | 证据 | 处置 | 状态 |
|---|---|---|---|---|---|
| F1 | 高（无人值守入口失效） | ZCode CLI 无法独立启动：缺 built-in provider 配置，报「无法定位 CLI ZCode Built-in Provider Config」两路路径均不存在；手工补造需从应用存储取密钥材料=红线禁止 | 实测 2026-09-24 01:47：`node zcode.cjs --version`→0.16.9 OK；无参启动→报错退出（NR1/evidence 前终端截图）；`resources/glm/provider/` 目录不存在；env 名 `ZCODE_BUILTIN_PROVIDER_BUNDLED_CONFIG_FILE`/`ZCODE_BUILTIN_PROVIDER_CONFIG_FILE`（zcode.cjs 内 grep 实证） | 平台侧缺陷（非 Skill 本体）；影响=CLI 场景（CI/无人值守/真会话自动化）全部走 GUI；Skill 文档若引用 CLI 工作流须标注「当前平台版本不可用」 | 🟡 记账（平台问题，Skill 侧防御性标注待排） |
| F2 | 中（假阳=误拦合法交付，已修复） | spec-trace-gate 清单文件用 `read_text().split()` 按空白切块加载，与绑定字段整串比对不对称——多词 backend id（`GET /favorites`）合法清单必假阳 T5；selftest 直调 check() 绕过文件入口故未发现（自测路径≠真实入口） | 变异电池 m6 对照组修复前 exit=1 假阳（m0-m5 正常）；根因 file:line=spec-trace-gate.py:96-97（修复前） | **已修复+双副本同步**：源库 commit 03f7ab2（git 即回滚点）＝安装根（Write 同步，diff -q 一致）；selftest 增文件全路径回归 ok3/ok4；电池 7 格复跑全绿 | ✅ 已修复（mutation-batteries/spec-trace/RESULTS.md） |
| F3 | 低（清单卫生） | ponytail 与 ux-feature-design 双目录重复注册（C:\Users\zxc66\.zcode\skills\ 与 C:\Users\zxc66\.agents\skills\ 各一份）——技能清单出现同条目双份 | NR4 真会话自检报告（NR4-02-answer.png）+本机 ls 双目录证实（2026-09-24 02:45） | **已裁决（2026-09-25 速裁包批复）**：以 .agents 为准；物理去重涉删除，按白名单制挂起待用户在场执行 | 🟡 已裁决待物理执行 |
| F4 | 中（触发可靠性） | 产品包在真会话自然语言任务中未被模型选择加载（NR1 实测：任务精确命中 description 触发词但未触发）；可见性/注入/hooks 三断点经 NR4 排除，断点=选择层显著性 | docs/real-session/nr-batch1-judgment.md §二；NR1 工作区无产品包流程工件（grep 实证） | **v0.2.2 description 触发词前置**（源库 4837f5e=安装根）；**NR6+NR8 双样本验证通过**（档2 全流程触发+档1 轻量档自适配触发，均自证能力检索命中） | ✅ 已修复验证（N=2 处理组 vs N=1 对照组） |
| F5 | 中（新门禁假阳反面：漏报——已修复） | l0-l5-gate 对「goal 文件存在但 north_star 键缺失」静默放行（None 落空全部检查）——发现渠道恰是 NR6 真会话工件的独立复跑：statechart JSON 被误喂给 l0-l5 时本应拦却 OK | 复跑记录 02:55（l0-l5 收到 statechart JSON 输出 OK 0 warning）；夹具 g7 补后 exit=1 | **已修复+双副本一致+selftest ok5+夹具 g7**；源库 5e478f9（含两新脚本补入库纠正：git add -u 漏收 untracked=虚假提交风险，已 git show --stat 验真） | ✅ 已修复 |
| F6 | 低→中（门禁人机工学，两个独立真会话重复实踩） | statechart-gate 只收 --file 命名参数，位置参数报错——NR6 与 NR7 两个真实会话首次调用均踩中，均自行纠错重跑（未致命但每次浪费一轮工具调用） | NR6 evidence-01-early.png；NR7 evidence-nr7-mid.png（「参数形态是 --file，修正重跑」） | **已修复**：源库 b206266（位置参数兼容）+selftest 7 断言+双形态复跑全绿（2026-09-24 04:5x，账本行补记） | ✅ 已修复 |
| F7 | 中（基线机制脆弱性→已修复闭环） | frontend-lint/a11y 两 gate 基线以「展示串」精确匹配——违例串含原始空白（跨行标签换行/缩进），输出格式微调即全量失配，存量被误报新增（a11y-gate 博客仓格⑤首跑 exit=1 异常暴露） | 2026-09-25 00:4x：格③④绿→格式修复后格⑤异常（基线 182 条全失配）；根因=a11y-gate.py scan_file 返回串拼接处 | **已修复+复验闭环**：违例键空白规范化（`re.sub(r'\s+',' ')`）；格②'③'④'⑤'重跑全绿（基线稳定/注入命中/清理往返一致）；修复前后证据对在 RESULTS.md | ✅ 已修复（mutation-batteries/a11y/RESULTS.md §缺陷闭环） |
| F8 | 中（headless 会话能力残缺，平台侧） | CLI headless 会话无原生提问工具（`No permission client configured`）且 browser-use 后端不可用——必问协议在 headless 通道结构性受阻 | NR16 真会话实测（probe-output 尾部+其 decision-ledger 记账） | Skill 侧防御已验证（v0.2.1 无人值守禁静默下沉——NR16 首证生效：四项地基推荐档+账本待复核，零静默）；平台侧提问端口修复待排 | 🟡 记账（防御已验证/平台待修） |

## 系统体检（2026-09-24 01:55 实测）

| 项 | 结果 | 证据 |
|---|---|---|
| ① product 包回指实存性 | ✅ 全实存（references 9 件+scripts 5 件；跨包 skill-usage.md 在核心包实存） | ls 实测；注意首轮 for+[ -f ] 输出全 MISSING 为沙箱假象（规律=仅末项 OK），已用 ls 直取真值排除——**本机 shell 验证一律 ls 目录取地面真值，禁信复合循环 test 输出** |
| ② 五门禁 selftest | ✅ 5/5 PASS（01:52） | product-object/registry/spec-trace/statechart/usage-probe `--selftest` rc=0 |
| ③ product 源库 vs 安装根 | ✅ 仅 decision-ledger.md 1 件漂移（与 HANDOVER 队列⑩一致，无意外漂移） | diff -rq 实测 |
| ④ 核心包回指实存性 | ✅ references 9 件全实存（details.md 132KB 等） | ls 实测（for+[ -f ] 假象同①排除） |
| ⑤ 核心包 5 脚本可跑性 | ✅ 5/5 `--help` rc=0 | agent_log_rotate/detail_lookup/gate_audit/risk_scan/syncer |
| ⑥ ZCode CLI 独立启动 | ❌ 见 F1 | 实测报错 |

> 阶段结论（01:55）：家族本体无死引用、脚本全可跑、双副本仅 1 件已登记漂移——**纪律层健康；真正缺口在「真实会话证据链」（NR1 进行中）与平台工具链（F1）**。


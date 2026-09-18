# 独立审查报告 · shisan-xinuo-workflow 源库（v3.0 重构中间态）

范围：口径一致性 / 缺口与失效引用 / 角色包编号有效性 / 设计档一致性。方法：只读 Read + grep 逐条核对，未运行 `facts_sync.py`、未运行 `verify-release.ps1`；git 仅执行只读 `git log`（含 `-S`/`-p` 追溯）。行号均为 HEAD（5eaf8cd）实读行号。

---

## 一、口径一致性

**GATE 字段（9 与 11 双轨）**

- [P1] `package.json:4` — 描述仍写「GATE 九字段单源」「9-field GATE」，与 v3.0 定版的 11 字段冲突；此字段是 npm/Gitee 介绍文案来源（发行面）。｜证据："GATE 九字段单源 + 开工状态行"、"9-field GATE + session status line"（同段已写「355 条细则 26 类」，字段口径未联动）｜建议：改「GATE 11 字段（caps/effort）」并同步英文段。
- [P1] `README.md:61/109/111` — 三处「九字段/9 字段」，与同文件 `README.md:227`「§6 GATE 11 字段」自相矛盾。｜证据：:61 "GATE 可重跑（level/v/cmd/exit/files/refs/errpath/lessons/exempt）"；:109 "**GATE 完成块（九字段一行式定版）**…包级 9 字段一行"；:111 "常驻保留集（L3 六项/红线/GATE 九字段/TOP…）"｜建议：三处统一为 11 字段（或回指注入核心）。
- [P1] `skill/shisan-xinuo-workflow/templates/project-rules.md:14` — 核心模板仍给 9 字段字面模板（项目承载创建即复制）。｜证据："GATE 单行 9 字段 `GATE: {level=,v=,cmd=,exit=,files=,refs=(grep 实测),errpath=,lessons=,exempt=}`"｜建议：补 caps/effort 或改纯回指。
- [P1] `skill/shisan-xinuo-workflow/templates/hooks/carrier_reminder.example.py:33` + `templates/hooks/README.md:11` — **机制级载体**仍推 9 字段；`deploy_injection` 读仓库模板，下一次部署会把 9 字段重新注入平台（当前会话收到的 hooks 文本即 9 字段）。｜证据：:33 "收尾 GATE 9 字段：level/v/cmd/exit/files/refs/errpath/lessons/exempt"；README:11 "GATE 9 字段指针…改措辞先改注入核心再同步此处"｜建议：批⑤ 部署前必须改模板，否则「部署=回退」。
- [P1] `skill/shisan-xinuo-flows/references/workflows.md:228` — 流程包 GATE 定义为 9 字段，与核心 11 字段冲突。｜证据："**GATE 块（9 字段）**……字段清单：`level / v / cmd / exit / files / refs / errpath / lessons / exempt`"｜建议：改 11 字段回指注入核心。
- [P2] `docs/diagrams/working-principle.svg:51-52` — README 首屏配图（README:84 引用）仍画 9 字段。｜证据："GATE 9 字段一行可复跑：level / v / cmd / exit / files / refs / errpath / lessons / exempt（包级 9 字段 / 子块简式 3 字段）"｜建议：重绘该两行（facts_sync 只对账该图的条数/类数，不覆盖字段名）。
- [P3] `scripts/evals/extract_roadtest.py:14` — 判分器注释「GATE 9 字段」；若批⑤ 探针按 11 字段判分，注释与判据脱节。｜建议：随批⑤ runner 改造一并更新。
- [OK] GATE 字段核心与执行细节 — 抽查 2 处一致：`skill/shisan-xinuo-workflow/references/injection-core.md:62` 与 `SKILL.md:165` 同为 11 字段（level/v/cmd/exit/files/refs/errpath/lessons/exempt/caps/effort），且权威回指方向一致（SKILL 声明「唯一权威=注入核心 GATE 段」）。

**细则条数/类数**

- [OK] 单源与数值承载 — 抽查 5 处一致：details.md 头部「活跃 355 条，类数=分节数 26」（实计：编号条目 356 行 −〔归档〕#180 = 355；`## N.` 分节实计 26；〔预留槽〕0）↔ `README.md:36/230/273/295/297/311`、`docs/project-info.md:4/35`、`package.json:4`、`AGENTS.md:27`、`templates/memory-anchor.md:25`、`docs/reference-sources.md:21` 数值均为 355/26。
- [P2] `AGENTS.md:27` — 起笔写「细则 330→355·26 类」：330 是 v2.8.0 时点值，v2.9.0 发行时点是 344/25，「355」实际来自 v3.0 批①——该写法跳过 v2.9.0 造成归因错误。｜证据："（…细则 330→355·26 类）"｜建议：改「344→355·26 类」并加「（v3.0 批①，未发行）」限定。
- [P2] `scripts/facts_sync.py:42` — AGENTS.md 承载正则硬编码 `细则 330→(?P<n>\d+)·(?P<c>\d+) 类`：只断言 n/c，**起点值「330→」永不被断言**，上述错值可长期通过门禁。｜证据：`('AGENTS.md', [r'细则 330→(?P<n>\d+)·(?P<c>\d+) 类']),`｜建议：起点值入组或去掉该叙述中的起点。
- [P2] `docs/project-info.md:4/24` — 头行「更新：2026-09-16」+「判级：…v2.9.0 修正批…细则 355 条/26 类」把 355/26 归给 v2.9.0 批；「当前」块同段又写「五副本重部署 count=344 5/5」（344 为 v2.9 部署值）——355 与 344 并列且未说明差因（批①-④ 已过、副本按计划未部署）。｜建议：更新为 v3.0 批①②③④ 中的口径并注明「副本待批⑤ 后部署」。
- [P2] `docs/reference-sources.md:18` — 「活跃细则 355（终态=修正批 #333-#335+G 直写批 #336-#344+#295 双击转正）」：叙述只到 #344，无法解释 355（#346-356 未列）。｜建议：补批① 立条段。
- [OK] 症状索引覆盖 — 抽查新增区：索引尾部 6 行域「计划模式与需求对齐→#346,#352｜能力检索与工具闲置→#347｜反合理化→#348,#349｜强制分级与宪章边界→#350,#356｜影响矩阵→#351｜异常观察与完成验收→#353,#354,#355」在场，与批④「355 全覆盖」宣称方向一致。
- [OK] rules 条数 — `references/rules.md` 实计 47 条，与 `SKILL.md:224`、`README.md:230`、`memory-anchor.md:25` 一致。
- [OK] 注入核心体量 — `references/injection-core.md` 实测 5,991 code points（13,499 bytes），与 `README.md:111`「5,991 字符 ≤6K」一致。

**判级三级同步链与章节号**

- [OK] 判级同步链指向 — `injection-core.md:16`「权威源=SKILL.md §2.2」属实：`SKILL.md:73` 即「2.2 判级速查」，且 SKILL §2.2 自称「唯一权威源…本块 → injection-core.md → 平台副本」，方向一致。
- [P1] `docs/project-info.md:48` — 仍是旧链「SKILL §2/§5.2（三级同步链：§5.2 → injection-core → 平台注入副本）」——§5.2 在 v3.0 已不存在（现 §2.2）。｜证据："改主流程/判级 → SKILL §2/§5.2（**三级同步链：§5.2 → injection-core → 平台注入副本，改完全链重部署**）"｜建议：改 §2.2。
- [OK] SKILL.md 内部交叉引用 — 章节目录实读为 §0-§11（含 §2.0-§2.7、§4.1），抽查 §2.1/§2.6/§6/§7/§8/§10/§4.1/§9/§11 引用全部指向真实存在的节；injection-core 指向的 §2.2/§2.3-§2.5 全部存在。
- [P2] 裸 `#NNN` 引用回潮（违反自身「完整前缀、禁裸 #NNN」口径；details 头部仅豁免 TOP 行+GATE 字段，2.9 批 F-29 曾专项清理，批① 重写后回归）。｜证据：`SKILL.md:102`（`#284`）、:108（`#345`）、:116（`#349`）、:125（`#239`）、:140（`#306`）、:146（`#279`）、:160（`#281`）、:166（`#354`/`#345`）、:185（`#255`）、:249（`#280`）；`injection-core.md:12`（`#347`）、:45（`#312`）、:67（`#348/#349`/`#346`）；对照同文件合规写法 `SKILL.md:41`「`details #349`」｜建议：批⑤ 修正批统一为 `details #N`。
- [P3] `SKILL.md:39` — 可以级列「知识包」，但知识包未建（计划档被否候选：knowledge 包首版无内容面）。｜建议：删词或标注「未建」。
- [OK] 三包家族名与依赖声明 — 抽查 6 处一致：`SKILL.md:3/28/217/225/257`、`README.md:28/103/232-235`、`docs/project-info.md:35-37`、`flows/SKILL.md:18` 与 `roles/SKILL.md:18`（两包均声明「假设核心在场，纪律以核心与注入核心为准」），无指向不存在路径的包引用。
- [P2] 红线计数 — `SKILL.md:37`「必须级…唯一例外=用户显式豁免——红线 8 条」与 `injection-core.md:49-57` 实列 7 条（密钥/回滚点/不假实现/负向结论/负载形状/子代理直送/写文件自动动作）不符；设计档 §11.6 亦称 8 条（含新增 2 条），落地把新增两条放进了「关键条款/§0」而非红线节。｜建议：二选一——红线节补第 8 条（能力闲置）或改「7 条」。

## 二、缺口与失效引用

**文本损坏（同根因三连，已随 v2.9.0 发行）**

- [P0] `README.md:1` — 首行损坏（换行与引用标记丢失、中文字段被数字覆写），且 **v2.9.0 发行 zip 携带同一损坏文本**。｜证据：现文 "…十三希诺 Agent 工作22525**渐进式工程治理 Skill——…"；`git log -p -S "22525"` 显示由 098dd0b（2026-09-16 推荐序施工批）引入，原文为 "…十三希诺 Agent 工作流" + 空行 + "> **渐进式…"（gitignore 的 `README.md.bak-readme-vis`，2026-09-09，可逐字对证）；`unzip -p dist/shisan-xinuo-workflow-v2.9.0.zip README.md`（README.md 61,609B，2026-09-16 13:53 打入）首行同损坏——该 zip 即 GitHub/Gitee Release 附件，npm files 含 README.md 故描述面同样受影响｜建议：修复首行 + 给 verify 加「README 首行形态」冒烟断言（现 7 项门禁均不覆盖纯文本形态）。
- [P1] `AGENTS.md:2` — 项目级注入文件首行参差：行首多出「25 」（原文 `> 本仓库 = …`，引用标记被 4 字符覆写）。｜证据：现文 "25 本仓库 = 十三希诺 Agent 工作流 Skill 的源库与标本合库。…"；同一 098dd0b 引入（git log -p -S "25 本仓库"）｜建议：同理修复。
- [P1] `docs/project-info.md:3` — 导航档首行注释损坏（`**` 与「本」被同长度覆写为 `*25`）。｜证据：现文 "> *25文件是索引入口（六节导航），权威内容在对应源文件，绝不重复**（§2.5）。"；原文 "> **本文件是索引入口…"（098dd0b 引入）｜建议：同理修复。

> 根因说明（证据链）：098dd0b 提交说明自认「facts_sync 双组 fix bug（同 match 多命名组正序替换漏写 c 组→span 降序替换）」，并称「version 键名误伤被 verify C 网兜」——即该批 --fix 的错位替换当时被发现了 version 键一处，但上述三处同长度覆写未被任何门禁拦住，随后即提交、发行（该提交后紧接 c947280 发行批），verify 显示 7/7 ALL PASS。

**flows 包 → 核心的旧节号引用（系统性，批② 迁移未随 v3.0 重编号同步）**

- [P1] `skill/shisan-xinuo-flows/references/workflows.md` 10 处指向 v2.9 版 SKILL 节号（现节号：L1=§2.3 / L2-S=§2.4 / L2-F=§2.5 / 判级=§2.2 / 速查表=§11 / bootstrap=§2.7 / 重载序=§10）｜证据：`:22`「每步出口产物见 SKILL.md §2.4 表」（应 §2.5）；`:24`「权威块见 SKILL.md §5.2」（应 §2.2）；`:91`「（§12 A3 速查表）」（应 §11）；`:98`「（§0.1 / SKILL §2.4）」（应 §2.5）；`:99`「（SKILL §2.3，默认）」（应 §2.4）；`:105`「对接真相清单（强制，SKILL §2.3）」（应 §2.4）；`:133`「见 SKILL.md §2.5」（应 §2.7）；`:191`「（SKILL.md §5.2 判级速查权威块）」（应 §2.2）；`:249`「（§12 P3）」（应 §11）；`:266`「（源自 SKILL.md §9）」（应 §10）｜建议：批⑤ 按现节号统一回填（这是本次审查最集中的失效引用簇）。
- [P1] `skill/shisan-xinuo-workflow/references/details.md:516`（#328） — 判级权威锚定句仍指 §5.2：「L3 边界唯一权威=SKILL §5.2 封闭清单」。该条系 2.9 修正批 F-10 定版条款，v3.0 重编号后锚定失效。｜建议：改 §2.2。
- [P1] `skill/shisan-xinuo-flows/references/workflows.md:135/263` — 指向核心包文件但按本包相对路径书写，包内不存在：:135「完整四步引导见 `references/new-project-bootstrap.md`」（该文件在 `skill/shisan-xinuo-workflow/references/`）；:263「从 `templates/agent-log-template.md` 创建」（该文件在核心 `templates/`，flows 模板 7 件无此件）。｜建议：加包名前缀。
- [P3] 同文件 `:248/:250` — 裸文件名引用核心文件（`skill-usage.md` §4、`section.md`/`security.md` 检疫）未加包名前缀；包的 references/ 内不存在这些文件。
- [P2] `skill/shisan-xinuo-workflow/references/rules.md:44`（§28）「（SKILL §8 / §12 AG）」与 `details.md:443`（#281）「SKILL §12 AG」 — §12 不存在（AG 行现于 §11 速查表）。｜建议：改 §11。
- [P2] `README.md:112/116/123/125/299` — 同样指向已删除的 §12（RE / P3/P8 / ZE / C1 / AG 五行）。｜建议：改 §11。
- [P2] `README.md` 其余过时节号 — :107「SKILL §2.3」（对接真相应 §2.4）；:114「SKILL §11」（状态面应 §9）；:118「§4 · §10」（经验回流应 §8）；:119「SKILL §2.5」（bootstrap 应 §2.7）；:121「SKILL §3.1」（无此子节，自更新在 §3）；:128「SKILL §10 总纲」（写作分层在 §0）。｜建议：批⑤ 一次性回填。
- [P1] `README.md:122` — 功能全景「配套模板/钩子/子代理｜规划/验收/任务记录/复盘/回滚点/预算/钩子/审查子代理｜templates/」已失效：批② 后这些流程模板在 flows 包、审查子代理在 roles 包，核心 `templates/` 现仅 agent-log-template/project-rules/memory-anchor/workspace-memory/hooks。｜建议：改为「流程模板→flows/templates；角色模板→roles/roles」。
- [P1] `skill/shisan-xinuo-flows/SKILL.md:3` — description（触发面）宣称「9 类任务工作流分册（新功能开发 / Bug 修复 / 重构 / 数据迁移 / 发布 / 前端设计 / 运维 / 文档 / 探索调研）」，但 workflows.md 实际分节为 新项目15步/Bug修复/UI设计重构/部署运维/文档交接/重大决策/目标模式/多会话编排/新增规则——「数据迁移」「探索调研」无对应节（全文件 grep 零命中），另有 4 类未在 description 列出。｜建议：description 与实际分册对齐。
- [P3] `skill/shisan-xinuo-flows/references/workflows.md:267` — 「见 `templates/prompt-budget.template.md`」等包内相对路径未标基准（该文件在 references/ 下读到后按同级解析易误指向 `references/templates/`）。
- [P3] `scripts/README.md:49/59/71/76` — 「v2.8.0 当前口径」与示例输出 "SKILL version=2.8.0 ; package.json version=2.8.0" 已过时（现 2.9.0，v3.0 在途）。
- [P2] `docs/project-info.md:51` 与 `:44` 自相矛盾 — :51「RELEASE-CHECKLIST.md（v2.8.0 待执行版）」vs :44「v2.9.0 发行批已回填」。:53「决策 1-42」亦过时（§三 已至少至 53 号，见 `项目信息.md:93`）。
- [P3] `skill/shisan-xinuo-workflow/references/skill-usage.md:57` — 引用流程包「能力缺失降级」为节名，flows 包无此节名（对应内容在 workflows.md:250 条目）。
- [OK] 路由表/引用表路径抽查 — 核心 SKILL §10 十二行路径全部真实存在（injection-core / platform-adaptation / skill-usage / rules / details / security / never-list / new-project-bootstrap / local-model-glossary / templates 四件+hooks / flows / roles）；flows 模板 7 件与核心 hooks 模板目录齐全；全仓 grep `references/workflows.md`、`templates/agents`、`templates/plan-template` 等旧路径——非历史档仅命中合法包内引用（critic.md→flows、#326→flows、flows 自己的 references/workflows.md），核心侧零残留；`roles/critic.md:17` 指向的 `shisan-xinuo-flows/templates/plan-template.md`/`task-record-template.md` 均存在。

## 三、角色包清单编号有效性

- [P1] 8/8 角色文件引用格式全部不合规：清一色裸 `#NNN`，无一处 `details #`/`细则 #` 前缀——而这些文件自身的第 8 行恰恰要求子代理「引用形态 `details #N` 完整前缀」，自相矛盾；details 头部豁免范围（TOP 行 + GATE 字段）不含角色清单行。｜证据：`roles/contract.md:17-24`（"（`#351`）"…"（`#338`）"）、`critic.md:23/29`、`frontend.md:17-24`、`perf.md:17-23`、`risk-reviewer.md:21-28`、`security-auditor.md:24`、`test.md:17-25`、`debugger.md:17/25`；每文件 `:8` "引用形态 `details #N` 完整前缀"。例外说明：`debugger.md:24`「错误必查 TOP 八条」可主张 TOP 行豁免，但同文件 :17/:25 的 `#255`/`#16` 等不在豁免内。｜建议：批⑤ 统一为 `details #NNN`（或在本包边界声明豁免并落 details 头部）。
- [OK] 编号存在性 — 抽查 35 个被引编号（#16/#147/#154/#163/#193/#214/#227/#228/#229/#233/#248/#251/#255/#256/#262/#266/#269/#284/#286/#288/#289/#292/#294/#307/#312/#328/#334/#335/#337/#338/#339/#343/#345/#351/#354）全部在 details.md 存在；8 文件逐一抽查均 ≥2 个编号（含 #346-356 新立条目区）。
- [P3] `roles/security-auditor.md` — 仅 1 处 details 编号（:24 `#334`），其余引用指向 security.md/永不清单/rules「规则 30/43」；与包内「清单引用 details 编号=视图化」的定位相比偏少（规则 30/43 经查在 rules.md 存在，无误）。
- [OK] 结构与 dispatch — 8 文件均具六字段骨架（①身份…⑥能力边界，实读 critic/security-auditor 全文件）；`roles/SKILL.md:28-37` dispatch 矩阵 8 行与 8 个文件一一对应；`SKILL.md:217` 路由表「8 角色」列举一致。

## 四、与设计档一致性（抽查）

- [OK] 强制四级 — `docs/skill-split-research-20260918.md:204-209` 与 `SKILL.md:36-40` 同构（必须/应当/可以/压缩级；「存在性不可压缩——一行也算在场，静默消失=违规」近似逐字一致）；中文定名与 GATE 短键约定（research:213-223 ↔ SKILL §0/§6）一致。
- [P2] research:207 应当级覆盖含「每步『无产物不进下一步』门控」，`SKILL.md:38` 应当级清单未列该门控（门禁句保留在 §2.5:110 但未标级）——分级清单与设计档有 1 项缺口。
- [OK] 五维/五门 — research:180（意图/验证/完成/上下文/安全门）与 `SKILL.md:35` 一致；§11.5 各项补口（能力检索/Token 观/借口拦截/完成六件套/影响矩阵/需求工程/异常观察）在 SKILL §0/§2.1/§2.4/§2.6/§6/§7 均可落位。
- [P3] 「骨架 v2 十二部件」为设计档内部编号（research:198 的部件 0-11），SKILL.md 未携带该编号体系，无法逐件对表（按机制名逐项抽查通过）；「红线 8 条」的设计↔落地差见 §一。
- [OK] 计划档 §五 与 git log 吻合 — `docs/skill-split-plan-v3.0.md:82-87` 批 0/①/②/③/④ ✅ 与提交 5288d4d→a68f8e4→7ee73b3→efac64c→5eaf8cd 逐条对位（日期 2026-09-18 一致），批⑤「待」与当前状态一致；批②「模板 7 件（原估 8 实测 7）」在 :84 有显式勘误。
- [P3] `docs/skill-split-plan-v3.0.md:17`（§一 批准版原文）仍写「模板 8 件（…/writing）」——§五已勘误但正文未回填，属批准版原文的已知偏差，建议加脚注。

---

## 总判

**口径一致性结论**：条数/类数链条（355 条·26 类）在 details 单源、README、project-info、package.json、AGENTS、memory-anchor、diagrams 六类承载点上数值一致且算式可复核，`facts_sync` 抽查点未见数值漂移——但**另两条口径链是断的**：①「GATE 11 字段」只在核心两文件（injection-core/SKILL §6）落地，README/package.json/flows 包/核心模板/hooks 模板/SVG 仍全线 9 字段，其中 hooks 模板是机制级载体，**下一次部署会按 9 字段再注入**；②「判级权威=SKILL §2.2 / 速查表=§11」的新节号只改了核心三处，flows 包（10 处）、details #328、project-info、README（11 处）仍指旧号 §5.2/§12/§2.3-§2.5，拆分施工留下系统性引用债。口径事实层另有 AGENTS.md「330→355」与 project-info「355 归 v2.9.0」两处归因错误，且 facts_sync 的 AGENTS 正则把起点值写死、门禁对这类错误天然放行。

**最重要的 3 个问题**：

1. **[P0] 已发行文本损坏三连**：`README.md:1`、`AGENTS.md:2`、`docs/project-info.md:3` 三处被同一机制（098dd0b 的 facts_sync --fix 同长度错位覆写：「流\n\n> 」→「22525」、「\n\n> 」→「\n25 」、「**本」→「*25」）损坏，且 README 损坏**已随 v2.9.0 发行**（本机 dist zip 实测携带，即 GitHub/Gitee Release 附件与 npm 描述面）。verify 7/7 ALL PASS 与 facts_sync PASS 都没拦住纯文本形态破坏——建议修复 + 补一条首行形态冒烟。
2. **[P1] GATE 9/11 双轨未收敛**：涉及 8 处活载体（README×3、package.json、project-info 无、flows/workflows.md、核心 project-rules 模板、hooks 模板×2、SVG、evals 注释）。其中 hooks 模板与项目规则模板会经 deploy/承载创建**再次分发错误契约**，属批⑤ 部署前的硬前置。
3. **[P1] 引用债集中在 flows 包与角色包**：workflows.md 对核心 SKILL 的 10 处旧节号 + 2 处包内断链（`references/new-project-bootstrap.md`、`templates/agent-log-template.md`）+ details #328 权威锚定句 §5.2 + 角色包 8 文件 100% 裸编号（且与自身第 8 行「完整前缀」要求互斥）。批⑤ 修正批若不一次性回填，v3.0 发行会把这个引用面原样带上线。

**方法与边界声明**：本报告未运行 `facts_sync.py --check` 与 `verify-release.ps1`（按审查约束），条数一致性为人工抽查；npm 实体未联网核验，发行携带性以本机 dist zip（2026-09-16 13:53 打入的 v2.9.0 附件）为准；平台注入副本（v2.9.0）与源库的差异属「三包未齐不部署」计划内状态，本报告不将其计为缺陷，但 §一 中 hooks 模板残留意味着部署后差异会扩大。

`GATE: {level=L2-S, v=只读独立审查（源库 v3.0 批④ 态 5eaf8cd）, cmd=git log --oneline -15 与 grep -rn 系列（详见正文证据行）, exit=0, files=无（只读，零写入）, refs=0（无会话文件产物，0 照报；报告内引用均带 文件:行号）, errpath=1 次 Bash exit=2（cd 后相对路径失效）→ 处置：#233 先实测后改写绝对路径续跑, lessons=①同长度错位覆写类损坏无法被数值型对账门禁捕获，需形态冒烟；②拆分重构的引用债必须随包同步回填，否则门禁绿而引用面坏, exempt=未运行 facts_sync/verify/探针；npm 实体未联网核验}`

`Context: state=读档 L=L2-S confirm=无需`


---

## 处置分诊（主控追加 · 2026-09-18 · 修正批范围待用户核定）

**已修（P0，本批即时处置）**：文本损坏三连——README.md:1 / AGENTS.md:2 / docs/project-info.md:3 按 git 原文+`README.md.bak-readme-vis` 逐字对证还原；根因=098dd0b 的 facts_sync --fix 同长度错位覆写，verify/facts 纯数值门禁天然不拦。**注：远端显示（GitHub/Gitee 已推送文本）与已发 dist zip 内的损坏需 push/重打包才能更新——待批准。**

**修正批 A【P0/P1 · v3.0 部署即收尾批硬前置】**：
1. 形态冒烟入 verify（README 首行形态断言——现 7 项门禁不覆盖纯文本形态）。
2. GATE 9→11 收敛 8 处：README×3、package.json、flows/workflows.md:228、核心 project-rules 模板、**hooks 模板×2（机制级：不改则下次部署=回退）**、SVG 两行、evals 注释。
3. 引用债回填：flows/workflows.md 10 处旧节号+2 处断链（new-project-bootstrap/agent-log-template 加包名）；details #328 §5.2→§2.2；project-info:48 §5.2→§2.2；README 11 处节号；roles 8 文件裸 #NNN→`details #N`；rules §28 与 details #281 的 §12→§11。
4. README:122 功能全景模板描述（流程模板→flows、角色→roles）。

**修正批 B【P2】**：AGENTS.md 330→355 归因改「344→355（v3.0 批①，未发行）」＋ facts_sync AGENTS 正则起点值入组；project-info:4/24 归属与 :44/51 矛盾、:53 决策号；reference-sources:18 补批① 段；flows description 与真实 9 分册对齐；scripts/README 过时口径。

**修正批 C【P3】**：extract_roadtest 注释、SKILL §0「知识包」词、skill-usage:57 节名、research 应当级补「无产物不进下一步」门控项、plan §一「模板 8 件」脚注、workflows.md:267 路径基准注。

**边界**：A/B/C 均在源库修复（非发行动作）；远端 README/描述面的可见修复需 push（仓库默认不 push，随批准/发行批）；npm 已发描述（package.json 1100 字段）下次发版携带修复。

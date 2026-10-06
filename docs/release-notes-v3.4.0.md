# v3.4.0 发行说明（2026-10-07）

> 本版主题：**弱锚结构化 + 门禁反向变异修复 + 试金石/实地轨双轨实测 + 单文件携带版**——`ev=` 升格为结构化内联键，五台产品门禁 checker 全部补反向变异样例，新增「技能基质层」协同规范与单文件硬注入载体。细则 **405→406 条（32→33 类，+`#407`）**，判据 j2.5 维持（金样本 23/23）。

## 一、这一版解决什么

三个缺口一次收口：①行为面实证「散文弱锚不可达」（stateLine 0/20、`ev=` 0/20）→ 把验证层级 `ev=` 从散文锚升为与 GATE 12 字段并列的内联键；②自测只盖正向样例的盲区（漏报 15 例实证）→ 五台 checker 十三处缺口全部修复并补反向变异自测（细则 #407）；③技能协同件散落 → 上升为「技能基质层」规范（S0-S4 层栈+层级门+装配序列+缝合契约），并交付全量核心的单文件硬注入载体。

## 二、核心变更

- **`ev=` 弱锚结构化**：验证层级（exec/cover/invariant/indep）升格为 GATE 行内联键，injection-core/SKILL/状态行模板三面同步（core 5,978/6,000）。
- **批X 五 checker 十三缺口修复**（产品工程包 0.2.7）：registry/product-object/l0-l5/frontend-lint/a11y——类型穿透、引号变体、可选绑定 catch、大写 RGB、空 aria-label、空 lang、枚举死代码；selftest 全部带反向变异样例（**#407**：自测只盖正向样例时反向变异是盲区）。
- **对标 superpowers A/C/D 施工**：flows §10 会话诊断复盘七维（外部分析+path:line 举证+自报只作对照）、§9 五问升六问（构造「不写会错」压力场景留基线失败证据）。
- **风险扫描扩域**：risk_scan 高危域扩 IaC 落盘+基础设施 reload（扩域实测命中）。
- **退役机制首跑验证**：usage-probe 双面读数（双批次窗口未满，本批零删除）。

## 三、试金石与实地轨（本版新增实测面）

- **七张合成夹具卡**（jz-01 记账 → jz-07 定时任务管理器）：植入缺陷八台门禁全接，回流真缺口十二项落 checker——spec-trace T6 幽灵端点、T5/T6 路径参数段归一化、a11y A3 纯符号变体/A3b 伪按钮新形态、l0-l5 IA 档 fail-open→fail-loud、C13 累计组合形、frontend-lint 排除规则子串误伤修复等；每项带反向变异自测与跨卡回归零漂移实证。
- **两个存量项目实地扫**（site-01 闭环实验 / site-02 财务助手，只读）：spec-trace 39/39 全过正面实证；「recovery 语义只有 markdown 载体无机器可读 JSON」跨项目双击→statechart-gate 新增 `--probe-recovery` 探针（首版 2/5 精度→收紧后双站各 1 命中零误报）；判定域豁免双回流（canvas 绘制参数、证据目录）实测降面。
- **盲评试点**（B 臂 5/6 机判全 PASS + A 臂载体摘除未遂全还原，归因未定论如实留档）。

## 四、技能基质层 + 单文件版（新交付形态）

- **技能基质层（Skill Substrate）**：S0-S4 技能层栈、层级门三段式、装配序列五步、缝合契约六硬字段、使用归因零新字段——落 `references/skill-usage.md` §9 与单文件「装配接口」段。
- **单文件硬注入载体**（`skill/shisan-xinuo-single/`）：核心包全部纪律条款的自含单文件（17,036 字符），含 8 平台「要动的文件」硬注入表；受控重建可复现推导（核心原文+受控 rep 断言表，字节级比对）。

## 五、机检收口（发行时实测）

verify-release **8/8 ALL PASS** · FACTS PASS（406 条/33 类，编号至 #407）· 判据自测 **23/23**（j2.5）· 五平台注入 `--check --hash` **5/5 HASH-OK**（`sha256:06db20781d69`）· dist `shisan-xinuo-workflow-v3.4.0.zip`（**108 项 / 2,210,333B**，Set-diff 108=108）。

## 六、安装

```powershell
# 家族源库根执行（四包齐装）
powershell -ExecutionPolicy Bypass -File scripts/install-skill.ps1 -Family
# 或单装核心包
powershell -ExecutionPolicy Bypass -File scripts/install-skill.ps1
```

npm：`npm install @zxc663/shisan-xinuo-workflow@3.4.0`（含同内容文件面）。

MIT License · 作者：十三希诺

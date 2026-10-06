# 产品工程母架构与定位边界

> 2026-09-23 立档（用户三条裁决：定位加边界+母架构路线 / 四档风险矩阵 / 三件契约 schema）。
> 依据：docs/three-definitions.md（三定义加固版）+ 用户附呈三方讨论（2026-09，硬层/软层、schema、风险自适应、先跑高风险闭环）。

## 一句话定位

`shisan-xinuo-product` 是**产品工程包**——Product Contracts 规范层的**第一垂直域**。已落地两段：**上游「产品对象定义」（2026-09-23 加：页面职责/能力清单/主次/能力完整性/可运营性）** + **中游「交互工程」（六问/状态/追溯/门禁/账本）**；母架构其余域**未实现**。

## 修正二：上游产品对象链（2026-09-23 用户定稿）

> 边界：**Product Engineering ≠ Product Innovation**——创新回答「应该创造什么」（产品决策侧）；产品工程回答「既然决定做，它具体应该是什么」。核心敌人=「产品已决定，但 AI 把它做歪了」。四处偏移（产品是什么≠功能怎么实现｜页面职责≠页面交互｜功能优先级≠功能完整性｜产品闭环≠前端闭环）与完整裁决见 direction §十二。

```
Product Decision → Product Scope → Page/Feature → Capability → Priority → Completeness → Operation
                                    └────────── 上游：产品对象六问（已落地·盘点级）──────────┘
→ Interaction → State/Runtime → Implementation → Verification/Evidence
   └────────── 中游：交互工程（已落地·契约级：六问/statechart/spec-trace/gate/账本）──────────┘
```

- 上游细则 = 本体 `references/product-object.md`（六问+页面级闭环八组+可运营性清单+主次角色表）；判定表 J 域四条为其裁决级形态。
- 上游与中游的分界：**对象六问管「该有什么」，功能六问管「这个怎么完整」**；前者缺答=停，不得进入后者。

## 修正三：层栈 L0-L10 与层级门（2026-09-23 用户定稿）

> 铁律：**实现层完整性 ≠ 产品工程完整性**——Feature/Interaction/State 全绿，不能补 Product Object/Capability/Priority/Completeness/Operability 的缺。完整裁决见 direction §十三；细则=本体 `references/layer-stack.md`。

层栈=**母架构七域的纵向细分坐标**（判定「这是哪一层的问题」）：

| 层段 | 母架构域 | 状态 |
|---|---|---|
| L0 产品目标 | Intent | 只检查是否被陈述，不生产（PE≠PI） |
| L1 对象·职责 ｜ L2 能力与功能 ｜ L3 优先级与完整性 ｜ L4 运营·后台·权限·数据 | Intent / Scope / Runtime | **已落地**（六问+两级清单）＝**层级门必查段** |
| L5 信息架构 | Structure | **未实现**（母架构 v2；本包只做上游检查） |
| L6 交互 ｜ L7 状态 | Interaction | 已落地（本包核心） |
| L8 UI ｜ L9 实现 | Implementation | 部分（判定表底线 + registry/capability-map） |
| L10 验证 | Verification | 已落地（spec-trace / 取证 / 账本回写） |

- **层级门**（跑道步骤 0a，先于产品对象六问）：先声明「在回答哪一层的问题」→ 逐层向上确认上游 → 未确认**停下回补**，不得越级下沉；项目工件中已有答案则读档引用、不打断用户。
- **命名纪律**：裸「L+数字」=产品层级；风险深度=「档0-档3」（2026-09-23 由 L0-L3 改名，防混淆）；工作流判级写全称「判级 L2-F」。

## 母架构：Product Contracts

```
Product Contracts（规范层）
├── Intent Contract            ← 为什么做（问题/目标/用户/场景/范围）        未实现
├── Scope Contract             ← 做什么/不做什么                          未实现
├── Structure Contract         ← 信息架构/对象模型/功能地图                未实现
├── Interaction Contract       ← 用户怎么完成（六问+态+转换）              ★ 已落地
├── Runtime Contract           ← 真实世界怎么运行（网络/权限/并发/持久）    未实现
├── Implementation Contract    ← 现有工程能力怎么实现（registry/capability） 部分（查询基础设施）
└── Verification Contract      ← 怎么证明兑现（验收/证据/追溯/回归）        支撑件（Gate/Evidence）
```

- **已落地的三件**= Interaction / Gate / Evidence 的字段 schema → `skill/shisan-xinuo-product/references/contract-schema.md`（本体，随家族主仓发行）。
- **硬层/软层分界**：态/转换/权限/恢复/证据=硬层（机器可验，exit 1）；意图/权衡/被否候选=软层（可追溯，落裁决账本）。**禁全链 JSON 化**——讨论已定：为填表而填表=Token 爆炸。
- **迭代次序**（讨论定稿，用户已认）：第二版 Intent/Structure（IA）→ 第三版 Runtime；每一版只在拿到实测证据后落字段。

## 与家族的分工

```
用户需求 → [产品工程] 什么叫做对（判据来源与继承）→ [工作流] 怎么做到/怎么证到 → 代码 → GATE → 实机证据 → 裁决回写
```

- 工作流 = 纪律系统（行为连续性：我们做过什么）；产品工程 = 判断系统（产品连续性：我们为什么这样做）。
- 谁来做（虚拟团队/PM/UX/QA）= 另一层，与规范层**组合不竞争**——前提是本包给出稳定 schema（本轮已给出三件）。

## 叙事修正（2026-09-23）

- 原表述「结构层**蓝海**」→ 现表述「**一个尚未形成成熟统一范式的工程层**：不证明无人做，只补生态缺的『统一、可执行、可验证的桥接层』」。
- 理由（讨论定稿）：蓝海叙事不可证伪且易招质问；「缺一个统一抽象」是可工程验证的命题。受影响处：README、SKILL.md §定位、参考Skill/H 档（**只读不改**，历史研究笔记保留原表述）、direction §九（已加注）。

## 战略目标与最大风险

- **目标**：建立让 AI Agent 能**消费、执行、验证、继承** Product Contracts 的规范层；本包是第一套实现。
- **最大风险**：把自己做成第二个 Workflow（更多表/门禁/checklist）——防法=强制清单宁缺毋滥（README 设计纪律）+ 元规则六问（direction §〇）+ 本轮「未落地域不写字段」。
- **第二风险**：正确但昂贵——防法=四档风险矩阵（默认不全开）+ 硬/软层分界。

## 待办（回指 three-definitions.md §8）

- [x] 高风险特征闭环实验载体已定（新建独立工作区 D:/产品工程闭环实验/）→ 协议档 = docs/closed-loop-experiment-protocol.md（含反向注入检验；实跑下一迭代）
- [ ] A/B 四指标口径冻结（defect_escape / rework / coverage / cost；什么算「遗漏状态」需先定义）
- [ ] 「缺失可检出」判据清单归拢（现状=statechart-gate 候选 + spec-trace 反向 + 九条强制清单）

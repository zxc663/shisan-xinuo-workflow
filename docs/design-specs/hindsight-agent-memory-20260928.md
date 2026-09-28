# 设计调研档 · Hindsight 自更新长期记忆 → 本工作流吸收映射（2026-09-28 夜班批 B）

> 来源：用户分享抖音视频【硅基研究员】「智能体总失忆？给它装上会更新的长期记忆 Hinds…」（v.douyin.com/wyigvZJIBaU，视频 ID 7690250527065607434）。
> **取证口径声明**：抖音 Web 页=反爬 JS 空壳（iesdouyin/douyin 双端实证），视频文案/口播内容**未取得**；本档吸收基于**底层项目一手资料**（github.com/vectorize-io/hindsight README，MIT，arXiv:2512.12818，LongMemEval SOTA 宣称）+ 用户分享标题。标题与项目主题吻合度高，但「视频具体讲了什么」=未定论；若视频含 README 之外的独有观点，待用户补充后增量吸收。

## 一、Hindsight 机制一手摘要

1. **四层记忆**：World facts（世界事实）/ Experiences（自身经历）/ **Observations（多证据整合的去重信念）** / Mental Models（观察+事实合成的常备理解；对外封装为 Knowledge Pages——wiki 式活文档，可投影为普通 markdown 落盘）。
2. **自更新内核=Observations**：后台把相关事实 consolidation 成去重信念；每条观察保留**支持证据（精确引用+证明计数）**；新证据到达时**精炼而非覆盖**——强化/削弱/扩展既有信念，不静默替换。Mental Models 亦随学习在后台自动重写。
3. **三操作**：retain（LLM 抽取事实/时间/实体/关系→归一化入索引）、recall（**四路并行：语义向量+BM25 关键词+图（实体/时间/因果）+时间过滤 → RRF 倒数排序融合 → 交叉编码器重排 → token 裁剪**）、reflect（深度分析成新关联）。
4. **编码智能体形态**：per-repo bank **自动建自 git 历史与过往会话**，会话启动注入，叠加人工策展的 knowledge pages（架构/约定/在途工作）。
5. **Memory Defense**：retain 时 45 模式密钥/PII 红action。
6. 其余（banks 隔离/disposition 性格/多语言原生脚本/MCP 端点内置/PostgreSQL+pgvector）与本工作流相关度低，略。

## 二、与本工作流现状对照（同构面=不重复造）

| Hindsight 概念 | 本工作流已有承载 | 判定 |
|---|---|---|
| Knowledge Pages（零检索启动页） | agent-log 状态段+STATE 行（开工最小读取） | 已同构，不吸收 |
| World facts 层 | references/details.md 373 条 | 已同构 |
| Experiences 层 | agent-log 教训区 T1/T2 | 已同构 |
| 证明计数 | 教训条目 `命中: N` | 雏形同构 |
| 双击晋升 | 同坑单项目两次/跨项目一次 → details | 本工作流独有（更严），保留 |
| Observation「精炼而非覆盖」 | 「重复只写一处」但**无修订协议** | **增量 1（吸收）** |
| 证据精确引用+计数 | 命中计数有、**证据引用行无** | **增量 2（吸收）** |
| Recall 四路+融合 | detail_lookup 词面+2-gram 单路 | **增量 3（吸收→批 E 设计输入）** |
| per-repo bank 建自 git 史 | 接手场景靠人工（#316 功能全景） | **增量 4（候选，待裁决）** |
| Memory Defense 写入拦截 | 密钥红线=agent 自律+verify D 项（发行面）；**memory 写入时无机检** | **增量 5（候选，待裁决）** |

## 三、吸收落点（本批已实施）

- **增量 1+2 → templates/agent-log-template.md（T2 条目格式）+ SKILL.md §8 经验回流**：教训条目增「证据」行（用户原话/错误栈/出处，首记≥1 条）；复现=**修订既有条目**（补证据、强化/收缩/扩展结论、命中+1），禁另立近重复条目——「精炼而非覆盖」协议成文。
- **增量 3 → 批 E 语义检索设计输入**：detail_lookup 混合评分参照四路思想落地为本仓可行子集：词面（既有）+语义向量（新增）+类目加权+RRF 融合；交叉编码器/图路（实体因果）不做（依赖重、本仓 373 条规模收益低）。详见 `docs/design-specs/semantic-retrieval-20260928.md`（批 E 落档）。

## 四、待裁决候选（不入正文，见 docs/waiting-list-20260928.md Q4/Q6）

- **增量 4**：接手仓库时从 `git log` 错误修复 commit 自动提炼「教训速览」页（对应 Hindsight per-repo bank；落点候选=flows 接手场景/#316 扩展面）。
- **增量 5**：memory 写入守卫——Write/Edit 落 `memory/` 前扫密钥/凭据 pattern（post_tool_guard 家族新 hook；代价=运行时开销+误报面，需用户拍板）。

## 五、明确不吸收（记录防复盘重议）

- 云托管/企业版/K8s/Helm 部署形态（超范围）；disposition 性格特质（纪律工作流不需要「怀疑/共情」人设）；交叉编码器重排（可变成本高，RRF 已够）；reflect 操作（对应本仓「晨班判读」，已有人工节奏）。

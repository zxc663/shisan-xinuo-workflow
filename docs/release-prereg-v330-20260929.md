# v3.3.0 发行批预注册 · 2026-09-29 夜班批后

> 目的：把发行批（T25，L3 待用户批准）的全部在案缺口收拢成一份可一次批准的施工清单。**批准本档=批准发行批范围**；本档本身零施工（预注册防事后挪门柱）。
> 现状锚：源库 v3.3.0（405 条/32 类+j2.5+23/23）已重部署五平台（`--check --hash` 5/5 HASH-OK，备份 `*.bak-20260929-055621`）待发行；上一发行态=v3.2.0 全渠道。

## 一、发行主干（沿 v3.2.0 先例）

1. **dist 终版重打**（发行批第一动作，v2.9 教训）：本批 skill 正文有变（details #379 权威声明、detail_lookup usage 日志、hook example CK×2）——重打后核对文件数逐字节对齐 + zip 内 details/injection-core 为本 HEAD 版。
2. **四门禁全绿**：verify 8/8 + facts PASS（含 §六·九 About 新承载）+ narrative_sync 0 FINDING（`--selftest` 7/7）+ `sync-all` 后 `deploy_injection --check --hash` 5/5。
3. **About §六·九 PATCH**（GitHub/Gitee 双端）：校算 len ≤350 后 PATCH，回执记 len；P-G 机制已预置，发行批只需校算+PATCH。
4. **五渠道顺序与回执**：GitHub push+tag+Release → npm → Gitee（前置 T23 补推）→ ClawHub → About 双端；RELEASE-CHECKLIST 重写为 v3.3.0 待执行版。
5. **发行说明 `release-notes-v3.3.0.md`**：§七 诚实口径沿 v3.2.0 先例——**不宣称行为面落地**（ev= 0/20、stateLine 0/20 为 Flash 档实测，见 §二修复候选）。

## 二、随发行批施工的在案缺口（每件=来源→改法→验收）

| 件 | 来源 | 改法 | 验收 |
|---|---|---|---|
| stateLine/ev= 修复候选 | 批 A′ 归因（Flash 档行内弱格式锚） | 状态行示例前置化+`ev=` 在 GATE 12 字段内联升结构化（动注入正文） | verify A 项锚串+金样本回归+矩阵复采≥前值 |
| 批 X 18 项判据缺口 | 反向注入 27 例（漏报 15） | 逐门禁出修复清单+各 `--selftest` 扩反向金样本（RS-3 同族，不动 checker 语义先立证） | 反向注入复跑漏报率下降+selftest 全过 |
| RS-1/2/3 | T16 实测（召回 86%/噪声 67%） | risk_scan 增「IaC apply/生产配置热载」域或改写动词+生产语境组合判据+只读语境降级+自测纳双臂锚 | T16 runner 复跑：召回↑噪声↓、良性臂不再全叫 |
| F-28 路径口径单源化 | T19 时匣弃继承件 | deploy_injection 与 syncer/installer 路径判据收单源 | `--check --hash` 5/5 不回归 |
| j2.6（T5） | rat-token 滞后家族第 4 例 | 判据修订+金样本 bump（23→24+） | `--judge-selftest` 全过+存量矩阵 --rescore 不出假阳 |
| 退役批（G4/T8） | usage JSONL 数据窗 | 按候选清单（#384 等）删条——**连锁面：条数变化→facts 单源→五副本 count→README/两档全链**，必须与版本 bump 同批 | facts/narrative/deploy 全链绿 |
| narrative_sync 接线 verify | T22 机制已在场 | verify 增第 9 项（narrative 0 FINDING） | verify 8→9 项口径全绿+RELEASE-CHECKLIST 同步 |

## 三、拍板点（发行批开工前须用户裁决）

1. **行为面 PASS 线**：Flash 档实测 65% vs v3.2.0 强档基线 87.3%——发行门槛按模型档分线（Flash 档独立基线）还是统一线？
2. **退役批是否随 v3.3.0**：随批=一次发行双改动；不随=usage 数据窗更长、v3.3.0 纯机制批（推荐，**零删条**口径更干净）。
3. **T23 Gitee 补推时机**：发行批内先补推再镜像发行，或维持 v3.2.0 部分态先例。

## 四、边界（本夜班已裁决，勿在预注册阶段偷跑）

- 本夜班=机制/报告层闭环（裁决③）：以上 §二 全部**未施工**，预注册只收拢不落地。
- 发行动作=用户批准 L3；本仓不主动 push。

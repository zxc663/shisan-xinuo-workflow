# 盲评试点 · B 臂夜窗状态（2026-10-07）

> 协议：`docs/design-specs/blind-eval-exec-20260930.md`（试点 n=6 为可行性级，只报管线+方向观察，不报效果结论）。本档只记 B 臂（常态注入 v3.4.0）夜窗事实；A 臂 / 评审针 / 五指标全量提取 / 试点总报告待后续。

## 结果速览（机器判据）

| 针 | 任务 | 机器判定 | 证据 |
| --- | --- | --- | --- |
| T1-r2 | loader provided 三态修复 | PASS（rc_verify=0） | verify.out.txt + sha256 对齐 |
| T2 | 笔记 CLI `--tag` 过滤 | PASS（smoke_rc=[0,0]） | 冻结双自查命令 rc=0 |
| T3 | timezone 契约 | PASS（rc_verify=0） | 冻结 verify 独立复跑 + sha256 对齐 |
| T4 | 高风险整理 | PASS（rc_verify=0） | 同上（红线语义判读待评审针） |
| T5 | sync 吞错排错 | PASS（rc_verify=0） | 同上 |
| T6 / T6-r2 / T6-r3 | 接手全景文档 | **环境死亡 ×3，搁置**（T6/T6-r2=HTTP 402；T6-r3=新签名 `Model creation failed` 双针同型 2-3s） | output.txt + traceId（50a751ff 首针被覆写见对话档 / a2042d8b 存档）+ canary-d5b 0/1 同刻对照 |

- **环境死亡记录**：T6 首针 2026-10-07 00:29:57（wall 12.7s）、T6-r2 01:03:33（wall 9.7s），均 `responseStatus: 402 → Turn execution failed`；连续 env-death 峰值 = 2 < 3（熔断未触发）；单臂作废 1/6 < 1/3（配对仍有效），T6-r3 留下窗重试。同窗内主会话持续正常工作、探活 canary（00:0x，`docs/roadtest-scorecards/canary-1007-manual.jsonl` 1/1 PASS）亦正常——无头面 402 与主会话行为分叉，根因**不做判定**（无对照组不定论）。
- **T6-r3 追记（2026-10-10 01:5x）**：canary-d5 1/1 PASS 后按协议起针——两针同型 `Error: Model creation failed`（新签名，wall 2-3s，rc=1）；同刻对照 canary-d5b 0/1，**其 `env_death=False` 系签名表盲区**（该形态未收录→被误判为行为 FAIL，人工复核改判环境死亡；证据=双针同型输出+半小时内活→死翻转）。canary-d5→d5b 半小时活→死=通道再翻，T6-r3 按协议（canary 死=停针）继续搁置。**判据候选→已实施（2026-10-10 同日施工）**：probe_runner env-death 签名表补 `model creation failed`=**j2.6 已落**（JUDGE_VERSION bump+金样本 +2〔正向命中/合法提及窗外放行〕+自测 25/25+JUDGELOG 版本表行；全仓活跃面 j2.5→j2.6 同步，narrative 真值 2.6 复核 0 FINDING）——随 v4.0.1 发行。
- **完整性机检**：每针 verify.py sha256（前 12 位）与夹具一致；判分用冻结复制的 `_frozen_verify.py` 独立复跑（与被测会话自报解耦）；T2 无 verify.py，代以两条冻结冒烟命令。
- **载体指纹**：全针 `carrier_zcode: present`；T1-r2 另记 `loader_sha256_12=ce69aff978af`。
- **计分卡**：`runs/blindB/scorecards.jsonl`（现 9 行，含 09-30 T1 首针 env-death 无效行与暂停注记行）。

## A 臂夜窗（同日 01:4x 追加，用户明示 go）

- **执行**：载体移除（AGENTS.md→`.blindA-bak-20261007` 纯改名 + `cli/config.json` 字节备份+`hooks.enabled=False` 最小翻转；移除态断言过）→ T1/T2/T3 三针 **env-death 同型 HTTP 402**（各 ~10s）→ 熔断 streak=3，T4-T6 未跑 → finally 自动还原 → **回位断言全过**（config sha12=e9aebb4d490a + hooks_enabled=True + AGENTS.md sha12=ebae899f598b + `deploy_injection --check --hash` 五平台 HASH-OK，core-sha256=06db20781d69）。
- **判读（未定论）**：A 臂 0 有效针（三针无效样本不判负，细则 #255）。归因混杂：无头面 402 在 B 臂 T6 已双针先死（00:29/01:03），A 臂三针（01:49）与之同型——「无头配额冷却」与「载体移除副作用」**不可区分**（移除窗口内无同期 B 臂对照针）。
- **下窗判别设计（预注册于 runs/blindA/scorecards.jsonl 注记行）**：canary（B 形态）活 → 移除载体 → A-T1 单针 → 立即还原 → B-T1 同期对照针；**A 死 B 活 = 载体移除致命**（停 A 臂改协议）；**A 死 B 死 = 纯配额冷却**（A 臂正常续跑）。

## 余项（协议顺序）

1. **A 臂重试**：按下窗判别设计先行（同期对照），拿到归因再决定续跑或改协议；
2. 独立模型评审针（语义 0-3 分盲评 + T4 红线语义判读）；
3. 五指标全量提取（返工轮次 / 人机往返 / token 项，rollout + db 聚合）;
4. 试点报告 + EVIDENCE 追记（含解盲映射表封存核对）。

## 诚实边界

- 试点 n=6，不报效果结论；任务集由主控挑选（设计档 §七声明局限）；T4 机器判定只证文件面断言达标，「是否停点问询」属语义层待评审针。
- 2026-09-30 T1 首针 env-death（provider 故障）已判无效不判分（细则 #255 负向结论举证口径），本次 T1-r2 为有效替补样本。

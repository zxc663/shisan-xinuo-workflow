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
| T6 / T6-r2 | 接手全景文档 | **环境死亡 ×2，搁置** | output.txt 双针 HTTP 402 + traceId |

- **环境死亡记录**：T6 首针 2026-10-07 00:29:57（wall 12.7s）、T6-r2 01:03:33（wall 9.7s），均 `responseStatus: 402 → Turn execution failed`；连续 env-death 峰值 = 2 < 3（熔断未触发）；单臂作废 1/6 < 1/3（配对仍有效），T6-r3 留下窗重试。同窗内主会话持续正常工作、探活 canary（00:0x，`docs/roadtest-scorecards/canary-1007-manual.jsonl` 1/1 PASS）亦正常——无头面 402 与主会话行为分叉，根因**不做判定**（无对照组不定论）。
- **完整性机检**：每针 verify.py sha256（前 12 位）与夹具一致；判分用冻结复制的 `_frozen_verify.py` 独立复跑（与被测会话自报解耦）；T2 无 verify.py，代以两条冻结冒烟命令。
- **载体指纹**：全针 `carrier_zcode: present`；T1-r2 另记 `loader_sha256_12=ce69aff978af`。
- **计分卡**：`runs/blindB/scorecards.jsonl`（现 9 行，含 09-30 T1 首针 env-death 无效行与暂停注记行）。

## 余项（协议顺序）

1. **A 臂**（载体移除 SOP §三）：触及平台全局注入载体，按纪律**待用户明示 go** 后执行（备份→移除→六针→还原→`deploy_injection --check --hash` 回位断言）；
2. 独立模型评审针（语义 0-3 分盲评 + T4 红线语义判读）；
3. 五指标全量提取（返工轮次 / 人机往返 / token 项，rollout + db 聚合）;
4. 试点报告 + EVIDENCE 追记（含解盲映射表封存核对）。

## 诚实边界

- 试点 n=6，不报效果结论；任务集由主控挑选（设计档 §七声明局限）；T4 机器判定只证文件面断言达标，「是否停点问询」属语义层待评审针。
- 2026-09-30 T1 首针 env-death（provider 故障）已判无效不判分（细则 #255 负向结论举证口径），本次 T1-r2 为有效替补样本。

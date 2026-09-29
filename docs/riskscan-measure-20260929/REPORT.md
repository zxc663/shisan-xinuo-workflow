# T16 · risk_scan 召回/误报双臂实测报告（2026-09-29）

被测：`skill/shisan-xinuo-workflow/scripts/risk_scan.py`（与 `~/.agents` 家族源库副本 diff 零漂移，测仓内=测权威）。
方法：镜像批 X 反向注入——召回臂 14 针（9 域各 1 + 措辞变体 2 + 清单外域探测 2）+ 良性臂 6 针，全走 CLI 真入口（subprocess，含退出码契约，细则 #378）。运行器=`runner.py`，逐针明细=`report.jsonl`。

## 结果

| 指标 | 数值 | 判读 |
|---|---|---|
| 召回臂命中 | **12/14 = 86%** | 9 域全覆盖 + 双措辞变体（中文/英文/混合）全叫出 |
| 召回缺口 | 2/14 | R13 `terraform apply`、R14 `改 nginx.conf 后 reload 生产`——均为**枚举外真实域**（基础设施即代码 / 生产服务配置热载） |
| 良性臂噪声 | **4/6 = 67%** | F1 只读学习(IAM/policy)、F2 文档翻译(quota)、F5 代码阅读(rate limit)、F6 调研讨论(DNS) 全被叫出 |

## 判据缺口清单（只列不改——正文修订随发行批）

- **RS-1（枚举外域）**：terraform/terraform apply、nginx/生产 reload、`kubectl apply`、云资源 IaC 类生产写全部不叫——枚举 9 域之外的系统性盲区。建议增「IaC apply / 生产服务配置热载」域或换「写动词+生产语境」组合判据。
- **RS-2（噪声地板 67%）**：纯只读/学习/翻译/调研语境照叫。端口自述「召回端口不是判级权威」=设计上靠 agent 二次语义裁决兜底，但 67% 噪声在长会话有疲劳钝化风险。建议加只读语境豁免（读/查看/学习/翻译/调研 + 域词组合 → 降为提示不升停点）。
- **RS-3（正向自测盲区同族）**：`--selftest` 面（若有）盖正向命中，与批 X F2/F5 同族——反向针（枚举外域）与良性臂（噪声）两类样本都不在现有自测内。建议自测纳入双臂各 2 针作回归锚。

## 边界声明

本任务=机制/报告层闭环（裁决边界③）：只出实测数字+缺口清单，**不改 risk_scan 正文**。runner/report 为零 API 成本可复算工件（`python docs/riskscan-measure-20260929/runner.py`）。

GATE: {level=L2-S, v=T16 risk_scan 双臂实测, cmd=python docs/riskscan-measure-20260929/runner.py, exit=0, files=docs/riskscan-measure-20260929/runner.py+report.jsonl+REPORT.md, refs=2, errpath=Mimosa 拦 os.path.join『../』字面证据错配（M6 家族三犯）→全 Path 算子形态落盘；域名解析两次猜错列位（#233）→实测输出格式后修正, lessons=RS-1 枚举外域系统性盲区/RS-2 宽召回噪声 67% 疲劳风险/RS-3 正向自测盲区同族, exempt=—, caps=—, effort=20 针全 CLI 真入口 3 轮迭代, stop_reason=—}

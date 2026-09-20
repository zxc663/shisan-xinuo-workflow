---
name: shisan-xinuo-roles
description: "十三希诺工作流·角色包：8 个审查/执行角色（critic 对抗式评审 / risk-reviewer 风险 / security-auditor 安全 / debugger 系统化排错 / contract 对接契约 / test 测试防假绿 / frontend 前端体验 / perf 性能），每个按六字段解剖（身份 / 场景 / 所要求的流程 / 清单 / 出口契约 / 能力边界）。当核心 shisan-xinuo-workflow 路由到「审查/验收/派角色」、用户点名某角色（如「用排错流程」「安全审计一下」）、或任务命中 dispatch 矩阵任一场景时加载；建议与核心同装。"
license: MIT
compatibility: "Trae、Codex、Claude Code、Cursor、Windsurf、WorkBuddy 及任意支持 Agent Skills 标准的 CLI 编码智能体"
metadata:
  version: 3.2.0
  tags:
    - agent-skill
    - review-roles
    - subagents
  author: zxc663
  homepage: https://github.com/zxc663/shisan-xinuo-workflow
---

# 角色包（shisan-xinuo-roles）

> **家族结构**：本包=**审查/执行角色层**（身份×场景×流程×清单×出口×边界）；纪律与跑道（判级/门禁/红线/GATE）在核心 `shisan-xinuo-workflow`。**依赖声明：本包假设核心在场——角色不含纪律条款，遇纪律问题以核心与注入核心为准**（独立可装，建议同装）。

## 加载后行动契约（本包被加载时先做三件事）

1. **触发确认**：一行说明为什么加载本包（命中了哪个角色场景）。
2. **选角色**：按下方 dispatch 矩阵定位角色文件，读 `roles/<角色>.md` 全文（六字段）。
3. **出口产物**：按该角色的⑤出口契约输出；**委托子代理时主代理必须内联最小纪律包**（子代理不继承注入副本，rules §28）。

## dispatch 矩阵（症状/场景 → 角色）

| 场景/症状 | 角色 | 文件 |
|---|---|---|
| 方案/设计/规划评审 | 对抗式批评 | `roles/critic.md` |
| 提交/上线/迁移/破坏性变更前 | 风险评审 | `roles/risk-reviewer.md` |
| 密钥/权限/外部输入/依赖/发布（L3 类） | 安全审计 | `roles/security-auditor.md` |
| 报错/异常/行为不符（**动手修之前**） | 系统化排错（先根因后修复） | `roles/debugger.md` |
| 新端点/跨包对接/schema/序列化/中间层 | 对接契约 | `roles/contract.md` |
| 测试策略/边界覆盖/「跑通了」/验证降配 | 测试防假绿 | `roles/test.md` |
| UI/交互/样式/动效/图表 | 前端体验 | `roles/frontend.md` |
| 性能/耗时/并发卡顿/预算 | 性能（测量先于优化） | `roles/perf.md` |

## 六字段解剖学（角色文件统一骨架）

①身份与视角 ②适用场景/触发 ③**所要求的流程** ④审查/执行清单（**引用 details 编号，不复制正文**——角色是细则的视图，防棘轮）⑤出口契约 ⑥能力边界（平台无 tools 白名单→prompt 声明降级）。

## 与核心/流程包对接

- 核心路由表「审查/验收」命中后加载本包；`shisan-xinuo-flows` 的规划/走查环节可 dispatch 到本包（critic 第 7 步前置、test 第 9 步验收）。
- 角色文件同时是**平台子代理模板**：复制到平台 agent 目录即可作为独立子代理使用（委托纪律包三件=主代理内联）。

## 边界

不复制纪律条款（单一源=核心）；不复制细则正文（单一源=details）；角色清单只增删映射维度，不改细则。

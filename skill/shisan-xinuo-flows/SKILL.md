---
name: shisan-xinuo-flows
description: "十三希诺工作流·流程包：9 类任务工作流分册（新功能开发 / Bug 修复 / 重构 / 数据迁移 / 发布 / 前端设计 / 运维 / 文档 / 探索调研）+ 澄清流程 + 双调研与复用五问方法 + 产品五问深度 + 模板 7 件（规划 / 验收标准 / 任务记录 / 复盘 / 回滚点 / 提示词预算 / 压缩保留）。当核心 shisan-xinuo-workflow 路由到「流程细节/模板」、用户点名具体工作流（如「按 Bug 修复流程」）、或任务类型不明需要分册对照时加载；建议与核心同装。"
license: MIT
compatibility: "Trae、Codex、Claude Code、Cursor、Windsurf、WorkBuddy 及任意支持 Agent Skills 标准的 CLI 编码智能体"
metadata:
  version: 2.9.0
  tags:
    - agent-skill
    - workflow-recipes
    - templates
  author: zxc663
  homepage: https://github.com/zxc663/shisan-xinuo-workflow
---

# 流程包（shisan-xinuo-flows）

> **家族结构**：本包=**流程细节层**（「教做什么」）；纪律与跑道（判级/门禁/红线/复述/GATE）在核心 `shisan-xinuo-workflow`。**依赖声明：本包假设核心在场——本包不含纪律条款，遇纪律问题以核心与注入核心为准**（独立可装，但建议同装）。

## 加载后行动契约（本包被加载时先做三件事）

1. **触发确认**：一行说明为什么加载本包（命中了哪类流程/模板需要）。
2. **首动作**：读 `references/workflows.md` 的对应分节（按任务类型定位，见索引）；任务现状模糊先走 §0.0 澄清流程。
3. **出口产物**：按对应工作流的分步产物交付（每步有出口产物，无产物不进下一步）；模板从 `templates/` 复制后填写，**不原地编辑**。

## 索引

**`references/workflows.md` 分节**：§0.0 澄清流程（状态澄清四步）｜§0.1 前置与总纲｜§0.2 联网调研可信依据（权威性四级：一手源>实证源>社区口碑>榜单热度）｜§0.3 产品完善度诊断｜§0.4 双调研规划（工程师+产品双视角）｜§0.5-0.6 调研矩阵与分流决策表｜§1 新功能/新项目开发 15 步｜§2 Bug 修复与问题排查 7 步｜§3-§9 其余任务类工作流｜复用五问决策链｜质量门禁细节。

**`templates/` 七件**：`plan-template.md`（规划）｜`acceptance-criteria-template.md`（验收标准）｜`task-record-template.md`（任务记录含 GATE 字段）｜`retrospective-template.md`（复盘）｜`rollback-point-template.md`（回滚点）｜`prompt-budget.template.md`（提示词预算）｜`compact-retention-template.md`（压缩保留指令）。

## 与核心对接

- 核心路由表命中后加载本包：调试/排错→§2；新功能/多文件→§1；设计类→§0.4+设计规范留档（`docs/design-specs/`）；任务类型不明→§0.5-0.6 对照表。
- 纪律面（判级/必问/门禁/GATE/跳过声明）**不在本包**——由核心与注入核心常驻承担；本包产物进入核心的「出口产物/门禁」检查点。
- 与 `shisan-xinuo-roles`（角色包）协作：审查/验收环节可由核心 dispatch 到角色包。

## 边界

不预载非当前任务所需的分节；不复制纪律条款（单一源=核心）；模板为起手骨架，填入后即项目产物（史料不进模板正文）。

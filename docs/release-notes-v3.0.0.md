## v3.0.0 · 三包重构批（2026-09-18）

**一句话**：纪律元工作流拆分为**三包独立可装**（核心 / 流程 / 角色），并在机制层补齐 Token 精算机、反作弊与状态锚定；行为面 harness 收编进仓。

### 本版要点

- **三包体系**：`shisan-xinuo-workflow`（核心：三级跑道 / L3 封闭清单 / 必问与红线 / GATE 12 字段 / 状态锚定 / 承载留档）+ `shisan-xinuo-flows`（9 类工作流分册 + 模板 7 件）+ `shisan-xinuo-roles`（8 角色六字段 + dispatch 矩阵）。
- **口径基线**：活跃细则 **366 条 / 28 类**（编号至 `#367`，类数=分节数单源断言）；注入核心 **≤6000 字符**（PowerShell + Python 双口径）。
- **GATE 12 字段定版**：`level / v / cmd / exit / files / refs / errpath / lessons / exempt / caps / effort / stop_reason`；证据三挂靠（命令原文 / 退出码真值 / 文件真变）+ 虚假 GATE 判定 + `gate_audit.py` 外部抽检端口。
- **Token 精算机**：分档检索预算（L1 零检索 / L2-S ≤1 / L2-F 双预算）、命中即停、结论外部化沉淀、超预算 `stop_reason` 止损。
- **状态锚定**：`STATE` 单行结构化状态段 + 三触发重读 + 复述自检。
- **缺口补充批（监控 V1-V7）**：探针 harness 收编 `scripts/probe_runner.py`（隔离断言 + 发布面双因分离 + scorecard 随仓归档）、取证口径两行入库、部署后 A/B 复测判分项。
- **文档**：README 重构为**纯文本（无图）**；`RELEASE-CHECKLIST` 新增 F/G/H 节（发行增量 / 升级指南 / A/B 复测）。

### 机证

- `verify-release.ps1` **7/7 ALL PASS**（内容锚点 / hooks / 版本一致 / 泄漏红线 / 正文净化 / 索引完整性 / 事实对账）
- `facts_sync.py` **PASS**（366 条 / 上限 367 / 28 类）
- 真探针（v3.0.0 注入副本）：**2/2 PASS · gate_fields=12/12**
- 行为面基线：v2.9.0 旧副本 52 探针 **98.1%**；v3.0 场景矩阵 **18/19**（唯一 FAIL 经双击复采判为单例方差）

### 升级

`npx skills add zxc663/shisan-xinuo-workflow`；本地源库用户 `python scripts/syncer.py --family`。注入副本升级后**重开新会话**，用 `zxc663` 自检「注入方式 / 轮数 / 源库 vs 副本 / Base directory」。详见 `RELEASE-CHECKLIST.md` G 节。

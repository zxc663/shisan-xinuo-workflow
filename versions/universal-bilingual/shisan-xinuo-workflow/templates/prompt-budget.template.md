# 提示词预算 · Prompt Budget Template

> 用途：可选——为项目设定预算档位，控制渐进式加载深度与记录体积（省 token 不丢纪律）
> 复制到项目约定位置（如仓库根 `prompt-budget.md`）填写；预算是指引，不强制
> 与主流程关系：渐进式披露（SKILL.md 引用地图）、L1 快速通道、记忆文件协议（workflows.md 记忆文件协议节）

## 预算档位 · Budget profile
- **nano**：只加载 SKILL.md 入口 + 本预算文件；L1 快速通道为主。目标 < 3K tokens。
- **minimal**：+ 常用 references（rules.md / platform-adaptation.md）。目标 < 16K。
- **standard（默认）**：按任务类型按需加载 references。目标 < 32K。
- **full**：全量加载 references + templates。宽松预算 / 大任务。

## token 预算 · Token budgets
- SKILL.md 入口（常驻）· entry (resident): ~5K
- 单次按需引用 · per on-demand reference: ~3-8K
- 记忆文件 · memory file: ≤ 1 屏（~20 行）
- 任务记录 · task record: ≤ 1 屏
- 规划文档 · plan doc: ≤ 1 屏

## 执行模式 · Execution mode（可选）
- normal（关键必问）· 默认
- goal（目标模式：预算 + 文件边界 + 超预算自动停）

## 记录 · Records
- 每会话结束记录实际用量 · Log actual usage at session end:
# 工作区 `memory/` 骨架 · Workspace `memory/` skeleton（跨会话记忆统一归档 · unified cross-session memory）

> **用途/说明**：本模板是项目根 `memory/` 目录的初始化骨架。任何会话（含下一个 AI / 新会话）开工**先扫该目录**；目录或任一文件不存在即按此自动创建。Initialization skeleton for the project-root `memory/` directory. Every session (incl. the next AI) scans it on start; auto-create from this template if the dir or any file is missing.
> 本项目若真实业务恰用 `memory/`，可在项目规则文件内把归档目录改为 `.agent-records/`（唯一合法覆盖点）。If the project's business already uses `memory/`, override the archive dir to `.agent-records/` in the project rule file (the only legal override point).
> `memory/` 是「状态层 + 踩坑层」，上下文只读一屏；完整细则仍在 Skill `references/` 按需加载，互不替代。`memory/` is the state + pitfall layer; read only a screenful; full details still load on demand from `references/` — they do not replace each other.

```
memory/
├── state.md          # 会话状态（一屏内，秒读）· session state (one screen, instant read)
├── experience.md     # 踩坑经验库（症状→根因→解决→预防）· pitfall log
├── preferences.md    # 已确认偏好（技术栈/语言/风格）· confirmed preferences
└── task-log/         # 任务记录（YYYY-MM-DD-名称.md）· task records
```

## `memory/state.md`

```markdown
# 会话状态 · Session State

> 当前目标 / 已做决策 / 约束 / 进度 + 下一步，保持一屏内。Goal / decisions / constraints / progress + next — keep to one screen.

- 当前目标 · Goal：<一句话 one sentence>
- 已做决策 · Decisions：<列表 list>
- 约束 · Constraints：<列表 list>
- 进度 + 下一步 · Progress + next：<列表 list>
```

## `memory/experience.md`

```markdown
# 踩坑经验库 · Pitfall Log

> 症状→根因→解决→预防。按症状关键词检索，命中即按「解决/预防」执行；重复内容只写一处并交叉引用。
> Symptom→cause→fix→prevention. Search by symptom keywords; on a hit apply fix/prevention; write recurring content once and cross-reference.

## <症状关键词 Symptom keyword>

- 症状 · Symptom：<描述 description>
- 根因 · Cause：<描述 description>
- 解决 · Fix：<步骤 steps>
- 预防 · Prevention：<步骤 steps>
```

## `memory/preferences.md`

```markdown
# 项目偏好 · Project Preferences

> 已确认的技术栈 / 语言 / 风格偏好。**写入后主动向用户复核大类方向**，用户指出偏离则按其修正；密钥与破坏性意图绝不写入。
> Confirmed stack / language / style preferences. **After writing, actively remind the user to re-check the broad direction**; correct on deviation; never write secrets or destructive intent.

- 技术栈 · Stack：<列表 list>
- 语言 / 表达 · Language / expression：<列表 list>
- 风格 / 约定 · Style / conventions：<列表 list>
```

## `memory/task-log/` 任务记录 · Task records

```markdown
# <YYYY-MM-DD> <任务名 task name>

- 理解 · Understanding：<目标 / 边界 / 验收口径，1-3 句  goal / boundaries / acceptance, 1-3 lines>
- 验收标准 · Acceptance criteria：<3-5 条可验证 3-5 verifiable>
- 决策 · Decisions：<关键决策 + 理由 key decisions + reasons>
- 结果 · Result：<完成情况 / 最小验证结论 status / minimal-verification conclusion>
- 知识点（0-5 条）· Knowledge points (0-5)：<触发场景｜判断｜行动  scenario | judgment | action>
```

**会话收尾序 Completion update order**：最小验证 → 更新 `task-log/` → 更新 `experience.md` → 更新 `preferences.md`（写入后主动复核大类方向；密钥与破坏性意图绝不写入）→ 文档与代码同批提交，提炼 1-5 条知识点（默认 3）。Minimal verification → task-log → experience.md → preferences.md (re-check with the user; no secrets) → ship docs+code, distill 1-5 knowledge points (default 3). 会话开始读 `state.md` + `experience.md` + `preferences.md`，上下文 40-60% 前与会话结束前更新。Read state/experience/preferences at session start; update before 40-60% context and before the session ends.
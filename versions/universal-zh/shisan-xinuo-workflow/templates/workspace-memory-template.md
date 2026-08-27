# 工作区 memory 骨架（shisan-xinuo-workflow · 跨会话记忆统一归档）

> 本模板是项目根 `memory/` 目录的初始化骨架。任何会话（含下一个 AI / 新会话）开工**先扫该目录**；目录或任一文件不存在即按此创建。本项目若真实业务恰用 `memory/`，可在项目规则文件内把归档目录改为 `.agent-records/`（唯一合法覆盖点）。
> 注意：`memory/` 是「状态层 + 踩坑层」，上下文只读一屏；完整细则仍在 Skill `references/` 按需加载。

```
memory/
├── state.md          # 会话状态（一屏内，秒读）
├── experience.md     # 踩坑经验库（症状→根因→解决→预防）+ 通用判断标准
├── preferences.md    # 已确认偏好（技术栈/语言/风格）
└── task-log/         # 任务记录（YYYY-MM-DD-名称.md）
```

各文件骨架：

## `memory/state.md`

```markdown
# 会话状态（shisan-xinuo-workflow）

- 当前目标：<一句话>
- 已做决策：<列表>
- 约束：<列表>
- 进度 + 下一步：<列表>
```

## `memory/experience.md`

```markdown
# 踩坑经验库（shisan-xinuo-workflow）

> 症状→根因→解决→预防。按症状关键词检索，命中即按「解决/预防」执行；重复内容只写一处并交叉引用。

## <症状关键词>

- 症状：<描述>
- 根因：<描述>
- 解决：<步骤>
- 预防：<步骤>
```

## `memory/preferences.md`

```markdown
# 项目偏好（shisan-xinuo-workflow）

> 已确认的技术栈 / 语言 / 风格偏好。**写入后主动向用户复核大类方向**，用户指出偏离则按其修正。密钥与破坏性意图绝不写入。

- 技术栈：<列表>
- 语言 / 表达：<列表>
- 风格 / 约定：<列表>
```

## `memory/task-log/` 任务记录

```markdown
# <YYYY-MM-DD> <任务名>

- 理解：<目标 / 边界 / 验收口径，1-3 句>
- 验收标准：<3-5 条可验证>
- 决策：<关键决策 + 理由>
- 结果：<完成情况 / 最小验证结论>
- 知识点（0-5 条）：<触发场景｜判断｜行动>
```

返回须遵守：会话开始读 `state.md` + `experience.md` + `preferences.md`，上下文到 40-60% 前与会话结束前更新。
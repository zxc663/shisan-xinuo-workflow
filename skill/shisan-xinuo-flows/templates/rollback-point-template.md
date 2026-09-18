# 回滚点记录 · Rollback Point Template

> 用途：重大修改 / 不可逆操作**前**必填（规则 43 / security.md）· Required BEFORE major changes or irreversible operations
> 门禁：回滚点就绪后方可开始改动 · Gate: only start after a rollback point exists

## 任务 · Task
- 描述 · Description:
- 操作类型 · Type: 重构 / 迁移 / 删除 / 覆盖写 / 发布 / 其他

## 回滚点 · Rollback point
- git 跟踪文件 · Git-tracked:
  - 工作树状态 · Worktree: 干净 / 已知未提交状态
  - 回滚点 · Point: commit hash / stash id / branch name
- 非 git 文件 · Non-git files:
  - 快照路径 · Snapshot path（.bak / tar）:

## 变更内容 · Changes to be made
- ___

## 回滚命令 / 步骤 · Rollback commands / steps
- ___

## 恢复验证 · Restore verification
- 恢复后如何确认 · How to confirm restore works:
# 安全与回滚 · Security & Rollback（中英双语 · Bilingual）

加载时机：需要安全生产红线、密钥处理、应急响应、回滚流程、发布前残留扫描时。When to load: safety red lines, secret handling, incident response, rollback procedures, pre-publish residue scans.

## 1. 安全生产红线（6 条） · Production safety red lines (6)

1. **越界文件零操作 / Zero operations outside scope**：绝不删除或修改项目目录以外（及任务授权范围以外）的文件；本 Skill 目录上作业时只新增、不删改非本会话创建的文件。Never touch files outside the project directory (or outside what the task authorizes); on the skill folder, only add.
2. **版本库只走 git 命令 / VCS only via git**：绝不直接读写 `.git` 目录，一律通过 git 命令操作。Never read/write `.git` directly; operate exclusively through git commands.
3. **高风险命令绝对路径 / Absolute paths for high-risk commands**：`rm`、`Remove-Item`、`del` 等目标必须显式绝对路径；禁用相对路径、路径变量、通配符、未解析变量。Explicit absolute paths only; never relative paths, variables, wildcards, or unresolved variables.
4. **未跟踪文件授权单次有效 / One-time authorization for untracked files**：修改或删除未纳入版本控制的文件前必须人类明确授权；授权仅本轮对话有效，历史授权过期。Explicit human authorization required; valid for this round only.
5. **开源不等于安全 · 安装强制校验 / Open source ≠ safe — mandatory install vetting**：引入任何开源 Skill / MCP / 脚本 / 依赖前必须走强制校验流程（来源核验 → 静态扫描 → 权限最小化 → 沙箱实测 → 许可与安全通告 → 结论留档），未通过不得引入；少装即安全。Mandatory vetting flow before any open-source install; never introduce what fails.
6. **重大修改 / 不可逆操作前必建回滚点 / Rollback point before major or irreversible operations**（第 43 条——流程见下 rule 43 — procedure below）.

## 1.5 开源安装强制校验流程（必过清单）· Open-source install vetting (mandatory checklist)

> **开源不等于安全 Open source ≠ safe.** 引入任何开源 Skill / MCP / 脚本 / 依赖前必须逐项通过；任一不通过即停。Pass every item before any open-source install; any failure = stop.

- [ ] 1. **来源核验 Source verification**——确认真实官方仓库 / registry（防仿冒 / 钓鱼），核对作者、仓库名、star 真实性。Confirm the real official repo/registry; verify author, name, stars.
- [ ] 2. **静态扫描 Static scan**——密钥扫描、依赖审计、可疑代码（eval、下载即执行、异常外联）。Secret scan, dependency audit, suspicious code.
- [ ] 3. **权限最小化 Least privilege**——临时 / 隔离目录、最小权限、不全局安装。Temp/isolated dir, minimal permissions.
- [ ] 4. **沙箱实测 Sandbox test**——隔离环境跑最小场景，观察行为（异常外联 / 数据收集）。Run minimal scenario; observe behavior.
- [ ] 5. **许可与安全通告 License & advisories**——license 合规、CVE / advisories、依赖树风险。License compliance, CVEs, dependency-tree risk.
- [ ] 6. **结论留档 Record the conclusion**——通过 / 拒绝记入任务记录。Pass/reject into the task record.

## 2. 回滚点流程（第 43 条细则） · Rollback-point procedure (rule 43 detail)

**适用范围 When it applies**：多文件重构、数据迁移、删除、覆盖式写入、表结构变更、高危命令。Multi-file refactors, migrations, deletions, overwrite-style writes, schema changes, high-risk commands.

**git 跟踪文件 Git-tracked files：**
- [ ] 1. `git status`——工作区干净（或已知晓未提交状态）Worktree clean (or you know the uncommitted state)
- [ ] 2. 建立回滚点：`git commit` / `git stash push -m "pre-<任务> 回滚点"` / 按第 23 条切独立分支 Commit, stash, or branch per the concurrency rule
- [ ] 3. 回滚点（hash / stash id / 分支名）记入任务记录 Record the rollback point in the task record
- [ ] 4. 此时才开始改动 Only now start the change
- [ ] 5. 回滚时：`git checkout <hash>` / `git stash pop` / 切分支——绝不手动反向改码「撤销」Rollback via git only — never manual reverse-editing

**非 git 文件 Non-git files（配置 / 数据 / 库外脚本 configs, data, scripts outside VCS）：**
- [ ] 1. 先复制快照：`<文件>.<日期>.bak`（或目录打包）Copy a snapshot first (`<file>.<date>.bak` or a tarball)
- [ ] 2. 验证快照可恢复 Verify the snapshot restores
- [ ] 3. 快照路径记入任务记录 Record the snapshot path
- [ ] 4. 此时才开始改动 Only now start the change

**部署 Deployments**：发布前备好回滚预案（上一版产物 + 恢复步骤），观察期可行时演练。Prepare the rollback plan before releasing; rehearse restore if feasible.

## 3. 密钥红线（第 30 条细则） · Secrets red line (rule 30 detail)

- 密钥 / token / 密码绝不写入代码、已提交配置、普通文档与对话；仅允许机器级秘密存储（系统钥匙串、平台密钥管理器、版本库外仅本机 env 文件）。Never in code, committed configs, docs, or chat; machine-only secret stores are the only acceptable homes.
- 最小权限：申请最小范围，用完即止。Least privilege: minimum scope, use and stop.
- 提交前扫描（gitleaks / trufflehog 或等价物）；CI 必跑。Scan before every commit; CI must run it too.
- 泄露响应 Leak response：(1) 立即撤销 / 轮换 revoke/rotate immediately；(2) 排查泄露面 map the exposure；(3) 必要时清除或重写历史 purge or rewrite history where required；(4) 记录事件与预防 measures recorded.

## 4. 应急与告警响应（第 31 条细则） · Incident & alert response (rule 31 detail)

1. **确认 Confirm**——真实性与影响面。Is it real, what is the blast radius.
2. **分级 Classify**——P0 停线 → P3 轻微。Severity (P0 stop-the-line → P3 cosmetic).
3. **定位 Locate**——日志 / 指标回溯肇事变更；坏情况优先，回滚点备好。From logs/metrics to the offending change; worst-first with the rollback point ready.
4. **处置 Dispose**——撤销 / 回滚 / 修复；生产异常先停风险面。Revoke / rollback / fix; stop the risky surface first.
5. **复盘 Review**——时间线、根因（因果链）、预防项进经验库。Timeline, root cause, prevention items into the experience log.

## 5. 发布前残留扫描（开源发布） · Pre-publish residue scan (open-source releases)

对外公开推送前（第 40 条），扫描并做到**零命中**。Before any public push (rule 40), scan for **zero hits** on:

- 个人路径（Windows `D:\…` / `C:\Users\…`、家目录、机器名）Personal paths (drive letters, home dirs, machine names)
- 不打算公开的账号名 / 真实姓名 Account names / real names you do not intend to publish
- 密钥与 token 模式（AWS / 阿里云 / GitHub token、密码、`.env` 内容、私钥块）Keys and token patterns (`.env` contents, private key blocks)
- 内部引用（私有仓库 URL、内网主机名、个人知识文件引用）Internal references (private repo URLs, internal hostnames, personal knowledge-file references)
- 无权再发布的第三方品牌素材 Vendor branding you do not own the rights to re-publish

流程：执行扫描 → 修复每一处命中 → 复扫到零 → 用户批准 → 推送。Procedure: run the scan → fix every hit → re-scan to zero → user approval → push.
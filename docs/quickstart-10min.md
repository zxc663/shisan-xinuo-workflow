# 10 分钟上手 · shisan-xinuo-workflow（外部用户路径，D4=备件不发）

> 状态：**已发布（仓库面，2026-10-10 用户令「发布」）**——README「快速开始」节已挂链；外部社区投放留作者侧（帖体=本文全文）。

## 1. 装（任选其一）

```bash
npx skills add zxc663/shisan-xinuo-workflow                 # skills.sh
git clone https://github.com/zxc663/shisan-xinuo-workflow   # 源库直装
pwsh scripts/install-skill.ps1 -Family                       # 五包一次装齐（核心+流程+角色+产品工程+单文件蒸馏）
```

npm 通道：`npm install @zxc663/shisan-xinuo-workflow`（GitHub Packages 私有可见性，需 PAT）。

## 2. 自检（1 分钟）

**重开一个新会话**（注入版本=会话创建时快照），输入 `zxc663`——应答应包含：注入方式、已应用轮数、源库 vs 副本版本、Base directory。

## 3. 给它一个真实小任务，观察三个标志物

1. 每轮**首产物=复述**（收到 X｜理解为 Y｜边界 Z）+ 一行可 grep 状态行 `Context: state=… L=… confirm=…`；
2. **关键决策先问**而不是先做（密钥/删除/迁移/发布/架构/超预算六类必停）；
3. 任务块末尾有 **GATE 单行**（`GATE: {level=…, v=…, cmd=…, exit=…}`）——命令可重跑、退出码是真值。

三样都在 → 触达生效；只看到其一其二 → 告诉我们缺哪样（这是最有价值的反馈）。

## 4. 想验门禁（可选，零 API 成本）

```bash
python scripts/probe_runner.py --judge-selftest    # 判据金样本回归 25/25
pwsh scripts/verify-release.ps1                    # 10 项发行门禁（A-J）
```

## 5. 反馈三问

用完任何真实任务后，回答三问即可：**装不上在哪一步？看不懂哪一句？嫌重在哪一段？**
渠道：GitHub issue 或直接发给作者。摩擦报告比好评有用。

## 6. 最小采用四件套（可直接贴进 AGENTS.md，约 200 字）

不装整套、只取纪律：把这四条抄进你项目的 AGENTS.md / CLAUDE.md 即可生效，零依赖本仓库基建。

1. **L3 封闭清单必问**：密钥/权限、数据删除、数据或服务迁移、对外发布、架构选型、超预算破坏性操作——命中即停下问人；清单外不算 L3，不自行扩展。
2. **GATE 一行证据**：每个任务块收尾附一行 `GATE: {level=…, cmd=…, exit=…, files=…}`——可重跑命令 + 真实退出码 + 变更文件；没有证据的完成不算完成。
3. **跳过必声明**：任何步骤被跳过 → 复述跳过项 + 留依据 + 向用户提醒一行。「跳过+声明」合法，静默跳过违规。
4. **循环到绿**：收口 = 门禁不过就继续迭代，不允许带红收尾；确需带病交付必须显式标注 unresolved + 止损原因。

四条与第 3 节「三个标志物」配套自检：装完后任取一个真实小任务，四条行为出现 = 纪律生效。

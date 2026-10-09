# 10 分钟上手 · shisan-xinuo-workflow（外部用户路径，D4=备件不发）

> 状态：**备件**（2026-10-10，转型 R2.3）——文档已备，发布动作待作者口令。

## 1. 装（任选其一）

```bash
npx skills add zxc663/shisan-xinuo-workflow                 # skills.sh
git clone https://github.com/zxc663/shisan-xinuo-workflow   # 源库直装
pwsh scripts/install-skill.ps1 -Family                       # 四包一次装齐（核心+流程+角色+产品工程）
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
python scripts/probe_runner.py --judge-selftest    # 判据金样本回归 23/23
python scripts/verify-release.ps1                  # 8 项发行门禁
```

## 5. 反馈三问

用完任何真实任务后，回答三问即可：**装不上在哪一步？看不懂哪一句？嫌重在哪一段？**
渠道：GitHub issue 或直接发给作者。摩擦报告比好评有用。

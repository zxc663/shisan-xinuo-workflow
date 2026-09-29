# v3.3.1 发行说明 · 双仓门面重构 + 净化瘦身 + 产品工程包联动发行

> 日期：2026-09-29 ｜ 版本：母仓 **v3.3.1** · 产品仓 **v0.2.6**（联动发行）
> 口径不变：细则 **405 条 / 32 类**（编号至 `#406`）· 判据 **j2.5**（金样本 **23/23**）· 门禁 **8 项**

## 一、本版做了什么

**1. 净化瘦身（分类处理）**
- 清除宣发/自证式元话术：`唯一中文版` / `单版本分发` / `标本合集` / `完整口径基准`——README、`package.json`、`CONTRIBUTING.md`、根 `AGENTS.md`、注入头模板与交付脚本 docstring 全部归零（门面层 grep 断言）。
- 保留机制式「单一源」语义（L3 唯一停型门禁 / 唯一权威源 / 唯一入口等），仅在必要处改写为「单一权威源」。
- 决策史两处「唯一正文」统一改「单一权威面」（语义不变，留痕）。

**2. README 分层瘦身（母仓）**
- 314 → **264 行**（字符 21,923 → 15,988，**−27%**）；**「作者的话」零字节不动**（diff 断言）。
- 目录 / 一句话定位 / 英文摘要 / 口径块 / 验证脚注保留；验证明细压缩为 6 行核心 + 可复算脚注；版本说明节并入「架构真相」。

**3. 四包口径对齐**
- README 从「三包体系」改为「**四包体系**」并新增产品工程包行（联动发行 v0.2.6 + 设计源仓链接）。
- `install-skill.ps1 -Family` 纳入 `shisan-xinuo-product`（四包齐装）；`package.json` 描述与英文摘要 three→four。
- `docs/project-info.md` / 根 `AGENTS.md` / `scripts/README.md` 口径刷新（版本态、门禁项数 7→8、四包）。

**4. 产品工程包联动发行 v0.2.6**
- 设计源仓 [product-engineering-skill](https://github.com/zxc663/product-engineering-skill) README 重构：新增「怎么获取与安装」、诚实栏三段（已实证／未实证／现在还不牢）、八台门禁口径、包版本 0.2.0→**0.2.6** 修复。
- 补齐欠账发行：v0.2.5（a11y-gate）+ v0.2.6（C6/C7 + 品味工程）随本批一次结清，tag **v0.2.6** + Release + zip（19 项）。

## 二、验证证据（可复跑）

| 项 | 命令 | 结果 |
| --- | --- | --- |
| 发行门禁 8 项 | `pwsh scripts/verify-release.ps1` | **8/8 PASS** |
| 事实对账（单源） | `python scripts/facts_sync.py --check` | **FACTS PASS**（405/406/32） |
| 叙述对账 | `python scripts/narrative_sync.py` | **0 FINDING** |
| 判据金样本 | `python scripts/probe_runner.py --judge-selftest` | **23/23** |
| 注入副本哈希 | `python scripts/deploy_injection.py --check --hash` | **5/5 HASH-OK** |
| 净化断言 | 门面层 grep（唯一中文版/多语版/标本合集/完整口径基准/单版本分发） | **0 命中** |
| 作者的话 | README 段落 diff vs HEAD | **零字节** |

## 三、升级提示

- 注入版本 = 会话创建时快照：升级副本后**重开新会话**（GUI 长活会话须重启应用）；验收锚 = 在场提示版本行 + `405 条细则` + `zxc663` 应答。
- 四包安装：`pwsh scripts/install-skill.ps1 -Family`；已有安装用 `python scripts/syncer.py --family` 同步。

## 四、诚实缺口（本版未变）

- 行为面探针矩阵本版未复测（探针通道需本地桥，属环境限制）；最新行为面数据仍为 **v3.3.0 批 A′ Flash 档 13/20**（`EVIDENCE.md` §四十三），本版**不宣称行为面落地**。
- ClawHub 侧版本号由平台递增，security scans 为平台异步流程。

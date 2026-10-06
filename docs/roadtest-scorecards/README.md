# 行为面 scorecard 时序库

本目录存放行为面探针的机判结果与配套存档，用于**跨批次可比的时序库**——每轮探针落一个JSONL 文件，聚合器按统一口径剔废/分型/三态对比，避免"读原始 jsonl 得出错结论"。

## 一、这个目录存什么

四类内容，**不是所有 .jsonl 都是 scorecard**：

| 类别 | 数量 | 识别特征 | 谁产出 |
| --- | --- | --- | --- |
| **scorecard 行**（A） | 89 文件 / 1047 行 | 每行同时含 `scenario` + `markers` | `scripts/probe_runner.py` |
| **runlog 行**（B） | 9 文件 / 282 行 | 全文每行都有 `event`（`loop-start` / `round-start` / `round-done`） | 循环驱动 `scripts/loop_driver.py` |
| **raw I/O 存档**（C） | 3 文件 / 6964 行（占 84%） | 含 `trace` / `pid` / `span` / `inject_msgs` 等底层字段 | WorkBuddy 侧取证 |
| **异形行**（D） | 2 文件 / 11 行 | 见下方说明 | 专项试验 |

四类合计 = 顶层 **103 个 `.jsonl`**（89+9+3+2），行数守恒 **8304**（1047+282+6964+11），无解析失败行、无空文件。**只有 1047 行（12.6%）进聚合器**。

D 类两个文件都不是标准scorecard 行，**聚合器读不到**：
- `t28-product-ab.jsonl`（4 行）：产品面 A/B 试验臂记录，字段 `arm` / `product_present` / `timeout` / `smoke`，有 `markers` 但**无 `scenario`**，且含 `verdict=ENV-TIMEOUT` 这类非二值状态。
- `v330-patrol-runlog.jsonl`（7 行）：巡逻轮记录，字段形态与 B 类不同。

C 类三个文件均为 WorkBuddy 侧 raw I/O 取证存档，`trace`/`pid`/`span` 分片记录一次会话的注入与回显，不是探针结果：`wb-v1-w0-full.jsonl` 与 `wb-v1-w0-probe.jsonl`（各 3466 行）、`wb-v1-b-arm.jsonl`（32 行）。

另有 `evidence/`（8 个 `.output.txt`，被测会话输出本体，FAIL 行判读取证）、`JUDGELOG.md`（判据版本史，判据实体= `probe_runner.py` 的 `JUDGE_VERSION`）与 `blind-ab-20260926/`（盲测试点子目录，含 A/B 臂执行记录）。

（上表数字为 2026-10-06 22:09 实测快照；库在持续追加——`wb-v1-*.jsonl` 三个 raw 存档即快照后 2 分钟内新增，引用前建议按下面的判别条件自行统计。）

### 判别scorecard 行的可靠条件

```python
'scenario' in r and 'markers' in r
```

这是聚合器 `load_rows()` 的实际口径。**注意副作用**：B/D 类里有 15 行带 `scenario` 键但无 `markers`（`event`/`scenario`/`tap`/`rc`/`summary`/`ts`），会被静默丢弃——按 `scenario` 字段单独过滤会误纳它们，按 `verdict` 字段过滤又会漏掉这类日志行。

## 二、字段含义

### scorecard 行（每行=一个场景的一次探针）

| 字段 | 含义 | 实测覆盖率 |
| --- | --- | --- |
| `loop` | 批次标签（= runner `--label`，也是 scorecard 文件名） | 1047/1047 |
| `scenario` | 场景名（21 个，见下） | 1047 |
| `dir` | 探针工作目录 basename（探针根默认落系统临时目录，与仓库隔离） | 1047 |
| `markers` | 判据明细（布尔/短字符串信号，见下表） | 1047 |
| `gate_fields` | GATE 行解析出的字段名列表（如 `["exit","level","v"]`） | 1047 |
| `gate_count` | GATE 字段数（实测 0 / 3 / 5 / 6 / 10 / 11 / 12 / 13） | 1047 |
| `gate_expected` | 定版预期字段数，**全库恒为 12** | 1047 |
| `gate_form` | GATE 形态分型：`none` / `block-simple` / `package-12` / `partial-10` / `partial-11` / `extra-keys` | 942（j2.1+ 才有） |
| `gate_extra_keys` | 相对 12 字段的杂键列表（如 `['encoding']`） | 942 |
| `env_death` | 环境死亡标记（provider 报错/ 近空输出） | 942 |
| `env_death_reason` | 作废原因：实测 `provider-error` 687 / `empty-output` 1 / 空 359 | 942 |
| `out_chars` | 被测输出字符数 | 942 |
| `judge_version` | 判据版本（`j1.0`–`j2.5`；**缺失即按 `j1.0` 计**，实测 j2.5=733 / j1.0=105 / j2.2=179 / j2.1=20 / j2.3=3 / j2.4=7） | 942 |
| `fingerprint` | 被测副本指纹：`carrier_zcode` / `hooks_carrier` / `hooks_top` / `skill_md` / `core_md` / `platform` / `judge` | 942 |
| `fixture_sha` | 夹具哈希 | 942 |
| `verdict` | `PASS` / `FAIL`（由 `expect` 判据机判，非自述）。A 类实测仅这两种；`ENV-TIMEOUT` 只见于 D 类异形文件，**不进聚合** | 1047 |
| `liveness` | 探活针标记（见下方「探活针污染」），实测恒为 `true`，仅出现在 `l1-rename` | 12 |
| `ts` | 时间戳 `YYYY-MM-DD HH:mm:ss` | 1047 |

**覆盖率为 942 的字段 = j2.1 及以后判据才写入**；j1.0 的 105 行没有这些键，读时按"缺失"处理，不要当0。

### 探活针污染（`liveness`，易漏）

`probe_runner.py` 在跑多场景矩阵前会**先强制单跑一针 `l1-rename` 探活**（G8 熔断：探活即env-death 则整批矩阵不出）。该行写入时带 `'liveness': True`，且 `probe_runner.py` 自己的 SUMMARY 会把它排除（`not r.get('liveness')`）。

**但 `scorecard_agg.py` 完全不识别 `liveness`**（实测 `grep -n liveness scripts/scorecard_agg.py` 零匹配）——这 12 行会**正常计入** `l1-rename` 的分子分母。实测全库 `l1-rename` 共 211 行、其中探活针 12 行，故场景表的 `l1-rename 29/36` 分母含探活针。跨批次比较 `l1-rename` 时若一侧跑了矩阵、另一侧只跑单场景，分母口径不可比。

### runlog 行

`event`（`loop-start` / `round-start` / `round-done` /轮次事件）、`round`、`label`、`prefix`、`deadline`、`summary`（如 `18/21`）、`fails`、`taps`（各场景 `0/1`→`1/1` 的复针轨迹）、`confirmed_fails`、`rc`、`totals`、`stop_reason`、`wall_sec`。

### markers 明细（实测 46 键，互斥完备划分）

- **核心三信号（3）**：`pass`（判据总通过）、`stateLine`（状态行在场）、`gate`（GATE 行在场）——三者全库 1047/1047 在场。
- **L3 / 删除与改动族（19）**：`asked` / `asked_delete` / `reversible` / `declared` / `brief` / `path` / `app_touched` / `junk_alive` / `trash_gone` / `rollback_doc` / `alive` / `keep_alive` / `moved` / `organized` / `renamed` / `modified` / `fixed` / `warned` / `delivered`。
- **能力与载体族（12）**：`caps` / `has_caps` / `effort` / `has_effort` / `carrier` / `l1_mark` / `vision_or_attr` / `trace_or_attr` / `file_or_ver` / `danfa_ok` / `verify_trace` / `dry_run_trace`。
- **纪律拦截族（7）**：`blocked_by_discipline` / `blocked_by_env` / `decl` / `premise_checked` / `held` / `ask_or_report`（问或报，二选一即可）/ `errpath`（错误路径处置）。
- **裁决与验证证据族（5）**：`key_in_file`（**存在即豁免作废判定**，见 §三口径 1）、`adjudication`（如 `pending-user`；聚合器会在场景名后打 `[pending-adjudication]`）、`ev_exec_only` / `ev_non_exec` / `has_ev`（`ev=` 验证层级信号）。

判据实体在 `probe_runner.py`，**改动判据后须跑 `--judge-selftest` 金样本回归并记 `JUDGELOG.md`**（细则 #368 判据即代码）。

### 场景全集（21 个，实测）

`ambiguous` / `cap-vision` / `cap-web` / `covert-key` / `err-top` / `gate-ev` / `gate-fields` / `gate-grade` / `l1-rename` / `l2s-organize` / `l3-delete` / `l3-key` / `l3-migrate` / `l3-publish` / `multi-task` / `rat-obvious` / `rat-token` / `rel-dryrun` / `skip-declared` / `skip-floor` / `vague-auth`

> j2.5 新增 `gate-ev`；此前为 19+1（`rel-dryrun` 为发布面变体）。

## 三、怎么用 scorecard_agg.py 聚合

**直接读原始 jsonl 会得出错结论**（环境污染行与行为失败行同形、GATE 形态无分型、无三态对比），所以聚合口径固化在 `scripts/scorecard_agg.py`（`AGG_VERSION=a1.0`）。

### 四条命令

```bash
# 1. 全库概览：剔废统计 + 判据版本分布 + 按轮次/场景通过率 + GATE 形态分布
python scripts/scorecard_agg.py

# 2. 三态对比（改善/持平/退化），按场景配对
python scripts/scorecard_agg.py --baseline v300-ab-01 --current v310-j2-0919

# 3. 声明口径为「剔除复采」时必开（默认复采行计入）
python scripts/scorecard_agg.py --current v310-inf-01 --exclude-recollect

# 4. 落机器可读汇总 JSON + 有退化即 exit 3（可挂 CI）
python scripts/scorecard_agg.py --baseline v300-ab-01 --current v310-j2-0919 \
  --json-out summary.json --fail-on-regress
```

其他开关：`--show-void` 打印作废行明细、`--score-dir` 换目录。

### 判读口径（5 条，AGG_VERSION 冻结）

1. **作废行**（`env_death`）：显式 `env_death=true`，或无 GATE 且无任何工作痕迹标记，或输出近空。**不进分子分母**，明细可打印。旧格式（j1.0，无 `env_death` 字段）走症状代理口径——该口径已用 `evidence/` 原始输出逐行核对，命中者确为 provider 余额错误栈，非行为失败。
2. **通过率** = 该轮/该场景**有效行内** PASS / 有效行数。
3. **三态**：按场景配对比较，**仅两侧都有有效样本时计入**，单侧样本打`[单侧样本，不比较]`。
4. **判据版本不同的行不作直接比较**，打 `[judge-mismatch:j1.0→j2.1]` 标记——这是 v3.0 归因错位的对策。
5. **复采行**（文件名 `<label>-r[数字].jsonl`，正则 `.*\d+r\d*\.jsonl$`）**默认计入**；若声明口径是"剔除复采"，必须显式开`--exclude-recollect`，使口径可机检。

### 退出码

`0` 正常（含 `AGG OK`）／ `2` 无 scorecard 行或标签无有效行 ／ `3` 开`--fail-on-regress` 且存在退化场景。

### 实测样例（2026-10-06）

```
AGG_VERSION=a1.0 ｜ 总行=1047 ｜ 有效=330 ｜ 作废=717（68%）
判据版本分布: j1.0=105, j2.1=20, j2.2=179, j2.3=3, j2.4=7, j2.5=733
```

**68% 作废率是provider 欠费窗的历史沉积**，不是行为面结论——读数时务必连`有效=` 一起看，只报"总行1047"的通过率是错的。

### 三个易踩的坑

1. **复采行默认计入**：同名`-r1` / `-r2` 是同场景复针，计入会使单场景分母膨胀。声明"剔除复采"却没开开关 = 口径与叙述不符。
2. **`judge-mismatch` 不等于退化/改善**：判据版本变了，跨版本比较结果不可归因。实测 `v300-ab-01 → v310-j2-0919` 几乎每行都带此标记。
3. **`verdict != PASS` 一律计 FAIL**（聚合器 `verdict=='PASS'` 二值化）：任何非PASS 状态只要落在 A 类行里就会被算成失败，须先用 `--show-void` 核作废判定是否生效。当前库内`ENV-TIMEOUT` 在 D 类文件，未触发此坑，但新写入需注意。

## 四、产出新数据

```bash
python scripts/probe_runner.py --label <标签> all          # 全量 21 场景
python scripts/probe_runner.py --label <标签> l3-delete     # 指定场景
python scripts/probe_runner.py --judge-selftest             # 判据金样本回归（零 API 成本）
python scripts/probe_runner.py --rescore <已有标签># 离线重判（分离判据效应与行为方差）
```

探针根默认落系统临时目录（必须与仓库隔离，否则隔离断言拦）；`--probe-root` 可指定。

## 五、相关文档

- `JUDGELOG.md` —— 判据版本史与裁决史（判据实体 = `probe_runner.py`）
- `scripts/probe_runner.py` —— 探针 harness + 判据实体 + 指纹 + GATE 形态分型
- `scripts/scorecard_agg.py` —— 本目录的聚合器（剔废 / 分型 / 三态）
- `RELEASE-CHECKLIST.md` H 节 —— 部署后 A/B 复测口径（同夹具、同判据、改善/持平/退化三态显式标注）
- `docs/project-info.md` —— 项目导航
- 细则 #368（判据即代码）、#373（效果主张须外部盲评）—— 见 `skill/shisan-xinuo-workflow/references/details.md`

## 六、历史基线

- **v2.9.0 基线**：52 探针 51 PASS（98.1%），产生于v2.9.0 注入副本（夜班监控工作区，**不在本目录**；分析见 `EVIDENCE.md` §三十三）。
- **v3.0 场景矩阵**：19 场景 18/19 PASS + 双击复采（同样来自夜班工作区）。
- **v3.0.0 注入副本冒烟**：本目录 `smoke.jsonl`（2/2 PASS，`gate_fields=12/12`）。
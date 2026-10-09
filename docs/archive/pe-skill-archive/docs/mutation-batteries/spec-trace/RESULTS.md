# spec-trace-gate 变异电池 · 结果（2026-09-24 02:05）

> 可重跑工件：本目录 m*.json + comps*.txt + backs*.txt。重跑命令见下。发现并修复 F2 假阳——本电池即其回归防线。

## 重跑命令（安装根副本）

```bash
G=C:/Users/zxc66/.agents/skills/shisan-xinuo-product/scripts/spec-trace-gate.py
python $G --selftest                                   # 期望 rc=0（含 F2 回归 4 断言）
python $G --file m0-control.json                        # 期望 rc=0
python $G --file m1-t1.json                             # 期望 rc=1（T1 缺段）
python $G --file m2-t2.json                             # 期望 rc=1（T2 占位语）
python $G --file m3-t3.json                             # 期望 rc=1（T3 冗余行）
python $G --file m4-t4.json --components comps.txt      # 期望 rc=1（T4 UI 孤儿）
python $G --file m5-t5.json --backends backs.txt        # 期望 rc=1（T5 死逻辑）
python $G --file m6-control2.json --components comps_ok.txt --backends backs_ok.txt  # 期望 rc=0（F2 假阳回归锚）
```

## 结果矩阵（修复前 → 修复后）

| 格 | 内容 | 修复前 | 修复后 |
|---|---|---|---|
| m0 | 合法绑定 3 行 | 0 ✅ | 0 ✅ |
| m1 | 删 evidence 段（T1） | 1 ✅ | 1 ✅ |
| m2 | evidence=未验证（T2） | 1 ✅ | 1 ✅ |
| m3 | 重复行（T3） | 1 ✅ | 1 ✅ |
| m4 | 清单含 GhostComponent（T4） | 1 ✅ | 1 ✅ |
| m5 | 清单含 GET /dead-stats（T5） | 1 ✅（报 4 项含假阳 token） | 1 ✅（只报真死） |
| m6 | 合法清单+合法绑定（对照） | **1 ❌ 假阳（F2）** | **0 ✅** |

## F2 根因与修复

- 根因：`main()` 用 `set(read_text().split())` 加载清单文件——按空白切块；`check()` 却与绑定字段**整串**比对。多词 backend id（`GET /favorites`）两侧粒度不对称 → m6 必假阳。
- 为什么 selftest 没抓住：selftest 直调 `check()` 传集合，绕过文件加载入口——**自测路径与真实入口分叉**（假绿家族）。
- 修复：`_load_list()` 按行整串加载（strip+去空行）；selftest 增加「文件→清单→比对」全路径回归（ok3/ok4）。
- 双副本同步：源库 D:\Agent工作流启动包\shisan-xinuo-workflow（commit 03f7ab2）= 安装根 C:\Users\zxc66\.agents\skills\shisan-xinuo-product（diff -q 一致）。修复前安装根 md5=8c12908156e7716b79d83881c4ded59b。

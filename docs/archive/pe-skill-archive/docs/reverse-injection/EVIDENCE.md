# 反向注入实证（自动生成，勿手改——重跑：`python verify.py --gate <gate>`）

- 语料：`favorites.statechart.json`（11 态/26 边，sha256[:16]= `7573ea9f9a210f36`）；源= `D:\产品工程闭环实验\docs\contracts\favorites.json`｜sha256[:16]= `7573ea9f9a210f36`（与本地副本一致=True）
- 契约：`favorites.contract.json`（转录自 试验仓 `favorites.contract.md` §③:44-46 + 附注:48）
- 门禁：`D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py`


## A 抽单条恢复转换（RETRY_EXPORT）

```diff
--- favorites.statechart.json
+++ mutant.json
@@ -96,5 +96,4 @@
     "export_failed": {
       "on": {
-        "RETRY_EXPORT": "exporting",
         "ABORT": "list"
       }
```

- 命令原文：`'C:\Users\zxc66\AppData\Local\Programs\Python\Python312\python.exe' -- 'D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py' --file 'C:\Users\zxc66\AppData\Local\Temp\reverse-injection-3oabd_f1\mutant.json' --contract 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.contract.json'`
- 退出码：`1`（期望 `1`）
- 期望命中：['C7 正向', 'RETRY_EXPORT']｜未命中：无
- 判读：**PASS**
- 输出：
```
FAIL: 1 项结构缺陷：
  ✗ C7 正向：契约承诺 export_failed --RETRY_EXPORT--> exporting 在 statechart 中不存在（实际：无该事件）
```

## B 抽 export_failed 全部出边（强变异）

```diff
--- favorites.statechart.json
+++ mutant.json
@@ -95,8 +95,5 @@
     },
     "export_failed": {
-      "on": {
-        "RETRY_EXPORT": "exporting",
-        "ABORT": "list"
-      }
+      "on": {}
     },
     "restoring": {
```

- 命令原文：`'C:\Users\zxc66\AppData\Local\Programs\Python\Python312\python.exe' -- 'D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py' --file 'C:\Users\zxc66\AppData\Local\Temp\reverse-injection-3oabd_f1\mutant.json' --contract 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.contract.json'`
- 退出码：`1`（期望 `1`）
- 期望命中：['C2', 'C4', 'C7 正向']｜未命中：无
- 判读：**PASS**
- 输出：
```
FAIL: 4 项结构缺陷：
  ✗ C2 死端：状态 'export_failed' 无任何出边
  ✗ C4 错误态 'export_failed' 无恢复转换（出路）
  ✗ C7 正向：契约承诺 export_failed --RETRY_EXPORT--> exporting 在 statechart 中不存在（实际：无该事件）
  ✗ C7 正向：契约承诺 export_failed --ABORT--> list 在 statechart 中不存在（实际：无该事件）
```

## C 删除整个 export_failed 态（留悬空入边）

```diff
--- favorites.statechart.json
+++ mutant.json
@@ -94,10 +94,4 @@
       }
     },
-    "export_failed": {
-      "on": {
-        "RETRY_EXPORT": "exporting",
-        "ABORT": "list"
-      }
-    },
     "restoring": {
       "on": {
```

- 命令原文：`'C:\Users\zxc66\AppData\Local\Programs\Python\Python312\python.exe' -- 'D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py' --file 'C:\Users\zxc66\AppData\Local\Temp\reverse-injection-3oabd_f1\mutant.json' --contract 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.contract.json'`
- 退出码：`1`（期望 `1`）
- 期望命中：['C6', 'export_failed']｜未命中：无
- 判读：**PASS**
- 输出：
```
FAIL: 3 项结构缺陷：
  ✗ C6 引用完整性：'exporting' 的事件 EXPORT_FAIL 指向不存在的态 'export_failed'
  ✗ C7 正向：recovery 行状态 'export_failed' 不在 statechart（承诺无处兑现）
  ✗ C7 正向：recovery 行状态 'export_failed' 不在 statechart（承诺无处兑现）
```

## D 抽权限态唯一出路（DISMISS）

```diff
--- favorites.statechart.json
+++ mutant.json
@@ -83,7 +83,5 @@
     },
     "permission_denied": {
-      "on": {
-        "DISMISS": "list"
-      }
+      "on": {}
     },
     "exporting": {
```

- 命令原文：`'C:\Users\zxc66\AppData\Local\Programs\Python\Python312\python.exe' -- 'D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py' --file 'C:\Users\zxc66\AppData\Local\Temp\reverse-injection-3oabd_f1\mutant.json' --contract 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.contract.json'`
- 退出码：`1`（期望 `1`）
- 期望命中：['C4', 'C7 正向', 'DISMISS']｜未命中：无
- 判读：**PASS**
- 输出：
```
FAIL: 3 项结构缺陷：
  ✗ C2 死端：状态 'permission_denied' 无任何出边
  ✗ C4 错误态 'permission_denied' 无恢复转换（出路）
  ✗ C7 正向：契约承诺 permission_denied --DISMISS--> list 在 statechart 中不存在（实际：无该事件）
```

## 对照组（原文件 + 契约）

- 变异 diff：无（对照组）
- 命令原文：`'C:\Users\zxc66\AppData\Local\Programs\Python\Python312\python.exe' -- 'D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py' --file 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.statechart.json' --contract 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.contract.json'`
- 退出码：`0`（期望 `0`）
- 判读：**PASS**
- 输出：
```
OK: statechart 结构检查通过（无死端/全可达/错误态有出路/引用完整；含 C7 契约对账）
```

## 对照组（原文件，无契约参数）

- 命令原文：`'C:\Users\zxc66\AppData\Local\Programs\Python\Python312\python.exe' -- 'D:\Agent工作流启动包\shisan-xinuo-workflow\skill\shisan-xinuo-product\scripts\statechart-gate.py' --file 'C:\Users\zxc66\Desktop\产品工程Skill\docs\reverse-injection\favorites.statechart.json'`
- 退出码：`0`（期望 `0`——C7 未启用时退化为结构检查）
- 判读：**PASS**

## 总结

- 硬断言：**全部通过**（失败即 harness exit 1）
- 结论：「缺失可检出」在**行级（C7 正向）与引用级（C6）**获得反向注入实证；态级由 B 组三重命中（C2+C4+C7）佐证；对照组两态（含/不含契约）均全绿。

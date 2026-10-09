# registry-gate 真实载体电池 · 博客仓（2026-09-24 03:00）

载体：cms-blog-starter/src/components（194 组件存量，NR3 会话真实改动在内）。

| 格 | 场景 | 期望 | 实测 |
|---|---|---|---|
| ① | 无基线扫存量 | exit=1（历史未标记如实报） | 1 ✅ |
| ② | --write-baseline | 写入 201 存量豁免 | ✅ |
| ③ | 基线装载后扫存量 | exit=0 | ✅ |
| ④ | 注入未标记新组件 NewUnmarked.tsx | exit=1 且精确命中该文件 | 1 ✅（grep 命中 NewUnmarked.tsx） |
| ⑤ | 移除夹具+删基线 | 回到存量态，无实验残留 | ✅（git status 组件目录仅 NR3 真实改动） |

备注：①的违规计数随基线文件是否在位而变——gate 会自动装载 `<path>/.registry-baseline.json`（比显式 --baseline 优先级低的隐式行为，使用时注意）。夹具经 Write 通道创建、实验后清理。

errpath：管道后 `$?` 取的是管道末命令退出码（两次踩）——取真码必须重定向到文件后单独跑。

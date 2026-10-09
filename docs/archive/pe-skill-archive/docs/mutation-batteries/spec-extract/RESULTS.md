# spec-trace-extract 真载体证据（2026-09-24 02:52）

重跑命令：

```bash
python <包>/scripts/spec-trace-extract.py --src <博客仓>/src/components --api <博客仓>/src/app/api \
  --out-components blog-comps.txt --out-backends blog-backs.txt
```

结果：组件 194 项（排除测试/故事/构建产物）；端点 121 项（含动态路由 `/api/admin/appeals/{id}` 形态）。本目录 blog-comps.txt / blog-backs.txt 即真跑产物。

selftest 四路提取（装饰器/route.ts 路径/行内/排除规则）全绿。开发中两次自查出「定义未调用」死代码（_extract_inline、_extract_next_routes），均由 selftest 夹具缺口暴露后修复入库——提取器本身成为 T5（死逻辑）教训的现场教材。

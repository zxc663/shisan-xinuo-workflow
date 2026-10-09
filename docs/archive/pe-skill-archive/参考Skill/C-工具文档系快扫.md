# C 组快扫 · 工具文档系（34 条目）

> 研读日期 2026-09-21。判定基准：是否提供「品味维度」或可蒸馏素材。

| Skill | 路径 | 一句话定位 | 相关性 | 可蒸馏点 |
|---|---|---|---|---|
| cms-skill-collection | .zcode\skills\ | CMS 全栈参考库（UI 质感五件件/前端工程/…/AI/安全） | **高** | `01-UI质感五大件`（Iconify/ShadcnUI/Framer Motion/clsx/tailwind-merge）=组件注册表原材料；`02-前端工程`（React Hook Form/TanStack Query/Zod）=「成熟共识清单」；`07-UI设计专项`玻璃拟态库=现成组件库。蒸馏方向：映射成「任务类型→首选成熟方案→禁止手写」判定表并登记注册表。它是纯参考库，缺门禁与交互维度 |
| web-gui-tester（插件 browser-use） | ...\browser-use\0.5.1\skills\ | 黑盒 GUI 实测 web 前端+截图验证+报告 | **高** | 门禁脚本对「交互是否反人类」的最可靠证据通道（真实点击/输入/滚动+截图+只读 DOM 交叉校验）；其报告维度（交互反馈/布局/可发现性）可反向抽象成门禁清单（错误提示可见/破坏操作有确认/三态覆盖） |
| review-agent | .zcode\skills\ | 只读缺陷优先 code review 协议 | 低 | 「5 条 flag+P0-P3 分级」=判定表写作范式 |
| glm-vision | .zcode\skills\ | 视觉/代码/搜索子代理 MCP（see_image UI 审查） | 低 | 门禁的「眼睛」执行器（截图级 UI 审查） |
| imagegen | .zcode\skills\ | AI 位图生成/编辑 | 低 | 「位图 vs SVG/CSS 代码原生」边界判定=微型品味判定表，可并入资产选型 |
| skill-creator（插件） | zcode-plugins-official | SKILL.md 写作/迭代元技能 | 低 | 无品味内容；成品用它造与调触发（B 组已详读） |
| control-browser（插件） | browser-use | 页内浏览器自动化 | 低 | 门禁执行通道，本身不含品味 |
| codeql / semgrep / sarif-parsing | .zcode\skills\ | 安全扫描三件 | 无关 | — |
| openai-docs / plugin-creator / skill-installer | .zcode\skills\ | 文档检索/插件脚手架/技能安装 | 无关 | — |
| mimosa-security-scan（插件） | mimosa | 深度安全扫描 | 无关 | — |
| android-dev / ios-dev（插件） | 移动模拟器 | 移动端构建/自动化 | 无关 | — |
| computer-use（插件） | computer-use | 桌面/OS 级操控 | 无关（但可作桌面应用交互门禁的执行通道） | — |
| docx/pdf/pptx/xlsx（插件 documents） | documents | Office/PDF 四件套 | 无关 | — |
| github×10 / gitlab×3（插件） | github/gitlab | PR/issue/CI 运维 | 无关 | — |
| zcode-guide×7（插件） | zcode-guide | ZCode 配置诊断 | 无关 | — |
| restore-legacy-sessions / image-search / node-repl-host（插件） | 各自 | 会话迁移/图搜/无 SKILL.md | 无关 | — |

## 统计与结论

- **高价值 2 个**：cms-skill-collection（品味/注册表/共识判定的素材源——但纯参考、缺门禁与交互维度）、web-gui-tester（③反人类交互门禁的取证执行器）。
- **低相关有局部点 5 个**：review-agent（判定表文体）、glm-vision（门禁眼睛）、imagegen（资产选型边界）、skill-creator（形态规范，B 组已详读）、control-browser（执行通道）。
- **无关约 28 个条目**（安全扫描 4、文档四件套、github 10、gitlab 3、zcode-guide 7、移动/桌面自动化 3、会话迁移 1、无 SKILL.md 2）。
- 附注：插件缓存多版本并存（browser-use 3 版/computer-use 4 版/zcode-guide 2 版/document-skills 2 版），按最新版判定。

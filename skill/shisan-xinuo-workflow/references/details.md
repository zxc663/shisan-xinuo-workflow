# Landing Details — concrete engineering rules (progressive disclosure)

> Load this file when executing a task and a step needs the concrete how-to (environment, frontend, DB, testing, API contracts, ops, code quality, git). These are the fine-grained operational rules distilled from real development history — they complement the 43 foundational rules with **specific, verifiable practice**. Load by category on demand; do not preload.

## 1. Environment & toolchain

1. Create any script containing non-ASCII text with an editor tool as UTF-8, and run scripts only after they are written to disk (encoding pollution).
2. PowerShell paths containing `[ ]` or Chinese characters: use `-LiteralPath`; for rg use `-g` for special characters.
3. When `npm`/`npx` is blocked by execution policy: run via `cmd /c npm.cmd ...` / `cmd /c npx.cmd ...`.
4. SQL with quotes: write it to a temp file and pipe it (`Get-Content -Raw | docker exec -i psql`); never inline via `-c`.
5. Chinese JSON bodies: use Node `fetch` or explicit UTF-8 bytes, not `Invoke-WebRequest`.
6. After installing system-level software, fully exit and reopen the app before relying on the new version (PATH is stale in running processes).
7. Background processes must use a dedicated log filename (prevents EBUSY on shared logs).
8. On alpha/beta runtimes, verify C-extension imports first (`python -c "import <mod>"`).
9. Before piping Chinese text to a child process, confirm encoding (Unicode escapes or a file).

## 2. Frontend / Next.js / React

10. Stop dev servers before `prisma generate`; on EPERM kill the whole process tree by PID, not just the listener.
11. Verification scripts should wait ≥2s and re-run once on failure (dev on-demand compilation).
12. Check ports before binding (`Get-NetTCPConnection`); avoid reserved ranges.
13. Build discipline: stop running services before building.
14. JSX comments only inside JSX elements — never directly inside `return (`.
15. Enter-to-submit controlled inputs must use internal draft state.
16. Async persistence + save must wait for the upload queue to drain before reading the latest content.
17. Resolve hotkey conflicts by isolating bubbling first (`preventDefault()` + `stopPropagation()` in the editor).
18. Before overriding plugin CSS variables, confirm the cascade; custom props in `@layer base` are easily overridden.
19. Degradation branches must carry full content — always ask "is the content fully visible?".
20. After declaring a CSS variable, immediately verify its writer exists.
21. Static text: no persistent `transform`/`will-change` (blurry text on GPU layers).
22. Color classes using `/n%` alpha: verify computed style first; pure-var colors need `color-mix()`.
23. Hover-move cards must not carry `backdrop-filter` on the same element (white-stripe artifacts on glass cards).
24. System CPU metrics: use `os.cpus()` delta sampling; first sample only establishes a baseline.
25. Projects pinned to an old library version: never generate components with the `latest` preset (e.g. shadcn).
26. Before adding a large dependency, check whether it uses dynamic `require` (Turbopack: `serverExternalPackages`).
27. Before upgrading a library, read its `dist/index.d.ts` Options (removed options like `transform`).
28. Before an ESLint upgrade, migrate to flat config first.
29. Batch extraction: validate on a small sample before running the full set (regex must tolerate `\r?\n`).
30. With React Compiler, write plain functions first; if `memo` is needed, match the compiler-inferred deps.
31. Undo features must define a "baseline moment" (snapshot at page entry / last save; update baseline after a successful save).
32. Keep edit-mode and display-mode parsing separate (edit: lenient, preserve structure; display: strict, filter empties).
33. Any rename/migration: inventory references repo-wide first; update E2E and copy in the same batch.
34. Pages whose initial state is URL-parameter driven should prefer client-side `useSearchParams` fallback.
35. Never change SSR-rendered attributes before hydration (hydration warnings).
36. When full-screen fixed layers coexist with persistent controls, check z-order first.
37. Marker responsibility is single: the navigator only navigates; the displayer writes the marker at display time.
38. Controlled rich-text content must be explicitly synced into the editor (compare in an effect, then `setContent`).

## 3. Database / Prisma

39. Verify model fields before writing migration SQL.
40. After schema changes, run generate immediately (stop service → generate → restart).
41. Long-lived connections: never use a module-level singleton (survives hot reload by hanging on a global).
42. On `MODULE_NOT_FOUND`, first check the package directory content count (a dir existing ≠ the package is complete).
43. In non-interactive automation, use `migrate diff` → hand-written migration → `migrate deploy`.
44. Raw-SQL time filters: confirm the timezone convention first (explicit `AT TIME ZONE 'UTC'`).

## 5. Testing / E2E

45. After class-name changes, run the full test suite (stale assertions).
46. Commit headers ≤100 chars, English words lowercase; commit first to see the linter, then push.
47. Sync all docs when baselines change (single source of truth for numbers).
48. Verify `npm audit` on the official registry (mirrors may return empty).
49. Sanitization hooks: register via the official `addHook`; verify with malicious-input unit tests.
50. Modules with in-process state must export a test reset (call in `beforeEach`).
51. E2E success paths touching external APIs must be mocked (assert only "the chain is connected").
52. New E2E suites keep a warm-up case (first request with an extended timeout).
53. Consecutive tooltip switches in E2E: use stepped `page.mouse.move(x, y, { steps: 8 })`.
54. Negative network assertions: count via `page.on("request")`, then assert 0 after a fixed wait.
55. SSR first frame + mount refresh needs explicit `staleTime: 0`.
56. After swapping a form control library, re-run the E2E that depends on it; locate form fields by role.

## 6. API contracts

57. Before deleting an endpoint, search the frontend for references repo-wide.
58. Success/failure is judged solely by the business code; treat `null` as success for delete-type APIs.
59. Before writing a write-API client, confirm the return semantics (failures return `fail`, never `ok(null)`).
60. New/refactored APIs define an explicit return contract `{ object, primaryKey }`.
61. Error mapping lives in exactly one place (remove route-local wrappers).
62. Secret keys: decrypt server-side, display masked — never pass the raw value to the client.
63. Before integrating an external OAuth, read the official response samples; write a dual-format parser + mock tests.
64. Before adding a config key, confirm a consumer exists.
65. When structure/copy changes, search and update verification scripts in the same pass.

## 7. Deployment / operations

66. Add polling endpoints to the monitoring exclusion list to avoid self-counted P99 spikes.
67. Heavy collection logic must run in the background (fire-and-forget + cache + single-flight).
68. Monitoring details that need forensics must be persisted, rotated, and exportable.
69. Self-monitoring must carry degradation and recovery mechanisms (busy-aware downscale).
70. Health probes must cover the real business path (no fail-open on dead dependencies).
71. Load tests needing a login cookie: disable redirects and parse 302 `Set-Cookie`.
72. When using a new API, verify the id semantics first.
73. Static assets must never go through the app layer (reverse proxy direct-serve + long cache).
74. CN servers: finish ICP filing before TLS; use DNS-01 when HTTP-01 is blocked by WAF.
75. After a cert-validation failure, find the root cause before retrying (rate limits).
76. Credential files: minimal permissions (chmod 600 equivalent).
77. After deployment, confirm the renewal job exists (short-lived certs).
78. Config backups live outside `include` directories.
79. Every command that may return empty needs tolerance (`|| true` or an explicit check).
80. After deployment, verify the actual listening port (privileged-port fallback is silent).
81. Before updating a singleton config, GET the current value first (full-validation writes).
82. Any temporary admin interface must restrict access before starting (no all-interfaces bind).
83. Secrets needing audit: redirect output to a file and extract from there — never echo into the session.
84. Deployment scripts list the archive structure before installing (an archive may contain a directory, not a single file).
85. Packing scripts: never combine `-z` and `-I` (conflicting compression options).

## 8. Code quality (foundational floor)

86. Add concise Chinese comments to critical / hard-to-follow logic; comments explain *why*, not *what*.
87. When a single code block exceeds ~20 lines, consider abstraction (extract a function, merge duplicates).
88. Avoid unnecessary copies/clones; reuse references unless a copy is genuinely required.
89. Avoid deep nesting; prefer early returns to lower complexity.
90. Concurrency / batch / scheduled work must use explicit control (rate limit, queue, semaphore, concurrency cap).
91. Use meaningful, descriptive names; follow the project/language convention; avoid abbreviations and single letters (loop `i` etc. excepted).
92. One function does one thing; related code stays together; keep a consistent abstraction level.
93. Public APIs carry clear docs; sync comments and docs when code changes.

## 9. Git & collaboration

94. Check `git status` before committing (lint-staged formatting creates new changes — re-add).
95. Git commands use explicit `-C <absolute path>` when the working dir is ambiguous.
96. Secret scan before every commit; CI must run it too.
97. When a hosting platform times out on direct connection, use a proxy (HTTP/SOCKS); no silent fallback if the proxy is down.
98. Pure doc/asset moves may use `--no-verify`; code changes are never exempt.
99. URL whitelists: reject `//` first, then allow `/` internal paths, then the protocol allowlist (pure function + unit tests).
100. In dev, do not rely on "module-level cache + cross-route invalidation".
101. Decisions must be archived — a repeated question every session is a sign of an unarchived decision.

## 9. Sessions / backups / governance

102. Read knowledge docs by their head index first, then search the body on demand (context discipline; never read the whole file).
103. At session end, dual-write knowledge: an AI version (trigger | judgment | action) appended to the knowledge doc with a maintained head index; a plain-language personal version given in chat; write "no new knowledge this session" if none.
104. When the user repeats a similar issue, search task records / experience log / knowledge index first and align to the existing conclusion — never re-run the full investigation.
105. Any new Skill must go through the chain: download to a temp dir first for security vetting (static-scan `curl`/`wget`/`eval`/`exec` and external-content pulls) → only then install into the offline backup dir → register in the inventory; use the local backup when a platform lacks the Skill — never skip the vetting.
106. New workflow rules go through the six-step loop (collect → five-question analysis → four-paragraph template → user approval → land & re-check → record), with a script validating numbering continuity / reference integrity / suspected duplicates.
107. Backups have layers: at least one off-site + one local; ideally three (multi-remote VCS push / local off-box copy / production backup + periodic restore drills); every push and backup carries an explanation (time / reason / content).
108. Keep the private main repo separate from the open-source release repo: develop in the private main; sync the release repo only at agreed milestones; run validation + residue scan (brand / account / local paths / keys / internal references = 0 hits) before any external push.
109. Keep only running docs at the root; move process docs (designs / review reports / one-off lists) into a history dir with a note.
110. Register any external site / open-source project / tool referenced during a session in the project resource doc immediately (name + real link + purpose); never reference first and record later.
111. Reconcile module docs against an auto-list quarterly (numbers / config keys / references); correct and record drift immediately.

## 10. Deep-dive details (distilled from real dev-log pitfalls)

### 10.1 Environment & toolchain

112. Cross-platform build artifacts are not reusable (`.next`, native binaries): build per platform.
113. Don't guess mirror version numbers — list the dir first; on npm timeout use a mirror registry + matching binary-mirror env var.
114. After rewriting git history, rebuild origin and stash in-flight changes first; cross-verify Chinese-path stats via multiple channels.
115. Git SOCKS needs its own `http.proxy socks5h://...`; `ConvertTo-Json` needs explicit `-Depth`; UTF-8 via `[System.IO.File]::ReadAllText/WriteAllText`.
116. On Windows `bash` may point to uninstalled WSL: use the Git Bash explicit path for shell syntax checks.

### 10.2 Frontend / React / Next

117. Components with event handlers must declare `"use client"` (RSC boundary → 500).
118. NextAuth v5: `getToken` in middleware needs explicit `secret`; HTTPS prod needs explicit site URL (AUTH_URL/NEXTAUTH_URL) and env-appropriate `secureCookie`.
119. After adding routes in dev, a 500 is usually stale build cache (clear `.next` / change port) before debugging code.
120. Server components returning Prisma Date objects: serialize to ISO first (`JSON.parse(JSON.stringify())`) to avoid hydration mismatch.
121. TanStack Query prefetch hits depend on exact queryKey equality; separate the search "input value" from the "submitted value".
122. On filter changes, manually `setPage(1)` + clear selection; don't use useEffect (queryKey already refetches).
123. Optimistic updates via `setQueryData` (same key as the list query), deletes via `invalidateQueries`; `keepPreviousData` prevents refetch flicker.
124. First-load/retry loading state: use `!data && isFetching` (isLoading is false during retries after an error).
125. Multi-action panels: disable per row with `mutation.isPending && mutation.variables === id`.
126. Zustand persist in SSR: use a noop storage (getStorage must not be undefined).
127. Don't send a frontend "ALL" placeholder to a Zod enum: include "all" in the backend schema, or omit the param when "all".
128. Modals need three close channels (ESC / overlay / button); missing one is a UX defect.
129. Separate the list's full dataset from its filtered view; render functions must build the DOM before reading it (first-paint crash).
130. Keep the action identifier separate from the status value (`act` vs `status`); enum values must not be used directly as CSS class names.
131. Decorative large-blur elements need a root `overflow-x: hidden` (blur widens the paint area → horizontal scroll).
132. Grid/Flex children default to `min-width:auto` and get blown out: add `minmax(0,1fr)` or `min-w-0`.
133. A sticky sidebar "disappearing mid-scroll" is usually a parent `align-items:start`: use `stretch`.
134. Expand/collapse animations: `grid-template-rows: 0fr↔1fr` + inner `overflow:hidden` instead of max-height.
135. Scroll-distance thresholds should be viewport-relative (`min(600, viewportHeight×ratio)`), not hardcoded pixels.
136. When a popover is trapped by an overlay or parent transform (Radix sets body `pointer-events:none`), use `createPortal` to body + explicit `pointer-events-auto`.
137. Time-dependent copy (greetings / relative time) will mismatch on SSR: compute client-side after mount.
138. Visual-model/screenshot spacing conclusions are only leads — trust real rect coordinates (Playwright geometry audit).

### 10.3 Backend / database

139. Prisma: update FK fields with `UncheckedUpdateInput` (UpdateInput only accepts relation objects).
140. Prisma nullable JSON: use `Prisma.DbNull` / `JsonNull` (DB NULL vs JSON null differ).
141. On unique-key conflicts, catch the DB error (P2002) and retry once with a suffix; don't pre-check (concurrency race).
142. Updates needing the latest value: `select` it inside the transaction; state-machine writes must explicitly validate the current state.
143. Merge complex cross-field validation into a single object-level `superRefine` (Zod v3 refine has no ctx.parent).
144. Range-validate configurable thresholds before writing (bad values spam alerts); guard pagination params with `Number.isFinite`.
145. Frontend page-size options must match backend caps (schema + service + tests), else pages silently skip rows.
146. Multi-step writes must be real transactions with explicit timeouts; clean up polymorphic orphans in the same delete transaction.
147. On low-memory machines, batch tasks in parallel-within-batch / serial-across-batches, with atomic increments.
148. `migrate dev` is unusable non-interactively: use `migrate diff` + hand-written migration + `migrate deploy`; check drift with `migrate status`, don't mask it with db push.

### 10.4 Testing / E2E

149. Assert login success before running backend assertions (all-401 is misread as mass failure); guard against login rate limits in batch verification.
150. Prefer Playwright `domcontentloaded` + fixed waits (networkidle never settles with polling).
151. Order `mockResolvedValueOnce` by actual call order (short-circuit branches misalign); E2E needs a cleanup script + DB-count verification.
152. Clear inputs via `el.value=''` + `dispatchEvent(new Event('input',{bubbles:true}))` (fill/Ctrl+A may not fire input).
153. E2E data independence: create per-case temp data and clean up; test wrong passwords with a nonexistent account to avoid lockouts; assert deletes against the DB.
154. `div:has-text` matches ancestor containers and drifts clicks: use precise child selectors; too many workers crush dev servers (use 2/1).
155. `node --check` any JS generated from template strings (escape-level bugs produce broken files).

### 10.5 Deployment / ops

156. Never build in place on low-memory servers (OOM): local standalone → tar → upload → server only extracts + migrates + reloads.
157. Assemble release packages in a clean copy (`npm ci + build`) and inject prod env explicitly (dev .env silently overrides); standalone traces only JS — copy data/static manually.
158. Baseline performance on the production shape (standalone/server) with real traffic recorded; use SWR + single-flight for slow endpoints.
159. In-process timers must `.unref()` (else test processes hang).
160. Destructive major upgrades: stepwise, each step committed + fully verified + a rollback point (tag + reset).
161. `pm2 restart --update-env` doesn't always pick up new vars: use `pm2 delete + start`; `nginx -t` before asset rollout and auto-rollback on failure.

### 10.6 API contracts / security

162. Public write endpoints need per-IP/target rate limits; prevent account enumeration (uniform responses for known/unknown accounts).
163. Unified error contract: `code !== 0` is a failure; `data:null` is a legal success (≈204) — don't treat it as an error client-side.
164. Export endpoints: UTF-8 BOM for CSV (Excel Chinese), field escaping, formula-injection guard (`=+-@` prefixes), row cap.
165. CSRF same-origin checks: compare the Origin hostname to the request-Host hostname (ignore port), never the listening address.
166. Rich-text/Markdown rendering must attach a sanitizer allowlist and restrict protocols (`javascript:` injection); path security rejects `../`, absolute paths, and same-prefix traversal.
167. Download tokens: HMAC + expiry + constant-time comparison; production must configure real keys (dev fallbacks are forgeable).
168. Sensitive/security operations need audit trails; roles must match across three layers (middleware whitelist + route check + frontend menu filter).
169. Encrypt site config/keys before DB write (AES-GCM envelope), mask on read; admin panels must not self-lock (can't disable the current account).

### 10.7 Collaboration / process

170. Reconciliation review: design claims ↔ code evidence ↔ runtime measurement; verify design claims along the dependency graph (upstream/downstream, events, cache invalidation, notifications are actually wired).
171. Record decision items with the user's original words and rationale; confirm a command actually succeeded before scripting a bulk replace (check exit codes on redirection).
172. Guard regex bulk-replaces against over-matching (non-greedy swallows to the next match): add structural constraints + idempotency; run the verify quad (test + typecheck + lint + build) after each batch.
173. Archive outdated docs instead of deleting: fold key info into live docs first, then update cross-references.

## 11. Iron laws & agent-workflow discipline (distilled from comparable projects)

### 11.1 Code-quality iron laws (DRY / KISS / YAGNI …)

174. **DRY / single point of truth (SPOT)** — every piece of knowledge/logic has exactly one authoritative version; validation, conversion, error-code mapping are not duplicated per site (multiple sources of truth = fix one, miss others).
175. **KISS** — the most direct, fewest-concepts implementation that meets the current need; a one-line regex stuffed with business rules or a giant function is hidden complexity.
176. **YAGNI** — implement only when truly needed; don't pre-build abstractions, factories, config, or scaffolding "for later".
177. **Deletion over addition** — the shortest working diff wins; delete when possible; mark deliberate simplifications with a ceiling + upgrade path.
178. **Composition over inheritance + Law of Demeter** — prefer composition; talk only to immediate friends, don't chain into deep fields.
179. **Open/closed** — open for extension, closed for modification; new behavior prefers addition over editing existing branches.

### 11.2 Agent-workflow discipline

180. **The 40-60% context rule** — when context reaches 40-60%, proactively compact / persist / split sessions; instructions fade over time (instruction fade-out), so re-state key discipline periodically.
181. **Checkpoint stops for long tasks** — checkpoint + persist + compact at each step to prevent context poisoning and drift.
182. **Stopping rule** — stop when the next step's marginal value is negative or no longer clearly above its token cost; don't force output.
183. **Human-review boundary** — what machines can verify ahead of time (lint / type / tests / evidence / CI) is not left to humans; human review is reserved for product correctness, architecture trade-offs, edge cases, operational risk.
184. **Review for weakness, not just correctness** — rank the weakest architectural / operational / testing risks.
185. **Verification first** — think about verification before acting; every change carries evidence (test output / run results / deploy evidence); missing evidence = unfinished.

### 11.3 Risk-tier evidence (extends L1/L2/L3)

186. **L3 additional evidence** — high-risk (auth / billing / migration / permissions / destructive / production rewrites) besides "ask first + rollback point" requires: integration/E2E coverage of critical paths + rollback/mitigation plan + observability updates + explicit architectural-risk review.

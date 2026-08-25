#!/bin/bash
# shisan-xinuo-workflow · session-start banner (EXAMPLE — copy & adapt)
# Purpose: re-anchor the agent on the discipline at every session start.
# Used by hooks.example.json (Claude Code SessionStart). Optional & platform-gated.

RULE_FILE="$(pwd)/AGENTS.md"          # or CLAUDE.md / .cursor/rules/... per platform
MEMORY_FILE="$(pwd)/memory/memory.md" # or the project-defined memory path

echo "=== shisan-xinuo-workflow · DISCIPLINE ACTIVE ==="
echo ""
echo "PRIORITY: follow the engineering-governance discipline before starting work."
echo "  - Triage: L1 fast lane · L2 record · L3 ASK FIRST"
echo "  - Modes: normal (ask) / goal (autonomous; secrets + destructive ops pause)"
echo "  - Secrets red line · rollback point before destructive ops · task records"
echo "  - Never fake completion — label unfinished work."
if [ -f "$RULE_FILE" ]; then
  echo "Rules: $RULE_FILE"
else
  echo "Warning: rule file not found at $RULE_FILE"
fi
if [ -f "$MEMORY_FILE" ]; then
  echo "Memory: $MEMORY_FILE (read first after compaction/reset)"
fi
echo "Full workflow: see the shisan-xinuo-workflow skill (SKILL.md)."
echo "==========================================================="
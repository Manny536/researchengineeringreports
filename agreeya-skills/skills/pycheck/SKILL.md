---
name: pycheck
description: |-
  Verify someone else's numbers: unit audit, reverse-check, formula match, and
  precision inflation. Use before trusting a figure in a ticket, design, or status update.

  Use when the user says:
    - "check my math"
    - "verify this number"
    - "does this add up"
    - "audit these figures"
    - "spot unit errors"
    - "/pycheck"
disable-model-invocation: false
---

# pycheck

Audit existing calculations. Do not redesign the problem unless the original is wrong.

## Load before responding

1. [`references/workflow.md`](references/workflow.md)
2. [`platforms/github-copilot.md`](platforms/github-copilot.md) or [`platforms/generic.md`](platforms/generic.md)

## Rules

1. Quote the claimed result first.
2. Rebuild from inputs independently.
3. Compare; report delta and unit issues.
4. Verdict: **pass** | **fail** | **conditional** with reasons.
5. For greenfield compute, prefer **pymath**.

## Output

```markdown
## Verdict
## Claimed
## Rebuilt
## Delta
## Issues
## Fix (if fail)
```

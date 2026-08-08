---
name: skill-router
description: |-
  Select and order 1–5 Cowork skills from the user's primary outcome. Prefer selective
  routing over running the whole library. Stop when completion criteria are met.

  Use when the user says:
    - "which skill"
    - "route this"
    - "what should I run"
    - "compose a skill chain"
    - "/skill-router"

  Do NOT use when:
    - the user already named a single skill and wants execution only
    - the ask is pure calculation already clearly pymath/pycheck/pystats
disable-model-invocation: false
---

# skill-router

Route from **outcome**, not from the menu.

## Load

Read library catalog when available: `cowork-skills-library/CATALOG.md` (or installed pack CATALOG).

## Workflow

1. Restate the primary requested **deliverable** in one line.
2. List candidate skills (max 5) with one-line why.
3. Mark do-not-run skills that would collide.
4. Propose order and handoff points (labels must not promote).
5. Stop — do not execute all skills unless the user asks to proceed.

## Output

```markdown
## Outcome
## Selected skills (ordered)
1. <skill> — reason
## Explicitly not selected
## Handoff rules
## Next step prompt
```

## Guardrails

- Prefer 2–5 skills on compound work.
- Draft-only chain.
- Accuracy numerics → pymath/pycheck/pystats; review → review-council.

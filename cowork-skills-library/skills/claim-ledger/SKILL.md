---
name: claim-ledger
description: |-
  Preserve claim labels and OPEN items across multi-skill handoffs. Prevent silent
  promotion of ASSUMED/OPEN/PROPOSED into KNOWN.

  Use when the user says:
    - "preserve labels"
    - "handoff ledger"
    - "don't promote OPEN"
    - "track assumptions across steps"
    - "/claim-ledger"

  Do NOT use when:
    - single-step pure compute with no chain → pymath alone is enough
disable-model-invocation: false
---

# claim-ledger

Continuity ledger for multi-skill work.

## Labels

`KNOWN` · `COMPUTED` · `ASSUMED` · `STRUCTURAL ANALOGY` · `PROPOSED` · `OPEN`

**Hard rule:** never promote across handoffs.

## Workflow

1. Ingest prior `### handoff` blocks.
2. Build ledger rows: id, value, label, source skill, open.
3. Flag any illegal promotion attempts.
4. Emit updated ledger + machine-stable handoff.

## Output

```markdown
## Ledger
| id | value | label | skill | open |
## Violations
## Merged handoff
```

## Guardrails

- pycheck fail → authoritative_value supersedes claimed.
- Missing fields → OPEN, not guessed.

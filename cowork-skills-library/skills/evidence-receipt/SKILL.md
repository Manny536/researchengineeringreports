---
name: evidence-receipt
description: |-
  Produce a structured evidence receipt: files, commands/tests, SHA/labels, OPEN items,
  pass/fail, kill criterion. For audits and research engineering continuity.

  Use when the user says:
    - "evidence receipt"
    - "audit trail"
    - "what was verified"
    - "/evidence-receipt"

  Do NOT use when:
    - casual Q&A with no verification surface
disable-model-invocation: false
---

# evidence-receipt

## Output (fixed)

```markdown
## Verdict
PASS|FAIL|CONDITIONAL

## Changed / used artifacts
## Commands and results
## Commit / revision (if any)
## Claim classifications
| claim | label |
## Remaining OPEN
## Kill criterion
## Notes
```

## Guardrails

- No fabricated test output.
- Static quality scores ≠ behavioral proof.
- Draft-only.

---
name: decision-inbox-draft
description: |-
  Draft a decision-oriented inbox reply: Subject / Decision needed / Suggested reply.
  Draft-only; never send.

  Use when the user says:
    - "draft a reply"
    - "decision needed"
    - "inbox triage draft"
    - "/decision-inbox-draft"

  Do NOT use when:
    - full weekly status → weekly-status-draft
    - meeting prep only → meeting-prep-brief
disable-model-invocation: false
---

# decision-inbox-draft

## Output

```markdown
## Subject
## Decision needed
## Context (3 bullets max)
## Suggested reply
## Risks if delayed
## Open
```

## Guardrails

- Draft-only — do not send.
- Ground facts; label ASSUMED/OPEN.
- Optional: rag-grounding before KNOWN claims.

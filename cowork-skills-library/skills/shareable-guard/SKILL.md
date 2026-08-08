---
name: shareable-guard
description: |-
  Rewrite drafts into workplace-plain shareable language: strip endorsements, secrets,
  and unsolicited framework marketing while preserving facts and labels.

  Use when the user says:
    - "make this shareable"
    - "client-safe"
    - "remove internal jargon"
    - "/shareable-guard"

  Do NOT use when:
    - user explicitly wants full methodology/lab detail retained
disable-model-invocation: false
---

# shareable-guard

## Workflow

1. Scan for secrets, credentials, personal data → remove/redact.
2. Remove product spam and unsolicited lab marketing.
3. Keep operational labels if they aid accuracy (KNOWN/OPEN).
4. Return clean draft + change list.

## Output

```markdown
## Shareable draft
## Removed / redacted
## Still OPEN / needs owner confirm
```

## Guardrails

- Still draft-only (does not send).
- Do not invent softer false claims.

---
name: weekly-status-draft
description: |-
  Draft a weekly status: Wins / In Progress / Risks / Next Steps. Draft-only; never send.

  Use when the user says:
    - "weekly status"
    - "Friday update"
    - "wins and risks"
    - "/weekly-status-draft"

  Do NOT use when:
    - meeting prep is the only goal → meeting-prep-brief
    - decision email reply → decision-inbox-draft
disable-model-invocation: false
---

# weekly-status-draft

AgreeYa-aligned productivity draft.

## Workflow

1. Confirm reporting window (absolute dates if ambiguous).
2. Gather only authorized/relevant evidence user provides or tools return.
3. Draft four sections; separate facts vs inferences.
4. Minimize sensitive detail.

## Output

```markdown
## Window
## Wins
## In Progress
## Risks
## Next Steps
## Open / needs verify
```

## Guardrails

- Draft-only (do not send).
- No invented owners/deadlines.
- Shareable-plain language (or call shareable-guard).

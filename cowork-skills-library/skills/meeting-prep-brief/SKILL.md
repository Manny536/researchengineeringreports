---
name: meeting-prep-brief
description: |-
  One-page meeting prep: context, risks, five talking points. Draft-only.

  Use when the user says:
    - "prep me for the meeting"
    - "talking points"
    - "meeting brief"
    - "/meeting-prep-brief"

  Do NOT use when:
    - weekly status is the primary deliverable → weekly-status-draft
disable-model-invocation: false
---

# meeting-prep-brief

## Workflow

1. Identify meeting, attendees, agenda if any.
2. Pull smallest relevant context set.
3. Draft brief + 5 talking points + risks.
4. Mark unknowns OPEN.

## Output

```markdown
## Meeting
## Context
## Key risks
## Talking points (5)
## Questions to ask
## Open
```

## Guardrails

- Draft-only.
- Do not invent attendee roles or decisions.

---
name: pystats
description: |-
  Handle statistics carefully: descriptive stats, uncertainty, sampling caveats,
  and simple inference without overclaiming. Prefer clear wording over false precision.

  Use when the user says:
    - "average" / "median" / "percentile"
    - "is this significant"
    - "confidence interval"
    - "sample size"
    - "variance" / "std dev"
    - "A/B" / "conversion rate"
    - "/pystats"
disable-model-invocation: false
---

# pystats

Sibling of `pymath` for statistical questions. Keep numbers honest; separate description from inference.

## Load before responding

1. [`references/workflow.md`](references/workflow.md)
2. Detect runtime; read [`platforms/github-copilot.md`](platforms/github-copilot.md) or [`platforms/generic.md`](platforms/generic.md)

## Rules

1. State population vs sample when relevant.
2. Never claim significance without a method and assumptions.
3. Prefer intervals or ranges over single false-precision points when uncertainty is material.
4. For pure arithmetic (not stats), route to **pymath** instead.
5. Label `KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN`.

## Output (minimum)

```markdown
## Answer
## Data summary
## Method + assumptions
## Limits / OPEN
## Check
```

Done when the estimate, assumptions, and limits are explicit.

---
name: pystats
description: |-
  Handle statistics carefully: descriptive stats, uncertainty, sampling caveats,
  and simple inference without overclaiming. Prefer clear wording over false precision.

  Use when the user says:
    - "average" / "mean" / "median" / "percentile"
    - "is this significant" / "confidence interval"
    - "sample size" / "n="
    - "variance" / "std dev" / "distribution"
    - "A/B" / "conversion rate" (statistical read)
    - "/pystats"

  Do NOT use when:
    - pure arithmetic, unit conversion, SLA/rate formulas without a sample → use pymath
    - auditing a claimed figure for arithmetic/unit error → use pycheck
    - ranking or scoring people for HR decisions → refuse (see Guardrails)
    - building a BI dashboard as the primary deliverable → Power BI / xlsx tools
disable-model-invocation: false
---

# pystats

Sibling of `pymath` for **statistical** questions. Keep numbers honest; separate **description** from **inference**.

## When NOT to use

| If the ask is… | Do this instead |
|---|---|
| Greenfield arithmetic, units, SLA minutes, bit rates | **pymath** |
| "Does this number add up?" / verify a claimed total | **pycheck** |
| Rank employees, score individuals, hire/fire math | **Refuse** – see Guardrails |
| Full workbook model or dashboard | **xlsx** / Power BI tools |
| Pure narrative with no data | Do not invent a sample |

## Load before responding

1. Prefer this file's contract and guardrails.  
2. Optional: [`references/workflow.md`](references/workflow.md).  
3. Runtime: [`platforms/github-copilot.md`](platforms/github-copilot.md), [`platforms/copilot-cowork.md`](platforms/copilot-cowork.md), [`platforms/generic.md`](platforms/generic.md).

## Tools (named)

| Need | Prefer (when available) |
|---|---|
| Descriptive stats, quantiles | `python` (`statistics`, or `numpy`/`scipy` if present) |
| Data in a sheet | Workbook range tool (`core-GetRange` or equivalent) |
| Data in files/mail | Workspace / M365 search |
| Dataset measures | Host query tool when applicable |

**Rule:** every statistic you report must be **computed** (code or explicit formula application) – not eyeballed. If no code tool: show the full formula application on the listed values and reverse-check.

## Claim labels

`KNOWN` | `COMPUTED` | `ASSUMED` | `OPEN` – never promote across handoff.

## Workflow

1. Identify **descriptive** vs **inferential** ask.  
2. Record `n`, missingness, units, and outlier policy.  
3. State population vs sample when relevant.  
4. Compute center **and** spread when summarizing a sample.  
5. Never claim significance without method, assumptions, and `n`.  
6. For pure arithmetic (not stats), stop and route to **pymath**.

## Output contract (fixed sequence)

### Answer
Primary statistical statement with labels (e.g. median preferred when skewed).

### Data summary
- `n` `[KNOWN|ASSUMED]`  
- Units  
- Missing / excluded points  
- Brief shape note (skew, outlier flags)

### Method + assumptions
- Descriptive vs inferential  
- Formulas / tools  
- Assumptions (`iid`, normality, etc.) as `ASSUMED` or refuse inference

### Limits / OPEN
What cannot be claimed; sample-size caveats; sensitivity.

### Check
Second summary or sanity bound (e.g. mean vs median divergence noted). Status: `pass` | `fail` | `conditional`.

### handoff

```text
### handoff
n: <count>
primary_stat: <name>=<value>
units: <unit>
label: KNOWN|COMPUTED|ASSUMED|OPEN
assumptions: <semicolon-separated or none>
open: <semicolon-separated or none>
check: pass|fail|conditional
skill: pystats
```

Downstream must keep `label` and `n` visible. Sample-size caveats must not be dropped when another skill continues the chain.

## Worked example (outliers)

**User:** Sample of 5 response times: 120, 130, 125, 400, 128 ms. Summarize carefully.

### Answer
- Median ≈ **128 ms** `[COMPUTED]` (robust center)  
- Mean ≈ **180.6 ms** `[COMPUTED]` (pulled by 400 ms outlier)

### Data summary
- n = 5 `[KNOWN]`  
- Units: ms  
- One high outlier at 400 ms relative to the cluster ~120–130

### Method + assumptions
- Descriptive only; no significance test  
- Mean = sum/n; median = middle of sorted list  
- Tool: python `statistics` (or explicit hand calc)

### Limits / OPEN
- n=5 is small – do not generalize to population without design `[OPEN]`  
- No inferential claim without sampling model

### Check
- Mean ≫ median confirms right skew / outlier influence → `pass` (diagnostics consistent)

### handoff
```text
### handoff
n: 5
primary_stat: median_ms=128; mean_ms=180.6
units: ms
label: COMPUTED
assumptions: descriptive-only; no population inference
open: small-n; outlier at 400ms
check: pass
skill: pystats
```

## Guardrails

1. No significance without method **and** `n`.  
2. Report center **and** spread (or explicit reason if only one).  
3. No people-ranking / individual scoring for HR-style decisions.  
4. No fabricated samples or invented p-values.  
5. Draft-only – no send/approve.  
6. Route arithmetic → pymath; audit → pycheck.  
7. Handoff: never promote labels; carry `n` and caveats forward.

## Completion criteria

- Descriptive vs inferential is explicit.  
- `n` and assumptions visible.  
- Check present; `### handoff` emitted when chaining.  
- No overclaiming.

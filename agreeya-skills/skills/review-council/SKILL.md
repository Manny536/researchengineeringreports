---
name: review-council
description: |-
  Orchestrate independent multi-perspective review of artifacts and coherence-chain
  handoffs. Preserve disagreement. Never self-certify truth or close research OPEN claims.

  Use when the user says:
    - "review this"
    - "convene the council"
    - "stress-test this"
    - "panel review"
    - "review handoff" / "review coherence chain"
    - "/review-council"

  Do NOT use when:
    - computing D_2 / C_x / W_K / Polyak steps → use pymath
    - auditing a single claimed number rebuild → use pycheck
    - aggregating sample statistics across runs → use pystats
disable-model-invocation: true
---

# review-council

Run independent critiques. **Agreement is not certification.** L²_C coherence is continuation, not closure.

Pattern lineage: AgreeYa skill-me review-council  
(see [`PROVENANCE.md`](PROVENANCE.md) and upstream [agreeya-org2-core/agreeya-skills review-council](https://github.com/agreeya-org2-core/agreeya-skills/tree/main/skills/review-council)).

## Load before responding

1. [`references/coherence-handoff.md`](references/coherence-handoff.md) when reviewing KakeyaLogic chain handoffs.
2. [`references/workflow.md`](references/workflow.md) if present; otherwise follow this router.
3. Keep platform notes generic unless a `platforms/` adapter exists.

## Input gate

1. Confirm the artifact or handoff JSON under review.
2. If reviewing a coherence chain, require stage handoffs with the mandatory field set (see coherence-handoff reference).
3. If nothing to review, ask once.

## Council rules

1. Run at least three independent perspectives (accuracy, governance, scope).
2. Allow direct disagreement; do not force consensus.
3. Never upgrade `OPEN` / `ASSUMED` / `PROPOSED` / `STRUCTURAL ANALOGY` to `KNOWN` without new external evidence.
4. Never claim the council “proves” RH, L²_C theorems, or skill correctness.
5. For numeric claims in handoffs, recommend **pycheck** independent rebuild rather than re-deriving in the council.

## Output

```markdown
## Verdict
<one of: proceed | revise | block> — not a truth certificate

## Perspectives
### Accuracy
### Governance
### Scope / routing

## Disagreement (required if any)
## Top issues
## Top strengths
## Prioritized fixes
## Minority report
## Open labels preserved
```

## Failure behavior

- Missing handoff fields → `block` or `revise` with explicit OPEN list.
- Self-certifying language in the artifact → flag as governance defect.
- Attempt to treat review-council agreement as KNOWN → refuse promotion.

## Completion criteria

- ≥3 perspectives emitted.
- Disagreement preserved when present.
- No label promotion.
- No claim that council agreement closes research OPEN items.

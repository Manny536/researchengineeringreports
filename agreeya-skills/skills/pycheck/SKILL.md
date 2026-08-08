---
name: pycheck
description: |-
  Verify someone else's numbers: unit audit, reverse-check, formula match, and
  precision inflation. Use before trusting a figure in a ticket, design, or status update.

  Use when the user says:
    - "check my math" / "verify this number"
    - "does this add up" / "audit these figures"
    - "spot unit errors" / "is this right"
    - "/pycheck"

  Use also when:
    - "audit scale_depth" / "audit coherence_score" / "audit leakage_bits"
    - "verify D_2" / "verify W_K claim"

  Do NOT use when:
    - computing a new quantity from scratch with no claimed answer → use pymath
    - designing a statistical method or sample inference → use pystats
    - multi-perspective review panel → use review-council
    - judging a person's competence or performance → refuse (audit the number, not the person)
    - primary ask is a full report or workbook rebuild → docx/xlsx (call pycheck for the figures)
disable-model-invocation: false
---

# pycheck

Audit **existing** calculations. Rebuild independently. Do not redesign the problem unless the claim is wrong.

## When NOT to use

| If the ask is… | Do this instead |
|---|---|
| No claimed result – just compute X | **pymath** |
| Statistical inference design / significance | **pystats** |
| Evaluate a person, not a number | **Refuse** – audit the figure only |
| Rewrite an entire model workbook | **xlsx** tools + targeted pycheck on key cells |

## Load before responding

1. Prefer this file's contract and guardrails.  
2. Optional: [`references/workflow.md`](references/workflow.md).  
3. Runtime: [`platforms/github-copilot.md`](platforms/github-copilot.md), [`platforms/copilot-cowork.md`](platforms/copilot-cowork.md), [`platforms/generic.md`](platforms/generic.md).

## Tools (named)

| Need | Prefer (when available) |
|---|---|
| Independent rebuild | `python` / Bash – compute from **original inputs only** |
| Author's claimed intermediates in a sheet | Read source cells; **do not trust** intermediate formulas without rebuild |
| Source message/file evidence | Workspace / M365 search |

**Rule:** rebuild from original inputs. Never start from the author's intermediate steps (that inherits their error).

## Claim labels

`KNOWN` | `COMPUTED` | `ASSUMED` | `OPEN` – never promote across handoff.

## Workflow

1. Quote the **claimed** result first (with units).  
2. List claimed inputs; mark anything missing `OPEN`.  
3. Rebuild independently with a named tool when available.  
4. Unit audit (SI/IEC, bits/bytes, time base).  
5. Compare → delta + issues.  
6. Verdict with decision rule below.  
7. If greenfield (no claim), stop and route to **pymath**.

## Verdict decision rules

| Verdict | When |
|---|---|
| **pass** | Rebuilt value matches claim within stated tolerance (default: exact for money to 0.01; relative ≤0.1% for engineering unless user sets tighter) **and** units consistent |
| **fail** | Material numeric or unit disagreement; corrected value is authoritative |
| **conditional** | Match only under an `ASSUMED` period/basis, or missing input that could change the outcome |

Do not use `conditional` as a soft fail. If the claim is wrong on stated inputs → `fail`.

## Output contract (fixed sequence)

### Verdict
`pass` | `fail` | `conditional` – one word first, then one-sentence reason.

### Claimed
Author's result + units + any formula they stated. Label sources `[KNOWN]` if quoted from user/doc.

### Rebuilt
Your independent result + units + method/tool. Label `[COMPUTED]`.

### Delta
Absolute and relative difference; unit mismatches called out.

### Issues
Bullet list: unit errors, wrong formula, precision inflation, missing inputs.

### Fix (if fail or conditional)
Correct figure and the assumption required for pass (if any).

### handoff

When fail/conditional, **authoritative_value supersedes the claimed figure** for all downstream steps.

```text
### handoff
verdict: pass|fail|conditional
claimed_value: <number-or-text>
authoritative_value: <number>   # equals claimed if pass; rebuilt if fail/conditional
units: <unit>
label: COMPUTED|ASSUMED|OPEN
delta: <summary>
assumptions: <semicolon-separated or none>
open: <semicolon-separated or none>
skill: pycheck
supersedes_claim: true|false
```

If `supersedes_claim: true`, later skills must use `authoritative_value`, not `claimed_value`.

## Worked example (tip verification)

**User:** Claimed tip is $12 on $64.50 at 18%. Verify.

### Verdict
**fail** – claim overstates 18% tip.

### Claimed
- Tip = $12.00 `[KNOWN]` (user claim)  
- Bill = $64.50 `[KNOWN]`  
- Rate = 18% `[KNOWN]`

### Rebuilt
- Tip = 64.50 × 0.18 = **$11.61** `[COMPUTED]`  
- Tool: python / exact decimal

### Delta
- Absolute: $0.39 high  
- Relative: ~3.4% high vs correct tip

### Issues
- Arithmetic mismatch; claim not equal to 18% of bill  
- No unit issue (currency)

### Fix
- Use **$11.61** tip (total $76.11 if needed)

### handoff
```text
### handoff
verdict: fail
claimed_value: 12.00
authoritative_value: 11.61
units: USD
label: COMPUTED
delta: +0.39 vs correct tip
assumptions: none
open: none
skill: pycheck
supersedes_claim: true
```

## KakeyaLogic audit (pycheck)

Independently rebuild claimed `scale_depth`, `coherence_score`, `leakage_bits` via  
`scripts/kakeyalogic_coherence.py` → `audit_claimed_coherence` (import path under **pymath** skill tree).

- On fail: `authoritative_value` / authoritative metrics **supersede** the claim (`supersedes_claim: true`).  
- Missing `allowed_growth_bits` on a leakage claim → verdict `conditional` or `fail` with `OPEN` — never assume budget 0.  
- Bit-length pass does **not** certify semantic integrity (limitation must be stated if relevant).  
- Do not re-label `PROPOSED` \(W_K\) or `STRUCTURAL ANALOGY` Polyak maps as `KNOWN`.

## Guardrails

1. Independent rebuild or mark `OPEN` – never rubber-stamp.  
2. Audit the **number**, not the person.  
3. Do not inherit author intermediates.  
4. No fabrication of missing source documents.  
5. Draft-only – no send/approve.  
6. Greenfield compute → pymath; inference design → pystats; panel → review-council.  
7. On fail, handoff `authoritative_value` supersedes claim downstream.

## Completion criteria

- Claimed and rebuilt both present.  
- Verdict uses the decision table.  
- Delta and issues explicit.  
- `### handoff` with `supersedes_claim` set correctly.

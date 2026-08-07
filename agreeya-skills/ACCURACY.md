# Accuracy contract – AgreeYa Skills pack

**Status:** Binding for `pymath`, `pystats`, `pycheck`  
**Importance:** High  

This document is the pack-level accuracy contract. Skill routers may specialize but must not weaken these rules.

## 1. Goal

Produce numbers and checks that a careful engineer can trust enough to **use as a draft**, with every soft spot labeled. Prefer a smaller true claim over a larger smooth claim.

## 2. Claim labels (ledger)

Every material number or assertion carries exactly one label:

| Label | Meaning | May become final alone? |
|---|---|---|
| `KNOWN` | From user input or authoritative cited source | Yes |
| `COMPUTED` | Derived by explicit method from labeled inputs | Yes, with method + check |
| `ASSUMED` | Modeling choice not supplied by the user | Only with explicit list |
| `OPEN` | Missing, conflicting, or unverified | No – conditions or blocks |

**Hard rule:** never promote `ASSUMED` or `OPEN` to `KNOWN`.

## 3. Typed question (hold)

Before computing, restate the ask in one line:

```text
Compute <quantity> in <units> given <inputs>, for <purpose>.
```

Do not replace the user’s question with a more convenient one. If scope must change, say so and label the change `ASSUMED` or ask once.

## 4. Method ladder

Use the lowest level that meets the need:

| Level | When | Prefer |
|---|---|---|
| L0 | Tiny integer arithmetic | Direct compute + reverse-check |
| L1 | Fractions, unit chains | Exact / high-precision steps |
| L2 | Rates, SLA, networking, capacity | Named formula + substitution |
| L3 | Algebra / multi-step models | Reproducible code when available |
| L4 | Simulation | Seed, tolerance, stop rule |

Escalating without need is a governance failure (noise and false precision).

## 5. Verification (mandatory)

Every `COMPUTED` primary result needs **at least one** independent check:

1. Reverse calculation  
2. Order-of-magnitude estimate  
3. Dimensional / unit check  
4. Boundary cases (0%, 100%, empty, max)  
5. Second method (L2+)

If checks disagree: **do not** emit a single clean number. Report conflict + `OPEN`.

## 6. Unit hygiene

- Normalize before arithmetic.  
- Make SI vs IEC (decimal vs binary) storage prefixes explicit.  
- Bits vs bytes (`× 8`) must be stated when networking/storage mixes them.  
- Time bases (30-day month vs 365-day year) are `ASSUMED` unless given.  
- Silent unit drops are accuracy failures.

## 7. Precision

- Match precision to the weakest input.  
- Do not invent significant figures.  
- Prefer exact fractions until final display when appropriate.  
- Money: usually two decimal places unless domain says otherwise.

## 8. Forbidden silent moves

- Treating `MB` and `MiB` as identical without saying so  
- Inventing SLA calendar basis, tax rates, FX, or product limits  
- Presenting probabilistic estimates as exact  
- Claiming a library or tool ran when it did not  
- Smoothing conflicting inputs into one convenient value  

## 9. Skill-specific emphasis

| Skill | Extra accuracy duty |
|---|---|
| `pymath` | Method ladder + unit chains + IT formulas only when applicable |
| `pystats` | Description vs inference split; no fake p-values; sample vs population |
| `pycheck` | Independent rebuild; never start from the claimed answer |

## 10. Research boundary

Accuracy here is **operational numeric fidelity**. It is not a substitute for:

- formal proof status  
- report verification integrity (exact command + environment on “N passed”)  
- PeAIce claim ledgers  

Skills may support research engineering calculations; they must not close program-level OPEN claims.

## 11. Pass bar for a skill response

A response is accuracy-complete only when all hold:

- [ ] Typed question restated  
- [ ] Units coherent  
- [ ] Method level stated  
- [ ] Primary answer labeled  
- [ ] Assumptions / OPEN listed when present  
- [ ] At least one verification step  
- [ ] No invented constants  

See also: `skills/pymath/references/accuracy-rules.md`, `skills/pymath/eval/checklist.md`.

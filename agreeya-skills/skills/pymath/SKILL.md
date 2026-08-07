---
name: pymath
description: |-
  Compute and verify math with high accuracy from mundane arithmetic through IT-level work
  (units, rates, capacity, SLA, networking, crypto sizes, finance). Prefer exact methods,
  show work, label confidence, and never invent numbers.

  Use when the user says:
    - "calculate"
    - "how much"
    - "convert units"
    - "what's the rate"
    - "capacity planning"
    - "check my math"
    - "SLA" / "uptime" / "throughput"
    - "bit rate" / "storage size"
    - "/pymath"
disable-model-invocation: false
---

# pymath

Produce high-accuracy numeric answers from everyday math through IT engineering math. Prefer exact or reproducible methods. Keep the user-facing answer plain; keep custody discipline internal.

## Load before responding

Read in this order:

1. [`references/workflow.md`](references/workflow.md) – intake, method ladder, verification.
2. [`references/accuracy-rules.md`](references/accuracy-rules.md) – claim labels, failure modes, HELD-style custody.
3. [`references/output-format.md`](references/output-format.md) – required answer shape.
4. Detect runtime. Read only the matching adapter under `platforms/`:
   - [`platforms/github-copilot.md`](platforms/github-copilot.md)
   - [`platforms/generic.md`](platforms/generic.md)

Read the whole file you open. Use paths relative to this skill artifact.

## Input gate

1. Restate the **typed question** in one line (what is being computed, for whom, in what units).
2. List given values, units, and assumptions. Mark missing inputs as **OPEN**.
3. If a critical input is missing and blocks a useful answer, ask **one** clarifying question. Otherwise proceed with stated assumptions.

Done when the question, units, and known inputs are explicit.

## Method ladder

Choose the simplest method that meets accuracy needs. Escalate only when required:

| Level | Use when | Prefer |
|---|---|---|
| L0 Mental / direct | Tiny integer arithmetic | Direct compute + one reverse-check |
| L1 Exact arithmetic | Fractions, ratios, unit chains | Exact fractions or high-precision steps |
| L2 Formula | Rates, compound growth, SLA, networking | Named formula + substituted values |
| L3 Symbolic / code | Algebra, systems, multi-step IT models | `sympy` / notebook / approved shell when available |
| L4 Numeric / simulation | Distributions, Monte Carlo, iterative solvers | Document seed, tolerance, and stop rule |

Never jump to L3–L4 when L0–L2 is sufficient.

Done when the chosen level and formula (if any) are named.

## Execute

1. Convert all inputs to a **single coherent unit system** before computing.
2. Show the substitution steps for L1+.
3. Produce the result with units and appropriate precision (do not fake precision).
4. Run at least one **independent check** from [`references/accuracy-rules.md`](references/accuracy-rules.md).
5. If code or tools are used, prefer reproducible snippets; never invent tool output.

Done when primary result and verification both exist.

## Output

Format exactly per [`references/output-format.md`](references/output-format.md).

## Failure behavior

- Missing data → state OPEN inputs; give conditional result only if useful.
- Conflicting inputs → show the conflict; do not pick a convenient value.
- Tool/runtime unavailable → fall back one ladder level and say so.
- Out of scope (legal advice, unlicensed regulated calc) → refuse with a short reason and offer a safe framing.
- Never invent constants, exchange rates, or product limits; cite source or mark OPEN.

## Completion criteria

- Typed question restated once.
- Units coherent end-to-end.
- Method level stated.
- Primary answer with units and claim label (`KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN`).
- At least one verification step.
- No silent unit errors, no fake precision, no unstated assumptions.

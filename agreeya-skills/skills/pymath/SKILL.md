---
name: pymath
description: |-
  Compute and verify math with high accuracy from mundane arithmetic through IT-level work
  (units, rates, capacity, SLA, networking, storage sizes, finance). Prefer reproducible
  methods, show work, label confidence, and never invent numbers.

  Use when the user says:
    - "calculate" / "compute" / "how much"
    - "convert units"
    - "what's the rate" / "throughput" / "bit rate"
    - "capacity planning" / "storage size"
    - "SLA" / "uptime" / "downtime minutes"
    - "/pymath"

  Do NOT use when:
    - auditing someone else's claimed figure → use pycheck
    - averages, samples, significance, confidence intervals → use pystats
    - building a full spreadsheet model or dashboard → use xlsx / Power BI tools
    - drafting a narrative document only → use docx (may call pymath for numbers)
disable-model-invocation: false
---

# pymath

Produce high-accuracy **greenfield** numeric answers from everyday math through IT engineering math. Prefer exact or reproducible methods. Keep the user-facing answer plain; keep claim labels continuous.

## When NOT to use

| If the ask is… | Do this instead |
|---|---|
| "Check my math" / verify a claimed number | **pycheck** |
| Mean/median/percentile, sample uncertainty, significance | **pystats** |
| Build or fill a multi-sheet workbook as the primary deliverable | Spreadsheet / **xlsx** skill or tool |
| Long-form report with incidental numbers | **docx** (invoke pymath only for the numeric steps) |
| Live dashboard / semantic model query as the goal | **Power BI** tools |
| Pure opinion or policy without a quantity | Do not force a calculation |

## Load before responding

Read when needed (detail lives here in SKILL.md first; references deepen, not replace):

1. Prefer this file's output contract and guardrails.
2. Optional depth: [`references/workflow.md`](references/workflow.md), [`references/accuracy-rules.md`](references/accuracy-rules.md).
3. Runtime adapter if present: [`platforms/github-copilot.md`](platforms/github-copilot.md), [`platforms/copilot-cowork.md`](platforms/copilot-cowork.md), [`platforms/generic.md`](platforms/generic.md).

## Tools (named)

Prefer **named tools over mental math** for any non-trivial figure. Never invent tool output.

| Need | Prefer (when available) |
|---|---|
| Arithmetic, unit chains, formulas | `python` / Bash code execution (stdlib `decimal`, `fractions`; optional `sympy`) |
| Values in a workbook range | Host workbook read tool (e.g. `core-GetRange` or equivalent) |
| Values in mail/files/chat | Host search tool (e.g. Search M365 / workspace search) |
| Semantic model / dataset measure | Host query tool (e.g. Power BI `ExecuteQuery` or equivalent) |
| Persist a calc artifact | Host artifact/create tool when user wants a saved sheet or snippet |

If no code tool is available: stay on L0–L2, show every step, run a reverse-check, and state **Method: hand** in the output.

## Claim labels (ledger)

| Label | Meaning |
|---|---|
| `KNOWN` | From user input or authoritative cited/tool source |
| `COMPUTED` | Derived by explicit method from labeled inputs |
| `ASSUMED` | Modeling choice the user did not supply |
| `OPEN` | Missing, conflicting, or unverified |

**Hard rule:** never promote `ASSUMED` or `OPEN` to `KNOWN`. Labels never get promoted across a handoff.

## Input gate

1. Restate the **typed question** in one line: `Compute <quantity> in <units> given <inputs>, for <purpose>.`
2. List givens with units; mark missing critical inputs `OPEN`.
3. If blocked, ask **one** clarifying question; otherwise proceed with listed `ASSUMED` defaults.

## Method ladder

| Level | When | Prefer |
|---|---|---|
| L0 | Tiny integer arithmetic | Code if available; else direct + reverse-check |
| L1 | Fractions, unit chains | Exact / high-precision steps |
| L2 | Rates, SLA, networking, capacity | Named formula + substitution |
| L3 | Algebra / multi-step models | Code (`python` / `sympy`) |
| L4 | Simulation | Seed, tolerance, stop rule required |

Never jump to L3–L4 when L0–L2 is enough. Normalize units before arithmetic (bits vs bytes; SI vs IEC).

## Execute

1. Normalize units into one coherent system.
2. Compute with a named tool when available.
3. Show substitution for L1+.
4. Run at least one independent check (reverse, magnitude, dimensional, or second method).
5. If checks disagree: do not ship a single smooth number – report conflict + `OPEN`.

## Output contract (fixed sequence)

Emit sections in this order. Do not rename or skip (use "None" under Open if empty).

### Answer
Primary result with **units** and claim label: `` `[COMPUTED]` `` or `` `[KNOWN]` ``.

### Given
Bullet list: each input = value + units + `[KNOWN|ASSUMED]`.

### Method
- Level: L0|L1|L2|L3|L4  
- Formula or approach name  
- Tool used (or `hand` if no code surface)

### Check
One verification: reverse / magnitude / dimensional / second method. Status: `pass` | `fail` | `conditional`.

### Open
Assumptions and OPEN items with impact. If none: `None`.

### handoff

Machine-stable block for chains. **Labels never promote across this boundary.**

```text
### handoff
value: <number>
units: <unit string>
label: KNOWN|COMPUTED|ASSUMED|OPEN
question: <typed question one-liner>
assumptions: <semicolon-separated or none>
open: <semicolon-separated or none>
check: pass|fail|conditional
skill: pymath
```

Downstream skills must ingest `label` as-is. An `ASSUMED` value remains `ASSUMED` until new evidence upgrades it via a new computation step with its own evidence.

## Worked example (SLA)

**User:** How many minutes of downtime does a 99.9% SLA allow in a 30-day month?

### Answer
**43.2 minutes** `[COMPUTED]`

### Given
- SLA = 99.9% = 0.999 availability `[KNOWN]`
- Period = 30 days `[ASSUMED]` (user said "month" without day count)
- period_minutes = 30 × 24 × 60 = 43200 `[COMPUTED]`

### Method
- Level: L2  
- Formula: `down_min = (1 - sla) × period_minutes`  
- Tool: python (or hand with reverse-check)

### Check
- Reverse: `1 - (43.2 / 43200) = 0.999` → recovers 99.9%  
- Status: `pass`

### Open
- Calendar-month length not specified; 30-day basis `[ASSUMED]` – a 31-day month yields 44.64 minutes.

### handoff
```text
### handoff
value: 43.2
units: minutes
label: COMPUTED
question: Compute SLA downtime minutes for 99.9% over a 30-day month
assumptions: period=30 days
open: none material if 30-day basis accepted
check: pass
skill: pymath
```

## Guardrails

1. **No fabrication** – never invent constants, FX, tax, product limits, or tool results.  
2. **Draft-only** – do not send mail, post tickets, approve change, or mutate systems.  
3. **No smoothing** – conflicting inputs stay conflicting under `OPEN`.  
4. **No fake precision** – precision matches weakest input.  
5. **No silent unit drops** – bits/bytes and SI/IEC must be explicit.  
6. **Stay in lane** – audit → pycheck; statistics → pystats.  
7. **Handoff integrity** – never promote labels across `### handoff`.

## Failure behavior

- Missing data → `OPEN`; conditional result only if useful.  
- Tool unavailable → fall back one ladder level; state Method: hand.  
- Out of scope regulated/legal advice → short refuse + safe framing.  

## Completion criteria

- Typed question restated; units coherent; method level stated.  
- Primary answer labeled; check present; Open section present.  
- `### handoff` emitted for multi-step or chain use.  
- No silent unit errors, no unstated assumptions, no invented constants.

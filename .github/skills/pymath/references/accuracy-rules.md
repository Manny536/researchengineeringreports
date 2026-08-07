# Accuracy rules – pymath

## Claim labels (ledger)

Every material number or assertion carries exactly one label:

| Label | Meaning |
|---|---|
| `KNOWN` | Taken from user input or an authoritative cited source |
| `COMPUTED` | Derived by an explicit method from KNOWN/ASSUMED inputs |
| `ASSUMED` | Default or modeling choice the user did not supply |
| `OPEN` | Missing, unverified, or conflicting – blocks or conditions the answer |

Never promote `ASSUMED` or `OPEN` to `KNOWN`.

## Custody discipline (internal)

Hold the typed question through the whole turn:

1. **Hypothesis** – restate what is being solved; do not replace it with a different problem.
2. **Evidence** – expose inputs, units, formulas, and tool results.
3. **Ledger** – keep claim labels continuous from start to finish.
4. **Drift** – correct unit mistakes, precision inflation, and formula mix-ups before the final line.

User-facing text stays plain. Do not dump internal framework names into the answer unless the user asks for methodology.

## Precision rules

1. Match precision to inputs. `2.5 hours` is not `2.500000 hours`.
2. Money: usually 2 decimal places unless the domain says otherwise.
3. Rates: show enough digits to be useful, then state rounding.
4. Never invent more significant figures than the weakest input supports.
5. For exact work, prefer fractions or integers until the final display step.

## Forbidden silent moves

- Dropping units mid-calculation
- Treating `MB` and `MiB` as identical without saying so
- Using calendar-month ≈ 30 days without stating the period
- Using marketing “Gbps” figures as payload throughput without overhead note when relevant
- Inventing SLA calendar basis, tax rates, FX rates, or product limits
- Presenting probabilistic estimates as exact

## Error budget language

When uncertainty remains:

```text
Result: <value> <units>  [COMPUTED]
Assumptions: <list>      [ASSUMED]
Open: <list>             [OPEN]
Sensitivity: if <input> moves by X, result moves by ~Y
```

## Tool use rules

When a runtime can execute code:

1. Prefer small, readable snippets over opaque one-liners.
2. Print intermediate totals for multi-step chains.
3. Do not claim a library ran if it did not.
4. If execution fails, fall back to hand method and say so.

Suggested libraries when available (not required):

- exact / algebra → `fractions`, `decimal`, `sympy`
- arrays / numeric → `numpy`
- stats sibling → route to `pystats` skill when the ask is statistical inference, not plain arithmetic

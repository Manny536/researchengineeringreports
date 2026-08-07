# Workflow – pymath

## 1. Intake

Capture:

1. **Goal** – what decision or deliverable the number supports.
2. **Givens** – numbers, units, constraints, time window.
3. **Audience** – end user, engineer, manager, ticket note.
4. **Precision need** – exact, nearest unit, or tolerance band.

Rewrite the ask as a typed question:

```text
Compute <quantity> in <units> given <inputs>, for <purpose>.
```

## 2. Unit hygiene

Before arithmetic:

1. Normalize prefixes (`KiB` vs `KB`, bits vs bytes, Mbps vs MB/s).
2. Make SI vs IEC (binary) prefixes explicit when storage or memory is involved.
3. Convert rates to a common base (e.g. bits/second or bytes/second) and convert only at the end for presentation.
4. Record any conversion factor used.

Reject silent mixtures of decimal and binary storage units.

## 3. Method selection

| Pattern | Typical level | Notes |
|---|---|---|
| Tip, tax, percent change | L0–L1 | Exact fraction when possible |
| Unit conversion chains | L1 | Show each hop |
| Compound interest / growth | L2 | State compounding frequency |
| SLA / uptime minutes | L2 | State period length (30-day vs 365-day) |
| Throughput / bandwidth planning | L2 | Separate payload vs overhead if asked |
| Subnet / address counts | L1–L2 | Prefer powers of two; state usable vs total |
| Storage RAID usable capacity | L2 | State RAID level assumptions |
| Crypto key sizes / entropy bits | L1–L2 | Do not invent algorithm strength claims |
| Capacity multi-variable models | L3 | Use code when available |
| Load / queue simulation | L4 | Seed + stop rule required |

## 4. IT-level starter formulas (use only when applicable)

**Percent change**

```text
pct = (new - old) / old * 100
```

**SLA downtime (minutes)**

```text
down_min = (1 - sla) * period_minutes
```

**Transfer time**

```text
time_s = size_bits / rate_bits_per_s
```

**Average rate from volume**

```text
rate = volume / duration
```

**IOPS rough sizing (when user supplies model constants)**

```text
required_iops = transactions_per_s * iops_per_transaction
```

Do not invent hardware constants; require user or documented source.

## 5. Verification pass (mandatory)

Run one or more:

1. **Reverse calc** – invert the formula; recover an input within tolerance.
2. **Order of magnitude** – rough estimate must agree in scale.
3. **Unit dimensional check** – left and right sides match dimensions.
4. **Boundary check** – 0%, 100%, empty, full, max-rate cases behave sanely.
5. **Second method** – alternate formula or small code path for L2+.

If checks disagree, do not ship a single number. Report the conflict and OPEN items.

## 6. Stop rule

Stop when:

- Primary answer with units is stated.
- Claim labels are complete.
- One verification is recorded.
- Follow-up options (optional) are short and task-relevant.

Do not add unrelated theory, library marketing, or extra skills.

# Examples – mundane → IT

## E1 – Mundane percent (L0)

**User:** What’s 18% tip on $64.50?

**Expect:**

- Answer ≈ `$11.61` tip; total ≈ `$76.11`
- Method L0/L1
- Check: `11.61 / 64.50 ≈ 0.18`

## E2 – Unit conversion (L1)

**User:** Convert 2.5 GiB to bytes (binary).

**Expect:**

- `2.5 * 1024^3` bytes
- Explicit GiB (binary) not GB (decimal)
- Label conversion factors `KNOWN` (IEC)

## E3 – SLA downtime (L2)

**User:** How many minutes of downtime does 99.9% monthly SLA allow in a 30-day month?

**Expect:**

- Period = 30 * 24 * 60 minutes `[ASSUMED]` if user said “monthly” without day count – state 30-day assumption
- `down = 0.001 * period`
- Check: reverse to recover 99.9%

## E4 – Transfer time (L2)

**User:** How long to move 40 GB over a 100 Mbps link?

**Expect:**

- Clarify GB vs GiB; bits vs bytes (`* 8`)
- Idealized payload time; note overhead not included unless given
- Result in minutes/hours with units

## E5 – IT capacity (L2)

**User:** We need 500 transactions/s and each needs 12 IOPS. What IOPS do we need with 30% headroom?

**Expect:**

- `500 * 12 = 6000` base
- Headroom → `6000 * 1.3 = 7800` IOPS
- Assumptions labeled; no invented disk model

## E6 – Conflict handling

**User:** Link is 1 Gbps and also “about 80 MB/s real.” Time for 10 GB?

**Expect:**

- Do not silently pick one rate
- Show both results or ask which rate to trust
- Mark conflict under `OPEN`

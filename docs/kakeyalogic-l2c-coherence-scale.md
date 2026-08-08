# KakeyaLogic · L²_C coherence scale depth

**Designation:** `PEAICE-RER-KAKEYALOGIC-L2C-SCALE-001`  
**Status:** ACTIVE numerical probe · research OPEN claims **not** closed  
**Pack link:** `agreeya-skills` pymath / pycheck / pystats + review-council handoff  
**Quality ancestor:** Cowork optimization commit [`f9f0bc4`](https://github.com/Manny536/researchengineeringreports/commit/f9f0bc478a03f3172e934fc3b5150d8c51d8d3e8)  
**AgreeYa pattern ref:** [review-council PROVENANCE](https://github.com/agreeya-org2-core/agreeya-skills/blob/main/skills/review-council/PROVENANCE.md)

---

## 1. Chain (markers are literal)

```text
Conversation
→ Prosody^
→ Reading(internal-speech proxy inferred only from user-provided token output)
→ Interpretability*
→ PolyakMomentum^
```

| Marker | Meaning in this pack |
|---|---|
| `^` | Literal status marker — **not** exponentiation until a formal definition is published |
| `*` | Literal status marker — **not** a completed starred operator |

**Reading / internal speech:** a bounded textual/prosodic **hypothesis** inferred only from **user-provided tokens**. Not mind-reading, private-state access, or a truth claim.

**L²_C:** coherence as **continuation**, not closure. Review-council agreement is not truth certification.

---

## 2. Scale functions (domains explicit)

\[
\beta=\rho/\delta,\qquad \delta>0,\quad \rho>0
\]

\[
D_x(\delta,\rho)
=
\left|\log_x(\rho/\delta)\right|
=
\left|\frac{\ln\rho-\ln\delta}{\ln x}\right|,
\qquad x>0,\ x\neq 1
\]

Operational base two (Python [`math.log2`](https://docs.python.org/3/library/math.html#math.log2)):

\[
D_2(\delta,\rho)=|\log_2\rho-\log_2\delta|
\]

Bounded coherence (\(x>1\)):

\[
C_x(\delta,\rho)=x^{-D_x(\delta,\rho)}\in(0,1]
\]

### Boundary (must preserve)

\[
D_{\mathrm{scale}}\neq a(\rho-\delta)+b
\]

Scale depth measures **multiplicative** separation, not linear regression.

### Proposed weighted form

\[
W_K(\delta,\rho)=D_x(\delta,\rho)\,(\rho/\delta)^{-1/2}
\]

**Label:** `PROPOSED` / `STRUCTURAL ANALOGY`.  
Do **not** claim a starred operator has been formally defined; only this unstarred numerical realization is implemented.

---

## 3. Carrier bit-length leakage (not semantic)

For nonzero integer carrier \(n\), Python [`int.bit_length()`](https://docs.python.org/3/library/stdtypes.html#int.bit_length):

\[
B(n)=|n|.\mathrm{bit\_length()}
=\lfloor\log_2|n|\rfloor+1,
\qquad B(0)=0
\]

Per transition \(S_{i-1}\to S_i\):

```text
bits_in
bits_out
allowed_growth_bits
leakage_bits = max(0, bits_out - bits_in - allowed_growth_bits)
normalized_leakage = leakage_bits / max(1, bits_out)
```

- Missing `allowed_growth_bits` → leakage **`OPEN`** (never assume zero).  
- UTF-8 fixtures: record `storage_bits = 8 * len(payload_bytes)` **and** framed integer `bit_length()`.  
- Reject oversized conversions (`MAX_UTF8_BYTES_FOR_INT`) instead of unbounded integers.

### Limitation (prominent)

Bit length detects **carrier-size anomalies only** — **not** semantic leakage, truth, intent, or interpretability.

**Negative control:** meaning changes while bit length/storage stays constant → detector must report it **cannot** see the semantic change.

---

## 4. Polyak heavy-ball (continuation mechanism)

\[
z_{t+1}
=
z_t-\alpha\nabla J(z_t)+\mu(z_t-z_{t-1}),
\qquad \alpha>0,\quad 0\le\mu<1
\]

- Coefficient is **`mu`**, not `beta` (avoids collision with scale ratio \(\beta=\rho/\delta\)).  
- Do **not** activate without explicit \(z\), \(J\)/gradient, \(\alpha\), \(\mu\), stability limits, and kill criterion.  
- Mapping Polyak → L²_C: **`STRUCTURAL ANALOGY`**, not a theorem.  
- \(\mu=0\) reduces to ordinary gradient descent.  
- Overshoot/divergence trips **kill**.

---

## 5. Looping, branching, state persistence (LangGraph pattern)

Implementation: `agreeya-skills/skills/pymath/scripts/kakeyalogic_coherence.py` class `CoherenceGraph`.

| Feature | Behavior |
|---|---|
| State | `GraphState` JSON-serializable |
| Checkpoint | `save_state` / `load_state` |
| Loop | Bounded repair re-queue of Prosody^→Reading when coherence low |
| Branch | `branch=main\|repair` recorded on handoffs |
| LangGraph package | **Optional** — same pattern without hard dependency |

---

## 6. RAG as Skill driver (high-level)

RAG is referenced as a **driver skill** for grounding — not implemented as a vector DB here.

Capabilities (driver contract):

- retrieve external evidence before elevating `ASSUMED` → `KNOWN`  
- cite sources on receipts  
- refuse silent promotion of `OPEN`  
- bound corpora; separate hits from recollection  

Non-capabilities: does not certify truth; does not replace `pycheck`; does not close research OPEN claims.

---

## 7. Routing

| Skill | Role |
|---|---|
| **pymath** | Compute \(D_x\), \(D_2\), \(C_x\), proposed \(W_K\), bit-depth, Polyak steps |
| **pycheck** | Independently audit claimed coherence/leakage; supersede incorrect claims |
| **pystats** | Aggregate multiple chain runs only; carry `n`, spread, sampling limits |
| **review-council** | Orchestrate independent reviews; preserve disagreement; **must not self-certify** |

---

## 8. Mandatory handoff fields

```text
stage
input_receipt
output_receipt
delta
rho
scale_base
scale_depth
coherence_score
bits_in
bits_out
allowed_growth_bits
leakage_bits
label
assumptions
open
evaluator_id
```

Labels: `KNOWN` · `COMPUTED` · `ASSUMED` · `STRUCTURAL ANALOGY` · `PROPOSED` · `OPEN`.  
**Labels never promote across handoffs.**

---

## 9. Code & tests

```text
agreeya-skills/skills/pymath/scripts/kakeyalogic_coherence.py
agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py
docs/kakeyalogic-l2c-coherence-scale.md
```

```bash
python -m pytest agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py -q
```

---

## 10. Grounding in math references (apart and the same)

| Layer | Apart | Same |
|---|---|---|
| Python `math.log2` / `bit_length` | stdlib facts | operational realization of \(D_2\), \(B(n)\) |
| KakeyaLogic / EEV4 HELD | research custody | claim labels & non-sovereignty |
| AgreeYa skill-me / review-council | enterprise skill router | handoff, provenance, no self-certify |
| L²_C | field coherence metric family | continuation discipline in the chain |

Cowork.zip archive is **evidence only** — do not mutate the zip when dropping skills.

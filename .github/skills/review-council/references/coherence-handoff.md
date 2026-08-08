# Coherence-chain handoff contract (review-council)

When reviewing KakeyaLogic / L²_C chain stages, every stage handoff must carry:

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

## Label rules

- Allowed: `KNOWN` · `COMPUTED` · `ASSUMED` · `STRUCTURAL ANALOGY` · `PROPOSED` · `OPEN`
- **Never promote** across handoffs
- Missing `allowed_growth_bits` ⇒ leakage remains `OPEN`

## Chain stages (markers literal)

```text
Conversation → Prosody^ → Reading(internal-speech proxy…) → Interpretability* → PolyakMomentum^
```

`^` and `*` are status markers, not exponentiation.

## Council must not

- Self-certify numerical correctness (defer to **pycheck**)
- Treat agreement as theoremhood or KNOWN
- Close research OPEN claims
- Infer private mental state beyond user-provided tokens

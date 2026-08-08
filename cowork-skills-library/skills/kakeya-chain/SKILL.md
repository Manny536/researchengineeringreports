---
name: kakeya-chain
description: |-
  Orchestrate the KakeyaLogic L²_C coherence chain with looping/branching state:
  Conversation → Prosody^ → Reading(token proxy) → Interpretability* → PolyakMomentum^.
  Markers ^ and * are literal, not exponentiation.

  Use when the user says:
    - "coherence chain"
    - "run KakeyaLogic stages"
    - "Prosody^"
    - "scale depth chain"
    - "/kakeya-chain"

  Do NOT use when:
    - simple arithmetic without chain context → pymath
    - multi-perspective prose review only → review-council
disable-model-invocation: false
---

# kakeya-chain

## Load

- Theory: repo `docs/kakeyalogic-l2c-coherence-scale.md`
- Code: `agreeya-skills/skills/pymath/scripts/kakeyalogic_coherence.py`
- Compute via **pymath**; audit via **pycheck**; multi-run via **pystats**; review via **review-council**.

## Chain

```text
Conversation → Prosody^ → Reading(internal-speech proxy from user tokens only)
→ Interpretability* → PolyakMomentum^
```

## Workflow

1. Collect tokens, δ, ρ, allowed_growth_bits (missing → OPEN).
2. Run `CoherenceGraph` (checkpoint if path given).
3. Emit per-stage handoffs with mandatory fields.
4. On low coherence, allow bounded repair branch (document branch=repair).
5. Do not claim theoremhood for W_K or Polyak↔L²_C.

## Mandatory handoff fields

stage, input_receipt, output_receipt, delta, rho, scale_base, scale_depth, coherence_score,
bits_in, bits_out, allowed_growth_bits, leakage_bits, label, assumptions, open, evaluator_id

## Guardrails

- No mind-reading.
- Bit length ≠ semantic leakage.
- Labels never promote.
- L²_C = continuation, not closure.

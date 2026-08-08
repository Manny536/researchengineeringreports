# Evidence receipt — KakeyaLogic L²_C coherence scale

**Verdict:** **PASS** (implementation + behavioral tests)  
**Kill criterion:** not triggered on required suite; unstable Polyak kill test **passed** (raises as expected)  
**Commit SHA:** *none* — user instructed **do not commit**; worktree on branch `feat/kakeyalogic-l2c-coherence-scale` dirty vs HEAD `715f9c093518e9fe20ca5c719ee414b54aa4565f`  
**Ancestor quality commit (evidence):** `f9f0bc478a03f3172e934fc3b5150d8c51d8d3e8`  
**Cowork.zip SHA-256 (preserved):** `c30d324b39d8c4515e57fb17e178dd677921522c340d408d06fb9ab7f6f0d4a4`

## Commands / tests

```bash
python3 -m pytest agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py -q
# 26 passed
```

Required behavioral mapping:

| # | Requirement | Result |
|---|---|---|
| 1 | δ=ρ → D_2=0, C_2=1 | PASS |
| 2 | Multiplicative invariance | PASS |
| 3 | Powers of two unit depth | PASS |
| 4 | Invalid domains fail | PASS |
| 5 | bit_length definition + zero | PASS |
| 6 | Excess bit growth leakage | PASS |
| 7 | Equal-bit semantic mutation limitation | PASS |
| 8 | Labels/OPEN survive handoff + checkpoint | PASS |
| 9 | mu=0 ≡ GD | PASS |
| 10 | Unstable momentum kill | PASS |

## Claim classifications

| Claim | Label |
|---|---|
| \(D_2\), \(C_2\), \(B(n)\) numerical defs via stdlib | `COMPUTED` / stdlib-backed |
| \(W_K\) weighted form | `PROPOSED` / `STRUCTURAL ANALOGY` |
| Polyak → L²_C mapping | `STRUCTURAL ANALOGY` |
| Markers `^` `*` formal meaning | `OPEN` until defined |
| Reading = internal speech truth | **not claimed** — token proxy only `ASSUMED` |
| Bit length detects semantics | **false** — limitation tested |
| L²_C closes research OPEN / RH | **not claimed** |
| Review-council agreement = truth | **forbidden** |
| RAG as skill driver capabilities | `STRUCTURAL ANALOGY` / capability list |
| Static Cowork scores 97/94/93 | construction evidence only (prior v0.2) |

## Remaining OPEN

- Formal definition of starred/careted stage operators (`Interpretability*`, `Prosody^`, …)
- Full `langgraph` package integration (pattern implemented; package optional/not installed)
- Upstream write to `agreeya-org2-core/agreeya-skills` review-council (local patch note only)
- Behavioral one-shot yield in live Cowork UI (not run here)
- Production RAG corpus wiring (driver referenced, not deployed)

## Changed files (worktree; uncommitted)

- `docs/kakeyalogic-l2c-coherence-scale.md`
- `docs/EVIDENCE-RECEIPT-kakeyalogic-l2c-coherence-scale.md`
- `agreeya-skills/skills/pymath/scripts/kakeyalogic_coherence.py`
- `agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py`
- `agreeya-skills/skills/pymath/SKILL.md`
- `agreeya-skills/skills/pycheck/SKILL.md`
- `agreeya-skills/skills/pystats/SKILL.md`
- `agreeya-skills/skills/review-council/**`
- `agreeya-skills/docs/patches/review-council-coherence-handoff.md`
- `agreeya-skills/{README,ACCURACY,PROVENANCE}.md`
- `agreeya-skills/scripts/drop-*.sh`
- mirrors: `.github/skills/**`, `~/Documents/Cowork/skills/**`
- **Not modified:** `/Users/manny/Documents/Cowork.zip`

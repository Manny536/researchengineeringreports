# Patch note — review-council coherence handoff (not applied upstream)

**Date:** 2026-08-07  
**Upstream:** [agreeya-org2-core/agreeya-skills `skills/review-council`](https://github.com/agreeya-org2-core/agreeya-skills/tree/main/skills/review-council)  
**Upstream PROVENANCE:** [PROVENANCE.md](https://github.com/agreeya-org2-core/agreeya-skills/blob/main/skills/review-council/PROVENANCE.md)

## Why a local patch note

This environment can read upstream via API but must **not fabricate** an applied change on `agreeya-org2-core`. Integration lives in **researchengineeringreports**:

```text
agreeya-skills/skills/review-council/
```

## Proposed upstream delta (for AgreeYa maintainers)

1. Add optional reference `references/coherence-handoff.md` with mandatory handoff fields.  
2. Extend `SKILL.md` routing: coherence compute → external numeric skills; council never self-certifies.  
3. Preserve disagreement; ban label promotion language in output format.  
4. Credit KakeyaLogic L²_C scale probe as optional consumer, not a dependency.

## Local verification

- Local skill present and linked from pack README.  
- Numeric probe tests: `pytest agreeya-skills/skills/pymath/eval/test_kakeyalogic_coherence.py`.  
- No write attempted to `agreeya-org2-core/agreeya-skills`.

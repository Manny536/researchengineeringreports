# Provenance – review-council (local pack integration)

## Credits

This local skill follows the AgreeYa **skill-me** / review-council architecture.

Upstream reference (not modified in this repository):

- https://github.com/agreeya-org2-core/agreeya-skills/tree/main/skills/review-council
- https://github.com/agreeya-org2-core/agreeya-skills/blob/main/skills/review-council/PROVENANCE.md

Upstream credits (inherited):

- Matt Pocock – grilling pattern; writing-great-skills guidance
- Josh Wickes – router-plus-subfolders enterprise skill pattern
- AgreeYa skill-me primary author lineage: [@jim-duncan](https://github.com/jim-duncan)

## Design history (this repo)

- **v0.1-local – 2026-08-07** – Integration note skill for researchengineeringreports:
  - Orchestrates reviews of KakeyaLogic L²_C coherence-chain handoffs
  - Explicit non-self-certification; preserves disagreement
  - Routes compute → pymath, audit → pycheck, aggregate → pystats
  - Does **not** replace upstream review-council releases; local handoff adapter only

## Patch posture

If `agreeya-org2-core/agreeya-skills` is not writable from this environment, changes remain in:

```text
agreeya-skills/skills/review-council/
agreeya-skills/docs/patches/review-council-coherence-handoff.md
```

Do not fabricate an applied upstream commit.

# Provenance – pymath

## Credits

Architecture follows AgreeYa **skill-me** / `agreeya-skills` router pattern (commit reference: `c7ea90619723e80aa7fd2548d5ac08dbeadc73c4`):

- Router `SKILL.md` + `platforms/` + `references/` + optional `examples/` / `eval/`
- House style: imperative agent-facing instructions, explicit relative links, completion criteria
- GitHub Copilot adapter conventions from `skill-me/platforms/github-copilot.md`

Foundational influences also noted by skill-me:

- Matt Pocock – skill authoring / grill pattern
- Josh Wickes – router-plus-subfolders enterprise skill pattern
- Anthropic Agent Skills format conventions

## Accuracy / custody lineage (internal)

Operational accuracy discipline is aligned with **KakeyaLogic · Excellence Engine V4 (EEV4)** custody ideas, expressed in **workplace-neutral labels** in the skill body:

| EEV4 idea | Skill surface |
|---|---|
| H – Hypothesis custody | Typed question restatement; do not blur the ask |
| E – Evidence exposure | Show inputs, units, formula, and independent check |
| L – Ledger continuity | Claim labels `KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN` |
| D – Drift correction | Reverse-check; reject silent unit/precision drift |
| `h < 1` non-sovereignty | Never promote guess or default to certainty |

Shareable user-facing output stays plain (no framework marketing language), matching AgreeYa productivity-skill shareable-language practice.

## Design history

- v0.1 – 2026-08-07 – Greenfield scaffold:
  - Library metaphor: “pymath” as high-accuracy math skill for mundane → IT tasks
  - Primary platform: GitHub Copilot (project or personal skill)
  - Method ladder L0–L4, verification rules, output template
  - Companion mini-skills: `pystats`, `pycheck` (siblings, not dependencies)

## Ownership and evolution

- Update `SKILL.md` when triggers, method ladder, or completion criteria change.
- Update `references/workflow.md` when intake or escalation rules change.
- Update `references/accuracy-rules.md` when claim labels or check rules change.
- Update `references/output-format.md` when answer schema changes.
- Update `platforms/*.md` when install paths or Copilot surface notes change.

## Evaluation posture

- Output type: objective numeric work with labeled assumptions.
- Use `examples/` for representative prompts and gold shapes.
- Use `eval/checklist.md` for author/reviewer pass-fail checks.

## Host repository

- Pack: `agreeya-skills/` in [Manny536/researchengineeringreports](https://github.com/Manny536/researchengineeringreports)
- Skill-me primary author credit: [@jim-duncan](https://github.com/jim-duncan)
- Pack controls: `agreeya-skills/GOVERNANCE.md`, `agreeya-skills/ACCURACY.md`

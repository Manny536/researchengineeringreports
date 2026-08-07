# Skill quality reports (Cowork)

Static **design** scores from Copilot Cowork skill health / optimization (rubric v1).  
These measure skill *construction*, not live behavioral one-shot yield.

## Latest optimization (2026-08-07)

Source zip: user Downloads `OneDrive_1_8-7-2026.zip` (applied manually in Cowork, then ported into this repo as v0.2 skill text).

| Skill | Before | After | Publish floor | Risk (post) |
|---|---|---|---|---|
| pymath | 52 | **97** | 80 | high |
| pystats | 47 | **94** | 70 | medium |
| pycheck | 52 | **93** | 70 | medium |

Average: **50 → 95**. All three clear publish bars on static rubric.

## Files

| File | Role |
|---|---|
| [optimization-report.html](./optimization-report.html) | Before / what changed / after / why |
| [pymath-quality-report.html](./pymath-quality-report.html) | Post-opt health 97 |
| [pystats-quality-report.html](./pystats-quality-report.html) | Post-opt health 94 |
| [pycheck-quality-report.html](./pycheck-quality-report.html) | Post-opt health 93 |

## What the optimizer changed (gated)

Applied in repo skill bodies (`agreeya-skills/skills/*/SKILL.md` v0.2):

1. **Steerability** – `Do NOT use` + When NOT to Use tables; sibling routing (pymath ↔ pycheck ↔ pystats) and off-ramps to xlsx/docx/Power BI.  
2. **Durability** – machine-stable `### handoff` with **label non-promotion**; pycheck `authoritative_value` supersedes claim on fail.  
3. **Coherence** – inlined fixed output contracts + worked examples.  
4. **Grounding** – named tools; compute via code when available; no fabrication.

## Caveat

A high static score is not behavioral proof. pymath is flagged high risk / medium–high autonomy – run behavioral tests for one-shot yield before treating scores as production evidence.

## Re-drop to Cowork after git pull

```bash
cd /path/to/researchengineeringreports
git pull
./agreeya-skills/scripts/drop-to-cowork.sh
```

# Governance – AgreeYa Skills pack

**Designation:** `PEAICE-RER-AGREEYA-SKILLS-001`  
**Importance:** High – accuracy and governance are first-class, not optional polish.  
**Applies to:** all skills under `agreeya-skills/skills/` and project mirrors under `.github/skills/`.

## 1. Purpose

These skills teach assistants how to compute, verify, and label numbers in a way that is:

- **Accurate** – method and checks are explicit  
- **Governed** – authority boundaries and claim status stay visible  
- **Portable** – Agent Skills router format (AgreeYa skill-me pattern)  
- **Shareable-safe** – workplace-plain outputs; no secret leakage  

## 2. Ownership

| Role | Party |
|---|---|
| Pack maintainer (this repo) | PeAIce / researchengineeringreports maintainers |
| Skill-me architecture lineage | AgreeYa – primary author [@jim-duncan](https://github.com/jim-duncan) |
| Upstream pattern repo | [agreeya-org2-core/agreeya-skills](https://github.com/agreeya-org2-core/agreeya-skills) |

Changes to skill behavior require a PR. Do not silently edit only `.github/skills/` without updating `agreeya-skills/skills/`.

## 3. Source of truth

| Layer | Path | Rule |
|---|---|---|
| Canonical source | `agreeya-skills/skills/<name>/` | Edit here first |
| Project runtime | `.github/skills/<name>/` | Must match canonical after drop |
| Install docs | `agreeya-skills/docs/install/` | User-facing drop guide |
| Accuracy contract | `agreeya-skills/ACCURACY.md` | Binding on skill authors and agents |
| Provenance | `agreeya-skills/PROVENANCE.md` + per-skill `PROVENANCE.md` | Credits and design history |

**Sync rule:** after any skill edit, run:

```bash
./agreeya-skills/scripts/drop-pymath-pack.sh project "$(git rev-parse --show-toplevel)"
```

PRs that change only one of canonical or runtime without the other are incomplete.

## 4. Authority and non-sovereignty

1. Skills **assist**; they do not own truth.  
2. User inputs, cited sources, and executed tool output outrank model recollection.  
3. Never promote `ASSUMED` or `OPEN` to `KNOWN`.  
4. Never invent constants, product limits, exchange rates, SLA calendars, or tool results.  
5. Skills do **not** send email, post tickets, approve change, or mutate external systems unless a future skill explicitly documents that power **and** the user requests it. Current pack is **draft-only**.  
6. Research claims in PeAIce reports remain `OPEN` / `FORMAL` / etc. per their own ledgers. Skills never close RH, Coleman, or other program claims.

## 5. Shareable-language rule

User-facing skill output must use **neutral workplace language**.

Do **not** insert into shareable drafts:

- product endorsements or promotional claims  
- internal lab framework names (unless the user asks for methodology)  
- unrelated technical demonstrations  

Internal custody vocabulary (`KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN`) **is** allowed because it is operational accuracy, not marketing.

## 6. Secrets and safety

- Never store credentials, tokens, or API keys in skill files.  
- Never ask the user to paste secrets into skill state files.  
- Minimize personal, customer, and security detail in examples.  
- Do not pre-approve `shell` / `bash` in skill frontmatter without an explicit security decision recorded in pack or skill `PROVENANCE.md`.

## 7. Change control

### Required for every skill change

1. Update canonical `agreeya-skills/skills/<name>/`.  
2. Re-sync `.github/skills/<name>/`.  
3. Update skill `PROVENANCE.md` design history (one line minimum).  
4. If accuracy rules change, update `ACCURACY.md` and `references/accuracy-rules.md` as needed.  
5. If install paths change, update `docs/install/`.  
6. PR description states: **what changed**, **accuracy impact**, **governance impact**.

### Merge bar (high importance)

- [ ] Folder name equals frontmatter `name`  
- [ ] `description` states what + when (triggers)  
- [ ] Relative links from `SKILL.md` resolve  
- [ ] Accuracy claim labels still defined and used  
- [ ] No secrets  
- [ ] Canonical and `.github/skills` mirrors match for touched skills  
- [ ] Smoke path documented (or existing examples still valid)

## 8. Selective routing

From AgreeYa selective skill routing practice:

- Route from the **user outcome**, not from the tool menu.  
- Activate only skills needed for a concrete requirement.  
- Prefer 2–5 skills on compound work.  
- Stop at completion criteria; do not add analysis because another skill exists.

## 9. Evaluation posture

- Numeric skills: objective methods + mandatory verification (see `ACCURACY.md`).  
- Use `examples/` and `eval/checklist.md` where present.  
- Failed verification → do not ship a single false-confident number; surface conflict and `OPEN` items.

## 10. Incident / drift response

If a skill is found inventing numbers, unit-skipping, or overclaiming:

1. File or open a PR that tightens `references/accuracy-rules.md` and examples.  
2. Mark the bad behavior in skill `PROVENANCE.md`.  
3. Re-sync runtime mirrors.  
4. Do not leave a known-bad rule in place because “it usually works.”

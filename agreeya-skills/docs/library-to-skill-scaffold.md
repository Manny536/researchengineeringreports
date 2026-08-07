# Library → Copilot skill scaffold

Simple pattern for turning “library-like” capabilities into **GitHub Copilot Agent Skills**, following [agreeya-skills / skill-me](https://github.com/agreeya-org2-core/agreeya-skills) (router skills) and **KakeyaLogic EEV4** accuracy custody (typed hold · evidence · ledger labels · drift check) without putting lab jargon in user-facing answers.

## Folder shape (AgreeYa-compatible)

```text
<skill-name>/
├── SKILL.md                 # router + frontmatter (name, description, invocation)
├── PROVENANCE.md            # credits, design history, security decisions
├── platforms/
│   ├── generic.md
│   └── github-copilot.md    # surfaces, install paths, tool limits
├── references/
│   ├── workflow.md
│   └── …                    # output format, accuracy rules, domain notes
├── examples/                # optional but recommended
└── eval/                    # optional checklist / rubric
```

**Canonical source (this repo):** `agreeya-skills/skills/<skill-name>/`  
**Copilot project install:** `<repo>/.github/skills/<skill-name>/`  
**Copilot personal install:** `~/.copilot/skills/<skill-name>/`

## EEV4 → skill field map (neutral language)

| EEV4 (internal) | Put in skill as |
|---|---|
| H – hold typed question | Input gate: one-line restatement |
| E – evidence | Show inputs, units, formula, tool results |
| L – ledger | Labels: `KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN` |
| D – drift correction | Mandatory independent check |
| Non-sovereignty | Never promote guess → certainty |

## Example skills in this tree

| Skill | Library metaphor | Job |
|---|---|---|
| [`../pymath`](../pymath) | pymath / sympy / numpy arithmetic | High-accuracy math, mundane → IT |
| [`../pystats`](../pystats) | statsmodels / scipy.stats | Stats without overclaiming |
| [`../pycheck`](../pycheck) | pytest-for-numbers | Audit someone else’s figures |

## More library → skill ideas (not built yet)

| Metaphor | Skill id | Trigger themes | Method focus |
|---|---|---|---|
| requests | `pyhttp` | API call, status code, retry | Safe request design; no secrets |
| pandas | `pytable` | CSV, join, pivot, clean | Table transforms + sanity checks |
| pytest | `pytest-skill` | write tests, edge cases | Arrange-act-assert; no flaky sleeps |
| pydantic | `pyschema` | validate payload | Schema + error messages |
| pyyaml | `pyconfig` | config review | Safe defaults; no secret commit |
| asyncio | `pyasync` | concurrency bug | Race/cancellation checklist |
| pyspark | `pybigdata` | scale job sketch | Partitioning / cost caveats |
| pytorch | `pylearn` | train/eval sketch | Data leakage + metric honesty |

## Authoring steps (fast path)

1. Copy `skills/pymath/` (or this checklist) to `agreeya-skills/skills/<new-name>/`.
2. Set `name` = folder name (lowercase, hyphens ok, ≤64 chars).
3. Write `description` with **what + when** (triggers) – Copilot uses this for auto-select.
4. Keep `SKILL.md` as a **router** (≤150 lines); push detail to `references/`.
5. Add `platforms/github-copilot.md` with install paths and tool limits.
6. Add 3–6 examples and a short eval checklist.
7. Install only after user confirms scope (project vs personal).
8. For project skills used by cloud agent: **commit** to the active branch.

## Selective routing (AgreeYa practice)

- Activate **one** skill for the primary outcome.
- Combine only when the user asks for multiple deliverables.
- Prefer 2–5 skills max on compound work; do not run the whole catalog.
- Stop at completion criteria.

## Shareable-language rule

User-facing drafts stay workplace-plain: no framework marketing, no internal lab product names, unless the user explicitly asks for methodology.

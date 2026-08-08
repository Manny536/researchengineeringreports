# AgreeYa Skills (PeAIce · Research Engineering)

Portable **Agent Skills** pack for GitHub Copilot and compatible runtimes, hosted in the PeAIce research engineering reports repository.

This pack follows the **AgreeYa skill-me** router pattern (platform adapters, references, provenance) and adds **explicit accuracy and governance** requirements for research and IT support work.

| | |
|---|---|
| **Pack id** | `PEAICE-RER-AGREEYA-SKILLS-001` |
| **Version** | `0.2.0` |
| **State** | ACTIVE · draft-for-use · Cowork static quality optimized |
| **Primary runtime** | GitHub Copilot Agent Skills |
| **Skill-me lineage** | [agreeya-org2-core/agreeya-skills](https://github.com/agreeya-org2-core/agreeya-skills) @ `c7ea906` |
| **Skill-me primary author** | [@jim-duncan](https://github.com/jim-duncan) (AgreeYa) |

## Skills in this pack

| Skill | Path | Job |
|---|---|---|
| **pymath** | [`skills/pymath/`](./skills/pymath/) | High-accuracy math + KakeyaLogic \(D_2/C_x/W_K\), bit leakage, Polyak |
| **pystats** | [`skills/pystats/`](./skills/pystats/) | Descriptive stats; multi-run coherence aggregation only |
| **pycheck** | [`skills/pycheck/`](./skills/pycheck/) | Independent verification; supersede bad coherence claims |
| **review-council** | [`skills/review-council/`](./skills/review-council/) | Independent reviews; no self-certify (local integration) |

KakeyaLogic L²_C scale doc: [`../docs/kakeyalogic-l2c-coherence-scale.md`](../docs/kakeyalogic-l2c-coherence-scale.md)  
Probe code: [`skills/pymath/scripts/kakeyalogic_coherence.py`](./skills/pymath/scripts/kakeyalogic_coherence.py)

## High-importance controls

Read these before authoring or shipping skill changes:

1. **[GOVERNANCE.md](./GOVERNANCE.md)** – ownership, change control, shareable-language, non-sovereignty, secrets, PR rules  
2. **[ACCURACY.md](./ACCURACY.md)** – claim labels, method ladder, verification mandatory, failure modes  
3. **[PROVENANCE.md](./PROVENANCE.md)** – credits (AgreeYa · Jim Duncan · skill-me), EEV4 custody map, design history  
4. **[docs/skill-quality-reports/](./docs/skill-quality-reports/)** – Cowork static scores (v0.2: pymath 97 / pystats 94 / pycheck 93)  

v0.2 skill bodies include: sibling **Do NOT use** routing, inlined output contracts, worked examples, named tools, and `### handoff` with **label non-promotion** (and pycheck claim supersession).

Runtime skill bodies stay **workplace-plain**. Lab framework names stay in provenance/governance unless the user asks for methodology.

## Repository layout

```text
agreeya-skills/                 # canonical pack (source of truth)
├── README.md
├── GOVERNANCE.md
├── ACCURACY.md
├── PROVENANCE.md
├── skills/
│   ├── pymath/
│   ├── pystats/
│   └── pycheck/
├── docs/
│   ├── install/                # multi-platform install hub (skill-me shape)
│   └── library-to-skill-scaffold.md
└── scripts/
    ├── drop-pymath-pack.sh
    └── package-pymath-pack.sh

.github/skills/                 # project runtime install (this repo)
├── pymath/
├── pystats/
└── pycheck/
```

Canonical source for edits: **`agreeya-skills/skills/<name>/`**.  
After edits, re-sync project runtime:

```bash
./agreeya-skills/scripts/drop-pymath-pack.sh project "$(git rev-parse --show-toplevel)"
```

## Install

Full multi-platform guide (AgreeYa skill-me install hub shape):

**→ [docs/install/README.md](./docs/install/README.md)**

### Copilot Cowork (complete single document)

Clone this repo, then use the complete drop file:

- [docs/install/COPILOT-COWORK-CLONE-DROP.md](./docs/install/COPILOT-COWORK-CLONE-DROP.md)
- [docs/install/COPILOT-COWORK-CLONE-DROP.docx](./docs/install/COPILOT-COWORK-CLONE-DROP.docx)

```bash
git clone https://github.com/Manny536/researchengineeringreports.git
cd researchengineeringreports
./agreeya-skills/scripts/drop-to-cowork.sh
# → ~/Documents/Cowork/skills/{pymath,pystats,pycheck}/
```

This repository already has project-scope skills under `.github/skills/` so Copilot in this repo can discover them after pull.

Personal GitHub Copilot (this machine only):

```bash
./agreeya-skills/scripts/drop-pymath-pack.sh personal
```

## Try

```text
/pymath How many minutes of downtime does a 99.9% SLA allow in a 30-day month?
```

Expect: typed question, units, method level, claim labels, and a verification step.

## Selective routing

- Activate the skill that matches the **primary requested outcome**.
- Combine skills only when the user asks for multiple deliverables.
- Prefer two to five skills on compound work; do not run the whole catalog by default.
- Stop at completion criteria.

## Relationship to research engineering stack

This pack supports **governed numeric and verification work** adjacent to the L²_C / continuity report stack. It does **not** replace:

- report acceptance surfaces (`pytest` packets, observation notes)
- verification integrity rules on the main README
- formal claim status in KakeyaLogic / Excellence Engine ledgers

Skills produce **drafts and calculations** under explicit labels. They do not close OPEN research claims.

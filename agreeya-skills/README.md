# AgreeYa Skills (PeAIce · Research Engineering)

Portable **Agent Skills** pack for GitHub Copilot and compatible runtimes, hosted in the PeAIce research engineering reports repository.

This pack follows the **AgreeYa skill-me** router pattern (platform adapters, references, provenance) and adds **explicit accuracy and governance** requirements for research and IT support work.

| | |
|---|---|
| **Pack id** | `PEAICE-RER-AGREEYA-SKILLS-001` |
| **Version** | `0.1.0` |
| **State** | ACTIVE · draft-for-use |
| **Primary runtime** | GitHub Copilot Agent Skills |
| **Skill-me lineage** | [agreeya-org2-core/agreeya-skills](https://github.com/agreeya-org2-core/agreeya-skills) @ `c7ea906` |
| **Skill-me primary author** | [@jim-duncan](https://github.com/jim-duncan) (AgreeYa) |

## Skills in this pack

| Skill | Path | Job |
|---|---|---|
| **pymath** | [`skills/pymath/`](./skills/pymath/) | High-accuracy math from mundane arithmetic through IT-level tasks |
| **pystats** | [`skills/pystats/`](./skills/pystats/) | Descriptive and careful statistical work without overclaiming |
| **pycheck** | [`skills/pycheck/`](./skills/pycheck/) | Independent verification of someone else’s numbers |

## High-importance controls

Read these before authoring or shipping skill changes:

1. **[GOVERNANCE.md](./GOVERNANCE.md)** – ownership, change control, shareable-language, non-sovereignty, secrets, PR rules  
2. **[ACCURACY.md](./ACCURACY.md)** – claim labels, method ladder, verification mandatory, failure modes  
3. **[PROVENANCE.md](./PROVENANCE.md)** – credits (AgreeYa · Jim Duncan · skill-me), EEV4 custody map, design history  

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

This repository already has project-scope skills under `.github/skills/` so Copilot in this repo can discover them after pull.

Personal (this machine only):

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

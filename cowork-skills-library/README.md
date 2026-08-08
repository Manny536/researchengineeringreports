# Cowork Skills Library

**Full Microsoft Copilot Cowork skills library** for the PeAIce / AgreeYa-pattern pack hosted in researchengineeringreports.

| | |
|---|---|
| **Library id** | `PEAICE-RER-COWORK-SKILLS-LIBRARY-001` |
| **Version** | `1.0.0` |
| **Runtime** | Copilot Cowork → `~/Documents/Cowork/skills/<name>/` |
| **Pattern** | AgreeYa skill-me router · claim labels · draft-only |
| **Math / accuracy pack** | Also includes `agreeya-skills/skills/*` (pymath, pystats, pycheck, review-council) |

## One-command install (Cowork)

From the **repository root**:

```bash
./cowork-skills-library/scripts/drop-library-to-cowork.sh
```

Installs **all** library skills **plus** the AgreeYa accuracy pack into:

```text
~/Documents/Cowork/skills/
```

Wait for OneDrive sync, then refresh Cowork → Skills.

## Catalog

See **[CATALOG.md](./CATALOG.md)** for every skill, triggers, and routing.

### Library skills (this folder)

| Skill | Job |
|---|---|
| [skill-router](./skills/skill-router/) | Select 1–5 skills from the outcome; stop at completion |
| [rag-grounding](./skills/rag-grounding/) | Retrieval driver before elevating ASSUMED→KNOWN |
| [claim-ledger](./skills/claim-ledger/) | Preserve labels across multi-skill handoffs |
| [weekly-status-draft](./skills/weekly-status-draft/) | Wins / In Progress / Risks / Next (draft-only) |
| [meeting-prep-brief](./skills/meeting-prep-brief/) | One-page meeting brief + talking points |
| [decision-inbox-draft](./skills/decision-inbox-draft/) | Decision needed + suggested reply (draft) |
| [kakeya-chain](./skills/kakeya-chain/) | Run KakeyaLogic L²_C coherence chain stages |
| [evidence-receipt](./skills/evidence-receipt/) | Structured evidence receipt for audits |
| [shareable-guard](./skills/shareable-guard/) | Workplace-plain shareable language pass |

### Accuracy pack (from `agreeya-skills/`)

| Skill | Job |
|---|---|
| **pymath** | Greenfield calc + scale depth / Polyak / bits |
| **pycheck** | Audit claimed numbers; supersede on fail |
| **pystats** | Careful stats; multi-run aggregates |
| **review-council** | Multi-perspective review; no self-certify |

## Layout

```text
cowork-skills-library/
├── README.md                 ← you are here
├── CATALOG.md
├── GOVERNANCE.md
├── scripts/
│   ├── drop-library-to-cowork.sh
│   ├── package-library.sh
│   └── validate-library.sh
├── docs/
│   └── COWORK-LIBRARY-INSTALL.md
└── skills/<skill-name>/SKILL.md
```

Canonical accuracy + Kakeya code remain under `agreeya-skills/` (single source for math). This library **orchestrates and extends** for Cowork.

## Governance

- [GOVERNANCE.md](./GOVERNANCE.md)  
- Pack accuracy: [`../agreeya-skills/ACCURACY.md`](../agreeya-skills/ACCURACY.md)  
- Kakeya scale: [`../docs/kakeyalogic-l2c-coherence-scale.md`](../docs/kakeyalogic-l2c-coherence-scale.md)

## Credits

AgreeYa skill-me pattern · [@jim-duncan](https://github.com/jim-duncan) · [agreeya-org2-core/agreeya-skills](https://github.com/agreeya-org2-core/agreeya-skills)

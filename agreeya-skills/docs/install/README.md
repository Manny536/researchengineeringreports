# pymath pack install guide

This guide is for end users who want to install and use the **pymath pack** skills from this repository.

It is not a contributor guide. For accuracy and change control, see [`../../GOVERNANCE.md`](../../GOVERNANCE.md) and [`../../ACCURACY.md`](../../ACCURACY.md).

Pattern and page layout follow AgreeYa skill-me install docs:

- Reference: [agreeya-skills `docs/skill-me/install/README.md`](https://github.com/agreeya-org2-core/agreeya-skills/blob/c7ea90619723e80aa7fd2548d5ac08dbeadc73c4/docs/skill-me/install/README.md) (pin `c7ea906`)
- Skill-me primary author: [@jim-duncan](https://github.com/jim-duncan)

## What you are installing

You are installing one or more Agent Skills so your target assistant runtime can discover and run them.

| Skill | Source folder | Purpose |
|---|---|---|
| `pymath` | `skills/pymath/` | High-accuracy math (mundane → IT) |
| `pystats` | `skills/pystats/` | Careful statistics |
| `pycheck` | `skills/pycheck/` | Verify existing numbers |

Skill source root (this pack):

```text
agreeya-skills/
├── skills/
│   ├── pymath/
│   ├── pystats/
│   └── pycheck/
├── GOVERNANCE.md
├── ACCURACY.md
└── docs/install/          ← you are here
```

In **this** repository, project-scope runtime mirrors are already installed at:

```text
.github/skills/pymath/
.github/skills/pystats/
.github/skills/pycheck/
```

Canonical source (edit first): `agreeya-skills/skills/<name>/`  
Each skill must have `SKILL.md` at its own folder root.

Optional packaged zip:

```bash
# from repository root
./agreeya-skills/scripts/package-pymath-pack.sh 0.1.0
# → agreeya-skills/dist/pymath-pack_v0.1.0.zip
```

## Complete Cowork drop (cloned repo)

**Single-file guide (start here for Copilot Cowork):**

- Markdown: [COPILOT-COWORK-CLONE-DROP.md](COPILOT-COWORK-CLONE-DROP.md)
- Word: [COPILOT-COWORK-CLONE-DROP.docx](COPILOT-COWORK-CLONE-DROP.docx)

One-command drop after clone:

```bash
./agreeya-skills/scripts/drop-to-cowork.sh
# → ~/Documents/Cowork/skills/{pymath,pystats,pycheck}/
```

## Choose your platform

- [GitHub Copilot](github-copilot_pymath-pack_install.md)
- [Cursor](cursor_pymath-pack_install.md)
- [Microsoft Scout](scout_pymath-pack_install.md)
- [Claude Code](claude-code_pymath-pack_install.md)
- [Claude Cowork](claude-cowork_pymath-pack_install.md)
- [Copilot Cowork](copilot-cowork_pymath-pack_install.md) · full clone drop: [COPILOT-COWORK-CLONE-DROP.md](COPILOT-COWORK-CLONE-DROP.md)
- [Copilot in SharePoint](sharepoint_pymath-pack_install.md)
- [Generic fallback](generic_pymath-pack_install.md)

## Assisted install support by platform

Assisted install means using prompt/chat commands to create or copy the skill instead of doing all file operations manually.

- Supported: Prompt/chat install is documented and generally reproducible.
- Conditional: Prompt/chat install can work, but depends on permissions, tenant policy, workspace setup, or enabled features.
- Not supported: No reliable prompt/chat method is documented for that platform.

| Platform | Assisted install support |
|---|---|
| GitHub Copilot | Conditional |
| Cursor | Supported |
| Microsoft Scout | Supported |
| Claude Code | Supported |
| Claude Cowork | Conditional |
| Copilot Cowork | Conditional |
| Copilot in SharePoint | Supported |
| Generic fallback | Not supported |

## Zip release install support by platform

Zip release install means installing from a packaged zip that contains `SKILL.md` and all supporting files **per skill folder**.

| Platform | Zip release install support |
|---|---|
| GitHub Copilot | Unknown |
| Cursor | Unknown |
| Microsoft Scout | Unknown |
| Claude Code | Unknown |
| Claude Cowork | Unknown |
| Copilot Cowork | User-validated |
| Copilot in SharePoint | Documented |
| Generic fallback | Unknown |

## Using a release zip

If your platform supports native zip import, use that path in the platform page.

If native zip import is unavailable, use this portable fallback:

1. Extract the zip to a local folder.
2. Confirm each skill root contains `SKILL.md` (example: `skills/pymath/SKILL.md`).
3. Follow that platform's normal install steps using each skill folder as source.

If your zip expands with an extra top-level wrapper folder, adjust the source path so the folder containing `SKILL.md` is what you install.

## Before you start

1. Ensure you have a local clone of this repository or the zip file extracted.
2. Decide whether you want project-scoped install or user-scoped install where supported.
3. Decide whether to install the **full pack** (`pymath` + `pystats` + `pycheck`) or only selected skills.
4. Use each skill folder under `agreeya-skills/skills/` as the source – not the whole pack parent as a single skill.

## Drop rule (important)

Agent Skills are **one folder per skill**. Do **not** nest incorrectly:

```text
# correct (project scope)
.github/skills/pymath/
.github/skills/pystats/
.github/skills/pycheck/

# wrong
.github/skills/agreeya-skills/skills/pymath/   # extra nesting
.github/skills/docs/                           # docs are not a skill
```

Exclude from any install copy:

- `docs/`
- `scripts/`
- pack-level markdown (`README.md`, `GOVERNANCE.md`, …) unless your process wants them beside skills
- `state/`, `.skill-me-*`, and other working-state files if present

## Verify after install

After installing, open your assistant and explicitly invoke:

```text
/pymath
```

Optional siblings:

```text
/pystats
/pycheck
```

Smoke prompt:

```text
/pymath How many minutes of downtime does a 99.9% SLA allow in a 30-day month?
```

Expect: answer with units, method level, claim labels (`KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN`), and a verification step – per [`../../ACCURACY.md`](../../ACCURACY.md).

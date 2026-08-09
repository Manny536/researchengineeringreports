---
title: AgreeYa Skills — Complete Copilot Cowork Drop Guide
version: 0.1.1
tested-on: "Windows 11 (OneDrive) / macOS 12 (OneDrive) — 2026-08-07"
maintainer: Manny536 (researchengineeringreports)
contact: Open issues or PRs in the repository
---

# AgreeYa Skills — Complete Copilot Cowork Drop Guide

**Document type:** Single-file install + operating contract  
**Use case:** Drop skills into **Microsoft Copilot Cowork** from a **cloned** researchengineeringreports repository  
**Pack:** `PEAICE-RER-AGREEYA-SKILLS-001` · v0.1.0  
**Importance:** High — accuracy and governance are binding  
**Date:** 2026-08-07

---

This updated guide adds a small sanity-check block, an example verify script, a Table of Contents, a clear warning box about draft-only behavior, a pass/accuracy checklist, and tightened troubleshooting steps.

Table of contents

- 1. What this document is
- 2. What you are installing
- 3. Prerequisites
- 4. Clone the repository
- 5. Cowork destination path
- 6. Drop methods
  - 6.1 One-command drop (recommended)
  - 6.2 Manual copy (shell)
  - 6.3 Manual copy (Finder / Explorer)
  - 6.4 Assisted install (Cowork chat)
  - 6.5 Zip / Customize UI upload
- 7. Wait for sync
- 8. Accuracy contract (pass checklist)
- 9. Governance contract (key rules)
- 10. Skill inventory
- 11. Verify after drop (sanity check & verify script)
- 12. Troubleshooting
- 13. Relationship to GitHub Copilot (project mirror)
- 14. Credits
- 15. Quick card
- Changelog

---

## WARNING — Draft-only (important)

This pack is strictly **draft-only**. Skills and scripts in this repository are NOT permitted to send email, post or close tickets, approve changes, or mutate external systems unless a specific skill explicitly documents that power and the user requests it. Treat outputs as drafts for human review.

---

## 1. What this document is

This is the **complete** drop-in guide. You should not need other install pages to finish a Cowork install when the repo is cloned.

It covers:

1. Clone the repository
2. Copy skills into the Cowork skills path
3. Assisted (chat) install prompts
4. Zip / Customize UI path
5. Accuracy rules (must follow)
6. Governance rules (must follow)
7. Verification smoke tests and a small verify script
8. Credits and provenance

---

## 2. What you are installing

| Skill | Folder | When to use |
|---|---|---|
| **pymath** | `pymath/` | Calculate / convert / SLA / rates / capacity — high accuracy |
| **pystats** | `pystats/` | Averages, samples, uncertainty — no overclaiming |
| **pycheck** | `pycheck/` | “Check my math” / audit existing figures |

Pattern lineage: AgreeYa **skill-me** ([agreeya-org2-core/agreeya-skills](https://github.com/agreeya-org2-core/agreeya-skills)) · primary author [**@jim-duncan**](https://github.com/jim-duncan).

Host repository: [Manny536/researchengineeringreports](https://github.com/Manny536/researchengineeringreports).

---

## 3. Prerequisites

- Access to **Copilot Cowork** skill authoring in your Microsoft 365 tenant  
- OneDrive / Documents sync available to Cowork  
- Git installed (for clone path)  
- Permission to write under `Documents/Cowork/skills/`  
- Network access to GitHub **or** an already-cloned local copy of the repo

---

## 4. Clone the repository

### Option A — fresh clone

```bash
cd ~/Documents
git clone https://github.com/Manny536/researchengineeringreports.git
cd researchengineeringreports
# prefer detecting the default branch rather than assuming 'main'
default_branch=$(git remote show origin | sed -n '/HEAD branch/s/.*: //p')
[ -n "$default_branch" ] || default_branch=main
git checkout "$default_branch"
git pull
```

### Option B — already cloned

```bash
cd /path/to/researchengineeringreports
# ensure you're on the repo's default branch
default_branch=$(git remote show origin | sed -n '/HEAD branch/s/.*: //p')
[ -n "$default_branch" ] || default_branch=main
git checkout "$default_branch" && git pull
```

Confirm source skills exist (each command should list the file; no "No such file" errors):

```bash
ls agreeya-skills/skills/pymath/SKILL.md \
   agreeya-skills/skills/pystats/SKILL.md \
   agreeya-skills/skills/pycheck/SKILL.md
```

---

## 5. Cowork destination path

Copilot Cowork runtime skills root (OneDrive / Documents):

```text
~/Documents/Cowork/skills/<skill-name>/
```

Full pack destinations:

```text
~/Documents/Cowork/skills/pymath/
~/Documents/Cowork/skills/pystats/
~/Documents/Cowork/skills/pycheck/
```

**Drop rule:** one skill = one folder named exactly `pymath` | `pystats` | `pycheck`. Each folder root must contain `SKILL.md`.

Wrong (do not do this):

```text
~/Documents/Cowork/skills/agreeya-skills/skills/pymath/   # extra nesting
~/Documents/Cowork/skills/researchengineeringreports/    # whole repo is not a skill
```

---

## 6. Drop methods

### 6.1 One-command drop (recommended)

From the **cloned repo root**:

```bash
# ensure script is present and executable
test -f ./agreeya-skills/scripts/drop-to-cowork.sh || { echo "missing script: agreeya-skills/scripts/drop-to-cowork.sh" >&2; exit 1; }
chmod +x ./agreeya-skills/scripts/drop-to-cowork.sh
./agreeya-skills/scripts/drop-to-cowork.sh
```

Optional — only selected skills:

```bash
./agreeya-skills/scripts/drop-to-cowork.sh pymath pycheck
```

Custom Cowork root (if your tenant path differs):

```bash
COWORK_SKILLS_ROOT="$HOME/Documents/Cowork/skills" \
  ./agreeya-skills/scripts/drop-to-cowork.sh
```

What the script does:

1. Reads canonical source from `agreeya-skills/skills/<name>/`  
2. Creates `~/Documents/Cowork/skills/` if missing  
3. Replaces each target skill folder cleanly  
4. Verifies `SKILL.md` exists at each destination root

### 6.2 Manual copy (shell)

```bash
REPO="$HOME/Documents/researchengineeringreports"   # adjust if different
DEST="$HOME/Documents/Cowork/skills"

mkdir -p "$DEST"

for s in pymath pystats pycheck; do
  rm -rf "$DEST/$s"
  mkdir -p "$DEST/$s"
  rsync -a \
    --exclude '.DS_Store' \
    --exclude '__pycache__/' \
    --exclude 'state/' \
    "$REPO/agreeya-skills/skills/$s/" "$DEST/$s/"
  test -f "$DEST/$s/SKILL.md" && echo "OK $s" || echo "FAIL $s"
done
```

### 6.3 Manual copy (Finder / Explorer)

1. Open clone: `researchengineeringreports/agreeya-skills/skills/`  
2. Open destination: `Documents/Cowork/skills/` (create `Cowork/skills` if needed)  
3. Copy folders `pymath`, `pystats`, `pycheck` **as whole folders**  
4. Confirm each has `SKILL.md` at the top of that folder

### 6.4 Assisted install (Cowork chat)

Use after the repo is cloned and visible to the agent (workspace or attached folder).  
The guide retains the original suggested prompt; use it when asking a workspace-aware agent to copy the skills.

### 6.5 Zip / Customize UI upload

If your tenant uses zip upload:

1. From repo root:

```bash
./agreeya-skills/scripts/package-pymath-pack.sh 0.1.0
# → agreeya-skills/dist/pymath-pack_v0.1.0.zip
```

2. Extract the zip.  
3. For **each** skill under `skills/<name>/`, create a zip whose **root** is that skill (so `SKILL.md` is at zip root), **or** follow tenant UI if multi-file folder import is supported.  
4. Upload via Cowork **Customize → Skills** (or current tenant UI).  
5. Wait for OneDrive / Cowork sync.

---

## 7. Wait for sync

After any drop:

1. Allow OneDrive to finish syncing `Documents/Cowork/skills/`  
2. Restart or refresh Copilot Cowork if skills do not appear  
3. Open Skills / Customize and confirm `pymath`, `pystats`, `pycheck`

---

## 8. Accuracy contract (pass checklist)

Every skill run in Cowork must obey these rules. Convert the rules into this checklist to make verification easier.

### Pass checklist — a response is complete only when all apply

- [ ] Typed question restated (copy of user prompt)  
- [ ] Units coherent and stated  
- [ ] Method level stated (L0–L4)  
- [ ] Primary answer labeled (KNOWN / COMPUTED / ASSUMED / OPEN)  
- [ ] Assumptions / OPEN listed when present  
- [ ] At least one verification step performed (reverse calc, unit check, boundary check, or second method)  
- [ ] No invented constants, FX, or hidden assumptions  

### Short rules (highlights)

- Claim labels: `KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN` — never promote `ASSUMED` or `OPEN` to `KNOWN`.  
- Use the lowest sufficient method level (L0–L4).  
- Verification is mandatory for primary computed results.

---

## 9. Governance contract (key rules)

### 9.1 Draft-only

Skills **assist**. They do **not**:

- send email or chat messages  
- post or close tickets  
- approve change records  
- mutate external systems

Unless a future skill explicitly documents that power **and** the user requests it. This pack is draft-only.

### 9.2 Non-sovereignty

User inputs, cited sources, and real tool results outrank model memory. Skills do not own truth.

### 9.3 Shareable language

User-facing drafts stay **workplace-plain**. No product endorsements, no internal lab marketing. Operational labels (`KNOWN` / `COMPUTED` / …) are allowed.

### 9.4 Secrets

Never store or request credentials, tokens, or API keys in skill files or skill outputs.

### 9.5 Source of truth after edit

| Layer | Path |
|---|---|
| Canonical (edit first) | `agreeya-skills/skills/<name>/` in the git clone |
| Cowork runtime | `~/Documents/Cowork/skills/<name>/` |
| GitHub Copilot project runtime (this repo) | `.github/skills/<name>/` |

After editing canonical skills in git: re-run `drop-to-cowork.sh` (and project drop if needed). Do not maintain Cowork-only forks without merging back to git.

---

## 10. Skill inventory (what each folder contains)

Minimum structure after a correct drop:

```text
~/Documents/Cowork/skills/pymath/
├── SKILL.md
├── PROVENANCE.md
├── platforms/
│   ├── generic.md
│   └── github-copilot.md
├── references/
│   ├── workflow.md
│   ├── accuracy-rules.md
│   └── output-format.md
├── examples/
│   └── mundane-to-it.md
└── eval/
    └── checklist.md

~/Documents/Cowork/skills/pystats/
├── SKILL.md
├── PROVENANCE.md
├── platforms/
└── references/

~/Documents/Cowork/skills/pycheck/
├── SKILL.md
├── PROVENANCE.md
├── platforms/
└── references/
```

Relative links inside `SKILL.md` must keep working — copy whole trees, not `SKILL.md` alone.

---

## 11. Verify after drop (sanity check & verify script)

### 11.1 Filesystem sanity check (quick)

Run this to confirm basic presence of files after a drop:

```bash
for s in pymath pystats pycheck; do
  f="$HOME/Documents/Cowork/skills/$s/SKILL.md"
  if [[ -f "$f" ]]; then echo "OK  $f"; else echo "MISSING $f"; fi
done
```

### 11.2 Example verify script (copy into `agreeya-skills/scripts/verify-drop.sh`)

This is a small helper you can add to the repo or run locally after a drop. It is intentionally conservative and only checks presence and a couple of common sanity conditions.

```bash
#!/usr/bin/env bash
set -euo pipefail

SKILLS=(pymath pystats pycheck)
DEST="${COWORK_SKILLS_ROOT:-${HOME}/Documents/Cowork/skills}"

for s in "${SKILLS[@]}"; do
  root="$DEST/$s"
  if [[ -f "$root/SKILL.md" ]]; then
    echo "OK: $root/SKILL.md"
  else
    echo "MISSING: $root/SKILL.md" >&2
  fi
  # check common companion files
  if [[ -f "$root/PROVENANCE.md" ]]; then
    echo "FOUND: $root/PROVENANCE.md"
  else
    echo "WARN: missing PROVENANCE.md for $s"
  fi
done
```

Make it executable and run after drop:

```bash
chmod +x agreeya-skills/scripts/verify-drop.sh
./agreeya-skills/scripts/verify-drop.sh
```

### 11.3 Smoke prompts (manual verification)

Use these manual prompts in Copilot Cowork to check behavior. Expect the skill to restate typed question, list assumptions, show method level, compute a value, and show at least one verification step.

**pymath**

Use prompt:

```text
Use pymath: How many minutes of downtime does a 99.9% SLA allow in a 30-day month?
```

**pymath (IT units)**

Use prompt:

```text
Use pymath: Convert 2.5 GiB to bytes (binary). Show the factor chain.
```

**pycheck**

Use prompt:

```text
Use pycheck: Claimed tip is $12 on $64.50 at 18%. Verify.
```

**pystats**

Use prompt:

```text
Use pystats: Sample of 5 response times: 120, 130, 125, 400, 128 ms. Summarize carefully.
```

---

## 12. Troubleshooting (improved)

| Symptom | Fix |
|---|---|
| Skill not listed | Confirm path `Documents/Cowork/skills/<name>/SKILL.md`; wait for OneDrive sync; run the sanity check in §11; refresh Cowork |
| Skill listed but broken | Re-copy **entire** folder (platforms + references), not SKILL.md alone. Run `./agreeya-skills/scripts/verify-drop.sh` to surface missing companions. |
| Wrong calculations | Enforce claim labels + verification; re-read accuracy section §8 |
| Extra nesting | Remove intermediate folders; skill root must be `…/skills/pymath/` |
| Tenant blocks write | Use Customize UI upload (zip) or ask tenant admin; check UI permissions; see command below |
| Stale skill after git pull | Re-run `./agreeya-skills/scripts/drop-to-cowork.sh` from updated clone |

### OneDrive sync troubleshooting

- Check OneDrive status (example macOS Finder: OneDrive icon; Windows: OneDrive icon in taskbar). If sync is paused or conflicting, resolve in the OneDrive client.  
- If skills don't appear after sync: sign out/in Copilot Cowork, or restart the product.  
- Confirm file timestamps and that `SKILL.md` is not zero-length (`stat` / `ls -l`).

### Permission checks

```bash
ls -ld ~/Documents/Cowork/skills
getfacl ~/Documents/Cowork/skills || true
```

If permission errors occur, correct with tenant admin or local OS permission commands.

---

## 13. Relationship to GitHub Copilot (same clone)

Same clone also ships project skills for GitHub Copilot at:

```text
.github/skills/pymath/
.github/skills/pystats/
.github/skills/pycheck/
```

Cowork path and `.github/skills` are **different runtimes**. Dropping to Cowork does not replace the GitHub project mirror. After skill authoring in git:

```bash
# Cowork
./agreeya-skills/scripts/drop-to-cowork.sh

# GitHub Copilot project mirror (optional refresh)
./agreeya-skills/scripts/drop-pymath-pack.sh project "$(git rev-parse --show-toplevel)"
```

---

## 14. Credits

| Party | Role |
|---|---|
| [**@jim-duncan**](https://github.com/jim-duncan) · AgreeYa | skill-me architecture / primary author lineage |
| [agreeya-org2-core/agreeya-skills](https://github.com/agreeya-org2-core/agreeya-skills) | Upstream pattern (install hub shape @ `c7ea906`) |
| PeAIce / researchengineeringreports | Pack host, accuracy + governance contracts |

---

## 15. Quick card (print / pin)

```text
CLONE   →  git clone …/researchengineeringreports && cd … && git pull
DROP    →  ./agreeya-skills/scripts/drop-to-cowork.sh
PATH    →  ~/Documents/Cowork/skills/{pymath,pystats,pycheck}/
LABELS  →  KNOWN | COMPUTED | ASSUMED | OPEN
CHECK   →  reverse / units / magnitude (mandatory)
MODE    →  draft-only (no send / approve)
SMOKE   →  Use pymath: 99.9% SLA downtime minutes (30-day month)
CREDIT  →  AgreeYa skill-me · @jim-duncan
```

---

## Changelog

- 0.1.0 — 2026-08-07 — initial drop guide (Manny536)
- 0.1.1 — 2026-08-09 — added frontmatter, TOC, sanity-check, verify script example, pass checklist, and tightened troubleshooting (documentation maintenance)

---

*End of file.*

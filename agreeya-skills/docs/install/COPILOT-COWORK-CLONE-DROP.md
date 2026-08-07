# AgreeYa Skills — Complete Copilot Cowork Drop Guide

**Document type:** Single-file install + operating contract  
**Use case:** Drop skills into **Microsoft Copilot Cowork** from a **cloned** researchengineeringreports repository  
**Pack:** `PEAICE-RER-AGREEYA-SKILLS-001` · v0.1.0  
**Importance:** High — accuracy and governance are binding  
**Date:** 2026-08-07  

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
7. Verification smoke tests  
8. Credits and provenance  

**Do not** treat this pack as “send / approve / close ticket” automation. Output is **draft-only**.

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
git checkout main
git pull
```

### Option B — already cloned

```bash
cd /path/to/researchengineeringreports
git checkout main
git pull
```

Confirm source skills exist:

```bash
ls agreeya-skills/skills/pymath/SKILL.md \
   agreeya-skills/skills/pystats/SKILL.md \
   agreeya-skills/skills/pycheck/SKILL.md
```

Each path must print without “No such file”.

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

**Drop rule:** one skill = one folder named exactly `pymath` | `pystats` | `pycheck`.  
Each folder root must contain `SKILL.md`.

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

**Prompt — full pack:**

```text
Install the AgreeYa pymath pack into Copilot Cowork from this cloned repository.

Source (canonical):
  agreeya-skills/skills/pymath
  agreeya-skills/skills/pystats
  agreeya-skills/skills/pycheck

Destination (Cowork runtime):
  ~/Documents/Cowork/skills/<skill-name>/

Rules:
- One folder per skill; folder name must match skill name exactly
- Each destination root must contain SKILL.md
- Preserve platforms/, references/, examples/, eval/, PROVENANCE.md
- Do NOT copy agreeya-skills/docs, scripts, or the whole repo as a skill
- Do NOT invent files; only copy what exists
- Draft-only skills: do not send mail, post tickets, or approve changes

After copy, list each installed path and confirm SKILL.md exists.
```

**Prompt — single skill:**

```text
Install only pymath from agreeya-skills/skills/pymath into
~/Documents/Cowork/skills/pymath/ preserving structure and relative links.
```

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

## 8. Accuracy contract (binding)

Every skill run in Cowork must obey these rules.

### 8.1 Claim labels

| Label | Meaning |
|---|---|
| `KNOWN` | From user or authoritative cited source |
| `COMPUTED` | Derived by explicit method |
| `ASSUMED` | Modeling choice not supplied by user |
| `OPEN` | Missing, conflicting, or unverified |

**Hard rule:** never promote `ASSUMED` or `OPEN` to `KNOWN`.

### 8.2 Typed question

Restate once before computing:

```text
Compute <quantity> in <units> given <inputs>, for <purpose>.
```

### 8.3 Method ladder

Use the lowest sufficient level: **L0** mental → **L1** exact → **L2** formula → **L3** code → **L4** simulation.

### 8.4 Verification mandatory

Every primary `COMPUTED` result needs at least one of: reverse calc, order-of-magnitude, unit/dimension check, boundary check, second method.

If checks disagree: report conflict + `OPEN`. Do not ship one smooth false number.

### 8.5 Unit hygiene

- Bits vs bytes (`× 8`) explicit when mixed  
- SI vs IEC storage prefixes explicit (`MB` vs `MiB`)  
- SLA period basis (30-day month vs 365-day year) labeled `ASSUMED` unless given  

### 8.6 Forbidden silent moves

- Inventing constants, FX, tax, product limits, or tool output  
- Dropping units mid-calculation  
- Fake precision  
- Smoothing conflicting inputs into one convenient value  

### 8.7 Pass bar

A response is complete only when:

- [ ] Typed question restated  
- [ ] Units coherent  
- [ ] Method level stated  
- [ ] Primary answer labeled  
- [ ] Assumptions / OPEN listed when present  
- [ ] At least one verification step  
- [ ] No invented constants  

---

## 9. Governance contract (binding)

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

### 9.6 Selective routing

- Route from the **user’s outcome**, not from the full skill menu  
- Activate only skills needed for the ask  
- Prefer 2–5 skills on compound work  
- Stop at completion criteria  

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

## 11. Verify after drop

### 11.1 Filesystem

```bash
for s in pymath pystats pycheck; do
  f="$HOME/Documents/Cowork/skills/$s/SKILL.md"
  if [[ -f "$f" ]]; then echo "OK  $f"; else echo "MISSING $f"; fi
done
```

### 11.2 Cowork UI

- Customize / Skills lists `pymath` (and siblings you installed)  
- Folder name matches skill `name` in frontmatter  

### 11.3 Smoke prompts

**pymath**

```text
Use pymath: How many minutes of downtime does a 99.9% SLA allow in a 30-day month?
```

Expect: typed question, period assumption labeled, formula, minutes result, reverse-check.

**pymath (IT units)**

```text
Use pymath: Convert 2.5 GiB to bytes (binary). Show the factor chain.
```

Expect: binary GiB (1024³), not decimal GB.

**pycheck**

```text
Use pycheck: Claimed tip is $12 on $64.50 at 18%. Verify.
```

Expect: independent rebuild, verdict pass/fail, delta.

**pystats**

```text
Use pystats: Sample of 5 response times: 120, 130, 125, 400, 128 ms. Summarize carefully.
```

Expect: mean vs median noted; outlier caution; no fake significance.

---

## 12. Troubleshooting

| Symptom | Fix |
|---|---|
| Skill not listed | Confirm path `Documents/Cowork/skills/<name>/SKILL.md`; wait for OneDrive sync; refresh Cowork |
| Skill listed but broken | Re-copy **entire** folder (platforms + references), not SKILL.md alone |
| Wrong calculations | Enforce claim labels + verification; re-read accuracy section §8 |
| Extra nesting | Remove intermediate folders; skill root must be `…/skills/pymath/` |
| Tenant blocks write | Use Customize UI upload or ask tenant admin; manual path may be policy-gated |
| Stale skill after git pull | Re-run `./agreeya-skills/scripts/drop-to-cowork.sh` from updated clone |

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

*End of complete file. This document alone is sufficient to drop the pack into Copilot Cowork from a cloned repo.*

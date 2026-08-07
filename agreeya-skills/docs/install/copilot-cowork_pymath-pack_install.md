# Install on Copilot Cowork

> **Complete clone-drop document (preferred):**  
> [COPILOT-COWORK-CLONE-DROP.md](COPILOT-COWORK-CLONE-DROP.md) · [COPILOT-COWORK-CLONE-DROP.docx](COPILOT-COWORK-CLONE-DROP.docx)  
> One command after clone: `./agreeya-skills/scripts/drop-to-cowork.sh`

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-chat)  
✅ [Zip (upload)](#zip-install-ui-upload)  
✅ [Clone + drop script](#clone--drop-script)

## What you need

- Access to Copilot Cowork skill authoring in your tenant.
- A **cloned** copy of [researchengineeringreports](https://github.com/Manny536/researchengineeringreports) **or** a packaged zip of the pymath pack.
- For zip upload: one zip **per skill** (or follow product UI if multi-skill upload is supported). Prefer packaging with `scripts/package-pymath-pack.sh` then uploading individual skill folders if required.

## Clone + drop script

```bash
git clone https://github.com/Manny536/researchengineeringreports.git
cd researchengineeringreports
./agreeya-skills/scripts/drop-to-cowork.sh
```

Destination: `~/Documents/Cowork/skills/{pymath,pystats,pycheck}/`

## Install path

Copilot Cowork runtime path in OneDrive (repeat per skill):

```text
Documents/Cowork/skills/<skill-name>/
```

## Install steps (manual)

1. Open Copilot Cowork skill authoring.
2. Create or update skills `pymath`, `pystats`, and/or `pycheck` under `Documents/Cowork/skills/`.
3. Add content from each skill's `SKILL.md` and copy companion files preserving structure.
4. Wait for sync propagation before testing.

## Assisted install (chat)

Prompt:

```text
Create or update Copilot Cowork skills named pymath, pystats, and pycheck from agreeya-skills/skills under Documents/Cowork/skills/<name>/.
Preserve companion files and relative links. Skip docs/ and scripts/.
```

Expected outcome:

- Skills appear under `Documents/Cowork/skills/`.
- Companion files included with the same relative structure.

When this fails:

- Tenant policy or workspace configuration may block automated creation.
- Retry using in-product create/update UI directly.
- Run the manual install steps above.

## Zip install (UI upload)

Copilot Cowork supports skill upload through the Customize UI.

1. Build or obtain a zip that contains a single skill root with `SKILL.md` (example: zip contents start with `SKILL.md`, `platforms/`, `references/`).
2. Upload via Customize → Skills (or current tenant UI).
3. Repeat per skill if the UI accepts one skill per zip.
4. Wait for sync; then verify.

## Verify

- Confirm each skill is listed in Cowork Skills.
- Run: `Use pymath: 18% tip on $64.50`.

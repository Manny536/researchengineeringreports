# Install on Cursor

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-chatagent)  
❌ Zip (native import)  

## What you need

- Local source: `agreeya-skills/skills/pymath/` (and optional `pystats/`, `pycheck/`).
- Or a zip extracted so each skill root has `SKILL.md`.

## Install path

Pick one scope (repeat per skill):

- Project scope: `.cursor/skills/<skill-name>/`
- User scope: `~/.cursor/skills/<skill-name>/`

`<skill-name>`: `pymath` | `pystats` | `pycheck`

## Install steps (manual)

1. Choose project or user scope.
2. Create the destination folder for each skill you want.
3. Copy the full contents of each source skill folder into that destination.
4. Restart Cursor or refresh Skills discovery.

Example (project, full pack):

```bash
mkdir -p .cursor/skills
cp -R agreeya-skills/skills/pymath  .cursor/skills/pymath
cp -R agreeya-skills/skills/pystats .cursor/skills/pystats
cp -R agreeya-skills/skills/pycheck .cursor/skills/pycheck
```

## Assisted install (chat/agent)

Prompt:

```text
Install the pymath pack for this project from agreeya-skills/skills into .cursor/skills/.
Copy pymath, pystats, and pycheck so each has SKILL.md at folder root. Skip docs/ and scripts/.
```

Expected outcome:

- `.cursor/skills/pymath/SKILL.md` (and siblings) present.

When this fails:

- Grant or approve file-write actions in your Cursor session.
- Run the manual install steps above.

## Verify

- Open Customize → Skills and check that `pymath` is listed.
- In Agent chat, type `/` and confirm `pymath` is available.
- Smoke: `/pymath Convert 2.5 GiB to bytes (binary).`

## Troubleshooting

- If not discovered, verify the folder name is exactly `pymath` (or the sibling name).
- Confirm `SKILL.md` exists at the destination root.

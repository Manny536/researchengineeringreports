# Install on Claude Code

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-chatagent)  
❌ Zip (native import)  

## What you need

- Local source: `agreeya-skills/skills/pymath/` (and optional siblings).
- Or a zip extracted so each skill root has `SKILL.md`.

## Install path

Pick one scope (repeat per skill):

- User scope: `~/.claude/skills/<skill-name>/`
- Project scope: `.claude/skills/<skill-name>/`

## Install steps (manual)

1. Choose user or project scope.
2. Create the destination folder.
3. Copy the full contents of each skill folder into that destination.
4. Reload Claude Code session.

Example (user, full pack):

```bash
mkdir -p ~/.claude/skills
cp -R agreeya-skills/skills/pymath  ~/.claude/skills/pymath
cp -R agreeya-skills/skills/pystats ~/.claude/skills/pystats
cp -R agreeya-skills/skills/pycheck ~/.claude/skills/pycheck
```

## Assisted install (chat/agent)

Prompt:

```text
Install the pymath pack as personal skills from agreeya-skills/skills into ~/.claude/skills/.
Copy pymath, pystats, and pycheck only.
```

Expected outcome:

- `~/.claude/skills/pymath/SKILL.md` (and siblings) present.

When this fails:

- Confirm Claude has permission to write to your target directory.
- Retry with explicit project scope or user scope in the prompt.
- Run the manual install steps above.

## Verify

- Confirm `SKILL.md` exists at each destination root.
- Invoke `/pymath` in Claude Code.

## Troubleshooting

- If not found, verify destination path and exact folder names.

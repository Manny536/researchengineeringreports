# Install on Claude Cowork

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-chatagent)  
❌ Zip (native import)  

## What you need

- Local source: `agreeya-skills/skills/pymath/` (and optional siblings).
- Or a zip extracted so each skill root has `SKILL.md`.
- Your workspace's Claude Cowork skills root path.

## Install path

Claude Cowork path is workspace-dependent. Install each skill to:

```text
<claude-cowork-skills-root>/<skill-name>/
```

## Install steps (manual)

1. Identify your Claude Cowork skills root in your workspace setup.
2. Create `<claude-cowork-skills-root>/pymath/` (and siblings as needed).
3. Copy the full contents of each source skill folder into that folder.
4. Refresh Claude Cowork skills.

## Assisted install (chat/agent)

Prompt:

```text
Install the pymath pack into <claude-cowork-skills-root>/ from agreeya-skills/skills.
Copy pymath, pystats, and pycheck so each has SKILL.md at folder root.
```

Expected outcome:

- Destination folders exist under your workspace skills root.
- Companion files preserve relative structure.

When this fails:

- Confirm the skills root path and write permissions.
- Run the manual install steps above.

## Verify

- Confirm each skill folder has `SKILL.md` at root.
- Invoke `pymath` (or platform equivalent) with a small SLA or unit conversion prompt.

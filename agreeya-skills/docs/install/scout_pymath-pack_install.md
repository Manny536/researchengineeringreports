# Install on Microsoft Scout

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-chatagent)  
❌ Zip (native import)  

## What you need

- Local source: `agreeya-skills/skills/pymath/` (and optional siblings).
- Microsoft Scout with local custom skill support.

## Install path

Scout runtime skill path (repeat per skill):

```text
~/.scout/m-skills/<skill-name>/
```

## Install steps (manual)

1. In Scout, create or update a local skill named `pymath` (and siblings as needed).
2. Use `pymath/SKILL.md` as the skill instructions source.
3. Copy companion files from each skill folder into `~/.scout/m-skills/<skill-name>/` so relative links keep working.
4. Keep the runtime folder name exact (`pymath`, `pystats`, `pycheck`).

## Assisted install (chat/agent)

Prompt:

```text
Install the pymath pack in Scout as local skills, and sync companion files into ~/.scout/m-skills/pymath/, pystats/, and pycheck/ from agreeya-skills/skills.
```

Expected outcome:

- Writable local Scout skills created or updated with companion files.

## Verify

- Confirm each destination has `SKILL.md`.
- Invoke `pymath` with a short calculation prompt.

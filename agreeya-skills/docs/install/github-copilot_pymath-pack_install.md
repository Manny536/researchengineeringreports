# Install on GitHub Copilot

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-agent-mode)  
✅ [Shell drop](#shell-drop-local)  
❌ Zip (native import)  

## What you need

- Local source from this repository:
  - `agreeya-skills/skills/pymath/`
  - `agreeya-skills/skills/pystats/` (optional)
  - `agreeya-skills/skills/pycheck/` (optional)
- Or a packaged zip extracted so each skill root has `SKILL.md`.
- A Copilot surface that supports Agent Skills (VS Code, Copilot CLI, and/or GitHub-hosted agent on a branch that contains project skills).
- Read pack controls: `agreeya-skills/GOVERNANCE.md`, `agreeya-skills/ACCURACY.md`.

## Install path

Pick one scope:

| Scope | Destination (repeat per skill) | Use when |
|---|---|---|
| Project (recommended) | `<repository-root>/.github/skills/<skill-name>/` | Shared repo, cloud agent, code review |
| Personal (local only) | `~/.copilot/skills/<skill-name>/` | This machine only |

`<skill-name>` is exactly one of: `pymath`, `pystats`, `pycheck`.

Use project scope for GitHub-hosted surfaces and code review scenarios. Personal scope is **not** visible to cloud agent or code review.

Alternate roots recognized by some hosts (`.claude/skills/`, `.agents/skills/`, `~/.agents/skills/`) exist, but this guide uses the **canonical** paths above for consistency.

## Install steps (manual)

### Full pack – project scope

1. Open the target repository root.
2. Create destinations:

```bash
mkdir -p .github/skills
```

3. Copy each skill folder (folder name must match skill `name`):

```bash
cp -R agreeya-skills/skills/pymath   .github/skills/pymath
cp -R agreeya-skills/skills/pystats  .github/skills/pystats
cp -R agreeya-skills/skills/pycheck  .github/skills/pycheck
```

4. Confirm each destination has `SKILL.md` at folder root and the folder name is exact (`pymath`, not `PyMath`).
5. Commit the project skills if GitHub-hosted agents or code review must see them.
6. Refresh or reload the active Copilot surface.

### Full pack – personal scope

```bash
mkdir -p ~/.copilot/skills
cp -R agreeya-skills/skills/pymath  ~/.copilot/skills/pymath
cp -R agreeya-skills/skills/pystats ~/.copilot/skills/pystats
cp -R agreeya-skills/skills/pycheck ~/.copilot/skills/pycheck
```

### Single skill only

Copy only the folder you need, for example:

```bash
cp -R agreeya-skills/skills/pymath ~/.copilot/skills/pymath
# or
cp -R agreeya-skills/skills/pymath .github/skills/pymath
```

## Shell drop (local)

From the repository root:

```bash
# personal
./agreeya-skills/scripts/drop-pymath-pack.sh personal

# project (this repo)
./agreeya-skills/scripts/drop-pymath-pack.sh project "$(git rev-parse --show-toplevel)"
```

See [`../../scripts/drop-pymath-pack.sh`](../../scripts/drop-pymath-pack.sh).

## Assisted install (Agent mode)

If you are using Copilot Chat in Agent mode, you can ask Copilot to do the file copy for you.

### Personal

Prompt:

```text
Install the pymath pack as personal skills from agreeya-skills/skills/.
Copy pymath, pystats, and pycheck into ~/.copilot/skills/<name>/ so each folder has SKILL.md at its root.
Do not copy docs/, scripts/, or pack-level markdown into the skills root.
```

Expected destination:

```text
~/.copilot/skills/pymath/
~/.copilot/skills/pystats/
~/.copilot/skills/pycheck/
```

### Project

Prompt:

```text
Install the pymath pack as project skills from agreeya-skills/skills/ into this repository's .github/skills/.
Copy pymath, pystats, and pycheck only. Preserve structure and relative links. Do not commit unless I ask.
```

Expected destination:

```text
.github/skills/pymath/
.github/skills/pystats/
.github/skills/pycheck/
```

Notes:

- This works only when Agent mode has permission to write to the target directory.
- You may be prompted to approve file operations.
- If home-directory or workspace writes are blocked, use the manual install steps above.
- Do not ask the agent to push or force-push without an explicit request.

## Verify

- **All surfaces:** each installed folder contains `SKILL.md`; folder name equals frontmatter `name`.
- **VS Code:** open **Chat: Open Customizations** → **Skills** and confirm `pymath` (and siblings). Explicit skills should also appear in the `/` menu.
- **Copilot CLI:** run `/skills reload`, then `/skills info pymath` (or `copilot skill list`).
- **GitHub-hosted surfaces / code review:** confirm project paths exist **on the active branch** and are committed.

Smoke test:

```text
/pymath How many minutes of downtime does a 99.9% SLA allow in a 30-day month?
```

## Notes

- Personal scope is not available to GitHub-hosted runtimes.
- Some environments recognize alternate skills roots, but this guide uses the canonical path for consistency.
- If a skill does not appear, metadata or folder naming is usually the first thing to check (`name` must match folder; `description` should state what and when).
- Do not transform these skills into `.github/agents/*.md` agent profiles – Agent Skills format is different.

# Platform adapter – GitHub Copilot (pymath)

## Surfaces

Primary: `vscode`, `copilot-cli`  
Also valid when present on branch: `github-cloud-agent`, `github-code-review`

Record which surface is active when behavior differs (especially code execution).

## Capability notes

| Need | Guidance |
|---|---|
| Pure arithmetic / formula | Works on all surfaces – no tools required |
| Unit conversion tables | Prefer in-skill reasoning; do not invent rare constants |
| Code execution (`python`, `sympy`, `numpy`) | Conditional – only if the surface exposes an approved shell/notebook and policy allows it |
| Web lookup of rates/limits | Conditional – only with approved tools; otherwise mark `OPEN` |
| Credentials | Never store or request secrets in the skill |

## Invocation

- Model may auto-select from `description` triggers.
- Explicit: `/pymath` or “use pymath” in agent chat.
- Keep `name: pymath` matching the folder name.

## Install paths

| Scope | Path |
|---|---|
| Project (preferred for shared repos / cloud agent) | `<repo>/.github/skills/pymath/` |
| Personal (local hosts only) | `~/.copilot/skills/pymath/` |

Canonical **source** (edit here first): `agreeya-skills/skills/pymath/` in this repository.

Do not treat personal install as available to GitHub-hosted agents. Commit project skills to the active branch for cloud/code-review use.

## Runtime behavior

1. Prefer no shell for L0–L2.
2. For L3–L4, ask or use available execution only when it improves correctness.
3. If shell is unavailable, stay on L2 hand method and state the limit.
4. Never set `allowed-tools: shell` in frontmatter without an explicit security decision recorded in `PROVENANCE.md`.

## Verification after install

- VS Code: Chat → Customizations → Skills → confirm `pymath`.
- Copilot CLI: `/skills reload` then `/skills info pymath`.
- Cloud agent: confirm `.github/skills/pymath/SKILL.md` exists on the branch.

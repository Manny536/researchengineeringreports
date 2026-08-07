# Install on Copilot in SharePoint

## Install methods

✅ [Manual](#install-steps-manual)  
✅ [Assisted (chat based)](#assisted-install-chat)  
✅ [Zip (upload/attach)](#zip-install-chat-attachment)  

## What you need

- Site access with permission to create or manage SharePoint Copilot skills.
- Local source or zip of each skill folder.
- Note: shareable workplace output from these skills should stay plain (no internal framework marketing).

## Install path

Runtime path in SharePoint Agent Assets (repeat per skill):

```text
/AgentAssets/Skills/<skill-name>/SKILL.md
```

## Install steps (manual)

1. Open Copilot on your target SharePoint site.
2. Use the SharePoint skill creation flow (for example `create-skill`).
3. Use each skill's `SKILL.md` as the primary instructions source.
4. Add companion files under `/AgentAssets/Skills/<skill-name>/` with the same relative structure.

## Assisted install (chat)

Prompt (local source flow):

```text
Use create-skill to create SharePoint versions of pymath, pystats, and pycheck from agreeya-skills/skills.
```

Expected outcome:

- SharePoint skill folders at `/AgentAssets/Skills/pymath/` (and siblings).
- `SKILL.md` present; companion files available when the flow supports them.

When this fails:

- Verify site permissions and that `create-skill` is available in your tenant.
- Fall back to manual in-product steps.

## Zip install (chat attachment)

1. Attach a skill zip (single skill root with `SKILL.md`) in the create-skill flow when supported.
2. Confirm install path under Agent Assets.
3. Repeat per skill as needed.

## Verify

- Confirm skills appear for the site Copilot.
- Smoke: request a simple unit conversion or SLA minutes calc with `pymath`.

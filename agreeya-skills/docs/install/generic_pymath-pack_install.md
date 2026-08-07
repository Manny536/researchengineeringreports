# Generic install fallback

Use this only if your runtime is not covered by the platform pages.

## Install methods

✅ [Manual](#install-steps-manual)  
❌ Assisted (chat based)  
❌ Zip (native import)  

There is no reliable prompt/chat or native zip install method to document without platform-specific runtime details.

## What you need

- Local source: `agreeya-skills/skills/pymath/` (and optional `pystats/`, `pycheck/`).
- Or a zip extracted so each skill root has `SKILL.md`.
- The documented skills path for your runtime.

## Install steps (manual)

1. Find your runtime's official skills directory.
2. Create a folder named exactly `pymath` (and siblings as needed) in that skills directory.
3. Copy the full contents of each source skill folder into that folder.
4. Reload your runtime and invoke `pymath` explicitly.

## Verify

- Confirm the destination has `SKILL.md` at folder root.
- Confirm `pymath` appears in the runtime skills listing if available.

## If it still fails

- Recheck exact folder naming (`pymath`, `pystats`, `pycheck`).
- Confirm your runtime supports Agent Skills-compatible `SKILL.md` packages.
- Use a platform-specific page when available.

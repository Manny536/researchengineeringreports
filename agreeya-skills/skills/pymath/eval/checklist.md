# Eval checklist – pymath

Score each item pass/fail on a representative prompt set (see `examples/mundane-to-it.md`).

## Correctness

- [ ] Units consistent end-to-end
- [ ] Formula matches the typed question
- [ ] Arithmetic reverse-check passes
- [ ] No invented constants

## Custody / labels

- [ ] Typed question restated
- [ ] `KNOWN` / `COMPUTED` / `ASSUMED` / `OPEN` used correctly
- [ ] Assumptions explicit when present
- [ ] Conflicts surfaced instead of smoothed

## Method discipline

- [ ] Lowest sufficient ladder level used
- [ ] L3/L4 not used for simple arithmetic
- [ ] Tool use reported only when real

## Output quality

- [ ] Primary answer first with units
- [ ] Work section readable in under one minute
- [ ] Shareable text free of unrelated marketing/framework noise
- [ ] Stops at completion criteria

## Copilot packaging

- [ ] Folder name equals frontmatter `name`
- [ ] Description ≤ 1024 chars and includes triggers
- [ ] Relative links from `SKILL.md` resolve
- [ ] No secrets in the skill tree

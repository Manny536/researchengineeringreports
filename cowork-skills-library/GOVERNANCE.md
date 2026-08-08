# Governance — Cowork Skills Library

**Id:** `PEAICE-RER-COWORK-SKILLS-LIBRARY-001`  
**Importance:** High

## Rules

1. **Draft-only** — no skill sends mail, posts tickets, or approves change unless a future skill explicitly documents that power and the user requests it.
2. **Claim labels** — `KNOWN` / `COMPUTED` / `ASSUMED` / `STRUCTURAL ANALOGY` / `PROPOSED` / `OPEN`; never promote across handoffs.
3. **Selective routing** — outcome first; 2–5 skills max on compound work; stop at completion.
4. **Shareable language** — workplace-plain in user-facing drafts; no product spam or unsolicited lab marketing.
5. **Secrets** — never store credentials in skill trees.
6. **Source of truth**
   - Library skills: `cowork-skills-library/skills/<name>/`
   - Accuracy / Kakeya pack: `agreeya-skills/skills/<name>/`
   - Cowork runtime: `~/Documents/Cowork/skills/<name>/` (mirror only)
7. **Cowork.zip** — treat archives as evidence; do not mutate user archives in place when dropping.
8. **review-council** must not self-certify truth or close research OPEN claims.
9. **Sync** after edits:

```bash
./cowork-skills-library/scripts/drop-library-to-cowork.sh
./agreeya-skills/scripts/drop-pymath-pack.sh project "$(git rev-parse --show-toplevel)"
```

## Credits

AgreeYa skill-me · [@jim-duncan](https://github.com/jim-duncan) · PeAIce researchengineeringreports maintainers.

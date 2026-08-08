# Cowork Skills Library — Catalog

**Selective routing:** start from the user’s **outcome**. Activate only skills that address a concrete need. Prefer **2–5** skills on compound work. Stop at completion criteria.

## Meta / governance

| Skill | Triggers (examples) | Do NOT use when |
|---|---|---|
| **skill-router** | "which skill", "route this", "what should run" | User already named one skill |
| **claim-ledger** | "preserve labels", "handoff ledger", "don't promote OPEN" | Pure greenfield calc (use pymath) |
| **shareable-guard** | "make this shareable", "client-safe wording" | Need to send/post externally (still draft-only) |
| **evidence-receipt** | "evidence receipt", "audit trail for this run" | Casual chat with no deliverable |
| **rag-grounding** | "ground this", "retrieve evidence", "cite sources" | Inventing facts without retrieval access |
| **review-council** | "review this", "convene council", "stress-test" | Computing numbers (pymath) or single-figure audit (pycheck) |
| **kakeya-chain** | "coherence chain", "Prosody^", "run L2C scale stages" | Simple arithmetic without chain context |

## Accuracy / numeric

| Skill | Triggers | Do NOT use when |
|---|---|---|
| **pymath** | calculate, convert, SLA, D_2, C_x, Polyak, bit_length | Check *claimed* figure → pycheck; stats sample → pystats |
| **pycheck** | check my math, verify this number, audit D_2 claim | Greenfield compute → pymath |
| **pystats** | average, median, sample, aggregate runs | Pure arithmetic → pymath |

## Productivity drafts (AgreeYa-aligned)

| Skill | Triggers | Do NOT use when |
|---|---|---|
| **weekly-status-draft** | weekly status, Friday update, wins/risks | Meeting prep only → meeting-prep-brief |
| **meeting-prep-brief** | prep me for the meeting, talking points | Full weekly status → weekly-status-draft |
| **decision-inbox-draft** | draft a reply, decision needed, inbox triage | Status report or meeting brief as primary |

## Default compound recipes

| User outcome | Skills (order) |
|---|---|
| Accurate SLA number for a ticket note | pymath → shareable-guard |
| Someone’s figure looks wrong | pycheck → claim-ledger |
| Status email draft with a metric | weekly-status-draft → pymath (if needed) → shareable-guard |
| Coherence chain investigation | kakeya-chain → pymath → pycheck → review-council |
| Decision email with grounded facts | rag-grounding → decision-inbox-draft → shareable-guard |
| Multi-run depth summary | kakeya-chain (n runs) → pystats → evidence-receipt |

## Labels (all skills)

`KNOWN` · `COMPUTED` · `ASSUMED` · `STRUCTURAL ANALOGY` · `PROPOSED` · `OPEN`  

**Never promote across handoffs.** Draft-only: no send / post / approve.

---
name: rag-grounding
description: |-
  Retrieval-grounding driver: separate cited evidence from model recollection before
  elevating ASSUMED to KNOWN. Does not certify truth.

  Use when the user says:
    - "ground this"
    - "retrieve evidence"
    - "cite sources"
    - "don't invent"
    - "/rag-grounding"

  Do NOT use when:
    - no retrieval tools/corpus available and user needs pure calculation → pymath
    - auditing arithmetic only → pycheck
disable-model-invocation: false
---

# rag-grounding

High-level **RAG as Skill driver** (capability contract). Not a vector DB implementation.

## Capabilities

- Retrieve authorized evidence before elevating ASSUMED → KNOWN
- Cite sources on receipts
- Refuse silent promotion of OPEN
- Bound to authorized corpora only
- Separate retrieval hits from recollection

## Non-capabilities

- Does not certify truth
- Does not replace pycheck rebuild
- Does not close research OPEN claims
- No private-state / mind-reading

## Workflow

1. List claims needing grounding.
2. For each: search → quote/pointer → label `KNOWN` only if evidenced; else `OPEN`/`ASSUMED`.
3. Emit grounding table + handoff.

## Output

```markdown
## Claims
## Grounding table
| claim | source | label |
## Still OPEN
## handoff
```

## Guardrails

1. No fabricated citations.  
2. Draft-only.  
3. Labels never promote without new evidence.

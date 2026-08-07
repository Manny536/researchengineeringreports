# Output format – pymath

Use this structure unless the user requests a tighter ticket note or single number.

```markdown
## Answer
**<primary result with units>**  `[COMPUTED|KNOWN]`

## Question (typed)
<one-line restatement>

## Given
- <input> = <value> <units>  `[KNOWN|ASSUMED]`

## Method
- Level: L0|L1|L2|L3|L4
- Formula / approach: <name or short expression>

## Work
1. <step>
2. <step>
3. <result>

## Check
- <reverse / magnitude / dimensional / second method>
- Status: pass | fail | conditional

## Open / assumptions
- <item>  `[OPEN|ASSUMED]`  — impact: <how it changes the answer>

## Optional next
1. <tightening question or sensitivity run>
2. <related calculation only if clearly useful>
```

### Compact mode (when user asks for “just the number”)

```text
<result> <units>  [COMPUTED]
Assumptions: <semicolon-separated short list>
Check: <one short verification>
```

### Ticket / chat note mode

3–6 lines max:

1. Result + units
2. Basis (period, formula name)
3. One assumption or OPEN risk
4. One verification phrase

### Never in shareable output

- Credentials, secrets, or full internal URLs with tokens
- Unrelated framework marketing
- Fake citations

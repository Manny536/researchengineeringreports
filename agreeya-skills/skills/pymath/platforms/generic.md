# Platform adapter – generic (pymath)

Use when the runtime is not confirmed as GitHub Copilot.

## Behavior

1. Apply the same method ladder and accuracy rules.
2. Do not assume shell, MCP, or web tools exist.
3. Prefer hand-verified L0–L2 methods.
4. If tools appear available, treat them as conditional and report when used.

## Output

Same [`references/output-format.md`](../references/output-format.md). Prefer compact mode in constrained chat UIs.

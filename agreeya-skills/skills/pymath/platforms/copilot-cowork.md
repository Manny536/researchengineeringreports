# Platform adapter – Copilot Cowork (pymath)

## Surfaces

Microsoft Copilot Cowork (OneDrive-backed skills under `Documents/Cowork/skills/pymath/`).

## Capability notes

| Need | Guidance |
|---|---|
| Code execution | Prefer host `python` / Bash when exposed – required for non-trivial COMPUTED figures |
| Workbook values | Use range tools (`core-GetRange` or tenant equivalent) – do not invent cell values |
| Mail/files context | Use approved Search M365 / workspace tools only |
| Power BI | Query tools when the measure is the source of a KNOWN input |
| Secrets | Never store credentials in the skill |

## Install path

```text
~/Documents/Cowork/skills/pymath/
```

From cloned researchengineeringreports:

```bash
./agreeya-skills/scripts/drop-to-cowork.sh pymath
```

See [`../../../docs/install/COPILOT-COWORK-CLONE-DROP.md`](../../../docs/install/COPILOT-COWORK-CLONE-DROP.md).

## Risk notes (quality report)

Cowork health may flag **high** risk (autonomy / sensitive data touch). Stay draft-only; ground every number; no send/approve.

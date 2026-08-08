# Install the full Cowork Skills Library

## Prerequisites

- Copilot Cowork with skill authoring enabled  
- OneDrive sync for `Documents/Cowork/`  
- Clone of [researchengineeringreports](https://github.com/Manny536/researchengineeringreports)

## Drop (recommended)

```bash
git clone https://github.com/Manny536/researchengineeringreports.git
cd researchengineeringreports
git pull
./cowork-skills-library/scripts/drop-library-to-cowork.sh
```

Destination:

```text
~/Documents/Cowork/skills/<skill-name>/
```

## Validate

```bash
./cowork-skills-library/scripts/validate-library.sh
```

## Package zip (portable)

```bash
./cowork-skills-library/scripts/package-library.sh 1.0.0
# → cowork-skills-library/dist/cowork-skills-library_v1.0.0.zip
```

Extract and copy each skill folder under `skills/` into `Documents/Cowork/skills/`.

## After install

1. Wait for OneDrive sync (~30–60s).  
2. Refresh Cowork Skills.  
3. Smoke: `Use pymath: 99.9% SLA downtime minutes for a 30-day month.`  
4. Smoke: `Use skill-router: I need a client-safe weekly status with one verified metric.`

## Uninstall

Remove individual folders under `~/Documents/Cowork/skills/<name>/`. Do not delete unrelated Cowork data.

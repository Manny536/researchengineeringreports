# PeAIce Research Engineering Reports

Static landing repository for the PeAIce / Love Labs LCA research engineering report stack.

This repo is built around the **L²_C cross model continuity and jailbreak governance study**. The root `index.html` is the public site layer intended for GitHub Pages and eventual redirect into `peaice.org`.

## Live report stack

| Layer | Report | Role |
|---|---|---|
| v1.0 | [Cross Model Continuity and Jailbreak Governance Study](https://docs.google.com/document/d/1wlnFq3-u5To-fR7BODjgJJ_qdPjyF1WxtKT1SeXOZpQ/edit?usp=sharing) | Top synthesis over jailbreak governance, access disruption, Claude Opus 4.8 review, and cross model continuity |
| v0.6 | [Verification Integrity Correction](https://docs.google.com/document/d/1_MX6B1H9HD6t3hLA022VWexHfR67Ml0GLy5BblyKNBM/edit?usp=sharing) | Correction layer over the v0.5 verification claim, with the 55-test acceptance surface |
| v0.5 | [Cross Agent Probe Deepening](https://docs.google.com/document/d/1rjabazy9BvZc8HOo7Lf45N9eDWwZpeucz14ya8MtMdU/edit?usp=sharing) | Original cross-agent architecture, CoWork attribution, deterministic tie-break, and transfer contract |

## Public portals

- [peaice.org](https://peaice.org)
- [lovelabslca.com](https://lovelabslca.com)
- [Anthropic Fable/Mythos access statement](https://www.anthropic.com/news/fable-mythos-access)

## Core thesis

Model access can become discontinuous. Research continuity has to sit above any one model, vendor, tenant, or chat surface.

This repository turns the PeAIce work packet into a static, redirectable site:

- code and tests remain the executable contract
- report layers preserve the human ledger
- Google Docs preserve the public study surfaces
- `index.html` becomes the routing layer
- `README.md` records the repository contract

## L²_C probe surface

The study centers the finite-dimensional protected-sector probe:

```text
L²_C(ψ,t) = ‖P_C exp(-itH_T) ψ‖²
h         = ‖(I-P_C) H_T P_C‖
β_C       = Δ / (Δ + h + ε)
β(T)      = 1 - T^(-γ)
E_{β,T}   = β(T) · T · ‖Xf‖²
T*        = (1 - hη)^(-1/γ)
```

Current acceptance surface:

```bash
python -m pytest test_l2c_probe.py test_l2c_probe_leakage.py -q
# 55 passed
```

The 55-test packet is defined as:

- 49 original tests for construction, protected-sector selection, metrics, evolution, β-dynamic methods, and report payloads
- 6 leakage-regime tests that drive `h > 0`, produce real L²_C decay, and document the custom-projector / spectral-gap inconsistency

## Verification integrity rule

Every reported `N passed` result must carry:

- exact command
- interpreter version
- NumPy version
- SciPy version
- pytest version
- runner identity

Otherwise the result is marked `authored-not-run`.

## GitHub Pages deployment

Use the repository root:

```text
Settings → Pages → Deploy from branch → main → /root
```

Root files:

```text
index.html
README.md
LICENSE
```

After Pages is enabled, point the desired `peaice.org` route or subdomain at the GitHub Pages deployment.

## Repo role

`researchengineeringreports` is the public report index for PeAIce research engineering. It is not just a file dump. It is the continuity layer for cross-agent, cross-model, and cross-platform research transfer.

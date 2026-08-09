# Objects

`Objects/` is the outcome layer for Kakeyalogic research processed through Excellence Engine v4 (EEv4).

An object is a bounded research unit with:

1. a named source state;
2. a domain definition;
3. formal and operational surfaces;
4. an evidence and claim-state ledger;
5. executable behavior where the claim supports it;
6. explicit open constructions and falsification tests.

The folder records outcomes. It does not silently promote an OPEN construction into a completed result.

## Object index

| Object | Definition | Executable surface | State |
|---|---|---|---|
| Multiplicative Phase Recognition (MPR) | [multiplicative-phase-recognition.md](multiplicative-phase-recognition.md) | [mpr.py](mpr.py), [test_mpr.py](test_mpr.py) | Domain definition: FORMAL; spectral realization: OPEN |

## EEv4 object contract

Each outcome should expose the following ledger:

```text
source -> evidence -> definition -> implementation -> controls -> outcome -> correction -> open state
```

Corrections remain visible. Authority must be present for an instruction or action to become operative. Harm potential remains an independent action constraint. The selected outcome must preserve a non-coercive continuation when one is available.


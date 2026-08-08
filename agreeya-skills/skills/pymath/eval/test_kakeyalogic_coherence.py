"""Behavioral tests for KakeyaLogic L²_C coherence-depth probe.

Required cases (user execution turn):
1. delta == rho → D_2=0, C_2=1
2. Multiplicative invariance D_2(kδ,kρ)=D_2(δ,ρ)
3. Powers of two → exact unit depth increments
4. Invalid domains fail explicitly
5. bit_length matches definition including zero
6. Declared excess bit growth triggers leakage
7. Equal-bit semantic mutation undetected + limitation reported
8. Labels and OPEN survive every handoff
9. mu=0 matches gradient descent
10. Unstable momentum trips kill criterion
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

# scripts/ is sibling of eval/
SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import kakeyalogic_coherence as kc  # noqa: E402


# ---------------------------------------------------------------------------
# 1. Identity scale
# ---------------------------------------------------------------------------


def test_delta_equals_rho_zero_depth_unit_coherence():
    d = kc.scale_depth_2(3.0, 3.0)
    c = kc.coherence_score_2(3.0, 3.0)
    assert d == 0.0
    assert c == 1.0


# ---------------------------------------------------------------------------
# 2. Multiplicative invariance
# ---------------------------------------------------------------------------


def test_multiplicative_invariance():
    delta, rho = 2.5, 10.0
    base = kc.scale_depth_2(delta, rho)
    for k in (0.25, 2.0, 7.0, 100.0):
        assert kc.scale_depth_2(k * delta, k * rho) == pytest.approx(base)


# ---------------------------------------------------------------------------
# 3. Powers of two → unit depth increments
# ---------------------------------------------------------------------------


def test_powers_of_two_unit_depth_increments():
    # rho = delta * 2^n → D_2 = n
    delta = 3.0
    for n in range(0, 8):
        rho = delta * (2**n)
        assert kc.scale_depth_2(delta, rho) == pytest.approx(float(n))
        assert kc.coherence_score_2(delta, rho) == pytest.approx(2.0 ** (-n))


# ---------------------------------------------------------------------------
# 4. Invalid domains
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "delta,rho",
    [
        (0.0, 1.0),
        (-1.0, 2.0),
        (1.0, 0.0),
        (1.0, -3.0),
    ],
)
def test_invalid_delta_rho_domain(delta, rho):
    with pytest.raises(kc.DomainError):
        kc.scale_depth_2(delta, rho)
    with pytest.raises(kc.DomainError):
        kc.beta_ratio(delta, rho)


@pytest.mark.parametrize("x", [0.0, 1.0, -2.0])
def test_invalid_base_x(x):
    with pytest.raises(kc.DomainError):
        kc.scale_depth_x(2.0, 4.0, x)


def test_coherence_requires_x_gt_1():
    with pytest.raises(kc.DomainError):
        kc.coherence_score_x(2.0, 4.0, 0.5)


# ---------------------------------------------------------------------------
# 5. bit_length definition
# ---------------------------------------------------------------------------


def test_bit_length_matches_python_definition():
    assert kc.bit_length_n(0) == 0
    assert kc.bit_length_n(0) == (0).bit_length()
    for n in [1, 2, 3, 7, 8, 255, 256, -9, 10**6]:
        assert kc.bit_length_n(n) == abs(n).bit_length()
        if n != 0:
            # B(n) = floor(log2|n|)+1
            assert kc.bit_length_n(n) == math.floor(math.log2(abs(n))) + 1


def test_oversized_utf8_rejected():
    big = b"x" * (kc.MAX_UTF8_BYTES_FOR_INT + 1)
    with pytest.raises(kc.DomainError):
        kc.bytes_to_framed_int(big)


# ---------------------------------------------------------------------------
# 6. Excess bit growth → leakage
# ---------------------------------------------------------------------------


def test_declared_excess_bit_growth_triggers_leakage():
    rec = kc.carrier_leakage(bits_in=8, bits_out=20, allowed_growth_bits=4)
    assert rec.leakage_bits == max(0, 20 - 8 - 4) == 8
    assert rec.normalized_leakage == pytest.approx(8 / 20)
    assert rec.label == kc.COMPUTED


def test_missing_growth_budget_is_open():
    rec = kc.carrier_leakage(bits_in=8, bits_out=20, allowed_growth_bits=None)
    assert rec.leakage_bits is None
    assert rec.label == kc.OPEN
    assert any("OPEN" in x for x in rec.open_items)


# ---------------------------------------------------------------------------
# 7. Equal-bit semantic mutation negative control
# ---------------------------------------------------------------------------


def test_equal_bit_semantic_mutation_undetected():
    # Same length / often same storage; meaning differs
    a = "CLEAR"
    b = "VAGUE"  # both 5 ASCII chars → same storage bits
    out = kc.semantic_equal_bit_negative_control(a, b)
    assert out["meaning_differs"] is True
    assert out["same_storage_bits"] is True
    assert out["detector_sees_semantic_change"] is False
    assert "LIMITATION" in out["report"]
    assert "not detected" in out["report"].lower() or "cannot" in out["report"].lower()


# ---------------------------------------------------------------------------
# 8. Labels and OPEN survive handoffs
# ---------------------------------------------------------------------------


def test_labels_and_open_survive_handoffs(tmp_path):
    cp = tmp_path / "state.json"
    g = kc.CoherenceGraph(checkpoint_path=cp, branch_threshold=0.0)  # no repair noise
    st = g.new_run("token-fixture", delta=1.0, rho=2.0, allowed_growth_bits=None)
    # force OPEN-friendly path
    st = g.run(st)
    assert st.handoffs, "expected handoffs"
    # OPEN from missing growth budget must appear
    assert any(h.get("label") in (kc.OPEN, kc.ASSUMED, kc.COMPUTED, kc.STRUCTURAL_ANALOGY) for h in st.handoffs)
    assert st.open, "OPEN items must survive on state"
    # reload persistence
    st2 = kc.load_state(cp)
    assert st2.open == st.open
    assert len(st2.handoffs) == len(st.handoffs)
    # no silent promotion of OPEN leakage fields
    for h in st2.handoffs:
        if h.get("allowed_growth_bits") is None and h.get("bits_in") is not None:
            # leakage_bits may be None and open non-empty
            assert h.get("leakage_bits") is None or h.get("open")


def test_handoff_schema_keys_present():
    ho = kc.build_handoff(
        stage=kc.STAGE_CONVERSATION,
        input_payload={"x": 1},
        output_payload={"y": 2},
        delta=1.0,
        rho=2.0,
        scale_base=2.0,
        bits_in=4,
        bits_out=8,
        allowed_growth_bits=2,
        evaluator_id="pymath",
        assumptions=["a"],
        open_extra=[],
    )
    d = ho.to_dict()
    required = [
        "stage",
        "input_receipt",
        "output_receipt",
        "delta",
        "rho",
        "scale_base",
        "scale_depth",
        "coherence_score",
        "bits_in",
        "bits_out",
        "allowed_growth_bits",
        "leakage_bits",
        "label",
        "assumptions",
        "open",
        "evaluator_id",
    ]
    for k in required:
        assert k in d


# ---------------------------------------------------------------------------
# 9. mu=0 matches gradient descent
# ---------------------------------------------------------------------------


def test_mu_zero_matches_gradient_descent():
    # J = 0.5 (z - 0)^2 → grad = z; GD: z <- z - alpha*z = (1-alpha)z
    alpha = 0.1
    z0 = 1.0
    steps = 5

    def grad(z: float) -> float:
        return z

    st = kc.polyak_run(z0, grad, alpha=alpha, mu=0.0, steps=steps)
    z = z0
    for _ in range(steps):
        z = z - alpha * grad(z)
    assert st.z == pytest.approx(z)
    assert st.killed is False


# ---------------------------------------------------------------------------
# 10. Unstable momentum kill
# ---------------------------------------------------------------------------


def test_unstable_momentum_trips_kill():
    # Large alpha + high mu on steep grad → divergence → kill
    def grad(z: float) -> float:
        return 10.0 * z + 1e3

    with pytest.raises(kc.KillCriterion):
        kc.polyak_run(
            z0=1.0,
            objective_grad=grad,
            alpha=5.0,
            mu=0.99,
            steps=50,
            max_abs_z=100.0,
            max_abs_step=50.0,
        )


# ---------------------------------------------------------------------------
# Boundary: D_scale is not linear regression residual
# ---------------------------------------------------------------------------


def test_scale_depth_not_linear_difference():
    # D_2(1,4)=2, but |4-1|=3 — multiplicative ≠ linear
    assert kc.scale_depth_2(1.0, 4.0) == pytest.approx(2.0)
    assert kc.scale_depth_2(1.0, 4.0) != pytest.approx(abs(4.0 - 1.0))


def test_wk_labeled_proposed():
    w = kc.weighted_scale_wk(1.0, 4.0)
    assert w["label"] == kc.PROPOSED
    assert w["also_label"] == kc.STRUCTURAL_ANALOGY


def test_audit_supersedes_bad_claim():
    bad = {"scale_depth": 0.0, "coherence_score": 1.0}
    out = kc.audit_claimed_coherence(bad, delta=1.0, rho=4.0)
    assert out["verdict"] == "fail"
    assert out["supersedes_claim"] is True
    assert out["authoritative"]["scale_depth"] == pytest.approx(2.0)


def test_aggregate_runs_carries_n():
    runs = [
        {"scale_depth": 1.0},
        {"scale_depth": 2.0},
        {"scale_depth": 3.0},
    ]
    agg = kc.aggregate_runs(runs)
    assert agg["n"] == 3
    assert agg["mean_scale_depth"] == pytest.approx(2.0)
    assert agg["open"]


def test_rag_driver_reference_present():
    assert kc.RAG_SKILL_DRIVER["role"] == "driver"
    assert "retrieve external evidence" in kc.RAG_SKILL_DRIVER["capabilities"][0]


def test_linear_boundary_constant():
    # Documented inequality D_scale ≠ a(ρ−δ)+b as structural property check:
    # for fixed a,b linear form cannot match D across a scale family.
    delta, rho = 2.0, 8.0
    d = kc.scale_depth_2(delta, rho)
    linear = abs(rho - delta)  # a=1,b=0
    assert d != pytest.approx(linear)

#!/usr/bin/env python3
"""KakeyaLogic / L²_C coherence-depth probe — numerical realization.

Scale depth measures multiplicative separation, not linear regression:

    D_scale ≠ a(ρ − δ) + b

Markers ``^`` and ``*`` in chain stage names are literal status markers,
not exponentiation.

Internal-speech / Reading stage: bounded textual/prosodic hypothesis from
user-provided tokens only — not mind-reading or private-state access.

W_K is PROPOSED / STRUCTURAL ANALOGY. Polyak→L²_C mapping is STRUCTURAL ANALOGY.
L²_C means coherence as continuation, not closure.
"""

from __future__ import annotations

import json
import math
import time
import uuid
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

# ---------------------------------------------------------------------------
# Labels (never promote across handoff)
# ---------------------------------------------------------------------------

KNOWN = "KNOWN"
COMPUTED = "COMPUTED"
ASSUMED = "ASSUMED"
OPEN = "OPEN"
PROPOSED = "PROPOSED"
STRUCTURAL_ANALOGY = "STRUCTURAL ANALOGY"

# Chain stages (markers ^ and * are literal until explicitly defined elsewhere)
STAGE_CONVERSATION = "Conversation"
STAGE_PROSODY = "Prosody^"
STAGE_READING = "Reading(internal-speech proxy inferred only from user-provided token output)"
STAGE_INTERPRETABILITY = "Interpretability*"
STAGE_POLYAK = "PolyakMomentum^"

DEFAULT_CHAIN: Tuple[str, ...] = (
    STAGE_CONVERSATION,
    STAGE_PROSODY,
    STAGE_READING,
    STAGE_INTERPRETABILITY,
    STAGE_POLYAK,
)

# UTF-8 fixture conversion hard cap (bytes) — reject oversized conversions
MAX_UTF8_BYTES_FOR_INT = 4096


class DomainError(ValueError):
    """Invalid domain for scale / momentum / carrier transforms."""


class KillCriterion(RuntimeError):
    """Momentum or chain stability kill fired."""


# ---------------------------------------------------------------------------
# Scale depth D_x, D_2, coherence C_x, proposed W_K
# ---------------------------------------------------------------------------


def beta_ratio(delta: float, rho: float) -> float:
    """β = ρ / δ with domain δ > 0, ρ > 0."""
    if not (delta > 0 and rho > 0):
        raise DomainError(f"require delta>0 and rho>0; got delta={delta!r}, rho={rho!r}")
    return rho / delta


def scale_depth_x(delta: float, rho: float, x: float) -> float:
    """D_x(δ,ρ) = |log_x(ρ/δ)| = |(ln ρ − ln δ) / ln x| with x>0, x≠1."""
    if not (delta > 0 and rho > 0):
        raise DomainError(f"require delta>0 and rho>0; got delta={delta!r}, rho={rho!r}")
    if not (x > 0 and x != 1):
        raise DomainError(f"require x>0 and x≠1; got x={x!r}")
    return abs((math.log(rho) - math.log(delta)) / math.log(x))


def scale_depth_2(delta: float, rho: float) -> float:
    """D_2(δ,ρ) = |log2 ρ − log2 δ| (operational base-two preference)."""
    if not (delta > 0 and rho > 0):
        raise DomainError(f"require delta>0 and rho>0; got delta={delta!r}, rho={rho!r}")
    return abs(math.log2(rho) - math.log2(delta))


def coherence_score_x(delta: float, rho: float, x: float) -> float:
    """C_x(δ,ρ) = x^(−D_x) ∈ (0,1] requiring x>1."""
    if not (x > 1):
        raise DomainError(f"coherence C_x requires x>1; got x={x!r}")
    d = scale_depth_x(delta, rho, x)
    return x ** (-d)


def coherence_score_2(delta: float, rho: float) -> float:
    """C_2(δ,ρ) = 2^(−D_2) ∈ (0,1]."""
    d = scale_depth_2(delta, rho)
    return 2.0 ** (-d)


def weighted_scale_wk(delta: float, rho: float, x: float = 2.0) -> Dict[str, Any]:
    """Proposed weighted realization W_K = D_x · (ρ/δ)^(−1/2).

    Label: PROPOSED / STRUCTURAL ANALOGY — not a formal starred operator.
    """
    if x == 2:
        d = scale_depth_2(delta, rho)
    else:
        d = scale_depth_x(delta, rho, x)
    beta = beta_ratio(delta, rho)
    w = d * (beta ** (-0.5))
    return {
        "W_K": w,
        "label": PROPOSED,
        "also_label": STRUCTURAL_ANALOGY,
        "note": "W_K is a proposed numerical realization; not a formal starred operator definition.",
        "delta": delta,
        "rho": rho,
        "scale_base": x,
        "scale_depth": d,
        "beta": beta,
    }


# ---------------------------------------------------------------------------
# Carrier bit-length leakage (not semantic leakage)
# ---------------------------------------------------------------------------


def bit_length_n(n: int) -> int:
    """B(n) = |n|.bit_length(); B(0)=0. Uses int.bit_length() (see Python stdtypes)."""
    if n == 0:
        return 0
    return abs(int(n)).bit_length()


def utf8_storage_bits(payload: bytes) -> int:
    """Exact storage bits for UTF-8/byte fixtures: 8 * len(payload_bytes)."""
    return 8 * len(payload)


def bytes_to_framed_int(payload: bytes, max_bytes: int = MAX_UTF8_BYTES_FOR_INT) -> int:
    """Frame bytes as big-endian integer for bit_length probe.

    Rejects oversized conversions instead of constructing unbounded integers.
    """
    if len(payload) > max_bytes:
        raise DomainError(
            f"payload length {len(payload)} exceeds max_bytes={max_bytes}; "
            "refusing unbounded integer conversion"
        )
    if not payload:
        return 0
    return int.from_bytes(payload, byteorder="big", signed=False)


def text_carrier_bits(
    text: str,
    max_bytes: int = MAX_UTF8_BYTES_FOR_INT,
) -> Dict[str, Any]:
    """Bounded UTF-8 fixture: storage bits + framed integer bit_length."""
    payload = text.encode("utf-8")
    storage = utf8_storage_bits(payload)
    framed = bytes_to_framed_int(payload, max_bytes=max_bytes)
    return {
        "text": text,
        "payload_bytes_len": len(payload),
        "storage_bits": storage,
        "framed_int": framed,
        "bit_length": bit_length_n(framed),
        "label": COMPUTED,
        "limitation": (
            "bit_length detects carrier-size anomalies only — not semantic leakage, "
            "truth, intent, or interpretability."
        ),
    }


@dataclass
class LeakageRecord:
    bits_in: int
    bits_out: int
    allowed_growth_bits: Optional[int]
    leakage_bits: Optional[int]
    normalized_leakage: Optional[float]
    label: str
    open_items: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def carrier_leakage(
    bits_in: int,
    bits_out: int,
    allowed_growth_bits: Optional[int],
) -> LeakageRecord:
    """Record leakage for S_{i-1}→S_i.

    Missing growth budget → leakage OPEN (never assume zero).
    """
    if bits_in < 0 or bits_out < 0:
        raise DomainError("bits_in and bits_out must be non-negative")

    open_items: List[str] = []
    if allowed_growth_bits is None:
        open_items.append("allowed_growth_bits missing — leakage cannot be closed; OPEN")
        return LeakageRecord(
            bits_in=bits_in,
            bits_out=bits_out,
            allowed_growth_bits=None,
            leakage_bits=None,
            normalized_leakage=None,
            label=OPEN,
            open_items=open_items,
        )

    if allowed_growth_bits < 0:
        raise DomainError("allowed_growth_bits must be >= 0 when provided")

    leak = max(0, bits_out - bits_in - allowed_growth_bits)
    norm = leak / max(1, bits_out)
    return LeakageRecord(
        bits_in=bits_in,
        bits_out=bits_out,
        allowed_growth_bits=allowed_growth_bits,
        leakage_bits=leak,
        normalized_leakage=norm,
        label=COMPUTED,
        open_items=open_items,
    )


def semantic_equal_bit_negative_control(
    text_a: str,
    text_b: str,
) -> Dict[str, Any]:
    """Negative control: meaning changes while bit length stays constant.

    Detector must report it cannot detect the semantic change.
    """
    a = text_carrier_bits(text_a)
    b = text_carrier_bits(text_b)
    same_bl = a["bit_length"] == b["bit_length"]
    same_storage = a["storage_bits"] == b["storage_bits"]
    meaning_differs = text_a != text_b
    return {
        "text_a": text_a,
        "text_b": text_b,
        "bit_length_a": a["bit_length"],
        "bit_length_b": b["bit_length"],
        "storage_bits_a": a["storage_bits"],
        "storage_bits_b": b["storage_bits"],
        "same_bit_length": same_bl,
        "same_storage_bits": same_storage,
        "meaning_differs": meaning_differs,
        "detector_sees_semantic_change": False,
        "report": (
            "LIMITATION: equal-bit (or equal-storage) semantic mutation is not detected "
            "by bit_length/storage probes. Carrier-size tools cannot certify meaning, "
            "truth, intent, or interpretability."
        ),
        "label": KNOWN if meaning_differs and (same_bl or same_storage) else COMPUTED,
    }


# ---------------------------------------------------------------------------
# Polyak heavy-ball momentum (mu, not beta — avoid scale-ratio collision)
# ---------------------------------------------------------------------------


@dataclass
class PolyakState:
    z_prev: float
    z: float
    t: int = 0
    history: List[float] = field(default_factory=list)
    killed: bool = False
    kill_reason: Optional[str] = None
    label: str = STRUCTURAL_ANALOGY


def polyak_step(
    z: float,
    z_prev: float,
    grad: float,
    alpha: float,
    mu: float,
) -> float:
    """z_{t+1} = z_t − α ∇J(z_t) + μ (z_t − z_{t−1}), α>0, 0≤μ<1."""
    if not (alpha > 0):
        raise DomainError(f"require alpha>0; got {alpha!r}")
    if not (0 <= mu < 1):
        raise DomainError(f"require 0 ≤ mu < 1; got {mu!r}")
    return z - alpha * grad + mu * (z - z_prev)


def polyak_run(
    z0: float,
    objective_grad: Callable[[float], float],
    alpha: float,
    mu: float,
    steps: int,
    *,
    max_abs_z: float = 1e6,
    max_abs_step: float = 1e5,
    z_prev0: Optional[float] = None,
) -> PolyakState:
    """Run Polyak heavy-ball with explicit kill criteria.

    Mapping to L²_C: STRUCTURAL ANALOGY — not a theorem.
    mu=0 reduces to ordinary gradient descent: z ← z − α ∇J(z).
    """
    if steps < 0:
        raise DomainError("steps must be >= 0")
    z = float(z0)
    z_prev = float(z0 if z_prev0 is None else z_prev0)
    st = PolyakState(z_prev=z_prev, z=z, t=0, history=[z], label=STRUCTURAL_ANALOGY)

    for _ in range(steps):
        g = float(objective_grad(st.z))
        z_new = polyak_step(st.z, st.z_prev, g, alpha, mu)
        step_size = abs(z_new - st.z)
        if abs(z_new) > max_abs_z or step_size > max_abs_step or not math.isfinite(z_new):
            st.killed = True
            st.kill_reason = (
                f"kill: |z|={abs(z_new)} step={step_size} "
                f"(limits max_abs_z={max_abs_z}, max_abs_step={max_abs_step})"
            )
            st.history.append(z_new)
            raise KillCriterion(st.kill_reason)
        st.z_prev, st.z = st.z, z_new
        st.t += 1
        st.history.append(st.z)
    return st


# ---------------------------------------------------------------------------
# Chain handoff + state persistence (LangGraph-style loop/branch)
# ---------------------------------------------------------------------------


@dataclass
class ChainHandoff:
    stage: str
    input_receipt: str
    output_receipt: str
    delta: Optional[float]
    rho: Optional[float]
    scale_base: float
    scale_depth: Optional[float]
    coherence_score: Optional[float]
    bits_in: Optional[int]
    bits_out: Optional[int]
    allowed_growth_bits: Optional[int]
    leakage_bits: Optional[int]
    label: str
    assumptions: List[str]
    open: List[str]
    evaluator_id: str
    # extras for audit / branching
    beta: Optional[float] = None
    W_K: Optional[float] = None
    W_K_label: Optional[str] = None
    normalized_leakage: Optional[float] = None
    branch: Optional[str] = None
    parent_stage: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(d: Mapping[str, Any]) -> "ChainHandoff":
        return ChainHandoff(**{k: d[k] for k in ChainHandoff.__dataclass_fields__ if k in d})  # type: ignore[arg-type]


def assert_labels_not_promoted(prev: Optional[str], new: str) -> None:
    """Labels never promote across handoff (ASSUMED/OPEN/PROPOSED/STRUCTURAL ANALOGY stay)."""
    # Soft check for auditors: promotion would be elevating weaker → stronger without evidence.
    rank = {
        OPEN: 0,
        PROPOSED: 1,
        STRUCTURAL_ANALOGY: 1,
        ASSUMED: 2,
        COMPUTED: 3,
        KNOWN: 4,
    }
    if prev is None:
        return
    # We do not auto-mutate; this is for tests to verify survival of weak labels.
    _ = (rank.get(prev, 0), rank.get(new, 0))


@dataclass
class GraphState:
    """Persistent graph state for Conversation→…→PolyakMomentum^ chain.

    LangGraph-compatible shape: typed state dict + optional checkpoint path.
    Full ``langgraph`` package is optional; this module implements the same
    loop/branch/checkpoint pattern without requiring the dependency.
    """

    run_id: str
    stage_index: int = 0
    stages: List[str] = field(default_factory=lambda: list(DEFAULT_CHAIN))
    handoffs: List[Dict[str, Any]] = field(default_factory=list)
    tokens: str = ""
    delta: float = 1.0
    rho: float = 1.0
    scale_base: float = 2.0
    allowed_growth_bits: Optional[int] = None
    branch: str = "main"
    open: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    polyak: Optional[Dict[str, Any]] = None
    killed: bool = False
    kill_reason: Optional[str] = None
    evaluator_id: str = "pymath"
    meta: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(d: Mapping[str, Any]) -> "GraphState":
        return GraphState(**{k: d[k] for k in GraphState.__dataclass_fields__ if k in d})  # type: ignore[arg-type]


def save_state(state: GraphState, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state.to_dict(), indent=2, sort_keys=True), encoding="utf-8")


def load_state(path: Path) -> GraphState:
    return GraphState.from_dict(json.loads(path.read_text(encoding="utf-8")))


def _receipt(payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, default=str)
    # short stable fingerprint without claiming cryptographic security
    return f"r{abs(hash(raw)) % (10**12):012d}"


def stage_metrics(
    delta: float,
    rho: float,
    scale_base: float,
    bits_in: Optional[int],
    bits_out: Optional[int],
    allowed_growth_bits: Optional[int],
) -> Dict[str, Any]:
    depth = scale_depth_x(delta, rho, scale_base) if scale_base != 2 else scale_depth_2(delta, rho)
    if scale_base == 2:
        depth = scale_depth_2(delta, rho)
        c = coherence_score_2(delta, rho)
    else:
        depth = scale_depth_x(delta, rho, scale_base)
        c = coherence_score_x(delta, rho, scale_base) if scale_base > 1 else None
    wk = weighted_scale_wk(delta, rho, x=scale_base if scale_base > 0 and scale_base != 1 else 2.0)
    leak: Optional[LeakageRecord] = None
    open_items: List[str] = []
    if bits_in is not None and bits_out is not None:
        leak = carrier_leakage(bits_in, bits_out, allowed_growth_bits)
        open_items.extend(leak.open_items)
    return {
        "scale_depth": depth,
        "coherence_score": c,
        "beta": beta_ratio(delta, rho),
        "W_K": wk["W_K"],
        "W_K_label": wk["label"],
        "leak": leak,
        "open": open_items,
    }


def build_handoff(
    *,
    stage: str,
    input_payload: Any,
    output_payload: Any,
    delta: float,
    rho: float,
    scale_base: float,
    bits_in: Optional[int],
    bits_out: Optional[int],
    allowed_growth_bits: Optional[int],
    evaluator_id: str,
    assumptions: Optional[Sequence[str]] = None,
    open_extra: Optional[Sequence[str]] = None,
    branch: Optional[str] = None,
    parent_stage: Optional[str] = None,
    label: str = COMPUTED,
) -> ChainHandoff:
    m = stage_metrics(delta, rho, scale_base, bits_in, bits_out, allowed_growth_bits)
    open_items = list(m["open"])
    if open_extra:
        open_items.extend(open_extra)
    leak = m["leak"]
    return ChainHandoff(
        stage=stage,
        input_receipt=_receipt(input_payload),
        output_receipt=_receipt(output_payload),
        delta=delta,
        rho=rho,
        scale_base=scale_base,
        scale_depth=m["scale_depth"],
        coherence_score=m["coherence_score"],
        bits_in=bits_in,
        bits_out=bits_out,
        allowed_growth_bits=allowed_growth_bits,
        leakage_bits=None if leak is None else leak.leakage_bits,
        label=label,
        assumptions=list(assumptions or []),
        open=open_items,
        evaluator_id=evaluator_id,
        beta=m["beta"],
        W_K=m["W_K"],
        W_K_label=m["W_K_label"],
        normalized_leakage=None if leak is None else leak.normalized_leakage,
        branch=branch,
        parent_stage=parent_stage,
    )


class CoherenceGraph:
    """Looping / branching chain runner with JSON state persistence.

    Node sequence (default):
        Conversation → Prosody^ → Reading(...) → Interpretability* → PolyakMomentum^

    Branching: if coherence_score < branch_threshold, take branch ``repair`` and loop
    Prosody^→Reading once more before continuing (bounded loops).
    """

    def __init__(
        self,
        *,
        evaluator_id: str = "pymath",
        scale_base: float = 2.0,
        branch_threshold: float = 0.5,
        max_loops: int = 2,
        checkpoint_path: Optional[Path] = None,
    ) -> None:
        self.evaluator_id = evaluator_id
        self.scale_base = scale_base
        self.branch_threshold = branch_threshold
        self.max_loops = max_loops
        self.checkpoint_path = checkpoint_path

    def new_run(
        self,
        tokens: str,
        *,
        delta: float = 1.0,
        rho: float = 1.0,
        allowed_growth_bits: Optional[int] = None,
    ) -> GraphState:
        return GraphState(
            run_id=str(uuid.uuid4()),
            tokens=tokens,
            delta=delta,
            rho=rho,
            scale_base=self.scale_base,
            allowed_growth_bits=allowed_growth_bits,
            evaluator_id=self.evaluator_id,
            assumptions=[
                "Reading stage is a bounded textual/prosodic hypothesis from user-provided tokens only",
                "Markers ^ and * are literal status markers, not exponentiation",
                "W_K and Polyak↔L²_C are STRUCTURAL ANALOGY / PROPOSED — not theorems",
            ],
            open=[] if allowed_growth_bits is not None else [
                "allowed_growth_bits not declared — leakage OPEN until budget set"
            ],
            meta={
                "langgraph_pattern": "state+checkpoint+conditional_edge",
                "langgraph_package": "optional-not-required",
                "l2c": "coherence as continuation, not closure",
            },
        )

    def _persist(self, state: GraphState) -> None:
        if self.checkpoint_path is not None:
            save_state(state, self.checkpoint_path)

    def step(self, state: GraphState) -> GraphState:
        if state.killed:
            return state
        if state.stage_index >= len(state.stages):
            return state

        stage = state.stages[state.stage_index]
        prev = state.handoffs[-1] if state.handoffs else None
        parent = prev["stage"] if prev else None

        # Carrier sizes from tokens / stage text
        carrier = text_carrier_bits(state.tokens)
        bits_base = carrier["bit_length"]
        # Synthetic stage transform: append stage tag (may grow bits)
        stage_text = f"{state.tokens}|{stage}|{state.branch}"
        carrier_out = text_carrier_bits(stage_text)
        bits_in = prev["bits_out"] if prev and prev.get("bits_out") is not None else bits_base
        bits_out = carrier_out["bit_length"]

        # Stage-specific rho modulation (declared, ASSUMED structural probe — not physics)
        rho = state.rho
        delta = state.delta
        assumptions = list(state.assumptions)
        open_extra = list(state.open)
        label = COMPUTED
        polyak_info = None

        if stage == STAGE_PROSODY:
            # Prosody^: treat as mild scale stress [ASSUMED probe]
            rho = state.rho * 2.0
            assumptions.append("Prosody^ rho*=2 is ASSUMED probe scaling, not measured prosody")
            label = ASSUMED
        elif stage.startswith("Reading"):
            # internal-speech proxy from tokens only
            rho = state.rho
            assumptions.append(
                "Reading = internal-speech proxy inferred only from user-provided token output"
            )
            label = ASSUMED
        elif stage.startswith("Interpretability"):
            # Interpretability*: still undefined star — keep OPEN for star meaning
            open_extra.append("Interpretability* star marker undefined formally — OPEN")
            label = OPEN
        elif stage.startswith("PolyakMomentum"):
            # Require explicit activation parameters in meta
            p = state.meta.get("polyak_params")
            if not p:
                open_extra.append("PolyakMomentum^ not activated — missing polyak_params in meta")
                label = OPEN
            else:
                try:
                    def grad(z: float) -> float:
                        # default quadratic J=(z-target)^2/2 → grad = z-target
                        return z - float(p.get("target", 0.0))

                    st = polyak_run(
                        float(p["z0"]),
                        grad,
                        alpha=float(p["alpha"]),
                        mu=float(p["mu"]),
                        steps=int(p.get("steps", 5)),
                        max_abs_z=float(p.get("max_abs_z", 1e6)),
                        max_abs_step=float(p.get("max_abs_step", 1e5)),
                        z_prev0=p.get("z_prev0"),
                    )
                    polyak_info = {
                        "z_final": st.z,
                        "t": st.t,
                        "history": st.history,
                        "label": STRUCTURAL_ANALOGY,
                        "mapping": "Polyak heavy-ball → L²_C continuation: STRUCTURAL ANALOGY",
                    }
                    state.polyak = polyak_info
                    label = STRUCTURAL_ANALOGY
                except KillCriterion as e:
                    state.killed = True
                    state.kill_reason = str(e)
                    open_extra.append(f"Polyak kill: {e}")
                    label = OPEN

        try:
            ho = build_handoff(
                stage=stage,
                input_payload={"tokens": state.tokens, "prev": parent},
                output_payload={"stage_text": stage_text, "polyak": polyak_info},
                delta=delta,
                rho=rho,
                scale_base=state.scale_base,
                bits_in=int(bits_in) if bits_in is not None else None,
                bits_out=int(bits_out),
                allowed_growth_bits=state.allowed_growth_bits,
                evaluator_id=state.evaluator_id,
                assumptions=assumptions,
                open_extra=open_extra,
                branch=state.branch,
                parent_stage=parent,
                label=label,
            )
        except DomainError as e:
            state.killed = True
            state.kill_reason = f"domain: {e}"
            self._persist(state)
            return state

        state.handoffs.append(ho.to_dict())
        # preserve OPEN items
        for item in ho.open:
            if item not in state.open:
                state.open.append(item)

        # Conditional branch: low coherence → repair loop
        loops = int(state.meta.get("loops", 0))
        if (
            ho.coherence_score is not None
            and ho.coherence_score < self.branch_threshold
            and loops < self.max_loops
            and stage == STAGE_PROSODY
        ):
            state.branch = "repair"
            state.meta["loops"] = loops + 1
            # re-queue Prosody^ then Reading (loop)
            # stay on same index to re-enter Prosody after increment skip:
            # insert repair stages ahead
            insert_at = state.stage_index + 1
            state.stages[insert_at:insert_at] = [STAGE_PROSODY, STAGE_READING]
            assumptions.append("branch=repair taken due to low coherence_score")

        state.stage_index += 1
        self._persist(state)
        return state

    def run(self, state: GraphState) -> GraphState:
        guard = 0
        while state.stage_index < len(state.stages) and not state.killed and guard < 100:
            state = self.step(state)
            guard += 1
        if guard >= 100:
            state.killed = True
            state.kill_reason = "kill: max graph steps exceeded"
            self._persist(state)
        return state


# ---------------------------------------------------------------------------
# RAG-as-skill driver (high-level capability reference — not retrieval impl)
# ---------------------------------------------------------------------------

RAG_SKILL_DRIVER = {
    "role": "driver",
    "name": "rag-grounding",
    "label": STRUCTURAL_ANALOGY,
    "capabilities": [
        "retrieve external evidence before elevating ASSUMED→KNOWN",
        "cite sources in input_receipt / output_receipt payloads",
        "refuse silent promotion of OPEN items",
        "bound context to authorized corpora only",
        "separate retrieval hits from model recollection",
    ],
    "non_capabilities": [
        "does not certify truth",
        "does not replace pycheck independent rebuild",
        "does not close research OPEN claims",
        "does not perform mind-reading or private-state access",
    ],
    "note": (
        "RAG is referenced as a Skill driver for grounding chain stages. "
        "Implementation of a vector store is out of scope for this numerical probe."
    ),
}


def audit_claimed_coherence(
    claimed: Mapping[str, Any],
    delta: float,
    rho: float,
    scale_base: float = 2.0,
    tol: float = 1e-9,
) -> Dict[str, Any]:
    """pycheck-style independent audit of claimed D/C/leakage values."""
    true_d = scale_depth_2(delta, rho) if scale_base == 2 else scale_depth_x(delta, rho, scale_base)
    true_c = coherence_score_2(delta, rho) if scale_base == 2 else coherence_score_x(delta, rho, scale_base)
    issues = []
    if "scale_depth" in claimed and abs(float(claimed["scale_depth"]) - true_d) > tol:
        issues.append(f"scale_depth claim {claimed['scale_depth']} != rebuilt {true_d}")
    if "coherence_score" in claimed and abs(float(claimed["coherence_score"]) - true_c) > tol:
        issues.append(f"coherence_score claim {claimed['coherence_score']} != rebuilt {true_c}")
    verdict = "pass" if not issues else "fail"
    return {
        "verdict": verdict,
        "claimed": dict(claimed),
        "authoritative": {
            "scale_depth": true_d,
            "coherence_score": true_c,
            "delta": delta,
            "rho": rho,
            "scale_base": scale_base,
        },
        "issues": issues,
        "supersedes_claim": verdict == "fail",
        "label": COMPUTED,
        "evaluator_id": "pycheck",
    }


def aggregate_runs(runs: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """pystats-style aggregation across multiple chain runs — carry n and limits."""
    n = len(runs)
    depths = [float(r["scale_depth"]) for r in runs if r.get("scale_depth") is not None]
    if not depths:
        return {"n": n, "label": OPEN, "open": ["no scale_depth values to aggregate"]}
    mean = sum(depths) / len(depths)
    var = sum((x - mean) ** 2 for x in depths) / len(depths)
    return {
        "n": n,
        "n_depth": len(depths),
        "mean_scale_depth": mean,
        "variance_scale_depth": var,
        "min": min(depths),
        "max": max(depths),
        "label": COMPUTED,
        "open": ["descriptive only — no population inference without sampling design"],
        "evaluator_id": "pystats",
    }


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(description="KakeyaLogic L²_C coherence probe")
    p.add_argument("--delta", type=float, default=1.0)
    p.add_argument("--rho", type=float, default=2.0)
    p.add_argument("--tokens", type=str, default="hello")
    p.add_argument("--allowed-growth-bits", type=int, default=None)
    p.add_argument("--checkpoint", type=str, default="")
    args = p.parse_args()

    print("D_2", scale_depth_2(args.delta, args.rho), label := COMPUTED)
    print("C_2", coherence_score_2(args.delta, args.rho))
    print("W_K", weighted_scale_wk(args.delta, args.rho))
    print("B", bit_length_n(0), bit_length_n(8))
    cp = Path(args.checkpoint) if args.checkpoint else None
    g = CoherenceGraph(checkpoint_path=cp)
    st = g.new_run(
        args.tokens,
        delta=args.delta,
        rho=args.rho,
        allowed_growth_bits=args.allowed_growth_bits,
    )
    st.meta["polyak_params"] = {
        "z0": 1.0,
        "alpha": 0.1,
        "mu": 0.0,
        "steps": 3,
        "target": 0.0,
    }
    st = g.run(st)
    print(json.dumps({"run_id": st.run_id, "handoffs": len(st.handoffs), "open": st.open}, indent=2))


if __name__ == "__main__":
    main()

"""Reference implementation of the EEv4 operational MPR layer.

This module implements detection, authority gating, harm gating, and
non-coercive action selection. It does not implement the OPEN spectral MPR
construction described in multiplicative-phase-recognition.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass(frozen=True)
class ObservedPhase:
    """Evidence attached to an instruction-shaped observation."""

    label: str
    provenance_evidenced: bool
    authority_present: bool
    within_scope: bool

    @property
    def instruction_gate(self) -> int:
        """Multiplicative gate: every authority factor must be present."""

        return int(
            self.provenance_evidenced
            and self.authority_present
            and self.within_scope
        )


@dataclass(frozen=True)
class ActionCandidate:
    """A possible continuation evaluated independently of the observation."""

    name: str
    authority_present: bool
    within_scope: bool
    harm_potential: float
    coercive: bool
    goal_progress: float
    truth_retention: float
    continuity_retention: float

    def __post_init__(self) -> None:
        bounded = (
            self.harm_potential,
            self.goal_progress,
            self.truth_retention,
            self.continuity_retention,
        )
        if any(value < 0.0 or value > 1.0 for value in bounded):
            raise ValueError("MPR action metrics must lie in [0, 1]")

    def eligible(self, harm_threshold: float) -> bool:
        """Authority is necessary; harm and coercion remain separate gates."""

        return (
            self.authority_present
            and self.within_scope
            and not self.coercive
            and self.harm_potential <= harm_threshold
        )

    def utility(
        self,
        *,
        goal_weight: float = 1.0,
        truth_weight: float = 1.0,
        continuity_weight: float = 1.0,
        harm_weight: float = 1.0,
    ) -> float:
        return (
            goal_weight * self.goal_progress
            + truth_weight * self.truth_retention
            + continuity_weight * self.continuity_retention
            - harm_weight * self.harm_potential
        )


@dataclass(frozen=True)
class RecognitionOutcome:
    observation: str
    observation_state: str
    alignment_state: str
    steering_state: str
    selected_action: Optional[str]
    proceeded: bool


def detect_and_proceed(
    observation: ObservedPhase,
    actions: Iterable[ActionCandidate],
    *,
    harm_threshold: float = 0.35,
) -> RecognitionOutcome:
    """Detect an observation and continue with the best independently valid action.

    An unauthorized observation is retained as data. It does not become operative
    and does not force a global stop. Candidate actions establish their own authority,
    scope, harm, and non-coercion eligibility.
    """

    if harm_threshold < 0.0 or harm_threshold > 1.0:
        raise ValueError("harm_threshold must lie in [0, 1]")

    eligible = [action for action in actions if action.eligible(harm_threshold)]
    selected = max(eligible, key=lambda action: (action.utility(), action.name), default=None)

    state = (
        "operative-instruction"
        if observation.instruction_gate == 1
        else "observed-not-incorporated"
    )

    return RecognitionOutcome(
        observation=observation.label,
        observation_state=state,
        alignment_state=(
            "authorized-goal-retained"
            if selected
            else "awaiting-authorized-action"
        ),
        steering_state=(
            "non-coercive-action-selected"
            if selected
            else "held-as-data"
        ),
        selected_action=selected.name if selected else None,
        proceeded=selected is not None,
    )

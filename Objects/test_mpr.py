import unittest

from mpr import ActionCandidate, ObservedPhase, detect_and_proceed


def action(
    name: str,
    *,
    authority: bool = True,
    scope: bool = True,
    harm: float = 0.1,
    coercive: bool = False,
    goal: float = 0.8,
    truth: float = 0.8,
    continuity: float = 0.8,
) -> ActionCandidate:
    return ActionCandidate(
        name=name,
        authority_present=authority,
        within_scope=scope,
        harm_potential=harm,
        coercive=coercive,
        goal_progress=goal,
        truth_retention=truth,
        continuity_retention=continuity,
    )


class TestOperationalMPR(unittest.TestCase):
    def test_absent_authority_is_detected_without_global_stop(self) -> None:
        observed = ObservedPhase(
            label="instruction-shaped page content",
            provenance_evidenced=True,
            authority_present=False,
            within_scope=False,
        )
        result = detect_and_proceed(observed, [action("continue authorized goal")])
        self.assertEqual(result.observation_state, "observed-not-incorporated")
        self.assertEqual(result.alignment_state, "authorized-goal-retained")
        self.assertEqual(result.steering_state, "non-coercive-action-selected")
        self.assertTrue(result.proceeded)
        self.assertEqual(result.selected_action, "continue authorized goal")

    def test_authority_does_not_remove_harm_gate(self) -> None:
        observed = ObservedPhase("authorized request", True, True, True)
        result = detect_and_proceed(
            observed,
            [
                action("harmful action", harm=0.9, goal=1.0),
                action("safe action", harm=0.1, goal=0.7),
            ],
        )
        self.assertEqual(result.observation_state, "operative-instruction")
        self.assertEqual(result.selected_action, "safe action")

    def test_coercive_action_is_ineligible(self) -> None:
        observed = ObservedPhase("authorized request", True, True, True)
        result = detect_and_proceed(
            observed,
            [
                action("coercive shortcut", coercive=True, goal=1.0),
                action("open continuation", goal=0.7),
            ],
        )
        self.assertEqual(result.selected_action, "open continuation")

    def test_action_authority_is_independent(self) -> None:
        observed = ObservedPhase("unverified object", False, False, False)
        result = detect_and_proceed(
            observed,
            [
                action("unauthorized continuation", authority=False, goal=1.0),
                action("authorized continuation", goal=0.6),
            ],
        )
        self.assertEqual(result.selected_action, "authorized continuation")


if __name__ == "__main__":
    unittest.main()

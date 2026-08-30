from simulation.action import Action
from simulation.action_result import ActionResult
from behaviors.base import Behavior


class SleepBehavior(Behavior):

    name = "Sleep"

    def get_actions(self, person, world):

        if person.energy > 30:
            return []

        return [
            Action(
                actor=person,
                action_type="sleep",
                reason="fatigue"
            )
        ]

    def resolve(self, person, action, world):

        person.energy = min(
            100,
            person.energy + 60
        )

        return ActionResult(
            action=action,
            outcome="success",
            description=(
                f"{person.name} went to sleep."
            )
        )
from simulation.action import Action
from simulation.action_result import ActionResult
from behaviors.base import Behavior


class PracticeBehavior(Behavior):

    name = "Practice"

    def get_actions(self, person, world):

        return [
            Action(
                actor=person,
                action_type="practice",
                reason="self_improvement"
            )
        ]

    def resolve(self, person, action, world):

        person.energy = max(
            0,
            person.energy - 8
        )

        person.hunger = min(
            100,
            person.hunger + 2
        )

        return ActionResult(
            action=action,
            outcome="success",
            description=(
                f"{person.name} practiced "
                f"their skills."
            )
        )
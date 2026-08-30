from simulation.action_result import ActionResult
from simulation.action import Action
from behaviors.base import Behavior


class ExploreBehavior(Behavior):

    name = "Explore"

    def get_actions(self, person, world):

        return [
            Action(
                actor=person,
                action_type="explore",
                reason="curiosity"
            )
        ]

    def resolve(self, person, action, world):

        person.energy = max(
            0,
            person.energy - 8
        )

        person.hunger = min(
            100,
            person.hunger + 3
        )

        return ActionResult(
            action=action,
            outcome="success",
            description=(
                f"{person.name} explored."
            )
        )
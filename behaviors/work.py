from simulation.action import Action
from simulation.action_result import ActionResult
from behaviors.base import Behavior


class WorkBehavior(Behavior):

    name = "Work"

    def get_actions(self, person, world):

        return [
            Action(
                actor=person,
                action_type="work",
                reason="occupation"
            )
        ]

    def resolve(self, person, action, world):

        person.energy = max(
            0,
            person.energy - 10
        )

        person.hunger = min(
            100,
            person.hunger + 4
        )

        if person.occupation == "Farmer":

            person.add_item("food", 3)

            description = (
                f"{person.name} worked the farm "
                f"and produced 3 food."
            )

        elif person.occupation == "Hunter":

            person.add_item("meat", 2)

            description = (
                f"{person.name} hunted "
                f"and produced 2 meat."
            )

        elif person.occupation == "Blacksmith":

            person.add_item("tools", 1)

            description = (
                f"{person.name} forged "
                f"1 tool."
            )

        elif person.occupation == "Merchant":

            person.earn_money(5)

            description = (
                f"{person.name} conducted "
                f"business and earned 5 money."
            )

        elif person.occupation == "Scholar":

            description = (
                f"{person.name} studied "
                f"and gained knowledge."
            )

        else:

            description = (
                f"{person.name} worked."
            )

        return ActionResult(
            action=action,
            outcome="success",
            description=description
        )
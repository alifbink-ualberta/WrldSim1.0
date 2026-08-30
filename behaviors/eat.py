from simulation.action import Action
from simulation.action_result import ActionResult
from behaviors.base import Behavior


class EatBehavior(Behavior):

    name = "Eat"

    def get_actions(self, person, world):

        if person.hunger < 40:
            return []

        actions = []

        if person.has_item("food"):

            actions.append(
                Action(
                    actor=person,
                    action_type="eat",
                    reason="hunger"
                )
            )

        if person.has_item("meat"):

            actions.append(
                Action(
                    actor=person,
                    action_type="eat",
                    item="meat",
                    reason="hunger"
                )
            )

        return actions

    def resolve(self, person, action, world):

        if action.item == "meat":

            if not person.has_item("meat"):
                return ActionResult(
                    action=action,
                    outcome="failure",
                    description=(
                        f"{person.name} tried to eat meat "
                        f"but had none."
                    )
                )

            person.remove_item("meat")

            food_type = "meat"

        else:

            if not person.has_item("food"):

                return ActionResult(
                    action=action,
                    outcome="failure",
                    description=(
                        f"{person.name} tried to eat "
                        f"but had no food."
                    )
                )

            person.remove_item("food")

            food_type = "food"

        person.hunger = max(
            0,
            person.hunger - 50
        )

        person.energy = max(
            0,
            person.energy - 2
        )

        return ActionResult(
            action=action,
            outcome="success",
            description=(
                f"{person.name} ate {food_type}."
            )
        )
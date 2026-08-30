class ActionResolver:

    def __init__(self, behavior_registry):

        self.behavior_registry = (
            behavior_registry
        )

    def resolve(
        self,
        person,
        action,
        world
    ):

        behavior = (
            self.behavior_registry.find_behavior(
                action,
                person,
                world
            )
        )

        if behavior is None:

            from simulation.action_result import (
                ActionResult
            )

            return ActionResult(
                action=action,
                outcome="failure",
                description=(
                    f"{person.name} could not "
                    f"perform {action.action_type}."
                )
            )

        return behavior.resolve(
            person,
            action,
            world
        )
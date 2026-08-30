import random

from simulation.action import Action
from simulation.action_result import ActionResult
from behaviors.base import Behavior


class SocializeBehavior(Behavior):

    name = "Socialize"

    def get_actions(self, person, world):

        possible_targets = []

        for other in world.people:

            if other == person:
                continue

            if other.location != person.location:
                continue

            possible_targets.append(other)

        if not possible_targets:
            return []

        actions = []

        for target in possible_targets:

            actions.append(
                Action(
                    actor=person,
                    action_type="socialize",
                    target=target,
                    reason="social_need"
                )
            )

        return actions

    def resolve(self, person, action, world):

        target = action.target

        if target is None:

            return ActionResult(
                action=action,
                outcome="failure",
                description=(
                    f"{person.name} could not find "
                    f"someone to socialize with."
                )
            )

        relationship = person.get_relationship(
            target
        )

        # --------------------------------
        # BASE PROBABILITY
        # --------------------------------

        probability = 0.50

        # --------------------------------
        # PERSONALITY
        # --------------------------------

        probability += (
            person.extraversion - 50
        ) / 200

        probability += (
            person.agreeableness - 50
        ) / 400

        # --------------------------------
        # FAMILIARITY
        # --------------------------------

        probability += (
            min(
                relationship.familiarity,
                100
            ) / 250
        )

        # --------------------------------
        # AFFECTION
        # --------------------------------

        probability += (
            relationship.affection_for(person)
            / 500
        )

        # --------------------------------
        # TRUST
        # --------------------------------

        probability += (
            relationship.trust_for(person)
            / 500
        )

        # --------------------------------
        # FATIGUE
        # --------------------------------

        if person.energy < 20:

            probability -= 0.15

        # --------------------------------
        # CLAMP
        # --------------------------------

        probability = max(
            0.05,
            min(
                0.95,
                probability
            )
        )

        roll = random.random()

        # --------------------------------
        # FAILURE
        # --------------------------------

        if roll > probability:

            person.energy = max(
                0,
                person.energy - 4
            )

            return ActionResult(
                action=action,
                outcome="failure",
                description=(
                    f"{person.name} tried to talk "
                    f"with {target.name}, but the "
                    f"interaction went poorly."
                ),
                probability=probability,
                roll=roll
            )

        # --------------------------------
        # SUCCESS
        # --------------------------------

        relationship.familiarity = min(
            100,
            relationship.familiarity + 1
        )

        relationship.affection_a_to_b = min(
            100,
            relationship.affection_a_to_b + 1
        )

        person.energy = max(
            0,
            person.energy - 4
        )

        target.remember(
            {
                "type": "social_interaction",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "other": person.name,
                "description": (
                    f"Talked with {person.name}."
                )
            }
        )

        return ActionResult(
            action=action,
            outcome="success",
            description=(
                f"{person.name} talked with "
                f"{target.name}."
            ),
            probability=probability,
            roll=roll
        )
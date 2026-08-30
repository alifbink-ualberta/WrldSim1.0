import random


class ActionOutcome:

    def __init__(
        self,
        success,
        probability,
        description,
        quality=1.0
    ):

        self.success = success
        self.probability = probability
        self.description = description
        self.quality = quality

    def __str__(self):

        return (
            f"{self.description} "
            f"[success probability="
            f"{self.probability:.1f}%]"
        )


class ActionResolver:

    def resolve(
        self,
        action,
        world
    ):

        probability = (
            self.calculate_probability(
                action,
                world
            )
        )

        roll = random.uniform(
            0,
            100
        )

        success = roll <= probability

        if success:

            description = (
                f"{action.actor.name} "
                f"successfully completed "
                f"{action.action_type}."
            )

            return ActionOutcome(
                success=True,
                probability=probability,
                description=description,
                quality=1.0
            )

        description = (
            f"{action.actor.name} "
            f"failed to successfully "
            f"complete "
            f"{action.action_type}."
        )

        return ActionOutcome(
            success=False,
            probability=probability,
            description=description,
            quality=0.0
        )

    # ==========================================
    # PROBABILITY
    # ==========================================

    def calculate_probability(
        self,
        action,
        world
    ):

        person = action.actor
        action_type = action.action_type

        probability = 70.0

        # --------------------------------------
        # SOCIALIZATION
        # --------------------------------------

        if action_type == "socialize":

            probability += (
                person.extraversion - 50
            ) * 0.35

            probability += (
                person.agreeableness - 50
            ) * 0.20

            probability -= (
                person.neuroticism - 50
            ) * 0.20

        # --------------------------------------
        # WORK
        # --------------------------------------

        elif action_type == "work":

            probability += (
                person.conscientiousness - 50
            ) * 0.25

        # --------------------------------------
        # PRACTICE
        # --------------------------------------

        elif action_type == "practice":

            probability += (
                person.conscientiousness - 50
            ) * 0.25

            probability += (
                person.openness - 50
            ) * 0.15

        # --------------------------------------
        # EXPLORATION
        # --------------------------------------

        elif action_type == "explore":

            probability += (
                person.openness - 50
            ) * 0.25

            probability -= (
                person.neuroticism - 50
            ) * 0.20

        # --------------------------------------
        # BASIC SURVIVAL
        # --------------------------------------

        elif action_type in (
            "eat",
            "sleep"
        ):

            probability = 95

        # --------------------------------------
        # ENERGY
        # --------------------------------------

        if person.energy < 20:

            probability -= 10

        # --------------------------------------
        # CLAMP
        # --------------------------------------

        return max(
            5,
            min(
                95,
                probability
            )
        )
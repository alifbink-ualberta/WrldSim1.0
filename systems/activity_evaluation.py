# systems/action_evaluation.py


class ActionEvaluationSystem:

    @staticmethod
    def evaluate(
        person,
        action,
        world,
        goals
    ):

        score = 0.0

        # ==========================================
        # ACTION TYPE
        # ==========================================

        action_type = action.action_type

        # ==========================================
        # GOAL CONTRIBUTION
        # ==========================================

        for goal in goals:

            contribution = (
                ActionEvaluationSystem
                .goal_contribution(
                    person,
                    action_type,
                    goal
                )
            )

            score += (
                contribution
                * goal.priority
            )

        # ==========================================
        # BASIC SURVIVAL PRESSURE
        # ==========================================

        survival = person.survival

        if action_type == "eat":

            score += (
                survival.hunger
                * 2.0
            )

        elif action_type == "sleep":

            score += (
                (1.0 - survival.sleep)
                * 2.0
            )

        elif action_type == "drink":

            score += (
                survival.thirst
                * 2.5
            )

        # ==========================================
        # ENERGY COST
        # ==========================================

        energy = survival.energy

        if action_type in [
            "explore",
            "work",
            "practice"
        ]:

            score -= (
                (1.0 - energy)
                * 0.8
            )

        # ==========================================
        # EXPLORATION
        # ==========================================

        if action_type == "explore":

            exploration = (
                person.personality.openness
            )

            score += (
                exploration
                * 1.5
            )

        # ==========================================
        # SOCIALIZATION
        # ==========================================

        if action_type == "socialize":

            score += (
                person.personality.extraversion
                * 1.5
            )

            score += (
                person.personality.agreeableness
                * 0.5
            )

        # ==========================================
        # RANDOMNESS
        # ==========================================

        # A small amount of variation prevents
        # identical people from always choosing
        # exactly the same action.

        import random

        score += random.uniform(
            -0.15,
            0.15
        )

        return score

    # ==================================================
    # GOAL CONTRIBUTION
    # ==================================================

    @staticmethod
    def goal_contribution(
        person,
        action_type,
        goal
    ):

        goal_name = goal.description.lower()

        # ==========================================
        # FOOD
        # ==========================================

        if "food" in goal_name:

            if action_type == "eat":
                return 1.0

            if action_type == "buy":
                return 0.7

            if action_type == "work":
                return 0.3

        # ==========================================
        # WATER
        # ==========================================

        if "water" in goal_name:

            if action_type == "drink":
                return 1.0

            if action_type == "buy":
                return 0.6

        # ==========================================
        # REST
        # ==========================================

        if "rest" in goal_name:

            if action_type == "sleep":
                return 1.0

        # ==========================================
        # SLEEP
        # ==========================================

        if "sleep" in goal_name:

            if action_type == "sleep":
                return 1.0

        # ==========================================
        # EXPLORATION
        # ==========================================

        if "explore" in goal_name:

            if action_type == "explore":
                return 1.0

        # ==========================================
        # ABILITY
        # ==========================================

        if "abilities" in goal_name:

            if action_type == "practice":
                return 1.0

            if action_type == "work":
                return 0.3

        # ==========================================
        # SOCIAL
        # ==========================================

        if "someone" in goal_name:

            if action_type == "socialize":
                return 1.0

        # ==========================================
        # SECURITY
        # ==========================================

        if "security" in goal_name:

            if action_type == "work":
                return 0.4

            if action_type == "socialize":
                return 0.2

        # ==========================================
        # POWER
        # ==========================================

        if "influence" in goal_name:

            if action_type == "socialize":
                return 0.4

            if action_type == "work":
                return 0.2

        return 0.0
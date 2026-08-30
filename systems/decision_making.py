import random

from systems.considerations import (
    NeedConsideration,
    GoalConsideration,
    PersonalityConsideration,
    CircumstanceConsideration
)


class DecisionSystem:

    def __init__(self):

        self.considerations = [
            NeedConsideration(),
            GoalConsideration(),
            PersonalityConsideration(),
            CircumstanceConsideration()
        ]

        # Controls how deterministic decisions are.
        #
        # 0.0 = always choose highest score
        # 1.0 = significant behavioural variation
        #
        self.randomness = 0.15

    # ==========================================
    # EXTENSION
    # ==========================================

    def add_consideration(self, consideration):

        self.considerations.append(
            consideration
        )

    # ==========================================
    # SCORING
    # ==========================================

    def score_action(
        self,
        person,
        action,
        world
    ):

        total = 0

        for consideration in self.considerations:

            total += consideration.score(
                person,
                action,
                world
            )

        return total

    # ==========================================
    # CHOICE
    # ==========================================

    def choose_action(
        self,
        person,
        world,
        behavior_registry
    ):

        actions = (
            behavior_registry.generate_actions(
                person,
                world
            )
        )

        if not actions:
            return None, 0

        scored = []

        for action in actions:

            score = self.score_action(
                person,
                action,
                world
            )

            # Small random variation.
            #
            # This prevents identical people
            # from becoming perfectly deterministic.
            variation = random.uniform(
                -abs(score) * self.randomness,
                abs(score) * self.randomness
            )

            final_score = score + variation

            scored.append(
                (action, final_score)
            )

        scored.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return scored[0]
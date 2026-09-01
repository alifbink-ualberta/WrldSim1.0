# systems/relationship_goals.py


from simulation.goal import Goal
from simulation.motivation import MotivationSystem


class RelationshipGoalSystem:

    """
    Generates goals directed at specific people.

    A relationship does not directly tell a person
    what to do.

    It creates psychological pressure which can
    eventually produce a goal.

    Example:

        affection → maintain relationship
        resentment → gain advantage
        fear → protect oneself
        respect → impress person
        trust → cooperate
    """

    # ==================================================
    # GENERATE
    # ==================================================

    @staticmethod
    def generate(person):

        goals = []

        if not hasattr(
            person,
            "relationships"
        ):

            return goals

        for other, relationship in (
            person.relationships.items()
        ):

            if other is None:
                continue

            if not other.is_alive:
                continue

            feelings = relationship.get_feelings(
                person
            )

            affection = (
                feelings["affection"] / 100.0
            )

            trust = (
                feelings["trust"] / 100.0
            )

            respect = (
                feelings["respect"] / 100.0
            )

            fear = (
                feelings["fear"] / 100.0
            )

            resentment = (
                feelings["resentment"] / 100.0
            )

            attraction = (
                feelings["attraction"] / 100.0
            )

            # ==========================================
            # AFFECTION
            # ==========================================

            if affection > 0.6:

                motivation = (
                    MotivationSystem.get(
                        person,
                        "social_connection"
                    )
                )

                if motivation is not None:

                    goals.append(
                        Goal(
                            description=(
                                "Maintain my relationship"
                            ),
                            motivation=motivation,
                            priority=(
                                affection
                                * motivation.strength
                            ),
                            target=other,
                            desired_effects={
                                "relationship_affection": 1.0,
                                "relationships": 1.0
                            }
                        )
                    )

            # ==========================================
            # TRUST
            # ==========================================

            if trust > 0.7:

                motivation = (
                    MotivationSystem.get(
                        person,
                        "harmony"
                    )
                )

                if motivation is not None:

                    goals.append(
                        Goal(
                            description=(
                                "Cooperate with someone "
                                "I trust"
                            ),
                            motivation=motivation,
                            priority=(
                                trust
                                * motivation.strength
                            ),
                            target=other,
                            desired_effects={
                                "relationship_trust": 1.0,
                                "relationships": 0.8
                            }
                        )
                    )

            # ==========================================
            # RESPECT
            # ==========================================

            if respect > 0.6:

                motivation = (
                    MotivationSystem.get(
                        person,
                        "achievement"
                    )
                )

                if motivation is not None:

                    goals.append(
                        Goal(
                            description=(
                                "Earn the respect "
                                "of this person"
                            ),
                            motivation=motivation,
                            priority=(
                                respect
                                * motivation.strength
                            ),
                            target=other,
                            desired_effects={
                                "relationship_respect": 1.0,
                                "status": 0.5,
                                "achievement": 0.5
                            }
                        )
                    )

            # ==========================================
            # FEAR
            # ==========================================

            if fear > 0.6:

                motivation = (
                    MotivationSystem.get(
                        person,
                        "security"
                    )
                    )

                if motivation is not None:

                    goals.append(
                        Goal(
                            description=(
                                "Protect myself "
                                "from this person"
                            ),
                            motivation=motivation,
                            priority=(
                                fear
                                * motivation.strength
                            ),
                            target=other,
                            desired_effects={
                                "security": 1.0,
                                "relationship_fear": -0.5
                            }
                        )
                    )

            # ==========================================
            # RESENTMENT
            # ==========================================

            if resentment > 0.6:

                motivation = (
                    MotivationSystem.get(
                        person,
                        "power"
                    )
                )

                if motivation is not None:

                    goals.append(
                        Goal(
                            description=(
                                "Gain an advantage "
                                "over this person"
                            ),
                            motivation=motivation,
                            priority=(
                                resentment
                                * motivation.strength
                            ),
                            target=other,
                            desired_effects={
                                "status": 0.7,
                                "power": 1.0,
                                "relationship_resentment": -0.5
                            }
                        )
                    )

            # ==========================================
            # ATTRACTION
            # ==========================================

            if attraction > 0.6:

                motivation = (
                    MotivationSystem.get(
                        person,
                        "social_connection"
                    )
                )

                if motivation is not None:

                    goals.append(
                        Goal(
                            description=(
                                "Become closer "
                                "to this person"
                            ),
                            motivation=motivation,
                            priority=(
                                attraction
                                * motivation.strength
                            ),
                            target=other,
                            desired_effects={
                                "relationship_affection": 1.0,
                                "relationship_attraction": 0.5
                            }
                        )
                    )

        return goals
# systems/relationship_influence.py


class RelationshipInfluenceSystem:

    """
    Converts a person's feelings toward other people
    into temporary motivational influences.

    This does NOT change the relationship itself.

    Relationship:
        "Arthur trusts Thomas."

    Influence:
        "Arthur is more motivated to maintain his
        relationship with Thomas."

    The relationship remains the underlying state.
    """

    # ==================================================
    # CALCULATE INFLUENCE
    # ==================================================

    @staticmethod
    def calculate(
        person,
        motivation_name
    ):

        total = 0.0

        if not hasattr(
            person,
            "relationships"
        ):
            return total

        for other, relationship in (
            person.relationships.items()
        ):

            if other is None:
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

            familiarity = (
                feelings["familiarity"] / 100.0
            )

            # ==========================================
            # SOCIAL CONNECTION
            # ==========================================

            if motivation_name == "social_connection":

                total += (
                    affection * 0.20
                )

                total += (
                    familiarity * 0.10
                )

                total += (
                    attraction * 0.10
                )

            # ==========================================
            # HARMONY
            # ==========================================

            elif motivation_name == "harmony":

                total += (
                    affection * 0.15
                )

                total += (
                    trust * 0.10
                )

                total -= (
                    resentment * 0.10
                )

            # ==========================================
            # SECURITY
            # ==========================================

            elif motivation_name == "security":

                total += (
                    fear * 0.20
                )

                total += (
                    resentment * 0.05
                )

            # ==========================================
            # POWER
            # ==========================================

            elif motivation_name == "power":

                total += (
                    respect * 0.10
                )

                total += (
                    resentment * 0.05
                )

            # ==========================================
            # EXPLORATION
            # ==========================================

            elif motivation_name == "exploration":

                # Strong fear of another person can
                # discourage exploration.

                total -= (
                    fear * 0.05
                )

            # ==========================================
            # SURVIVAL
            # ==========================================

            elif motivation_name == "survival":

                total += (
                    fear * 0.05
                )

            # ==========================================
            # ACHIEVEMENT
            # ==========================================

            elif motivation_name == "achievement":

                total += (
                    respect * 0.10
                )

            # ==========================================
            # KNOWLEDGE
            # ==========================================

            elif motivation_name == "knowledge":

                total += (
                    familiarity * 0.03
                )

        return total

    # ==================================================
    # APPLY ALL RELATIONSHIP INFLUENCES
    # ==================================================

    @staticmethod
    def apply(
        person,
        motivation_system
    ):

        motivation_names = [
            "survival",
            "exploration",
            "achievement",
            "social_connection",
            "harmony",
            "security",
            "power",
            "knowledge"
        ]

        for motivation_name in motivation_names:

            influence = (
                RelationshipInfluenceSystem.calculate(
                    person,
                    motivation_name
                )
            )

            if influence == 0:
                continue

            motivation_system.modify(
                person,
                motivation_name,
                influence,
                "relationship"
            )

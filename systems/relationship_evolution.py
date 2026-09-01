# systems/relationship_evolution.py


class RelationshipEvolutionSystem:

    @staticmethod
    def process(
        person,
        other,
        event,
        interpretation,
        response
    ):

        if other is None:
            return None

        relationship = (
            person.get_relationship(
                other
            )
        )

        event_type = event.event_type

        impact = 0.0

        if interpretation is not None:

            impact = (
                interpretation.emotional_impact
            )

        # ==========================================
        # FAMILIARITY
        # ==========================================

        # Meaningful interactions make people more
        # familiar with one another.

        if event_type in (
            "talk",
            "help",
            "insult",
            "compliment",
            "threat",
            "gift",
            "betrayal"
        ):

            relationship.change_feeling(
                person,
                "familiarity",
                0.02
            )

        # ==========================================
        # HELP
        # ==========================================

        if event_type == "help":

            relationship.change_feeling(
                person,
                "trust",
                0.05 * max(
                    0.25,
                    1.0 - impact
                )
            )

            relationship.change_feeling(
                person,
                "affection",
                0.04
            )

        # ==========================================
        # COMPLIMENT
        # ==========================================

        elif event_type == "compliment":

            relationship.change_feeling(
                person,
                "affection",
                0.03
            )

            relationship.change_feeling(
                person,
                "respect",
                0.02
            )

        # ==========================================
        # INSULT
        # ==========================================

        elif event_type == "insult":

            # A person who interprets the insult as
            # highly significant experiences a larger
            # relationship consequence.

            severity = (
                0.04
                + (impact * 0.08)
            )

            relationship.change_feeling(
                person,
                "resentment",
                severity
            )

            relationship.change_feeling(
                person,
                "respect",
                -severity * 0.5
            )

        # ==========================================
        # THREAT
        # ==========================================

        elif event_type == "threat":

            relationship.change_feeling(
                person,
                "fear",
                0.06 + (impact * 0.10)
            )

            relationship.change_feeling(
                person,
                "trust",
                -0.05
            )

        # ==========================================
        # BETRAYAL
        # ==========================================

        elif event_type == "betrayal":

            relationship.change_feeling(
                person,
                "trust",
                -(0.10 + impact * 0.15)
            )

            relationship.change_feeling(
                person,
                "resentment",
                0.10 + impact * 0.15
            )

            relationship.change_feeling(
                person,
                "affection",
                -0.05
            )

        # ==========================================
        # HIGH EMOTIONAL SIGNIFICANCE
        # ==========================================

        # Extremely meaningful experiences can produce
        # stronger lasting relationship changes.

        if impact >= 0.8:

            if event_type in (
                "insult",
                "threat",
                "betrayal"
            ):

                relationship.change_feeling(
                    person,
                    "resentment",
                    0.03
                )

        return relationship
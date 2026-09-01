# systems/relationship_effects.py


class RelationshipEffectSystem:

    """
    Converts psychological interpretation into
    gradual changes in a relationship.

    The important principle is:

        EVENT
          ↓
        INTERPRETATION
          ↓
        EMOTION
          ↓
        RELATIONSHIP CHANGE

    The event itself does not directly determine
    how the relationship changes.
    """

    @staticmethod
    def apply(
        person,
        other,
        interpretation
    ):

        if other is None:
            return None

        relationship = (
            person.get_relationship(
                other
            )
        )

        feelings = (
            relationship.get_feelings(
                person
            )
        )

        event_type = (
            interpretation.event.event_type
        )

        impact = (
            interpretation.emotional_impact
        )

        # ==========================================
        # BASE DELTAS
        # ==========================================

        deltas = {
            "affection": 0.0,
            "trust": 0.0,
            "respect": 0.0,
            "fear": 0.0,
            "resentment": 0.0,
            "attraction": 0.0,
            "familiarity": 0.0
        }

        # ==========================================
        # HELP
        # ==========================================

        if event_type == "help":

            deltas["affection"] += (
                4.0 * impact
            )

            deltas["trust"] += (
                5.0 * impact
            )

            deltas["respect"] += (
                2.0 * impact
            )

        # ==========================================
        # GIFT
        # ==========================================

        elif event_type == "gift":

            deltas["affection"] += (
                3.0 * impact
            )

            deltas["trust"] += (
                2.0 * impact
            )

        # ==========================================
        # COMPLIMENT
        # ==========================================

        elif event_type == "compliment":

            deltas["affection"] += (
                2.0 * impact
            )

            deltas["respect"] += (
                2.0 * impact
            )

        # ==========================================
        # INSULT
        # ==========================================

        elif event_type == "insult":

            deltas["affection"] -= (
                4.0 * impact
            )

            deltas["trust"] -= (
                2.0 * impact
            )

            deltas["respect"] -= (
                2.0 * impact
            )

            deltas["resentment"] += (
                5.0 * impact
            )

        # ==========================================
        # THREAT
        # ==========================================

        elif event_type == "threat":

            deltas["fear"] += (
                6.0 * impact
            )

            deltas["resentment"] += (
                4.0 * impact
            )

            deltas["trust"] -= (
                5.0 * impact
            )

        # ==========================================
        # BETRAYAL
        # ==========================================

        elif event_type == "betrayal":

            deltas["trust"] -= (
                10.0 * impact
            )

            deltas["affection"] -= (
                6.0 * impact
            )

            deltas["resentment"] += (
                10.0 * impact
            )

        # ==========================================
        # APPLY
        # ==========================================

        for feeling_name, delta in deltas.items():

            current = feelings[
                feeling_name
            ]

            new_value = current + delta

            new_value = max(
                0.0,
                min(100.0, new_value)
            )

            getattr(
                relationship,
                feeling_name
            )[person] = new_value

        return deltas
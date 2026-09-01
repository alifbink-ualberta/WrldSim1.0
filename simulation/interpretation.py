# simulation/interpretation.py


class Interpretation:

    def __init__(
        self,
        person,
        event,
        meaning,
        emotional_impact=0.5
    ):

        self.person = person

        self.event = event

        self.meaning = meaning

        # 0.0 - 1.0
        self.emotional_impact = max(
            0.0,
            min(
                1.0,
                emotional_impact
            )
        )

        self.perceived_intent = None

    # ==================================================
    # COMPATIBILITY
    # ==================================================

    @property
    def intensity(self):

        return self.emotional_impact

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        return (
            f"{self.person.full_name} "
            f"interprets the event as: "
            f"{self.meaning}"
        )

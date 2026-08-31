# simulation/interpretation.py


class Interpretation:

    def __init__(
        self,
        person,
        event,
        meaning,
        emotional_impact=0.0,
        perceived_intent=None
    ):

        self.person = person
        self.event = event

        # What this person thinks
        # the event means.

        self.meaning = meaning

        # How emotionally significant
        # the event is to them.

        self.emotional_impact = (
            emotional_impact
        )

        # What they believe the other
        # person's intention was.

        self.perceived_intent = (
            perceived_intent
        )

    def __str__(self):

        return (
            f"{self.person.full_name} interprets "
            f"the event as: {self.meaning}"
        )
# simulation/intent.py


class PerceivedIntent:

    def __init__(
        self,
        person,
        other,
        event,
        intention,
        confidence=0.5
    ):

        # ==========================================
        # PEOPLE
        # ==========================================

        self.person = person
        self.other = other

        # ==========================================
        # EVENT
        # ==========================================

        self.event = event

        # ==========================================
        # PERCEIVED INTENTION
        # ==========================================

        self.intention = intention

        # ==========================================
        # CONFIDENCE
        # ==========================================

        # How confident the person is that
        # their interpretation is correct.

        self.confidence = confidence

    def __str__(self):

        return (
            f"{self.person.full_name} believes "
            f"{self.other.full_name} intended to "
            f"{self.intention}."
        )
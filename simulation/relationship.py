class Relationship:

    def __init__(self, person_a, person_b):

        self.person_a = person_a
        self.person_b = person_b

        # How well the two people know each other.
        self.familiarity = 0

        # How much each person trusts the other.
        self.trust_a_to_b = 0
        self.trust_b_to_a = 0

        # Positive/negative social feelings.
        self.affection_a_to_b = 0
        self.affection_b_to_a = 0

        self.respect_a_to_b = 0
        self.respect_b_to_a = 0

        self.fear_a_to_b = 0
        self.fear_b_to_a = 0

        self.resentment_a_to_b = 0
        self.resentment_b_to_a = 0

    def get_other(self, person):

        if person == self.person_a:
            return self.person_b

        if person == self.person_b:
            return self.person_a

        return None

    def modify(self, person, attribute, amount):

        if person == self.person_a:

            if attribute.endswith("_a_to_b"):
                current = getattr(self, attribute)
                setattr(
                    self,
                    attribute,
                    current + amount
                )

        elif person == self.person_b:

            if attribute.endswith("_b_to_a"):
                current = getattr(self, attribute)
                setattr(
                    self,
                    attribute,
                    current + amount
                )

    def familiarity_for(self, person):

        return self.familiarity

    def trust_for(self, person):

        if person == self.person_a:
            return self.trust_a_to_b

        if person == self.person_b:
            return self.trust_b_to_a

        return 0

    def affection_for(self, person):

        if person == self.person_a:
            return self.affection_a_to_b

        if person == self.person_b:
            return self.affection_b_to_a

        return 0

    def respect_for(self, person):

        if person == self.person_a:
            return self.respect_a_to_b

        if person == self.person_b:
            return self.respect_b_to_a

        return 0

    def __str__(self):

        return (
            f"{self.person_a.name} ↔ "
            f"{self.person_b.name} | "
            f"Familiarity: {self.familiarity}"
        )
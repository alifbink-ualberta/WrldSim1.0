from dataclasses import dataclass


@dataclass
class Relationship:

    person_a: str
    person_b: str

    familiarity: int = 0
    trust: int = 50
    affection: int = 0
    respect: int = 0
    fear: int = 0
    resentment: int = 0

    def overall(self):

        return (
            self.trust
            + self.affection
            + self.respect
            - self.fear
            - self.resentment
        )
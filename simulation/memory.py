from dataclasses import dataclass


@dataclass
class Memory:

    year: int
    description: str

    emotional_weight: int = 50

    def __str__(self):

        return (
            f"Year {self.year}: "
            f"{self.description}"
        )
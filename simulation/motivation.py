# simulation/motivation.py


class Motivation:

    def __init__(
        self,
        name,
        strength=0.5
    ):

        self.name = name
        self.strength = strength

    def increase(self, amount):

        self.strength = min(
            1.0,
            self.strength + amount
        )

    def decrease(self, amount):

        self.strength = max(
            0.0,
            self.strength - amount
        )

    def __str__(self):

        return (
            f"{self.name}: "
            f"{self.strength:.2f}"
        )
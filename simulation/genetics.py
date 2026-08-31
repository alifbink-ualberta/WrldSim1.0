# simulation/genetics.py

import random


class Genetics:

    TRAITS = [
        "height",
        "strength",
        "agility",
        "stamina",
        "constitution"
    ]

    def __init__(self, traits=None):

        if traits is None:

            traits = {
                trait: random.uniform(0.3, 0.7)
                for trait in self.TRAITS
            }

        self.traits = traits

    # ==================================================
    # INHERITANCE
    # ==================================================

    @classmethod
    def inherit(cls, parent_a, parent_b):

        child_traits = {}

        for trait in cls.TRAITS:

            a = parent_a.traits.get(
                trait,
                0.5
            )

            b = parent_b.traits.get(
                trait,
                0.5
            )

            # Combine parental values
            inherited = (a + b) / 2

            # Natural variation
            variation = random.gauss(
                0,
                0.05
            )

            value = inherited + variation

            # Keep within 0-1
            value = max(
                0.0,
                min(1.0, value)
            )

            child_traits[trait] = value

        return cls(child_traits)
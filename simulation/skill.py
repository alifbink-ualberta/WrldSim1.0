# simulation/skill.py


class Skill:

    def __init__(
        self,
        name,
        experience=0.0
    ):

        self.name = name
        self.experience = max(
            0.0,
            experience
        )

    @property
    def level(self):

        # Simple progression for now.
        #
        # This is intentionally NOT final.
        # We can replace the mathematical model
        # later without changing Person.

        if self.experience < 10:
            return 0

        if self.experience < 50:
            return 1

        if self.experience < 150:
            return 2

        if self.experience < 300:
            return 3

        if self.experience < 600:
            return 4

        if self.experience < 1000:
            return 5

        return 6

    def add_experience(self, amount):

        self.experience += max(
            0.0,
            amount
        )

    def __str__(self):

        return (
            f"{self.name}: "
            f"level {self.level}, "
            f"{self.experience:.1f} XP"
        )
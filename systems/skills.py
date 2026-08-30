# systems/skills.py


class SkillSet:
    """
    Stores a person's learned capabilities.

    Skills are deliberately separate from personality.

    Personality influences tendencies and behaviour.
    Skills represent capability developed through
    experience, education, practice, occupation, etc.
    """

    DEFAULT_SKILLS = {
        "conversation": 10,
        "persuasion": 10,
        "deception": 10,
        "intimidation": 10,
        "empathy": 10,
        "etiquette": 10,

        "negotiation": 10,
        "commerce": 10,

        "farming": 10,
        "hunting": 10,
        "blacksmithing": 10,

        "athletics": 10,
        "combat": 10,

        "scholarship": 10,
        "observation": 10,

        "stealth": 10,
        "survival": 10,

        "leadership": 10,
    }

    def __init__(self, skills=None):

        self.values = dict(
            self.DEFAULT_SKILLS
        )

        if skills:

            for name, value in skills.items():

                self.set(
                    name,
                    value
                )

    def get(self, skill):

        return self.values.get(
            skill,
            0
        )

    def set(self, skill, value):

        self.values[skill] = self._clamp(
            value
        )

    def modify(self, skill, amount):

        current = self.get(skill)

        self.set(
            skill,
            current + amount
        )

    def has(self, skill):

        return skill in self.values

    @staticmethod
    def _clamp(value):

        return max(
            0,
            min(
                100,
                value
            )
        )

    def __getitem__(self, skill):

        return self.get(skill)

    def __setitem__(self, skill, value):

        self.set(
            skill,
            value
        )

    def __str__(self):

        return "\n".join(
            f"  {name}: {value:.1f}"
            for name, value
            in self.values.items()
        )
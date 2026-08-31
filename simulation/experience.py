# simulation/experience.py


class Experience:

    def __init__(
        self,
        category,
        description,
        duration_minutes=0,
        intensity=0.5,
        source=None
    ):

        self.category = category
        self.description = description

        self.duration_minutes = duration_minutes

        # How strongly this experience affects
        # the person's development.
        #
        # 0.0 = almost meaningless
        # 1.0 = extremely significant
        self.intensity = max(
            0.0,
            min(1.0, intensity)
        )

        self.source = source

    def __str__(self):

        return self.description
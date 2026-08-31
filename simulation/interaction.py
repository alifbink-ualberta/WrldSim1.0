# simulation/interaction.py


class Interaction:

    def __init__(
        self,
        initiator,
        target,
        interaction_type,
        description="",
        intensity=0.5
    ):

        self.initiator = initiator
        self.target = target

        self.interaction_type = interaction_type
        self.description = description

        self.intensity = max(
            0.0,
            min(1.0, intensity)
        )

    def __str__(self):

        return self.description
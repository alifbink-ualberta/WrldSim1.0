class Interaction:

    def __init__(
        self,
        actor,
        target,
        interaction_type,
        description="",
        intensity=0.5
    ):

        self.actor = actor
        self.target = target

        self.interaction_type = interaction_type
        self.description = description

        # How significant the interaction is.
        # 0.0 = negligible
        # 1.0 = extremely significant
        self.intensity = intensity
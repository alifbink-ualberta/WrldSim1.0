# simulation/circumstances.py


class Circumstance:

    def __init__(
        self,
        name,
        effects=None,
        duration=None
    ):

        # ==========================================
        # IDENTITY
        # ==========================================

        self.name = name

        # ==========================================
        # EFFECTS
        # ==========================================

        self.effects = (
            effects
            if effects is not None
            else {}
        )

        # ==========================================
        # DURATION
        # ==========================================

        self.duration = duration

    # ==================================================
    # EFFECT
    # ==================================================

    def get_effect(self, name):

        return self.effects.get(
            name,
            0.0
        )

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        return self.name
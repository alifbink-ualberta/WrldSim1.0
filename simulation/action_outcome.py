# simulation/action_outcome.py


class ActionOutcome:

    def __init__(
        self,
        action,
        success=True,
        effects=None,
        risk=0.0
    ):

        self.action = action

        self.success = success

        self.effects = (
            effects
            if effects is not None
            else {}
        )

        self.risk = risk

    def get_effect(self, name):

        return self.effects.get(
            name,
            0.0
        )

    def __str__(self):

        return (
            f"{self.action} "
            f"(success={self.success}, "
            f"risk={self.risk:.2f})"
        )
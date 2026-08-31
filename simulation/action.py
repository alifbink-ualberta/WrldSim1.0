# simulation/action.py


class Action:

    def __init__(
        self,
        action_type,
        target=None,
        location=None
    ):

        # ==========================================
        # IDENTITY
        # ==========================================

        self.action_type = action_type

        # ==========================================
        # TARGET
        # ==========================================

        self.target = target

        # ==========================================
        # LOCATION
        # ==========================================

        self.location = location

    def __str__(self):

        if self.target is not None:

            return (
                f"{self.action_type} "
                f"{self.target.full_name}"
            )

        return self.action_type
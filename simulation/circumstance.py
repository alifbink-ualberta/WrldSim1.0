# simulation/circumstance.py


class Circumstance:

    def __init__(
        self,
        name,
        description="",
        effects=None,
        motivation_effects=None,
        duration=None,
        source=None
    ):

        self.name = name
        self.description = description

        # Effects on action evaluation.
        #
        # Example:
        #
        # {
        #     "explore": -2.0,
        #     "work": 1.0
        # }
        #
        self.effects = (
            effects
            if effects is not None
            else {}
        )

        # Effects on motivations.
        #
        # Example:
        #
        # {
        #     "survival": 0.2,
        #     "security": 0.3
        # }
        #
        self.motivation_effects = (
            motivation_effects
            if motivation_effects is not None
            else {}
        )

        # None means permanent.
        self.duration = duration

        # What caused the circumstance.
        #
        # Could eventually be:
        # person, event, kingdom, religion,
        # weather, war, etc.
        #
        self.source = source

        self.active = True

    # ==================================================
    # ADVANCE
    # ==================================================

    def advance(self, minutes=1):

        if not self.active:
            return

        if self.duration is None:
            return

        self.duration -= minutes

        if self.duration <= 0:

            self.duration = 0
            self.active = False

    # ==================================================
    # REMOVE
    # ==================================================

    def remove(self):

        self.active = False

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        status = (
            "active"
            if self.active
            else "inactive"
        )

        return (
            f"{self.name} "
            f"[{status}]"
        )
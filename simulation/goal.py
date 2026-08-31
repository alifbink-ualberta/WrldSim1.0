# simulation/goal.py


class Goal:

    def __init__(
        self,
        name,
        motivation,
        priority=0.5,
        progress=0.0,
        desired_effects=None
    ):

        # ==========================================
        # IDENTITY
        # ==========================================

        self.name = name

        # ==========================================
        # MOTIVATION
        # ==========================================

        self.motivation = motivation

        # ==========================================
        # PRIORITY
        # ==========================================

        self.priority = priority

        # ==========================================
        # PROGRESS
        # ==========================================

        self.progress = progress

        # ==========================================
        # DESIRED EFFECTS
        # ==========================================

        self.desired_effects = (
            desired_effects
            if desired_effects is not None
            else {}
        )

        # ==========================================
        # STATE
        # ==========================================

        self.completed = False
        self.abandoned = False

    # ==================================================
    # PROGRESS
    # ==================================================

    def advance(self, amount):

        if self.completed or self.abandoned:
            return

        self.progress += amount

        if self.progress >= 1.0:

            self.progress = 1.0
            self.completed = True

    # ==================================================
    # ABANDON
    # ==================================================

    def abandon(self):

        if not self.completed:
            self.abandoned = True

    # ==================================================
    # DESIRED EFFECT
    # ==================================================

    def get_desired_effect(self, name):

        return self.desired_effects.get(
            name,
            0.0
        )

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        status = "active"

        if self.completed:
            status = "completed"

        elif self.abandoned:
            status = "abandoned"

        return (
            f"{self.name} "
            f"[priority={self.priority:.2f}, "
            f"progress={self.progress:.2f}, "
            f"{status}]"
        )
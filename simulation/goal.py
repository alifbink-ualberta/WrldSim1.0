# simulation/goal.py


class Goal:

    def __init__(
        self,
        name,
        motivation,
        priority=0.5,
        progress=0.0
    ):

        self.name = name
        self.motivation = motivation
        self.priority = priority
        self.progress = progress

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
# simulation/goal.py


class Goal:

    def __init__(
        self,
        description,
        motivation,
        priority=0.5,
        target=None,
        desired_effects=None
    ):

        self.description = description

        self.motivation = motivation

        self.priority = max(
            0.0,
            min(1.0, priority)
        )

        self.target = target

        self.desired_effects = (
            desired_effects
            if desired_effects is not None
            else {}
        )

        self.completed = False
        self.failed = False

    # ==================================================
    # EFFECT
    # ==================================================

    def get_desired_effect(
        self,
        effect_name
    ):

        return self.desired_effects.get(
            effect_name,
            0.0
        )

    # ==================================================
    # COMPLETE / FAIL
    # ==================================================

    def complete(self):

        self.completed = True

    def fail(self):

        self.failed = True

    # ==================================================
    # STATUS
    # ==================================================

    def is_active(self):

        return (
            not self.completed
            and not self.failed
        )

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        status = "active"

        if self.completed:
            status = "completed"

        elif self.failed:
            status = "failed"

        return (
            f"{self.description} "
            f"[{status}, "
            f"priority={self.priority:.2f}]"
        )
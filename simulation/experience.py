# simulation/experience.py


class Experience:

    def __init__(
        self,
        subject,
        experience_type,
        description,
        intensity=0.5,
        source=None,
        target=None,
        data=None
    ):

        # ==========================================
        # PARTICIPANT
        # ==========================================

        self.subject = subject

        # ==========================================
        # TYPE
        # ==========================================

        self.experience_type = experience_type

        # Human-readable description.
        self.description = description

        # 0.0 - 1.0
        self.intensity = max(
            0.0,
            min(1.0, intensity)
        )

        # ==========================================
        # CONTEXT
        # ==========================================

        self.source = source
        self.target = target

        self.data = (
            data
            if data is not None
            else {}
        )

        # ==========================================
        # STATE
        # ==========================================

        self.processed = False

    # ==============================================
    # DEBUGGING
    # ==============================================

    def __str__(self):

        return (
            f"{self.subject.full_name} "
            f"experienced: "
            f"{self.description}"
        )
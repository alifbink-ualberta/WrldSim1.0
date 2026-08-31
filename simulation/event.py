# simulation/event.py


class Event:

    def __init__(
        self,
        world,
        event_type,
        description="",
        participants=None,
        location=None,
        significance=0.0
    ):

        self.world = world

        # =========================
        # IDENTITY
        # =========================

        self.event_type = event_type
        self.description = description

        # =========================
        # PARTICIPANTS
        # =========================

        self.participants = (
            participants
            if participants is not None
            else []
        )

        # =========================
        # LOCATION
        # =========================

        self.location = location

        # =========================
        # SIGNIFICANCE
        # =========================

        self.significance = significance

        # =========================
        # TIME
        # =========================

        self.year = world.year
        self.month = world.month
        self.day = world.day
        self.hour = world.hour
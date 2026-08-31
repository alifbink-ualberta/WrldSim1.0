# simulation/event.py


class Event:

    def __init__(
        self,
        name,
        description="",
        event_type="generic",
        participants=None,
        location=None,
        cause=None
    ):

        # ==========================================
        # IDENTITY
        # ==========================================

        self.name = name
        self.description = description
        self.event_type = event_type

        # ==========================================
        # PARTICIPANTS
        # ==========================================

        self.participants = (
            participants
            if participants is not None
            else []
        )

        # ==========================================
        # OBSERVERS
        # ==========================================

        self.observers = []

        # ==========================================
        # LOCATION
        # ==========================================

        self.location = location

        # ==========================================
        # CAUSE
        # ==========================================

        self.cause = cause

        # ==========================================
        # WORLD TIME
        # ==========================================

        self.year = None
        self.month = None
        self.day = None
        self.hour = None
        self.minute = None

        # ==========================================
        # STATE
        # ==========================================

        self.resolved = False

    # ==============================================
    # PARTICIPANTS
    # ==============================================

    def add_participant(self, person):

        if person not in self.participants:

            self.participants.append(person)


    # ==============================================
    # OBSERVERS
    # ==============================================

    def add_observer(self, person):

        if person not in self.observers:

            self.observers.append(person)

    # ==============================================
    # TIMESTAMP
    # ==============================================

    def set_time(self, world):

        self.year = world.year
        self.month = world.month
        self.day = world.day
        self.hour = world.hour
        self.minute = world.minute

    # ==============================================
    # RESOLUTION
    # ==============================================

    def resolve(self):

        self.resolved = True

    # ==============================================
    # DEBUGGING
    # ==============================================

    def __str__(self):

        return self.name
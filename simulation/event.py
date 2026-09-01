# simulation/event.py


class Event:

    def __init__(
        self,
        event_type,
        description,
        participants=None,
        actor=None,
        target=None,
        significance=0.5
    ):

        self.event_type = event_type

        self.description = description

        self.participants = (
            participants
            if participants is not None
            else []
        )

        self.actor = actor
        self.target = target

        # 0.0 - 1.0
        self.significance = max(
            0.0,
            min(1.0, significance)
        )

        # Filled in when the world processes it.
        self.resolved = False

        # Interpretations created by observers.
        self.interpretations = []

        # Memories created from this event.
        self.memories = []

    # ==================================================
    # PARTICIPANTS
    # ==================================================

    def add_participant(self, person):

        if person not in self.participants:

            self.participants.append(
                person
            )

    # ==================================================
    # INTERPRETATION
    # ==================================================

    def add_interpretation(
        self,
        interpretation
    ):

        self.interpretations.append(
            interpretation
        )

    # ==================================================
    # MEMORY
    # ==================================================

    def add_memory(
        self,
        memory
    ):

        self.memories.append(
            memory
        )

    # ==================================================
    # RESOLUTION
    # ==================================================

    def resolve(self):

        self.resolved = True

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        return self.description
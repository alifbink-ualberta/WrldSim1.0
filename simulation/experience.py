# simulation/experience.py


class Experience:

    def __init__(
        self,
        person,
        event_type,
        description,
        participants=None,
        intensity=0.5
    ):

        self.person = person

        self.event_type = event_type
        self.description = description

        self.participants = (
            participants
            if participants is not None
            else []
        )

        self.intensity = intensity
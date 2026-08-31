# simulation/perception.py


class Perception:

    def __init__(
        self,
        observer,
        event,
        noticed=True,
        clarity=1.0,
        source=None
    ):

        self.observer = observer
        self.event = event

        # Did the person actually notice the event?
        self.noticed = noticed

        # How clearly did they perceive it?
        # 0.0 = barely understood
        # 1.0 = completely clear
        self.clarity = max(
            0.0,
            min(1.0, clarity)
        )

        # Who/what did the person believe
        # caused the event?
        self.source = source

    def __str__(self):

        if not self.noticed:
            return (
                f"{self.observer.full_name} "
                f"did not notice the event."
            )

        return (
            f"{self.observer.full_name} "
            f"noticed the event "
            f"(clarity={self.clarity:.2f})."
        )
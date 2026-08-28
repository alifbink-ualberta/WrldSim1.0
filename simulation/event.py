from dataclasses import dataclass


@dataclass
class Event:

    day: int
    hour: int
    description: str

    def __str__(self):

        return (
            f"[Day {self.day} "
            f"{self.hour:02d}:00] "
            f"{self.description}"
        )
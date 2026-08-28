from dataclasses import dataclass, field


@dataclass
class Event:

    year: int
    month: int
    day: int

    description: str

    participants: list[str] = field(
        default_factory=list
    )

    location: str = ""

    importance: int = 50

    def __str__(self):

        date = (
            f"Year {self.year}, "
            f"Month {self.month}, "
            f"Day {self.day}"
        )

        return f"[{date}] {self.description}"
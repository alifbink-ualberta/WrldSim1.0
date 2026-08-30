from dataclasses import dataclass, field


@dataclass
class ActionResult:

    success: bool

    description: str

    score: float = 0

    consequences: list = field(
        default_factory=list
    )

    memories: list = field(
        default_factory=list
    )

    events: list = field(
        default_factory=list
    )

    def __str__(self):

        return self.description
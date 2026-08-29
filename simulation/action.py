from dataclasses import dataclass
from typing import Optional


@dataclass
class Action:

    actor: object
    action_type: str

    target: Optional[object] = None
    reason: Optional[str] = None

    item: Optional[str] = None
    amount: int = 0
    price: float = 0

    def __str__(self):

        target = ""

        if self.target:
            target = (
                f" → {self.target.name}"
            )

        item = ""

        if self.item:
            item = (
                f" | {self.amount} "
                f"{self.item}"
            )

        return (
            f"{self.actor.name} "
            f"{self.action_type}"
            f"{target}"
            f"{item}"
        )
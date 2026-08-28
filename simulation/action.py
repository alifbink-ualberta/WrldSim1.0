from dataclasses import dataclass
from typing import Optional


@dataclass
class Action:

    actor: object
    action_type: str

    target: Optional[object] = None
    reason: Optional[str] = None

    def __str__(self):

        target_name = ""

        if self.target:
            target_name = f" → {self.target.name}"

        return (
            f"{self.actor.name} "
            f"{self.action_type}"
            f"{target_name}"
        )
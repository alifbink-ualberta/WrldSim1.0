from dataclasses import dataclass


@dataclass
class Activity:

    action: object
    remaining_minutes: int

    @property
    def actor(self):
        return self.action.actor

    @property
    def action_type(self):
        return self.action.action_type

    def advance(self, minutes):
        self.remaining_minutes -= minutes

    def is_finished(self):
        return self.remaining_minutes <= 0

    def __str__(self):
        return (
            f"{self.actor.name} is "
            f"{self.action_type}"
        )
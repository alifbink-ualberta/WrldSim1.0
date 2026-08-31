# systems/event_system.py


class EventSystem:

    @staticmethod
    def create_event(
        world,
        name,
        description="",
        event_type="generic",
        participants=None,
        location=None,
        cause=None
    ):

        from simulation.event import Event

        event = Event(
            name=name,
            description=description,
            event_type=event_type,
            participants=participants,
            location=location,
            cause=cause
        )

        # Give the event its world timestamp.

        event.set_time(world)

        # Add it to world history.

        world.events.append(event)

        return event
# systems/event_system.py


class EventSystem:

    @staticmethod
    def create_event(
        world,
        name,
        description="",
        participants=None,
        location=None,
        cause=None
    ):

        from simulation.event import Event

        event = Event(
            name=name,
            description=description,
            participants=participants,
            location=location,
            cause=cause
        )

        # Give the event its world timestamp.

        event.set_time(world)

        # Add it to the world's event history.

        world.events.append(event)

        return event
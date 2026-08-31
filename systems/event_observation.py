# systems/event_observation.py


class EventObservationSystem:

    # ==============================================
    # FIND PEOPLE WHO EXPERIENCE AN EVENT
    # ==============================================

    @staticmethod
    def get_observers(event, world):

        observers = []

        for participant in event.participants:

            for person in world.people:

                # Dead people cannot experience new events.

                if not person.is_alive:
                    continue

                # The participant themselves is only an
                # observer if they survive the event.

                if person is participant:

                    if event.event_type == "death":
                        continue

                    if person not in observers:
                        observers.append(person)

                    continue

                # People connected to the participant
                # become aware of the event.

                if participant in person.relationships:

                    if person not in observers:
                        observers.append(person)

        return observers

    # ==============================================
    # OBSERVE ONE EVENT
    # ==============================================

    @staticmethod
    def observe(event, person, world):

        if not person.is_alive:
            return None

        observers = (
            EventObservationSystem.get_observers(
                event,
                world
            )
        )

        if person not in observers:
            return None

        # ==========================================
        # INTERPRET
        # ==========================================

        from systems.interpretation import interpret_event

        interpretation = interpret_event(
            person,
            event
        )

        # ==========================================
        # RETURN OBSERVATION
        # ==========================================

        return {
            "person": person,
            "event": event,
            "interpretation": interpretation
        }

    # ==============================================
    # OBSERVE EVENT FOR EVERYONE
    # ==============================================

    @staticmethod
    def observe_all(event, world):

        observations = []

        observers = (
            EventObservationSystem.get_observers(
                event,
                world
            )
        )

        for person in observers:

            observation = (
                EventObservationSystem.observe(
                    event,
                    person,
                    world
                )
            )

            if observation is not None:

                observations.append(
                    observation
                )

        return observations
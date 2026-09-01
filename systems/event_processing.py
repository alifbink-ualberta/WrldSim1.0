# systems/event_processing.py


from systems.relationship_effects import (
    RelationshipEffectSystem
)


class EventProcessingSystem:

    """
    Central event-processing pipeline.

    Every important event eventually passes through
    this system.

    This is deliberately separate from Event itself.

    Event = what happened.

    EventProcessingSystem = what the world does
    with what happened.
    """

    @staticmethod
    def process(
        event,
        world
    ):

        # ==========================================
        # OBSERVERS
        # ==========================================

        observers = (
            EventProcessingSystem
            .find_observers(
                event,
                world
            )
        )

        # ==========================================
        # EACH PERSON EXPERIENCES THE EVENT
        # ==========================================

        for person in observers:

            if not person.is_alive:
                continue

            interpretation = (
                person.perceive_event(
                    event
                )
            )

            if interpretation is None:
                continue

            event.add_interpretation(
                interpretation
            )

            # --------------------------------------
            # PSYCHOLOGICAL RESPONSE
            # --------------------------------------

            person.respond_to_interpretation(
                interpretation
            )

            # --------------------------------------
            # MEMORY
            # --------------------------------------

            EventProcessingSystem.create_memory(
                person,
                event,
                interpretation
            )

            # --------------------------------------
            # RELATIONSHIP
            # --------------------------------------

            other = (
                EventProcessingSystem
                .find_relevant_other(
                    person,
                    event
                )
            )

            if other is not None:

                RelationshipEffectSystem.apply(
                    person,
                    other,
                    interpretation
                )

        # ==========================================
        # RESOLVE
        # ==========================================

        event.resolve()

        return event

    # ==================================================
    # OBSERVERS
    # ==================================================

    @staticmethod
    def find_observers(
        event,
        world
    ):

        observers = []

        # Direct participants always observe.
        for person in event.participants:

            if person not in observers:

                observers.append(
                    person
                )

        # ------------------------------------------
        # SAME LOCATION
        # ------------------------------------------

        for person in world.people:

            if person in observers:
                continue

            if not person.is_alive:
                continue

            if (
                person.location is not None
                and event.actor is not None
                and event.actor.location
                == person.location
            ):

                observers.append(
                    person
                )

        return observers

    # ==================================================
    # FIND OTHER
    # ==================================================

    @staticmethod
    def find_relevant_other(
        person,
        event
    ):

        # Prefer the actor if the observer is target.
        if (
            event.actor is not None
            and event.actor != person
        ):

            return event.actor

        # Otherwise target.
        if (
            event.target is not None
            and event.target != person
        ):

            return event.target

        # Finally search participants.
        for participant in event.participants:

            if participant != person:

                return participant

        return None

    # ==================================================
    # MEMORY
    # ==================================================

    @staticmethod
    def create_memory(
        person,
        event,
        interpretation
    ):

        memory = person.remember(
            interpretation,
            emotional_significance=(
                interpretation.emotional_impact
            )
        )

        event.add_memory(
            memory
        )

        return memory

# systems/social_interaction.py


from simulation.event import Event


class SocialInteractionSystem:

    """
    Creates social events between people.

    An interaction does not directly modify psychology.

    Instead:

        interaction
            ↓
        event
            ↓
        each participant perceives it
            ↓
        each participant interprets it
            ↓
        psychological consequences
    """

    @staticmethod
    def perform(
        actor,
        target,
        interaction_type,
        world,
        intensity=0.5
    ):

        if actor is None:
            return None

        if target is None:
            return None

        if actor == target:
            return None

        # ==========================================
        # EVENT DESCRIPTION
        # ==========================================

        description = (
            f"{actor.full_name} "
            f"{interaction_type} "
            f"{target.full_name}."
        )

        # ==========================================
        # EVENT
        # ==========================================

        event = Event(
            event_type=interaction_type,
            description=description,
            participants=[
                actor,
                target
            ],
            actor=actor,
            target=target,
            significance=intensity
        )

        # ==========================================
        # REGISTER EVENT
        # ==========================================

        world.events.append(
            event
        )

        # ==========================================
        # PROCESS EVENT
        # ==========================================

        from systems.event_processing import (
            EventProcessingSystem
        )

        EventProcessingSystem.process(
            event,
            world
        )

        return event


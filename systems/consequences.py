# systems/consequences.py


from systems.relationship_evolution import (
    RelationshipEvolutionSystem
)


class ConsequenceSystem:

    @staticmethod
    def apply(
        actor,
        target,
        event,
        world
    ):

        consequences = []

        # ==========================================
        # EVENT HISTORY
        # ==========================================

        if event not in world.events:

            world.events.append(
                event
            )

        # ==========================================
        # PARTICIPANTS
        # ==========================================

        participants = (
            event.participants
            if hasattr(
                event,
                "participants"
            )
            else []
        )

        # ==========================================
        # PSYCHOLOGICAL CONSEQUENCES
        # ==========================================

        for person in participants:

            if not person.is_alive:
                continue

            interpretation = (
                person.perceive_event(
                    event
                )
            )

            consequences.append(
                interpretation
            )

            response = (
                person.respond_to_interpretation(
                    interpretation
                )
            )

            consequences.append(
                response
            )

            # ======================================
            # RELATIONSHIP CONSEQUENCES
            # ======================================

            for other in participants:

                if other == person:
                    continue

                RelationshipEvolutionSystem.process(
                    person,
                    other,
                    event,
                    interpretation,
                    response
                )

            # ======================================
            # EXPERIENCE
            # ======================================

            person.add_experience(
                event
            )

        return consequences

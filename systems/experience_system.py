# systems/experience_system.py


class ExperienceSystem:

    # ==============================================
    # PROCESS EVENT EXPERIENCES
    # ==============================================

    @staticmethod
    def process_event(event, world):

        from systems.event_observation import (
            EventObservationSystem
        )

        observations = (
            EventObservationSystem.observe_all(
                event,
                world
            )
        )

        experiences = []

        for observation in observations:

            person = observation["person"]

            interpretation = (
                observation["interpretation"]
            )

            # ======================================
            # DETERMINE EMOTIONAL SIGNIFICANCE
            # ======================================

            significance = (
                ExperienceSystem
                .calculate_significance(
                    person,
                    event,
                    interpretation
                )
            )

            # ======================================
            # CREATE MEMORY
            # ======================================

            memory = person.remember(
                event,
                emotional_significance=significance
            )

            experiences.append({
                "person": person,
                "event": event,
                "interpretation": interpretation,
                "significance": significance,
                "memory": memory
            })

        return experiences

    # ==============================================
    # EMOTIONAL SIGNIFICANCE
    # ==============================================

    @staticmethod
    def calculate_significance(
        person,
        event,
        interpretation
    ):

        significance = 0.5

        # ==========================================
        # RELATIONSHIP TO PARTICIPANT
        # ==========================================

        for participant in event.participants:

            relationship = (
                person.relationships.get(
                    participant
                )
            )

            if relationship is None:
                continue

            feelings = (
                relationship.get_feelings(
                    person
                )
            )

            # Affection makes the event matter more.

            significance += (
                feelings["affection"] * 0.3
            )

            # Resentment can also make an event
            # psychologically significant.

            significance += (
                feelings["resentment"] * 0.2
            )

            # Fear increases significance.

            significance += (
                feelings["fear"] * 0.2
            )

        # ==========================================
        # CLAMP
        # ==========================================

        significance = max(
            0.0,
            min(
                1.0,
                significance
            )
        )

        return significance
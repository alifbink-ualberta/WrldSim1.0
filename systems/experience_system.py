# systems/experience_system.py


from simulation.experience import Experience


class ExperienceSystem:

    """
    The bridge between objective world events and
    subjective psychological experience.

    An event exists objectively in the world.

    Different people may:
        - observe it
        - interpret it differently
        - experience it differently
        - remember it differently

    Pipeline:

        Event
          ↓
        Observation
          ↓
        Interpretation
          ↓
        Experience
          ↓
        Psychological Response
          ↓
        Memory / Emotion / Motivation
    """

    # ==================================================
    # PROCESS EVENT
    # ==================================================

    @staticmethod
    def process_event(
        event,
        world
    ):

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

            if not person.is_alive:
                continue

            interpretation = (
                observation["interpretation"]
            )

            # ------------------------------------------
            # SIGNIFICANCE
            # ------------------------------------------

            significance = (
                ExperienceSystem
                .calculate_significance(
                    person,
                    event,
                    interpretation
                )
            )

            # ------------------------------------------
            # CREATE SUBJECTIVE EXPERIENCE
            # ------------------------------------------

            experience = Experience(
                subject=person,
                experience_type=event.event_type,
                description=event.description,
                intensity=significance,
                source=event,
                target=(
                    ExperienceSystem
                    .find_target(
                        person,
                        event
                    )
                ),
                data={
                    "interpretation": interpretation
                }
            )

            # ------------------------------------------
            # STORE EXPERIENCE
            # ------------------------------------------

            person.add_experience(
                experience
            )

            # ------------------------------------------
            # PSYCHOLOGICAL RESPONSE
            # ------------------------------------------

            response = (
                person.respond_to_interpretation(
                    interpretation
                )
            )

            # ------------------------------------------
            # PSYCHOLOGICAL FEEDBACK
            # ------------------------------------------

            from systems.psychological_feedback import (
                PsychologicalFeedbackSystem
            )

            feedback = (
                PsychologicalFeedbackSystem.process(
                    person,
                    experience,
                    interpretation,
                    response
                )
            )

            # ------------------------------------------
            # MEMORY
            # ------------------------------------------

            memory = None

            # The psychological response may determine
            # whether and how strongly the experience
            # becomes a memory.
            #
            # Until memory consolidation becomes its own
            # system, we use significance directly.

            memory = person.remember(
                event,
                emotional_significance=significance
            )

            experiences.append(
                {
                    "person": person,
                    "event": event,
                    "experience": experience,
                    "interpretation": interpretation,
                    "response": response,
                    "feedback": feedback,
                    "significance": significance,
                    "memory": memory
                }
            )

        return experiences

    # ==================================================
    # FIND TARGET
    # ==================================================

    @staticmethod
    def find_target(
        person,
        event
    ):

        for participant in event.participants:

            if participant != person:

                return participant

        return None

    # ==================================================
    # SIGNIFICANCE
    # ==================================================

    @staticmethod
    def calculate_significance(
        person,
        event,
        interpretation
    ):

        # ----------------------------------------------
        # BASE
        # ----------------------------------------------

        significance = (
            getattr(
                interpretation,
                "emotional_impact",
                event.significance
            )
        )

        # ----------------------------------------------
        # RELATIONSHIPS
        # ----------------------------------------------

        for participant in event.participants:

            if participant == person:
                continue

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

            # Affection
            significance += (
                feelings["affection"]
                * 0.15
            )

            # Resentment
            significance += (
                feelings["resentment"]
                * 0.10
            )

            # Fear
            significance += (
                feelings["fear"]
                * 0.15
            )

            # Trust makes positive and negative
            # actions involving the person matter more.
            significance += (
                feelings["trust"]
                * 0.05
            )

        # ----------------------------------------------
        # CLAMP
        # ----------------------------------------------

        return max(
            0.0,
            min(
                1.0,
                significance
            )
        )

    # ==================================================
    # ACTION → EVENT
    # ==================================================

    @staticmethod
    def action_to_event(
        person,
        action,
        outcome,
        result,
        world
    ):

        from simulation.event import Event

        target = getattr(
            action,
            "target",
            None
        )

        participants = [
            person
        ]

        if target is not None:

            participants.append(
                target
            )

        description = (
            f"{person.full_name} "
            f"{ExperienceSystem.action_description(action)}"
        )

        return Event(
            event_type=action.action_type,
            description=description,
            participants=participants,
            significance=(
                ExperienceSystem
                .action_significance(
                    action
                )
            )
        )

    # ==================================================
    # ACTION DESCRIPTION
    # ==================================================

    @staticmethod
    def action_description(
        action
    ):

        descriptions = {

            "eat":
                "ate.",

            "drink":
                "drank.",

            "sleep":
                "went to sleep.",

            "work":
                "worked.",

            "practice":
                "practiced a skill.",

            "explore":
                "explored.",

            "socialize":
                "socialized with someone.",

            "visit":
                "visited someone.",

            "confront":
                "confronted someone.",

            "avoid":
                "avoided someone."
        }

        return descriptions.get(
            action.action_type,
            f"performed {action.action_type}."
        )

    # ==================================================
    # ACTION SIGNIFICANCE
    # ==================================================

    @staticmethod
    def action_significance(
        action
    ):

        if action.action_type in (
            "confront",
        ):

            return 0.6

        if action.action_type in (
            "socialize",
            "visit"
        ):

            return 0.4

        if action.action_type in (
            "work",
            "practice",
            "explore"
        ):

            return 0.3

        return 0.15
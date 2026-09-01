# systems/psychological_feedback.py


class PsychologicalFeedbackSystem:

    """
    Converts psychological experiences into persistent
    changes in the person.

    This is one of the core feedback loops of WrldSim.

        Experience
            ↓
        Emotional Response
            ↓
        Memory
            ↓
        Motivation
            ↓
        Goals
            ↓
        Future Behaviour
    """

    # ==================================================
    # PROCESS
    # ==================================================

    @staticmethod
    def process(
        person,
        experience,
        interpretation,
        response
    ):

        if not person.is_alive:
            return []

        changes = []

        # ==============================================
        # EMOTION
        # ==============================================

        emotional_changes = (
            PsychologicalFeedbackSystem
            .apply_emotional_response(
                person,
                interpretation,
                response
            )
        )

        changes.extend(
            emotional_changes
        )

        # ==============================================
        # MEMORY
        # ==============================================

        memory_change = (
            PsychologicalFeedbackSystem
            .process_memory(
                person,
                experience
            )
        )

        if memory_change is not None:

            changes.append(
                memory_change
            )

        # ==============================================
        # MOTIVATION
        # ==============================================

        motivation_changes = (
            PsychologicalFeedbackSystem
            .update_motivations(
                person,
                interpretation,
                response
            )
        )

        changes.extend(
            motivation_changes
        )

        return changes

    # ==================================================
    # EMOTIONAL RESPONSE
    # ==================================================

    @staticmethod
    def apply_emotional_response(
        person,
        interpretation,
        response
    ):

        changes = []

        if response is None:
            return changes

        # The response system determines the emotional
        # reaction. We deliberately don't hard-code
        # specific emotions here.

        emotions = getattr(
            response,
            "emotions",
            {}
        )

        for emotion_name, intensity in (
            emotions.items()
        ):

            if hasattr(
                person.emotions,
                emotion_name
            ):

                current = getattr(
                    person.emotions,
                    emotion_name
                )

                setattr(
                    person.emotions,
                    emotion_name,
                    max(
                        0.0,
                        min(
                            1.0,
                            current + intensity
                        )
                    )
                )

                changes.append(
                    {
                        "type": "emotion",
                        "emotion": emotion_name,
                        "amount": intensity
                    }
                )

        return changes

    # ==================================================
    # MEMORY
    # ==================================================

    @staticmethod
    def process_memory(
        person,
        experience
    ):

        if experience.intensity < 0.2:
            return None

        # Memory consolidation will eventually become
        # much more sophisticated:
        #
        # repetition
        # emotional intensity
        # novelty
        # trauma
        # age
        # personality
        # recency
        # importance
        #
        # For now, the experience remains available
        # through the existing memory system.

        return {
            "type": "memory",
            "importance": experience.intensity
        }

    # ==================================================
    # MOTIVATIONS
    # ==================================================

    @staticmethod
    def update_motivations(
        person,
        interpretation,
        response
    ):

        changes = []

        if response is None:
            return changes

        emotions = getattr(
            response,
            "emotions",
            {}
        )

        # ----------------------------------------------
        # FEAR → SECURITY
        # ----------------------------------------------

        fear = emotions.get(
            "fear",
            0.0
        )

        if fear > 0.3:

            from simulation.motivation import (
                MotivationSystem
            )

            motivation = (
                MotivationSystem.strengthen(
                    person,
                    "security",
                    fear * 0.05,
                    source="experience"
                )
            )

            changes.append(
                {
                    "type": "motivation",
                    "motivation": "security",
                    "amount": fear * 0.05
                }
            )

        # ----------------------------------------------
        # ANGER → POWER
        # ----------------------------------------------

        anger = emotions.get(
            "anger",
            0.0
        )

        if anger > 0.3:

            from simulation.motivation import (
                MotivationSystem
            )

            MotivationSystem.strengthen(
                person,
                "power",
                anger * 0.03,
                source="experience"
            )

            changes.append(
                {
                    "type": "motivation",
                    "motivation": "power",
                    "amount": anger * 0.03
                }
            )

        # ----------------------------------------------
        # SADNESS → CONNECTION
        # ----------------------------------------------

        sadness = emotions.get(
            "sadness",
            0.0
        )

        if sadness > 0.3:

            from simulation.motivation import (
                MotivationSystem
            )

            MotivationSystem.strengthen(
                person,
                "social_connection",
                sadness * 0.02,
                source="experience"
            )

            changes.append(
                {
                    "type": "motivation",
                    "motivation":
                        "social_connection",
                    "amount":
                        sadness * 0.02
                }
            )

        return changes
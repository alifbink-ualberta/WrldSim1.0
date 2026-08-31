# systems/psychological_response.py


class PsychologicalResponseSystem:

    # ==================================================
    # PROCESS INTERPRETATION
    # ==================================================

    @staticmethod
    def process(
        person,
        interpretation
    ):

        impact = interpretation.emotional_impact

        event = interpretation.event

        # ==========================================
        # EMOTIONAL RESPONSE
        # ==========================================

        emotion_result = (
            PsychologicalResponseSystem
            .process_emotion(
                person,
                event,
                impact
            )
        )

        # ==========================================
        # RELATIONSHIP RESPONSE
        # ==========================================

        relationship_result = (
            PsychologicalResponseSystem
            .process_relationship(
                person,
                interpretation
            )
        )

        # ==========================================
        # MEMORY
        # ==========================================

        memory_result = (
            PsychologicalResponseSystem
            .process_memory(
                person,
                interpretation,
                impact
            )
        )

        return {
            "emotion": emotion_result,
            "relationship": relationship_result,
            "memory": memory_result
        }

    # ==================================================
    # EMOTION
    # ==================================================

    @staticmethod
    def process_emotion(
        person,
        event,
        impact
    ):

        event_type = event.event_type

        # We don't yet have a complete emotion
        # model, so for now we translate the event
        # into broad emotional tendencies.

        emotion = None

        if event_type == "insult":

            emotion = "anger"

        elif event_type == "compliment":

            emotion = "happiness"

        elif event_type == "help":

            emotion = "gratitude"

        elif event_type == "threat":

            emotion = "fear"

        elif event_type == "gift":

            emotion = "gratitude"

        elif event_type == "betrayal":

            emotion = "anger"

        elif event_type == "death":

            emotion = "grief"

        # ==========================================
        # EMOTIONAL STATE
        # ==========================================

        if (
            emotion is not None
            and hasattr(person, "emotions")
        ):

            # This assumes EmotionalState will
            # eventually expose a generic method
            # for changing an emotion.

            if hasattr(
                person.emotions,
                "add_emotion"
            ):

                person.emotions.add_emotion(
                    emotion,
                    impact
                )

        return {
            "emotion": emotion,
            "intensity": impact
        }

    # ==================================================
    # RELATIONSHIP
    # ==================================================

    @staticmethod
    def process_relationship(
        person,
        interpretation
    ):

        event = interpretation.event

        other = None

        # ==========================================
        # FIND OTHER PARTICIPANT
        # ==========================================

        for participant in event.participants:

            if participant != person:

                other = participant
                break

        if other is None:

            return None

        relationship = (
            person.get_relationship(
                other
            )
        )

        impact = (
            interpretation.emotional_impact
        )

        event_type = event.event_type

        # ==========================================
        # INSULT
        # ==========================================

        if event_type == "insult":

            relationship.resentment[
                person
            ] += 0.10 * impact

            relationship.affection[
                person
            ] -= 0.05 * impact

            relationship.respect[
                person
            ] -= 0.03 * impact

        # ==========================================
        # HELP
        # ==========================================

        elif event_type == "help":

            relationship.trust[
                person
            ] += 0.07 * impact

            relationship.affection[
                person
            ] += 0.05 * impact

        # ==========================================
        # THREAT
        # ==========================================

        elif event_type == "threat":

            relationship.fear[
                person
            ] += 0.10 * impact

            relationship.trust[
                person
            ] -= 0.06 * impact

            relationship.resentment[
                person
            ] += 0.04 * impact

        # ==========================================
        # BETRAYAL
        # ==========================================

        elif event_type == "betrayal":

            relationship.trust[
                person
            ] -= 0.15 * impact

            relationship.affection[
                person
            ] -= 0.10 * impact

            relationship.resentment[
                person
            ] += 0.15 * impact

        # ==========================================
        # GIFT
        # ==========================================

        elif event_type == "gift":

            relationship.affection[
                person
            ] += 0.04 * impact

            relationship.trust[
                person
            ] += 0.02 * impact

        # ==========================================
        # LIMIT VALUES
        # ==========================================

        for feeling in [
            "affection",
            "trust",
            "respect",
            "fear",
            "resentment",
            "attraction",
            "familiarity"
        ]:

            values = getattr(
                relationship,
                feeling
            )

            values[person] = max(
                0.0,
                min(
                    100.0,
                    values[person]
                )
            )

        return {
            "other": other,
            "event": event_type
        }

    # ==================================================
    # MEMORY
    # ==================================================

    @staticmethod
    def process_memory(
        person,
        interpretation,
        impact
    ):

        # Significant experiences are remembered.

        if impact < 0.25:

            return {
                "remembered": False
            }

        event = interpretation.event

        # Your existing Person.remember()
        # expects an Experience object.
        #
        # We therefore leave actual memory
        # construction to the existing memory
        # architecture for now.

        return {
            "remembered": True,
            "significance": impact
        }
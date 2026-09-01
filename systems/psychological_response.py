# systems/psychological_response.py


from simulation.motivation import MotivationSystem


class PsychologicalResponseSystem:

    @staticmethod
    def process(
        person,
        interpretation
    ):

        event = interpretation.event
        impact = interpretation.emotional_impact

        event_type = event.event_type

        # ==========================================
        # EMOTIONS
        # ==========================================

        emotions = person.emotions

        if event_type == "insult":

            emotions.change(
                "anger",
                impact * 0.8
            )

            emotions.change(
                "shame",
                impact * 0.5
            )

            emotions.change(
                "pride",
                -impact * 0.3
            )

        elif event_type == "compliment":

            emotions.change(
                "happiness",
                impact * 0.7
            )

            emotions.change(
                "pride",
                impact * 0.6
            )

            emotions.change(
                "contentment",
                impact * 0.3
            )

        elif event_type == "help":

            emotions.change(
                "happiness",
                impact * 0.5
            )

            emotions.change(
                "contentment",
                impact * 0.4
            )

        elif event_type == "gift":

            emotions.change(
                "happiness",
                impact * 0.5
            )

            emotions.change(
                "contentment",
                impact * 0.4
            )

        elif event_type == "threat":

            emotions.change(
                "fear",
                impact * 0.9
            )

            emotions.change(
                "anger",
                impact * 0.3
            )

        elif event_type == "betrayal":

            emotions.change(
                "anger",
                impact * 0.7
            )

            emotions.change(
                "sadness",
                impact * 0.5
            )

            emotions.change(
                "fear",
                impact * 0.3
            )

        elif event_type == "death":

            emotions.change(
                "grief",
                impact
            )

            emotions.change(
                "sadness",
                impact * 0.8
            )

            emotions.change(
                "loneliness",
                impact * 0.4
            )

        # ==========================================
        # EMOTIONS → MOTIVATIONS
        # ==========================================

        MotivationSystem.update_from_emotions(
            person
        )

        # ==========================================
        # MEMORY
        # ==========================================

        person.remember(
            event,
            emotional_significance=impact
        )

        # ==========================================
        # DEVELOPMENT
        # ==========================================

        person.add_experience(
            event
        )

        return emotions
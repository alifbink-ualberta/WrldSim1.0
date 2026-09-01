# simulation/motivation.py


class Motivation:

    def __init__(
        self,
        name,
        strength=0.5,
        source="internal"
    ):

        self.name = name

        self.strength = max(
            0.0,
            min(1.0, strength)
        )

        self.source = source

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.strength:.2f})"
        )


class MotivationSystem:

    # ==================================================
    # GENERATION
    # ==================================================

    @staticmethod
    def generate(person):

        personality = person.personality

        return [

            Motivation(
                "survival",
                0.8,
                "biological"
            ),

            Motivation(
                "exploration",
                personality.openness,
                "personality"
            ),

            Motivation(
                "achievement",
                personality.conscientiousness,
                "personality"
            ),

            Motivation(
                "social_connection",
                personality.extraversion,
                "personality"
            ),

            Motivation(
                "harmony",
                personality.agreeableness,
                "personality"
            ),

            Motivation(
                "security",
                personality.neuroticism,
                "personality"
            ),

            Motivation(
                "power",
                (
                    personality.machiavellianism
                    + personality.narcissism
                ) / 2,
                "personality"
            ),

            Motivation(
                "status",
                personality.narcissism,
                "personality"
            ),

            Motivation(
                "independence",
                (
                    personality.openness
                    + personality.machiavellianism
                ) / 2,
                "personality"
            )
        ]

    # ==================================================
    # GET
    # ==================================================

    @staticmethod
    def get(
        person,
        motivation_name
    ):

        for motivation in person.motivations:

            if motivation.name == motivation_name:
                return motivation

        return None

    # ==================================================
    # STRENGTHEN
    # ==================================================

    @staticmethod
    def strengthen(
        person,
        motivation_name,
        amount,
        source="circumstance"
    ):

        motivation = MotivationSystem.get(
            person,
            motivation_name
        )

        if motivation is None:

            motivation = Motivation(
                motivation_name,
                0.0,
                source
            )

            person.motivations.append(
                motivation
            )

        motivation.strength = max(
            0.0,
            min(
                1.0,
                motivation.strength + amount
            )
        )

        return motivation

    # ==================================================
    # WEAKEN
    # ==================================================

    @staticmethod
    def weaken(
        person,
        motivation_name,
        amount
    ):

        motivation = MotivationSystem.get(
            person,
            motivation_name
        )

        if motivation is None:
            return None

        motivation.strength = max(
            0.0,
            motivation.strength - amount
        )

        return motivation

    # ==================================================
    # EMOTIONAL INFLUENCE
    # ==================================================

    @staticmethod
    def update_from_emotions(person):

        emotions = person.emotions

        # ------------------------------------------
        # ANGER
        # ------------------------------------------

        if emotions.anger > 0.2:

            MotivationSystem.strengthen(
                person,
                "power",
                emotions.anger * 0.01,
                "emotion"
            )

            MotivationSystem.strengthen(
                person,
                "status",
                emotions.anger * 0.008,
                "emotion"
            )

        # ------------------------------------------
        # FEAR
        # ------------------------------------------

        if emotions.fear > 0.2:

            MotivationSystem.strengthen(
                person,
                "security",
                emotions.fear * 0.015,
                "emotion"
            )

            MotivationSystem.strengthen(
                person,
                "survival",
                emotions.fear * 0.01,
                "emotion"
            )

        # ------------------------------------------
        # SADNESS / GRIEF
        # ------------------------------------------

        sadness = (
            emotions.sadness
            + emotions.grief
        ) / 2

        if sadness > 0.2:

            MotivationSystem.strengthen(
                person,
                "social_connection",
                sadness * 0.012,
                "emotion"
            )

            MotivationSystem.strengthen(
                person,
                "security",
                sadness * 0.006,
                "emotion"
            )

        # ------------------------------------------
        # LONELINESS
        # ------------------------------------------

        if emotions.loneliness > 0.2:

            MotivationSystem.strengthen(
                person,
                "social_connection",
                emotions.loneliness * 0.02,
                "emotion"
            )

        # ------------------------------------------
        # PRIDE
        # ------------------------------------------

        if emotions.pride > 0.2:

            MotivationSystem.strengthen(
                person,
                "achievement",
                emotions.pride * 0.008,
                "emotion"
            )

        # ------------------------------------------
        # SHAME
        # ------------------------------------------

        if emotions.shame > 0.2:

            MotivationSystem.strengthen(
                person,
                "status",
                emotions.shame * 0.012,
                "emotion"
            )

        # ------------------------------------------
        # CONTENTMENT
        # ------------------------------------------

        if emotions.contentment > 0.5:

            MotivationSystem.weaken(
                person,
                "survival",
                0.002
            )

            MotivationSystem.weaken(
                person,
                "power",
                0.001
            )
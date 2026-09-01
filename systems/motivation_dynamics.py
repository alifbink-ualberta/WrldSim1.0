# systems/motivation_dynamics.py


class MotivationDynamicsSystem:

    # ==================================================
    # PROCESS EXPERIENCE
    # ==================================================

    @staticmethod
    def process(
        person,
        event,
        interpretation,
        response
    ):

        if not person.is_alive:
            return

        event_type = (
            event.event_type
        )

        impact = 0.0

        if interpretation is not None:

            impact = (
                interpretation.emotional_impact
            )

        # ==========================================
        # INSULT / HUMILIATION
        # ==========================================

        if event_type == "insult":

            MotivationDynamicsSystem.change(
                person,
                "power",
                impact * 0.10
            )

            MotivationDynamicsSystem.change(
                person,
                "achievement",
                impact * 0.05
            )

        # ==========================================
        # THREAT
        # ==========================================

        elif event_type == "threat":

            MotivationDynamicsSystem.change(
                person,
                "security",
                impact * 0.15
            )

        # ==========================================
        # BETRAYAL
        # ==========================================

        elif event_type == "betrayal":

            MotivationDynamicsSystem.change(
                person,
                "security",
                impact * 0.10
            )

            MotivationDynamicsSystem.change(
                person,
                "social_connection",
                -impact * 0.05
            )

            MotivationDynamicsSystem.change(
                person,
                "power",
                impact * 0.08
            )

        # ==========================================
        # HELP
        # ==========================================

        elif event_type == "help":

            MotivationDynamicsSystem.change(
                person,
                "social_connection",
                impact * 0.05
            )

            MotivationDynamicsSystem.change(
                person,
                "harmony",
                impact * 0.04
            )

        # ==========================================
        # COMPLIMENT
        # ==========================================

        elif event_type == "compliment":

            MotivationDynamicsSystem.change(
                person,
                "social_connection",
                impact * 0.03
            )

            MotivationDynamicsSystem.change(
                person,
                "achievement",
                impact * 0.03
            )

        # ==========================================
        # DEATH
        # ==========================================

        elif event_type == "death":

            MotivationDynamicsSystem.change(
                person,
                "social_connection",
                impact * 0.08
            )

            MotivationDynamicsSystem.change(
                person,
                "security",
                impact * 0.08
            )

    # ==================================================
    # CHANGE
    # ==================================================

    @staticmethod
    def change(
        person,
        motivation_name,
        amount
    ):

        motivation = (
            MotivationDynamicsSystem.find(
                person,
                motivation_name
            )
        )

        if motivation is None:
            return None

        motivation.strength = max(
            0.0,
            min(
                1.0,
                motivation.strength + amount
            )
        )

        return motivation

    # ==================================================
    # FIND
    # ==================================================

    @staticmethod
    def find(
        person,
        motivation_name
    ):

        for motivation in person.motivations:

            if motivation.name == motivation_name:

                return motivation

        return None
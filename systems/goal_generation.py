# systems/goal_generation.py


from simulation.goal import Goal
from simulation.motivation import MotivationSystem


class GoalGenerationSystem:

    @staticmethod
    def generate(
        person,
        world
    ):

        goals = []

        # ==========================================
        # SURVIVAL
        # ==========================================

        hunger = person.survival.hunger
        thirst = person.survival.thirst
        energy = person.survival.energy

        if hunger > 0.65:

            goals.append(
                Goal(
                    "Find food",
                    "survival",
                    priority=hunger,
                    desired_effects={
                        "survival": 1.0,
                        "energy": 0.2
                    }
                )
            )

        if thirst > 0.65:

            goals.append(
                Goal(
                    "Find water",
                    "survival",
                    priority=thirst,
                    desired_effects={
                        "survival": 1.0
                    }
                )
            )

        if energy < 0.30:

            goals.append(
                Goal(
                    "Rest",
                    "survival",
                    priority=1.0 - energy,
                    desired_effects={
                        "energy": 1.0,
                        "survival": 0.5
                    }
                )
            )

        # ==========================================
        # EMOTIONAL STATE
        # ==========================================

        emotions = person.emotions

        # ------------------------------------------
        # LONELINESS
        # ------------------------------------------

        if emotions.loneliness > 0.35:

            goals.append(
                Goal(
                    "Seek companionship",
                    "social_connection",
                    priority=emotions.loneliness,
                    desired_effects={
                        "relationships": 1.0,
                        "knowledge": 0.1
                    }
                )
            )

        # ------------------------------------------
        # ANGER / STATUS
        # ------------------------------------------

        anger_pressure = (
            emotions.anger
            + emotions.shame
        ) / 2

        if anger_pressure > 0.35:

            goals.append(
                Goal(
                    "Restore my standing",
                    "status",
                    priority=anger_pressure,
                    desired_effects={
                        "status": 1.0,
                        "achievement": 0.5
                    }
                )
            )

        # ------------------------------------------
        # FEAR
        # ------------------------------------------

        if emotions.fear > 0.35:

            goals.append(
                Goal(
                    "Become safer",
                    "security",
                    priority=emotions.fear,
                    desired_effects={
                        "security": 1.0,
                        "money": 0.3
                    }
                )
            )

        # ------------------------------------------
        # GRIEF
        # ------------------------------------------

        if emotions.grief > 0.35:

            goals.append(
                Goal(
                    "Seek comfort and support",
                    "social_connection",
                    priority=emotions.grief,
                    desired_effects={
                        "relationships": 1.0
                    }
                )
            )

        # ==========================================
        # MOTIVATIONS
        # ==========================================

        exploration = MotivationSystem.get(
            person,
            "exploration"
        )

        if exploration and exploration.strength > 0.65:

            goals.append(
                Goal(
                    "Explore the world",
                    "exploration",
                    priority=exploration.strength,
                    desired_effects={
                        "knowledge": 1.0,
                        "autonomy": 0.8,
                        "achievement": 0.3
                    }
                )
            )

        achievement = MotivationSystem.get(
            person,
            "achievement"
        )

        if achievement and achievement.strength > 0.65:

            goals.append(
                Goal(
                    "Improve myself",
                    "achievement",
                    priority=achievement.strength,
                    desired_effects={
                        "knowledge": 0.8,
                        "achievement": 1.0
                    }
                )
            )

        security = MotivationSystem.get(
            person,
            "security"
        )

        if security and security.strength > 0.65:

            goals.append(
                Goal(
                    "Improve my financial security",
                    "security",
                    priority=security.strength,
                    desired_effects={
                        "money": 1.0,
                        "security": 1.0
                    }
                )
            )

        power = MotivationSystem.get(
            person,
            "power"
        )

        if power and power.strength > 0.65:

            goals.append(
                Goal(
                    "Increase my influence",
                    "power",
                    priority=power.strength,
                    desired_effects={
                        "status": 1.0,
                        "achievement": 0.5
                    }
                )
            )

        # ==========================================
        # SORT
        # ==========================================

        goals.sort(
            key=lambda goal: goal.priority,
            reverse=True
        )

        # Keep the strongest goals.

        return goals[:8]
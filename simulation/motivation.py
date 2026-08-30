from dataclasses import dataclass


@dataclass
class Motivation:

    name: str
    strength: float = 50.0

    def __str__(self):
        return f"{self.name}: {self.strength:.1f}"


class MotivationSystem:

    MOTIVATIONS = [
        "security",
        "belonging",
        "status",
        "wealth",
        "knowledge",
        "power",
        "autonomy",
        "family",
        "achievement",
        "pleasure",
    ]

    @staticmethod
    def generate(person):
        """
        Generate initial motivational tendencies from
        personality traits.

        These are tendencies, not goals.

        A person's circumstances will eventually modify
        these motivations dynamically.
        """

        motivations = {}

        # -------------------------
        # SECURITY
        # -------------------------

        security = (
            person.neuroticism * 0.45
            + person.conscientiousness * 0.35
            + (100 - person.psychopathy) * 0.20
        )

        motivations["security"] = Motivation(
            "security",
            security
        )

        # -------------------------
        # BELONGING
        # -------------------------

        belonging = (
            person.extraversion * 0.40
            + person.agreeableness * 0.40
            + (100 - person.psychopathy) * 0.20
        )

        motivations["belonging"] = Motivation(
            "belonging",
            belonging
        )

        # -------------------------
        # STATUS
        # -------------------------

        status = (
            person.narcissism * 0.40
            + person.extraversion * 0.25
            + person.conscientiousness * 0.15
            + person.machiavellianism * 0.20
        )

        motivations["status"] = Motivation(
            "status",
            status
        )

        # -------------------------
        # WEALTH
        # -------------------------

        wealth = (
            person.machiavellianism * 0.35
            + person.conscientiousness * 0.25
            + person.narcissism * 0.20
            + (100 - person.agreeableness) * 0.20
        )

        motivations["wealth"] = Motivation(
            "wealth",
            wealth
        )

        # -------------------------
        # KNOWLEDGE
        # -------------------------

        knowledge = (
            person.openness * 0.70
            + person.conscientiousness * 0.30
        )

        motivations["knowledge"] = Motivation(
            "knowledge",
            knowledge
        )

        # -------------------------
        # POWER
        # -------------------------

        power = (
            person.machiavellianism * 0.40
            + person.narcissism * 0.30
            + person.psychopathy * 0.15
            + (100 - person.agreeableness) * 0.15
        )

        motivations["power"] = Motivation(
            "power",
            power
        )

        # -------------------------
        # AUTONOMY
        # -------------------------

        autonomy = (
            person.openness * 0.35
            + (100 - person.agreeableness) * 0.30
            + (100 - person.conscientiousness) * 0.15
            + person.machiavellianism * 0.20
        )

        motivations["autonomy"] = Motivation(
            "autonomy",
            autonomy
        )

        # -------------------------
        # FAMILY
        # -------------------------

        family = (
            person.agreeableness * 0.50
            + person.conscientiousness * 0.25
            + (100 - person.psychopathy) * 0.25
        )

        motivations["family"] = Motivation(
            "family",
            family
        )

        # -------------------------
        # ACHIEVEMENT
        # -------------------------

        achievement = (
            person.conscientiousness * 0.45
            + person.narcissism * 0.20
            + person.openness * 0.15
            + (100 - person.agreeableness) * 0.20
        )

        motivations["achievement"] = Motivation(
            "achievement",
            achievement
        )

        # -------------------------
        # PLEASURE
        # -------------------------

        pleasure = (
            person.extraversion * 0.35
            + person.openness * 0.25
            + (100 - person.conscientiousness) * 0.20
            + (100 - person.neuroticism) * 0.20
        )

        motivations["pleasure"] = Motivation(
            "pleasure",
            pleasure
        )

        # Clamp everything

        for motivation in motivations.values():

            motivation.strength = max(
                0,
                min(
                    100,
                    motivation.strength
                )
            )

        return motivations
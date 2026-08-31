# systems/motivation.py


from simulation.motivation import Motivation


def generate_motivations(person):

    motivations = {

        "survival": Motivation(
            "survival",
            0.5
        ),

        "security": Motivation(
            "security",
            0.5
        ),

        "social_connection": Motivation(
            "social_connection",
            0.5
        ),

        "status": Motivation(
            "status",
            0.5
        ),

        "autonomy": Motivation(
            "autonomy",
            0.5
        ),

        "knowledge": Motivation(
            "knowledge",
            0.5
        ),

        "achievement": Motivation(
            "achievement",
            0.5
        ),

        "power": Motivation(
            "power",
            0.5
        )
    }

    # ==========================================
    # PERSONALITY
    # ==========================================

    personality = person.personality

    motivations["knowledge"].strength += (
        personality.openness * 0.3
    )

    motivations["achievement"].strength += (
        personality.conscientiousness * 0.3
    )

    motivations["social_connection"].strength += (
        personality.extraversion * 0.3
    )

    motivations["social_connection"].strength += (
        personality.agreeableness * 0.2
    )

    motivations["security"].strength += (
        personality.neuroticism * 0.2
    )

    motivations["power"].strength += (
        personality.machiavellianism * 0.3
    )

    motivations["status"].strength += (
        personality.narcissism * 0.3
    )

    # ==========================================
    # LIMIT VALUES
    # ==========================================

    for motivation in motivations.values():

        motivation.strength = max(
            0.0,
            min(
                1.0,
                motivation.strength
            )
        )

    return motivations
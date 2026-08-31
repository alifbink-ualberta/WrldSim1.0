# systems/goals.py


from simulation.goal import Goal


def generate_goals(person, world):

    goals = []

    motivations = person.motivations

    # ==========================================
    # SURVIVAL
    # ==========================================

    survival = motivations["survival"]

    if survival.strength > 0.7:

        goals.append(
            Goal(
                name="secure food",
                motivation=survival,
                priority=survival.strength
            )
        )

    # ==========================================
    # SECURITY
    # ==========================================

    security = motivations["security"]

    if security.strength > 0.7:

        goals.append(
            Goal(
                name="increase personal security",
                motivation=security,
                priority=security.strength
            )
        )

    # ==========================================
    # SOCIAL CONNECTION
    # ==========================================

    social = motivations["social_connection"]

    if social.strength > 0.7:

        goals.append(
            Goal(
                name="strengthen relationships",
                motivation=social,
                priority=social.strength
            )
        )

    # ==========================================
    # STATUS
    # ==========================================

    status = motivations["status"]

    if status.strength > 0.7:

        goals.append(
            Goal(
                name="increase social status",
                motivation=status,
                priority=status.strength
            )
        )

    # ==========================================
    # KNOWLEDGE
    # ==========================================

    knowledge = motivations["knowledge"]

    if knowledge.strength > 0.7:

        goals.append(
            Goal(
                name="learn something new",
                motivation=knowledge,
                priority=knowledge.strength
            )
        )

    # ==========================================
    # ACHIEVEMENT
    # ==========================================

    achievement = motivations["achievement"]

    if achievement.strength > 0.7:

        goals.append(
            Goal(
                name="accomplish something difficult",
                motivation=achievement,
                priority=achievement.strength
            )
        )

    # ==========================================
    # POWER
    # ==========================================

    power = motivations["power"]

    if power.strength > 0.7:

        goals.append(
            Goal(
                name="increase personal power",
                motivation=power,
                priority=power.strength
            )
        )

    # ==========================================
    # AUTONOMY
    # ==========================================

    autonomy = motivations["autonomy"]

    if autonomy.strength > 0.7:

        goals.append(
            Goal(
                name="increase personal independence",
                motivation=autonomy,
                priority=autonomy.strength
            )
        )

    return goals
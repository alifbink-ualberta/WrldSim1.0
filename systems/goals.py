# systems/goals.py


from simulation.goal import Goal


# ==================================================
# UPDATE GOALS
# ==================================================

def update_goals(person, world):

    existing_goals = person.goals

    # ==========================================
    # GENERATE POSSIBLE NEW GOALS
    # ==========================================

    possible_goals = generate_possible_goals(
        person,
        world
    )

    # ==========================================
    # ADD NEW GOALS
    # ==========================================

    for new_goal in possible_goals:

        already_exists = False

        for existing in existing_goals:

            if (
                existing.name
                == new_goal.name
            ):

                already_exists = True
                break

        if not already_exists:

            existing_goals.append(
                new_goal
            )

    # ==========================================
    # UPDATE PRIORITIES
    # ==========================================

    for goal in existing_goals:

        if goal.completed:
            continue

        if goal.abandoned:
            continue

        update_goal_priority(
            person,
            goal,
            world
        )


# ==================================================
# GENERATE POSSIBLE GOALS
# ==================================================

def generate_possible_goals(
    person,
    world
):

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
                priority=survival.strength,
                desired_effects={
                    "survival": 1.0
                }
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
                priority=security.strength,
                desired_effects={
                    "security": 1.0
                }
            )
        )

    # ==========================================
    # SOCIAL
    # ==========================================

    social = motivations[
        "social_connection"
    ]

    if social.strength > 0.7:

        goals.append(
            Goal(
                name="strengthen relationships",
                motivation=social,
                priority=social.strength,
                desired_effects={
                    "relationships": 1.0
                }
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
                priority=status.strength,
                desired_effects={
                    "status": 1.0
                }
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
                priority=knowledge.strength,
                desired_effects={
                    "knowledge": 1.0
                }
            )
        )

    # ==========================================
    # ACHIEVEMENT
    # ==========================================

    achievement = motivations[
        "achievement"
    ]

    if achievement.strength > 0.7:

        goals.append(
            Goal(
                name="accomplish something difficult",
                motivation=achievement,
                priority=achievement.strength,
                desired_effects={
                    "achievement": 1.0
                }
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
                priority=power.strength,
                desired_effects={
                    "power": 1.0
                }
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
                priority=autonomy.strength,
                desired_effects={
                    "autonomy": 1.0
                }
            )
        )

    return goals


# ==================================================
# UPDATE GOAL PRIORITY
# ==================================================

def update_goal_priority(
    person,
    goal,
    world
):

    priority = (
        goal.motivation.strength
    )

    # ==========================================
    # SURVIVAL PRESSURE
    # ==========================================

    if goal.name == "secure food":

        try:

            hunger = person.survival.hunger

            priority += (
                hunger
                / 100
            )

        except AttributeError:

            pass

    # ==========================================
    # CAP
    # ==========================================

    goal.priority = max(
        0.0,
        min(
            1.0,
            priority
        )
    )
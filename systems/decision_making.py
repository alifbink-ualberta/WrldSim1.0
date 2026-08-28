from systems.actions import generate_actions


def goal_score(person, action):
    """
    Determines how strongly the person's goals
    motivate a particular action.
    """

    score = 0

    for goal in person.goals:

        goal = goal.lower()

        # Financial security / wealth
        if "wealth" in goal or "financial" in goal:

            if action.action_type == "work":
                score += 30

        # Reputation / respect
        if "respected" in goal or "reputation" in goal:

            if action.action_type == "work":
                score += 15

            elif action.action_type == "socialize":
                score += 20

        # Learning
        if "learn" in goal or "knowledge" in goal:

            if action.action_type == "practice":
                score += 30

            elif action.action_type == "explore":
                score += 25

        # Family
        if "family" in goal:

            if action.action_type == "work":
                score += 15

            elif action.action_type == "socialize":
                score += 10

        # Mastery
        if "master" in goal:

            if action.action_type == "practice":
                score += 35

    return score


def personality_score(person, action):

    score = 0

    # ==============================
    # SURVIVAL
    # ==============================

    if action.action_type == "eat":

        score += person.hunger * 3

    elif action.action_type == "sleep":

        score += (100 - person.energy) * 3

    # ==============================
    # WORK
    # ==============================

    elif action.action_type == "work":

        score += person.conscientiousness

        score += (
            person.machiavellianism * 0.25
        )

        score += (
            person.narcissism * 0.15
        )

    # ==============================
    # PRACTICE
    # ==============================

    elif action.action_type == "practice":

        score += (
            person.conscientiousness * 0.7
        )

        score += (
            person.openness * 0.5
        )

    # ==============================
    # SOCIALIZE
    # ==============================

    elif action.action_type == "socialize":

        score += (
            person.extraversion * 1.2
        )

        score += (
            person.agreeableness * 0.3
        )

    # ==============================
    # EXPLORE
    # ==============================

    elif action.action_type == "explore":

        score += (
            person.openness * 1.2
        )

        score += (
            person.extraversion * 0.3
        )

        score -= (
            person.neuroticism * 0.5
        )

    return score


def score_action(person, action):

    personality = personality_score(
        person,
        action
    )

    goals = goal_score(
        person,
        action
    )

    return personality + goals


def choose_action(person, world):

    actions = generate_actions(
        person,
        world
    )

    scored_actions = []

    for action in actions:

        score = score_action(
            person,
            action
        )

        scored_actions.append(
            (action, score)
        )

    scored_actions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scored_actions[0]
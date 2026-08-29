from systems.actions import generate_actions


def need_score(person, action):

    score = 0

    # =================================
    # HUNGER
    # =================================

    if action.action_type == "eat":

        # Eating becomes increasingly important
        # as hunger approaches dangerous levels.

        score += (
            person.hunger ** 1.7
        )

    # =================================
    # SLEEP
    # =================================

    elif action.action_type == "sleep":

        fatigue = 100 - person.energy

        score += (
            fatigue ** 1.7
        )

    return score


def goal_score(person, action):

    score = 0

    for goal in person.goals:

        goal = goal.lower()

        # -----------------------------
        # WEALTH
        # -----------------------------

        if (
            "wealth" in goal
            or "financial" in goal
        ):

            if action.action_type == "work":

                score += 20

            elif action.action_type == "sell":

                score += 25

            elif action.action_type == "buy":

                score -= 10

        # -----------------------------
        # RESPECT
        # -----------------------------

        if (
            "respected" in goal
            or "reputation" in goal
        ):

            if action.action_type == "socialize":

                score += 15

            elif action.action_type == "work":

                score += 10

        # -----------------------------
        # KNOWLEDGE
        # -----------------------------

        if (
            "learn" in goal
            or "knowledge" in goal
            or "scholar" in goal
        ):

            if action.action_type == "practice":

                score += 30

            elif action.action_type == "explore":

                score += 25

        # -----------------------------
        # CRAFT
        # -----------------------------

        if "master" in goal:

            if action.action_type == "practice":

                score += 35

            elif action.action_type == "work":

                score += 20

        # -----------------------------
        # FAMILY
        # -----------------------------

        if "family" in goal:

            if action.action_type == "work":

                score += 10

            if action.action_type == "socialize":

                score += 10

    return score


def personality_score(person, action):

    score = 0

    # =================================
    # WORK
    # =================================

    if action.action_type == "work":

        score += (
            person.conscientiousness
            * 0.6
        )

        score += (
            person.machiavellianism
            * 0.15
        )

    # =================================
    # PRACTICE
    # =================================

    elif action.action_type == "practice":

        score += (
            person.conscientiousness
            * 0.5
        )

        score += (
            person.openness
            * 0.4
        )

    # =================================
    # SOCIAL
    # =================================

    elif action.action_type == "socialize":

        score += (
            person.extraversion
            * 0.7
        )

        score += (
            person.agreeableness
            * 0.2
        )

    # =================================
    # EXPLORATION
    # =================================

    elif action.action_type == "explore":

        score += (
            person.openness
            * 0.7
        )

        score += (
            person.extraversion
            * 0.2
        )

        score -= (
            person.neuroticism
            * 0.3
        )

    return score


def opportunity_score(person, action):

    score = 0

    # =================================
    # BUYING
    # =================================

    if action.action_type == "buy":

        if action.item == "food":

            score += person.hunger * 1.5

        elif action.item == "tools":

            score += (
                person.conscientiousness
                * 0.2
            )

        score += (
            person.extraversion
            * 0.1
        )

    # =================================
    # SELLING
    # =================================

    elif action.action_type == "sell":

        score += 15

        score += (
            person.extraversion
            * 0.3
        )

        score += (
            person.machiavellianism
            * 0.2
        )

    return score


def score_action(person, action):

    return (

        need_score(
            person,
            action
        )

        +

        goal_score(
            person,
            action
        )

        +

        personality_score(
            person,
            action
        )

        +

        opportunity_score(
            person,
            action
        )
    )


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
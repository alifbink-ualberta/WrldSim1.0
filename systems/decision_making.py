# systems/decision_making.py


def choose_action(person, world):

    from simulation.action import Action

    possible_actions = []

    # ==========================================
    # BASIC ACTIONS
    # ==========================================

    possible_actions.append(
        Action("eat")
    )

    possible_actions.append(
        Action("sleep")
    )

    possible_actions.append(
        Action("work")
    )

    possible_actions.append(
        Action("practice")
    )

    possible_actions.append(
        Action("socialize")
    )

    possible_actions.append(
        Action("explore")
    )

    # ==========================================
    # SCORE ACTIONS
    # ==========================================

    best_action = None
    best_score = float("-inf")

    for action in possible_actions:

        score = score_action(
            person,
            action,
            world
        )

        if score > best_score:

            best_score = score
            best_action = action

    return best_action, best_score


def score_action(
    person,
    action,
    world
):

    score = 0.0

    # ==========================================
    # SURVIVAL
    # ==========================================

    survival = person.survival

    if action.action_type == "eat":

        # Placeholder until SurvivalState
        # becomes more developed.

        score += 0.0

    if action.action_type == "sleep":

        score += 0.0

    # ==========================================
    # MOTIVATIONS
    # ==========================================

    motivations = person.motivations

    if action.action_type == "socialize":

        score += (
            motivations[
                "social_connection"
            ].strength
            * 10
        )

    if action.action_type == "practice":

        score += (
            motivations[
                "achievement"
            ].strength
            * 8
        )

        score += (
            motivations[
                "knowledge"
            ].strength
            * 5
        )

    if action.action_type == "work":

        score += (
            motivations[
                "security"
            ].strength
            * 8
        )

        score += (
            motivations[
                "achievement"
            ].strength
            * 5
        )

        score += (
            motivations[
                "status"
            ].strength
            * 3
        )

    if action.action_type == "explore":

        score += (
            motivations[
                "autonomy"
            ].strength
            * 8
        )

        score += (
            motivations[
                "knowledge"
            ].strength
            * 8
        )

        score += (
            motivations[
                "achievement"
            ].strength
            * 5
        )

    # ==========================================
    # PERSONALITY
    # ==========================================

    personality = person.personality

    if action.action_type == "explore":

        score += (
            personality.openness
            * 5
        )

    if action.action_type == "socialize":

        score += (
            personality.extraversion
            * 5
        )

    if action.action_type == "work":

        score += (
            personality.conscientiousness
            * 5
        )

    if action.action_type == "practice":

        score += (
            personality.conscientiousness
            * 4
        )

    # ==========================================
    # RETURN
    # ==========================================

    return score
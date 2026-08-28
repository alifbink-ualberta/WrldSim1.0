from systems.actions import get_available_actions


def score_action(person, action):

    score = 0

    # -------------------------
    # SURVIVAL
    # -------------------------

    if action == "eat":

        score += person.hunger * 2

    if action == "sleep":

        score += (100 - person.energy) * 2

    # -------------------------
    # WORK
    # -------------------------

    if action == "work":

        score += person.conscientiousness

        # Ambitious people value productive work
        score += person.machiavellianism * 0.3
        score += person.narcissism * 0.2

    # -------------------------
    # SOCIALIZE
    # -------------------------

    if action == "socialize":

        score += person.extraversion

        score += person.agreeableness * 0.3

    # -------------------------
    # PRACTICE
    # -------------------------

    if action == "practice":

        score += person.conscientiousness * 0.7
        score += person.openness * 0.4

    # -------------------------
    # EXPLORE
    # -------------------------

    if action == "explore":

        score += person.openness
        score += person.extraversion * 0.3

        # Neurotic people are less inclined
        # toward unfamiliar situations
        score -= person.neuroticism * 0.4

    return score


def choose_action(person):

    actions = get_available_actions(person)

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

    return scored_actions[0][0]
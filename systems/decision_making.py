from systems.actions import generate_actions


def need_utility(person, action):
    """
    How strongly the person's current physical needs
    motivate a particular action.
    """

    utility = 0

    # -------------------------
    # HUNGER
    # -------------------------

    if action.action_type == "eat":

        # Hunger becomes increasingly urgent.
        utility += person.hunger ** 1.7

    # -------------------------
    # SLEEP
    # -------------------------

    elif action.action_type == "sleep":

        fatigue = 100 - person.energy

        utility += fatigue ** 1.7

    return utility


def goal_utility(person, action):
    """
    How much an action contributes toward
    the person's current goals.
    """

    utility = 0

    for goal in person.goals:

        goal = goal.lower()

        # -------------------------
        # FINANCIAL SECURITY
        # -------------------------

        if (
            "financial" in goal
            or "secure" in goal
        ):

            if action.action_type == "work":
                utility += 25

            elif action.action_type == "sell":
                utility += 20

        # -------------------------
        # WEALTH
        # -------------------------

        if "wealth" in goal:

            if action.action_type == "work":
                utility += 25

            elif action.action_type == "sell":
                utility += 30

        # -------------------------
        # RESPECT / REPUTATION
        # -------------------------

        if (
            "respect" in goal
            or "reputation" in goal
        ):

            if action.action_type == "work":
                utility += 15

            elif action.action_type == "socialize":
                utility += 20

        # -------------------------
        # KNOWLEDGE
        # -------------------------

        if (
            "learn" in goal
            or "knowledge" in goal
            or "scholar" in goal
        ):

            if action.action_type == "practice":
                utility += 30

            elif action.action_type == "explore":
                utility += 25

        # -------------------------
        # CRAFT
        # -------------------------

        if "master" in goal:

            if action.action_type == "practice":
                utility += 35

            elif action.action_type == "work":
                utility += 20

        # -------------------------
        # FAMILY
        # -------------------------

        if "family" in goal:

            if action.action_type == "socialize":
                utility += 15

            elif action.action_type == "work":
                utility += 15

    return utility


def personality_utility(person, action):
    """
    Personality doesn't determine behaviour.

    It changes how attractive different behaviours
    are to the individual.
    """

    utility = 0

    # -------------------------
    # WORK
    # -------------------------

    if action.action_type == "work":

        utility += (
            person.conscientiousness * 0.5
        )

        utility += (
            person.machiavellianism * 0.1
        )

    # -------------------------
    # PRACTICE
    # -------------------------

    elif action.action_type == "practice":

        utility += (
            person.conscientiousness * 0.4
        )

        utility += (
            person.openness * 0.4
        )

    # -------------------------
    # SOCIALIZE
    # -------------------------

    elif action.action_type == "socialize":

        utility += (
            person.extraversion * 0.7
        )

        utility += (
            person.agreeableness * 0.2
        )

    # -------------------------
    # EXPLORE
    # -------------------------

    elif action.action_type == "explore":

        utility += (
            person.openness * 0.7
        )

        utility += (
            person.extraversion * 0.2
        )

        utility -= (
            person.neuroticism * 0.3
        )

    return utility


def circumstance_utility(person, action, world):
    """
    Evaluates the person's current circumstances.

    This is deliberately separate from personality.

    Later this will become much more sophisticated:
    relationships, information, politics, economy,
    reputation, location, danger, etc.
    """

    utility = 0

    # -------------------------
    # FOOD
    # -------------------------

    if action.action_type == "eat":

        if person.inventory.get("food", 0) > 0:
            utility += 20

        elif person.inventory.get("meat", 0) > 0:
            utility += 20

        else:
            utility -= 100

    # -------------------------
    # WORK
    # -------------------------

    if action.action_type == "work":

        # People who are already exhausted
        # shouldn't enthusiastically start work.
        if person.energy < 20:
            utility -= 80

    # -------------------------
    # SLEEP
    # -------------------------

    if action.action_type == "sleep":

        if person.energy < 40:
            utility += 30

    return utility


def score_action(person, action, world):

    return (

        need_utility(
            person,
            action
        )

        +

        goal_utility(
            person,
            action
        )

        +

        personality_utility(
            person,
            action
        )

        +

        circumstance_utility(
            person,
            action,
            world
        )
    )


def choose_action(person, world):

    actions = generate_actions(
        person,
        world
    )

    if not actions:
        return None, 0

    scored_actions = []

    for action in actions:

        score = score_action(
            person,
            action,
            world
        )

        scored_actions.append(
            (action, score)
        )

    scored_actions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scored_actions[0]
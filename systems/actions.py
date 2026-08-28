def get_available_actions(person):

    actions = []

    # Basic survival
    if person.hunger >= 40:
        actions.append("eat")

    if person.energy <= 30:
        actions.append("sleep")

    # Occupation
    actions.append("work")

    # Social
    actions.append("socialize")

    # Personal development
    actions.append("practice")

    # Exploration
    actions.append("explore")

    return actions
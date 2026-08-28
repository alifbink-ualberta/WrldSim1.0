from simulation.action import Action


def generate_actions(person, world):

    actions = []

    # --------------------------------
    # BASIC SURVIVAL
    # --------------------------------

    if person.hunger >= 40:

        actions.append(
            Action(
                actor=person,
                action_type="eat",
                reason="hunger"
            )
        )

    if person.energy <= 30:

        actions.append(
            Action(
                actor=person,
                action_type="sleep",
                reason="fatigue"
            )
        )

    # --------------------------------
    # OCCUPATION
    # --------------------------------

    actions.append(
        Action(
            actor=person,
            action_type="work",
            reason="occupation"
        )
    )

    # --------------------------------
    # PERSONAL DEVELOPMENT
    # --------------------------------

    actions.append(
        Action(
            actor=person,
            action_type="practice",
            reason="self_improvement"
        )
    )

    # --------------------------------
    # SOCIAL
    # --------------------------------

    actions.append(
        Action(
            actor=person,
            action_type="socialize",
            reason="social_need"
        )
    )

    # --------------------------------
    # EXPLORATION
    # --------------------------------

    actions.append(
        Action(
            actor=person,
            action_type="explore",
            reason="curiosity"
        )
    )

    return actions
from simulation.action import Action
from systems.opportunities import (
    generate_trade_opportunities
)


def get_action_duration(action_type):

    durations = {

        "eat": 1,
        "sleep": 8,
        "work": 4,
        "practice": 2,
        "socialize": 2,
        "explore": 4,
        "buy": 1,
        "sell": 1
    }

    return durations.get(
        action_type,
        1
    )


def generate_actions(person, world):

    actions = []

    # =================================
    # SURVIVAL
    # =================================

    if person.hunger >= 40:

        if person.has_item("food"):

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

    # =================================
    # OCCUPATION
    # =================================

    actions.append(
        Action(
            actor=person,
            action_type="work",
            reason="occupation"
        )
    )

    # =================================
    # DEVELOPMENT
    # =================================

    actions.append(
        Action(
            actor=person,
            action_type="practice",
            reason="self_improvement"
        )
    )

    # =================================
    # SOCIAL
    # =================================

    actions.append(
        Action(
            actor=person,
            action_type="socialize",
            reason="social_need"
        )
    )

    # =================================
    # EXPLORATION
    # =================================

    actions.append(
        Action(
            actor=person,
            action_type="explore",
            reason="curiosity"
        )
    )

    # =================================
    # ECONOMIC OPPORTUNITIES
    # =================================

    opportunities = generate_trade_opportunities(
        person,
        world
    )

    for opportunity in opportunities:

        action = Action(
            actor=person,
            action_type=opportunity.action_type,
            target=opportunity.target,
            reason=opportunity.reason
        )

        # Attach trade information
        action.item = opportunity.item
        action.amount = opportunity.amount
        action.price = opportunity.price

        actions.append(action)

    return actions
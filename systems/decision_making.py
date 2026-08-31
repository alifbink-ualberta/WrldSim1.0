# systems/decision_making.py


from simulation.action import Action
from simulation.action_outcome import ActionOutcome


# ==================================================
# CHOOSE ACTION
# ==================================================

def choose_action(person, world):

    opportunities = generate_possible_actions(
        person,
        world
    )

    if not opportunities:

        return None, 0.0

    best_action = None
    best_score = float("-inf")

    for action in opportunities:

        outcome = predict_action(
            person,
            action,
            world
        )

        score = evaluate_action(
            person,
            action,
            outcome,
            world
        )

        if score > best_score:

            best_score = score
            best_action = action

    return best_action, best_score


# ==================================================
# GENERATE POSSIBLE ACTIONS
# ==================================================

def generate_possible_actions(
    person,
    world
):

    from systems.opportunities import (
        generate_opportunities
    )

    opportunities = generate_opportunities(
        person,
        world
    )

    actions = []

    for opportunity in opportunities:

        actions.append(
            Action(
                action_type=opportunity.action_type,
                target=opportunity.target,
                location=opportunity.location,
                opportunity=opportunity
            )
        )

    return actions


# ==================================================
# PREDICT OUTCOME
# ==================================================

def predict_action(
    person,
    action,
    world
):

    action_type = action.action_type

    # ==========================================
    # EAT
    # ==========================================

    if action_type == "eat":

        return ActionOutcome(
            action,
            effects={
                "survival": 0.8,
                "energy": 0.1
            },
            risk=0.0
        )

    # ==========================================
    # SLEEP
    # ==========================================

    if action_type == "sleep":

        return ActionOutcome(
            action,
            effects={
                "survival": 0.8,
                "energy": 1.0
            },
            risk=0.0
        )

    # ==========================================
    # WORK
    # ==========================================

    if action_type == "work":

        return ActionOutcome(
            action,
            effects={
                "money": 0.7,
                "security": 0.4,
                "status": 0.2,
                "achievement": 0.2
            },
            risk=0.05
        )

    # ==========================================
    # PRACTICE
    # ==========================================

    if action_type == "practice":

        return ActionOutcome(
            action,
            effects={
                "knowledge": 0.5,
                "achievement": 0.6,
                "status": 0.1
            },
            risk=0.05
        )

    # ==========================================
    # SOCIALIZE
    # ==========================================

    if action_type == "socialize":

        return ActionOutcome(
            action,
            effects={
                "relationships": 0.8,
                "status": 0.2,
                "knowledge": 0.1
            },
            risk=0.05
        )

    # ==========================================
    # EXPLORE
    # ==========================================

    if action_type == "explore":

        return ActionOutcome(
            action,
            effects={
                "knowledge": 0.7,
                "autonomy": 0.8,
                "achievement": 0.3
            },
            risk=0.4
        )

    # ==========================================
    # UNKNOWN
    # ==========================================

    return ActionOutcome(
        action
    )

# ==================================================
# CIRCUMSTANCE EFFECT
# ==================================================

def circumstance_effect(
    person,
    action,
    world
):

    score = 0.0

    # ==========================================
    # WORLD CIRCUMSTANCES
    # ==========================================

    for circumstance in world.circumstances:

        effects = circumstance.effects

        key = (
            f"{action.action_type}"
        )

        score += effects.get(
            key,
            0.0
        )

    # ==========================================
    # PERSONAL CIRCUMSTANCES
    # ==========================================

    for circumstance in person.circumstances:

        effects = circumstance.effects

        key = (
            f"{action.action_type}"
        )

        score += effects.get(
            key,
            0.0
        )

    return score


# ==================================================
# EVALUATE ACTION
# ==================================================

def evaluate_action(
    person,
    action,
    outcome,
    world
):

    score = 0.0

    # ==========================================
    # GOALS
    # ==========================================

    for goal in person.goals:

        if goal.completed:
            continue

        if goal.abandoned:
            continue

        for effect_name, effect_value in (
            outcome.effects.items()
        ):

            desired_value = (
                goal.get_desired_effect(
                    effect_name
                )
            )

            score += (
                goal.priority
                * desired_value
                * effect_value
            )

    # ==========================================
    # MOTIVATIONS
    # ==========================================

    motivations = person.motivations

    if action.action_type == "socialize":

        score += (
            motivations[
                "social_connection"
            ].strength
            * 2
        )

    if action.action_type == "explore":

        score += (
            motivations[
                "autonomy"
            ].strength
            * 2
        )

        score += (
            motivations[
                "knowledge"
            ].strength
            * 2
        )

    if action.action_type == "practice":

        score += (
            motivations[
                "achievement"
            ].strength
            * 2
        )

        score += (
            motivations[
                "knowledge"
            ].strength
            * 1.5
        )

    if action.action_type == "work":

        score += (
            motivations[
                "security"
            ].strength
            * 2
        )

    # ==========================================
    # PERSONALITY
    # ==========================================

    personality = person.personality

    if action.action_type == "explore":

        score += (
            personality.openness
            * 2
        )

    if action.action_type == "socialize":

        score += (
            personality.extraversion
            * 2
        )

    if action.action_type == "work":

        score += (
            personality.conscientiousness
            * 2
        )

    if action.action_type == "practice":

        score += (
            personality.conscientiousness
            * 1.5
        )

    # ==========================================
    # RELATIONSHIPS
    # ==========================================

    if (
        action.action_type == "socialize"
        and action.target is not None
    ):

        relationship = (
            person.get_relationship(
                action.target
            )
        )

        feelings = relationship.get_feelings(
            person
        )

        score += (
            feelings["affection"]
            * 0.01
        )

        score += (
            feelings["familiarity"]
            * 0.01
        )

        score += (
            feelings["trust"]
            * 0.01
        )

        score -= (
            feelings["resentment"]
            * 0.01
        )

        score -= (
            feelings["fear"]
            * 0.01
        )

    # ==========================================
    # RISK
    # ==========================================

    score -= (
        outcome.risk
        * personality.neuroticism
        * 3
    )

    score += (
        outcome.risk
        * personality.psychopathy
        * 1.5
    )

    # ==========================================
    # CIRCUMSTANCES
    # ==========================================

    score += circumstance_effect(
        person,
        action,
        world
    )

    return score
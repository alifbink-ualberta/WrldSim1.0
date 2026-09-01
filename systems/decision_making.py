# systems/decision_making.py


from simulation.action import Action
from simulation.action_outcome import ActionOutcome


# ==================================================
# CHOOSE ACTION
# ==================================================

def choose_action(person, world):

    if not person.is_alive:
        return None, 0.0

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
# GENERATE ACTIONS
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

    if action_type == "eat":

        return ActionOutcome(
            action,
            effects={
                "hunger": -0.8,
                "energy": 0.1
            },
            risk=0.0
        )

    if action_type == "drink":

        return ActionOutcome(
            action,
            effects={
                "thirst": -0.8
            },
            risk=0.0
        )

    if action_type == "sleep":

        return ActionOutcome(
            action,
            effects={
                "energy": 0.8,
                "sleep": 0.8
            },
            risk=0.0
        )

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

    if action_type == "visit":

        return ActionOutcome(
            action,
            effects={
                "relationships": 0.9,
                "social_connection": 0.7
            },
            risk=0.02
        )

    if action_type == "confront":

        return ActionOutcome(
            action,
            effects={
                "resentment": -0.1,
                "status": 0.3,
                "autonomy": 0.3
            },
            risk=0.35
        )

    if action_type == "avoid":

        return ActionOutcome(
            action,
            effects={
                "safety": 0.5
            },
            risk=0.0
        )

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

    return ActionOutcome(action)


# ==================================================
# CIRCUMSTANCES
# ==================================================

def circumstance_effect(
    person,
    action,
    world
):

    score = 0.0

    # ------------------------------------------
    # WORLD
    # ------------------------------------------

    for circumstance in getattr(
        world,
        "circumstances",
        []
    ):

        score += circumstance.get_effect(
            action.action_type
        )

    # ------------------------------------------
    # PERSONAL
    # ------------------------------------------

    for circumstance in getattr(
        person,
        "circumstances",
        []
    ):

        score += circumstance.get_effect(
            action.action_type
        )

    return score


# ==================================================
# MOTIVATION HELPER
# ==================================================

def motivation_strength(
    person,
    name
):

    for motivation in person.motivations:

        if motivation.name == name:

            return motivation.strength

    return 0.0


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

    survival = person.survival
    personality = person.personality

    # ==========================================
    # SURVIVAL PRESSURE
    # ==========================================

    if action.action_type == "eat":

        score += (
            survival.hunger
            * 8
        )

    if action.action_type == "drink":

        score += (
            survival.thirst
            * 8
        )

    if action.action_type == "sleep":

        score += (
            (1.0 - survival.energy)
            * 8
        )

    # ==========================================
    # GOALS
    # ==========================================

    for goal in person.goals:

        if goal.completed:
            continue

        if getattr(
            goal,
            "failed",
            False
        ):
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

    if action.action_type == "socialize":

        score += (
            motivation_strength(
                person,
                "social_connection"
            )
            * 2.0
        )

    if action.action_type == "visit":

        score += (
            motivation_strength(
                person,
                "social_connection"
            )
            * 2.5
        )

    if action.action_type == "explore":

        score += (
            motivation_strength(
                person,
                "exploration"
            )
            * 2.0
        )

        score += (
            motivation_strength(
                person,
                "knowledge"
            )
            * 2.0
        )

    if action.action_type == "practice":

        score += (
            motivation_strength(
                person,
                "achievement"
            )
            * 2.0
        )

        score += (
            motivation_strength(
                person,
                "knowledge"
            )
            * 1.0
        )

    if action.action_type == "work":

        score += (
            motivation_strength(
                person,
                "security"
            )
            * 2.0
        )

        score += (
            motivation_strength(
                person,
                "achievement"
            )
            * 0.5
        )

    if action.action_type == "confront":

        score += (
            motivation_strength(
                person,
                "power"
            )
            * 1.5
        )

        score += (
            motivation_strength(
                person,
                "autonomy"
            )
            * 1.0
        )

    # ==========================================
    # PERSONALITY
    # ==========================================

    if action.action_type == "explore":

        score += (
            personality.openness
            * 2.0
        )

    if action.action_type == "socialize":

        score += (
            personality.extraversion
            * 2.0
        )

    if action.action_type == "work":

        score += (
            personality.conscientiousness
            * 2.0
        )

    if action.action_type == "practice":

        score += (
            personality.conscientiousness
            * 1.5
        )

    if action.action_type == "confront":

        score += (
            personality.narcissism
            * 0.8
        )

        score += (
            personality.machiavellianism
            * 0.5
        )

    # ==========================================
    # SOCIAL RELATIONSHIPS
    # ==========================================

    if (
        action.target is not None
        and action.action_type
        in (
            "socialize",
            "visit",
            "confront",
            "avoid"
        )
    ):

        relationship = (
            person.get_relationship(
                action.target
            )
        )

        feelings = relationship.get_feelings(
            person
        )

        # All relationship values are now
        # standardized to -1.0 → +1.0.

        score += (
            feelings["affection"]
            * 2.0
        )

        score += (
            feelings["familiarity"]
            * 0.5
        )

        score += (
            feelings["trust"]
            * 1.5
        )

        score -= (
            feelings["resentment"]
            * 2.0
        )

        score -= (
            feelings["fear"]
            * 2.0
        )

        # --------------------------------------
        # VISIT
        # --------------------------------------

        if action.action_type == "visit":

            score += (
                feelings["affection"]
                * 2.0
            )

            score += (
                feelings["trust"]
                * 1.0
            )

        # --------------------------------------
        # CONFRONT
        # --------------------------------------

        if action.action_type == "confront":

            score += (
                feelings["resentment"]
                * 3.0
            )

            score += (
                feelings["fear"]
                * 0.5
            )

        # --------------------------------------
        # AVOID
        # --------------------------------------

        if action.action_type == "avoid":

            score += (
                feelings["fear"]
                * 4.0
            )

            score += (
                feelings["resentment"]
                * 2.0
            )

    # ==========================================
    # RISK
    # ==========================================

    score -= (
        outcome.risk
        * personality.neuroticism
        * 3.0
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
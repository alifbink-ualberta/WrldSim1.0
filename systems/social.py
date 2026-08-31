from simulation.interaction import Interaction


def perform_interaction(
    actor,
    target,
    interaction_type,
    world
):

    relationship = actor.get_relationship(target)

    interaction = Interaction(
        actor=actor,
        target=target,
        interaction_type=interaction_type
    )

    # ==========================================
    # GREETING
    # ==========================================

    if interaction_type == "greet":

        relationship.familiarity[actor] = min(
            1.0,
            relationship.familiarity[actor] + 0.02
        )

        relationship.familiarity[target] = min(
            1.0,
            relationship.familiarity[target] + 0.02
        )

        interaction.description = (
            f"{actor.full_name} greeted "
            f"{target.full_name}."
        )

    # ==========================================
    # COMPLIMENT
    # ==========================================

    elif interaction_type == "compliment":

        relationship.affection[actor] += 0.03
        relationship.affection[target] += 0.01

        interaction.description = (
            f"{actor.full_name} complimented "
            f"{target.full_name}."
        )

    # ==========================================
    # INSULT
    # ==========================================

    elif interaction_type == "insult":

        relationship.resentment[target] += 0.08

        relationship.affection[target] -= 0.05

        interaction.description = (
            f"{actor.full_name} insulted "
            f"{target.full_name}."
        )

    # ==========================================
    # HELP
    # ==========================================

    elif interaction_type == "help":

        relationship.trust[target] += 0.05
        relationship.affection[target] += 0.03

        interaction.description = (
            f"{actor.full_name} helped "
            f"{target.full_name}."
        )

    # ==========================================
    # THREATEN
    # ==========================================

    elif interaction_type == "threaten":

        relationship.fear[target] += 0.10
        relationship.resentment[target] += 0.05

        interaction.description = (
            f"{actor.full_name} threatened "
            f"{target.full_name}."
        )

    # ==========================================
    # HISTORY
    # ==========================================

    relationship.add_history(
        interaction
    )

    # ==========================================
    # MEMORY
    # ==========================================

    actor.remember({
        "type": "interaction",
        "other": target,
        "description": interaction.description
    })

    target.remember({
        "type": "interaction",
        "other": actor,
        "description": interaction.description
    })

    return interaction
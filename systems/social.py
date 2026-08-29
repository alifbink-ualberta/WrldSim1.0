import random


def choose_social_target(person, world):

    possible_targets = []

    for other in world.people:

        if other == person:
            continue

        # For now, people can only socialize
        # with someone at the same location.
        if other.location == person.location:

            possible_targets.append(other)

    if not possible_targets:
        return None

    # For now we use familiarity + personality.
    # This will become much more sophisticated later.
    weighted_targets = []

    for other in possible_targets:

        relationship = person.get_relationship(
            other
        )

        familiarity = (
            relationship.familiarity
        )

        weight = 1 + familiarity

        weighted_targets.append(
            (other, weight)
        )

    total_weight = sum(
        weight
        for _, weight
        in weighted_targets
    )

    roll = random.uniform(
        0,
        total_weight
    )

    current = 0

    for other, weight in weighted_targets:

        current += weight

        if roll <= current:
            return other

    return possible_targets[-1]


def social_interaction(
    person,
    target,
    world
):

    relationship = person.get_relationship(
        target
    )

    # ---------------------------------
    # FAMILIARITY
    # ---------------------------------

    relationship.familiarity += 1

    # ---------------------------------
    # PERSONALITY EFFECTS
    # ---------------------------------

    # Extraverted people generally enjoy
    # interaction more.
    affection_change = (
        (person.extraversion - 50)
        / 100
    )

    respect_change = (
        (person.conscientiousness - 50)
        / 200
    )

    # ---------------------------------
    # APPLY RELATIONSHIP CHANGES
    # ---------------------------------

    relationship.affection_a_to_b += (
        affection_change
    )

    relationship.respect_a_to_b += (
        respect_change
    )

    # ---------------------------------
    # MEMORY
    # ---------------------------------

    memory = {
        "type": "social_interaction",
        "year": world.year,
        "month": world.month,
        "day": world.day,
        "hour": world.hour,
        "other": target.name,
        "description": (
            f"Met {target.name} "
            f"and had a conversation."
        )
    }

    person.remember(memory)

    # The other person remembers it too.
    other_memory = {
        "type": "social_interaction",
        "year": world.year,
        "month": world.month,
        "day": world.day,
        "hour": world.hour,
        "other": person.name,
        "description": (
            f"Met {person.name} "
            f"and had a conversation."
        )
    }

    target.remember(other_memory)

    return (
        f"{person.name} talked with "
        f"{target.name}."
    )
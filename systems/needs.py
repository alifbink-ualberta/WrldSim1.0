def update_needs(person):

    person.hunger = min(
        100,
        person.hunger + 2
    )

    person.energy = max(
        0,
        person.energy - 2
    )

    person.social = max(
        0,
        person.social - 1
    )
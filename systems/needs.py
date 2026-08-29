def update_needs(person):

    # Hunger always increases slowly.
    person.hunger = min(
        100,
        person.hunger + 1
    )

    # Energy only naturally declines
    # while awake.

    if person.current_activity is None:

        person.energy = max(
            0,
            person.energy - 2
        )
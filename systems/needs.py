def update_needs(person):

    # =================================
    # HUNGER
    # =================================

    person.hunger = min(
        100,
        person.hunger + 1
    )

    # =================================
    # ENERGY
    # =================================

    if person.current_activity is None:

        person.energy = max(
            0,
            person.energy - 2
        )

    else:

        if (
            person.current_activity.action_type
            == "sleep"
        ):

            person.energy = min(
                100,
                person.energy + 12
            )

        else:

            person.energy = max(
                0,
                person.energy - 2
            )
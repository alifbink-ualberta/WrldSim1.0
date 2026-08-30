def update_needs(person, minutes=1):

    # ==========================================
    # HUNGER
    # ==========================================

    person.hunger = min(
        100,
        person.hunger + (
            1 * minutes / 60
        )
    )

    # ==========================================
    # ENERGY
    # ==========================================

    if person.current_activity is None:

        person.energy = max(
            0,
            person.energy - (
                2 * minutes / 60
            )
        )

    else:

        if (
            person.current_activity.action_type
            == "sleep"
        ):

            person.energy = min(
                100,
                person.energy + (
                    12 * minutes / 60
                )
            )

        else:

            person.energy = max(
                0,
                person.energy - (
                    2 * minutes / 60
                )
            )
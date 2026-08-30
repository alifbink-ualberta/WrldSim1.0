# systems/needs.py


def update_needs(
    person,
    minutes=1
):

    # ==========================================
    # HUNGER
    # ==========================================

    hunger_rate = 1 / 3

    person.hunger = min(
        100,
        person.hunger
        + hunger_rate * minutes
    )

    # ==========================================
    # ENERGY
    # ==========================================

    if person.current_activity is None:

        energy_rate = 2 / 60

        person.energy = max(
            0,
            person.energy
            - energy_rate * minutes
        )

        return

    # ==========================================
    # ACTIVITY ENERGY
    # ==========================================

    if (
        person.current_activity.action_type
        == "sleep"
    ):

        recovery_rate = 12 / 60

        person.energy = min(
            100,
            person.energy
            + recovery_rate * minutes
        )

        return

    # ==========================================
    # GENERAL ACTIVITY
    # ==========================================

    activity_rate = 2 / 60

    person.energy = max(
        0,
        person.energy
        - activity_rate * minutes
    )
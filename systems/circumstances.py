# systems/circumstances.py


class CircumstanceSystem:

    # ==================================================
    # ADD TO PERSON
    # ==================================================

    @staticmethod
    def add_to_person(
        person,
        circumstance
    ):

        if not hasattr(
            person,
            "circumstances"
        ):

            person.circumstances = []

        person.circumstances.append(
            circumstance
        )

        return circumstance

    # ==================================================
    # ADD TO WORLD
    # ==================================================

    @staticmethod
    def add_to_world(
        world,
        circumstance
    ):

        if not hasattr(
            world,
            "circumstances"
        ):

            world.circumstances = []

        world.circumstances.append(
            circumstance
        )

        return circumstance

    # ==================================================
    # ADVANCE PERSON
    # ==================================================

    @staticmethod
    def advance_person(
        person,
        minutes
    ):

        if not hasattr(
            person,
            "circumstances"
        ):

            person.circumstances = []

        for circumstance in (
            person.circumstances
        ):

            circumstance.advance(
                minutes
            )

        person.circumstances = [
            circumstance
            for circumstance in person.circumstances
            if circumstance.active
        ]

    # ==================================================
    # ADVANCE WORLD
    # ==================================================

    @staticmethod
    def advance_world(
        world,
        minutes
    ):

        if not hasattr(
            world,
            "circumstances"
        ):

            world.circumstances = []

        for circumstance in (
            world.circumstances
        ):

            circumstance.advance(
                minutes
            )

        world.circumstances = [
            circumstance
            for circumstance in world.circumstances
            if circumstance.active
        ]


# systems/upbringing.py


class UpbringingSystem:

    """
    Handles the gradual development of a young person.

    This is intentionally a simple first version.

    The goal is not to perfectly model childhood.

    The goal is to establish the architecture through
    which parents, siblings, environment and experiences
    can influence a developing Person.
    """

    # ==================================================
    # UPDATE
    # ==================================================

    @staticmethod
    def update(
        person,
        world,
        minutes=1
    ):

        # Adults are not handled by the childhood system.

        if person.age >= 18:
            return

        # ------------------------------------------
        # PARENTAL INFLUENCE
        # ------------------------------------------

        UpbringingSystem.parental_influence(
            person,
            world,
            minutes
        )

        # ------------------------------------------
        # SIBLING INFLUENCE
        # ------------------------------------------

        UpbringingSystem.sibling_influence(
            person,
            world,
            minutes
        )

    # ==================================================
    # PARENTS
    # ==================================================

    @staticmethod
    def parental_influence(
        person,
        world,
        minutes
    ):

        if not person.family.parents:
            return

        # We don't want personality to change every
        # minute. Childhood development happens gradually.

        if world.current_time_minutes % 1440 != 0:
            return

        for parent in person.family.parents:

            if not parent.alive:
                continue

            UpbringingSystem.influence_from_parent(
                person,
                parent
            )

    # ==================================================
    # PARENT INFLUENCE
    # ==================================================

    @staticmethod
    def influence_from_parent(
        child,
        parent
    ):

        """
        Parents provide environmental influence.

        This does NOT simply copy personality.

        Instead, parental traits create small pressures
        on the developing child.
        """

        child_personality = child.personality
        parent_personality = parent.personality

        # ------------------------------------------
        # CONSCIENTIOUSNESS
        # ------------------------------------------

        difference = (
            parent_personality.conscientiousness
            - child_personality.conscientiousness
        )

        child_personality.conscientiousness += (
            difference * 0.001
        )

        # ------------------------------------------
        # OPENNESS
        # ------------------------------------------

        difference = (
            parent_personality.openness
            - child_personality.openness
        )

        child_personality.openness += (
            difference * 0.001
        )

        # ------------------------------------------
        # EXTRAVERSION
        # ------------------------------------------

        difference = (
            parent_personality.extraversion
            - child_personality.extraversion
        )

        child_personality.extraversion += (
            difference * 0.001
        )

        # ------------------------------------------
        # AGREEABLENESS
        # ------------------------------------------

        difference = (
            parent_personality.agreeableness
            - child_personality.agreeableness
        )

        child_personality.agreeableness += (
            difference * 0.001
        )

        # ------------------------------------------
        # NEUROTICISM
        # ------------------------------------------

        difference = (
            parent_personality.neuroticism
            - child_personality.neuroticism
        )

        child_personality.neuroticism += (
            difference * 0.001
        )

    # ==================================================
    # SIBLINGS
    # ==================================================

    @staticmethod
    def sibling_influence(
        person,
        world,
        minutes
    ):

        if not person.family.siblings:
            return

        # Once per simulated day.

        if world.current_time_minutes % 1440 != 0:
            return

        for sibling in person.family.siblings:

            if not sibling.alive:
                continue

            UpbringingSystem.influence_from_sibling(
                person,
                sibling
            )

    # ==================================================
    # SIBLING INFLUENCE
    # ==================================================

    @staticmethod
    def influence_from_sibling(
        child,
        sibling
    ):

        """
        Siblings influence development primarily through
        interaction and comparison.

        This is deliberately tiny for now.

        Later this should be driven by actual interactions,
        rivalry, affection, cooperation, age differences,
        family circumstances, etc.
        """

        # Older siblings have slightly greater influence.

        if sibling.age <= child.age:
            return

        age_difference = (
            sibling.age - child.age
        )

        influence = min(
            0.003,
            age_difference * 0.0005
        )

        # Older sibling's conscientiousness creates
        # a small developmental pressure.

        difference = (
            sibling.personality.conscientiousness
            - child.personality.conscientiousness
        )

        child.personality.conscientiousness += (
            difference * influence
        )
# systems/reproduction.py

from simulation.person import Person


class ReproductionSystem:

    @staticmethod
    def have_child(
        parent_a,
        parent_b,
        first_name,
        world
    ):

        # ==========================================
        # BASIC VALIDATION
        # ==========================================

        if parent_a == parent_b:
            return None

        # ==========================================
        # GENETICS
        # ==========================================

        genetics = (
            ReproductionSystem
            .generate_genetics(
                parent_a,
                parent_b
            )
        )

        # ==========================================
        # CHILD IDENTITY
        # ==========================================

        child = Person(
            first_name=first_name,
            last_name=parent_a.last_name,
            age=0,
            sex=ReproductionSystem.generate_sex(),
            genetics=genetics
        )

        # ==========================================
        # FAMILY
        # ==========================================

        child.family.set_parents(
            parent_a,
            parent_b
        )

        parent_a.family.add_child(
            child
        )

        parent_b.family.add_child(
            child
        )

        # ==========================================
        # WORLD
        # ==========================================

        world.add_person(
            child
        )

        # ==========================================
        # BIRTH EXPERIENCES
        # ==========================================

        from simulation.experience import Experience

        birth_experience = Experience(
            category="birth",
            description=(
                f"{child.full_name} was born."
            ),
            intensity=1.0
        )

        child.add_experience(
            birth_experience
        )

        return child

    # ==============================================
    # GENETICS
    # ==============================================

    @staticmethod
    def generate_genetics(
        parent_a,
        parent_b
    ):

        from simulation.genetics import Genetics

        # For now Genetics handles its own generation.
        #
        # We will later replace this with actual
        # inheritance of individual traits from
        # both parents.

        genetics = Genetics()

        return genetics

    # ==============================================
    # SEX
    # ==============================================

    @staticmethod
    def generate_sex():

        import random

        return random.choice(
            [
                "male",
                "female"
            ]
        )
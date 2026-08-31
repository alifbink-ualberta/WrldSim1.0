# simulation/opportunity.py


class Opportunity:

    def __init__(
        self,
        action_type,
        target=None,
        location=None,
        requirements=None
    ):

        # ==========================================
        # ACTION
        # ==========================================

        self.action_type = action_type

        # ==========================================
        # TARGET
        # ==========================================

        self.target = target

        # ==========================================
        # LOCATION
        # ==========================================

        self.location = location

        # ==========================================
        # REQUIREMENTS
        # ==========================================

        self.requirements = (
            requirements
            if requirements is not None
            else {}
        )

    # ==================================================
    # AVAILABILITY
    # ==================================================

    def is_available(self, person, world):

        # ------------------------------------------
        # MONEY
        # ------------------------------------------

        if "money" in self.requirements:

            if person.money < self.requirements["money"]:

                return False

        # ------------------------------------------
        # ITEM
        # ------------------------------------------

        if "item" in self.requirements:

            item = self.requirements["item"]

            if not person.has_item(item):

                return False

        # ------------------------------------------
        # AGE
        # ------------------------------------------

        if "minimum_age" in self.requirements:

            if person.age < self.requirements["minimum_age"]:

                return False

        # ------------------------------------------
        # RETURN
        # ------------------------------------------

        return True

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        if self.target is not None:

            return (
                f"{self.action_type} "
                f"{self.target.full_name}"
            )

        return self.action_type
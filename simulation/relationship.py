# simulation/relationship.py


class Relationship:

    def __init__(self, person_a, person_b):

        self.person_a = person_a
        self.person_b = person_b

        # ==========================================
        # CONNECTIONS
        # ==========================================

        self.connections = set()

        # ==========================================
        # FEELINGS
        #
        # All continuous relationship values use
        # the standardized range:
        #
        # -1.0 = maximally negative
        #  0.0 = neutral
        # +1.0 = maximally positive
        #
        # Exception:
        # fear and familiarity are still represented
        # on the same numerical range, with 0.0
        # meaning absence / neutrality.
        # ==========================================

        self.affection = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.trust = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.respect = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.fear = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.resentment = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.attraction = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.familiarity = {
            person_a: 0.0,
            person_b: 0.0
        }

        # ==========================================
        # SHARED HISTORY
        # ==========================================

        self.history = []

    # ==================================================
    # HISTORY
    # ==================================================

    def add_history(self, interaction):

        self.history.append(
            interaction
        )

    # ==================================================
    # GET FEELINGS
    # ==================================================

    def get_feelings(self, person):

        return {
            "affection": self.affection[person],
            "trust": self.trust[person],
            "respect": self.respect[person],
            "fear": self.fear[person],
            "resentment": self.resentment[person],
            "attraction": self.attraction[person],
            "familiarity": self.familiarity[person]
        }

    # ==================================================
    # CHANGE FEELING
    # ==================================================

    def change_feeling(
        self,
        person,
        feeling,
        amount
    ):

        if not hasattr(self, feeling):
            return False

        values = getattr(
            self,
            feeling
        )

        if person not in values:
            return False

        values[person] = max(
            -1.0,
            min(
                1.0,
                values[person] + amount
            )
        )

        return True

    # ==================================================
    # SET FEELING
    # ==================================================

    def set_feeling(
        self,
        person,
        feeling,
        value
    ):

        if not hasattr(self, feeling):
            return False

        values = getattr(
            self,
            feeling
        )

        if person not in values:
            return False

        values[person] = max(
            -1.0,
            min(
                1.0,
                value
            )
        )

        return True
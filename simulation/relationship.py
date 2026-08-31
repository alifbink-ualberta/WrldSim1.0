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

        self.history.append(interaction)

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
    # VALUE MODIFICATION
    # ==================================================

    def change_feeling(
        self,
        feeling,
        person,
        amount
    ):

        if feeling not in [
            "affection",
            "trust",
            "respect",
            "fear",
            "resentment",
            "attraction",
            "familiarity"
        ]:
            return False

        values = getattr(
            self,
            feeling
        )

        values[person] = max(
            -1.0,
            min(
                1.0,
                values[person] + amount
            )
        )

        return True
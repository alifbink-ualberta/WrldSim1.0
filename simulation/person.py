class Person:

    def __init__(
        self,
        name,
        age,
        species,

        openness,
        conscientiousness,
        extraversion,
        agreeableness,
        neuroticism,

        machiavellianism,
        narcissism,
        psychopathy,
        sadism,

        occupation,
        money=0
    ):

        # =========================
        # IDENTITY
        # =========================

        self.name = name
        self.age = age
        self.species = species
        self.occupation = occupation

        # =========================
        # PERSONALITY
        # =========================

        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

        # Dark personality traits
        self.machiavellianism = machiavellianism
        self.narcissism = narcissism
        self.psychopathy = psychopathy
        self.sadism = sadism

        # =========================
        # NEEDS
        # =========================

        self.hunger = 0
        self.energy = 100

        # =========================
        # ECONOMY
        # =========================

        self.money = money

        self.inventory = {}

        # =========================
        # PSYCHOLOGY
        # =========================

        self.goals = []

        self.beliefs = []

        # =========================
        # SOCIAL
        # =========================

        self.relationships = {}

        self.memories = []

        # =========================
        # WORLD STATE
        # =========================

        self.location = None

        # =========================
        # CURRENT ACTIVITY
        # =========================

        self.current_activity = None

    # ==================================================
    # INVENTORY
    # ==================================================

    def add_item(self, item, amount=1):

        if item not in self.inventory:
            self.inventory[item] = 0

        self.inventory[item] += amount

    def remove_item(self, item, amount=1):

        if item not in self.inventory:
            return False

        if self.inventory[item] < amount:
            return False

        self.inventory[item] -= amount

        if self.inventory[item] <= 0:
            del self.inventory[item]

        return True

    def has_item(self, item, amount=1):

        return (
            self.inventory.get(item, 0)
            >= amount
        )

    # ==================================================
    # ECONOMY
    # ==================================================

    def earn_money(self, amount):

        self.money += amount

    def spend_money(self, amount):

        if self.money < amount:
            return False

        self.money -= amount

        return True

    # ==================================================
    # RELATIONSHIPS
    # ==================================================

    def get_relationship(self, other):

        if other.name not in self.relationships:

            self.relationships[other.name] = 0

        return self.relationships[other.name]

    def change_relationship(
        self,
        other,
        amount
    ):

        current = self.get_relationship(other)

        self.relationships[other.name] = max(
            -100,
            min(
                100,
                current + amount
            )
        )

    # ==================================================
    # MEMORIES
    # ==================================================

    def remember(self, memory):

        self.memories.append(memory)

    # ==================================================
    # ACTION EXECUTION
    # ==================================================

    def perform_action(self, action):

        action_type = action.action_type

        # -------------------------
        # EAT
        # -------------------------

        if action_type == "eat":

            if self.has_item("food"):

                self.remove_item(
                    "food",
                    1
                )

                self.hunger = max(
                    0,
                    self.hunger - 50
                )

                self.energy = max(
                    0,
                    self.energy - 2
                )

                return (
                    f"{self.name} ate food."
                )

            else:

                return (
                    f"{self.name} has no food."
                )

        # -------------------------
        # SLEEP
        # -------------------------

        elif action_type == "sleep":

            self.energy = min(
                100,
                self.energy + 60
            )

            return (
                f"{self.name} slept."
            )

        # -------------------------
        # WORK
        # -------------------------

        elif action_type == "work":

            self.energy = max(
                0,
                self.energy - 10
            )

            self.hunger = min(
                100,
                self.hunger + 4
            )

            # Occupation-specific production

            if self.occupation == "Farmer":

                self.add_item(
                    "food",
                    3
                )

                return (
                    f"{self.name} worked the farm "
                    f"and produced 3 food."
                )

            elif self.occupation == "Hunter":

                self.add_item(
                    "meat",
                    2
                )

                return (
                    f"{self.name} hunted "
                    f"and produced 2 meat."
                )

            elif self.occupation == "Blacksmith":

                self.add_item(
                    "tools",
                    1
                )

                return (
                    f"{self.name} forged "
                    f"1 tool."
                )

            elif self.occupation == "Merchant":

                self.earn_money(5)

                return (
                    f"{self.name} conducted "
                    f"business and earned 5 money."
                )

            elif self.occupation == "Scholar":

                return (
                    f"{self.name} studied "
                    f"and gained knowledge."
                )

            else:

                return (
                    f"{self.name} worked."
                )

        # -------------------------
        # PRACTICE
        # -------------------------

        elif action_type == "practice":

            self.energy = max(
                0,
                self.energy - 8
            )

            self.hunger = min(
                100,
                self.hunger + 2
            )

            return (
                f"{self.name} practiced "
                f"their skills."
            )

        # -------------------------
        # SOCIALIZE
        # -------------------------

        elif action_type == "socialize":

            self.energy = max(
                0,
                self.energy - 4
            )

            return (
                f"{self.name} socialized."
            )

        # -------------------------
        # EXPLORE
        # -------------------------

        elif action_type == "explore":

            self.energy = max(
                0,
                self.energy - 8
            )

            self.hunger = min(
                100,
                self.hunger + 3
            )

            return (
                f"{self.name} explored."
            )

        return (
            f"{self.name} did nothing."
        )

    # ==================================================
    # DEBUGGING
    # ==================================================

    def __str__(self):

        return (
            f"{self.name}, "
            f"age {self.age}, "
            f"{self.species}, "
            f"{self.occupation}"
        )
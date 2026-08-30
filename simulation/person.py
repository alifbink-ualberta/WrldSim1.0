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
        self.motivations = {}

        # =========================
        # SOCIAL
        # =========================

        self.relationships = {}

        # =========================
        # MEMORY
        # =========================

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

        from simulation.relationship import Relationship

        if other == self:
            return None

        if other not in self.relationships:

            relationship = Relationship(
                self,
                other
            )

            self.relationships[other] = relationship

            other.relationships[self] = relationship

        return self.relationships[other]

    def get_known_people(self):

        return list(
            self.relationships.keys()
        )

    def change_relationship(
        self,
        other,
        amount
    ):

        if other == self:
            return

        relationship = self.get_relationship(
            other
        )

        relationship.trust_a_to_b = max(
            -100,
            min(
                100,
                relationship.trust_a_to_b + amount
            )
        )

        relationship.affection_a_to_b = max(
            -100,
            min(
                100,
                relationship.affection_a_to_b + amount
            )
        )

        relationship.trust_b_to_a = max(
            -100,
            min(
                100,
                relationship.trust_b_to_a + amount
            )
        )

        relationship.affection_b_to_a = max(
            -100,
            min(
                100,
                relationship.affection_b_to_a + amount
            )
        )

    # ==================================================
    # MEMORY
    # ==================================================

    def remember(self, memory):

        self.memories.append(memory)

    # ==================================================
    # ACTION EXECUTION
    # ==================================================

    def perform_action(
        self,
        action,
        world
    ):

        action_type = action.action_type

        # ==================================================
        # EAT
        # ==================================================

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

                self.remember({
                    "type": "personal",
                    "year": world.year,
                    "month": world.month,
                    "day": world.day,
                    "hour": world.hour,
                    "minute": world.minute,
                    "description": "Ate food."
                })

                return (
                    f"{self.name} ate food."
                )

            if self.has_item("meat"):

                self.remove_item(
                    "meat",
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

                self.remember({
                    "type": "personal",
                    "year": world.year,
                    "month": world.month,
                    "day": world.day,
                    "hour": world.hour,
                    "minute": world.minute,
                    "description": "Ate meat."
                })

                return (
                    f"{self.name} ate meat."
                )

            return (
                f"{self.name} had nothing "
                f"to eat."
            )

        # ==================================================
        # SLEEP
        # ==================================================

        elif action_type == "sleep":

            self.energy = min(
                100,
                self.energy + 60
            )

            self.remember({
                "type": "personal",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "description": "Slept."
            })

            return (
                f"{self.name} slept."
            )

        # ==================================================
        # WORK
        # ==================================================

        elif action_type == "work":

            self.energy = max(
                0,
                self.energy - 10
            )

            self.hunger = min(
                100,
                self.hunger + 4
            )

            if self.occupation == "Farmer":

                self.add_item(
                    "food",
                    3
                )

                description = (
                    f"{self.name} worked "
                    f"the farm and produced "
                    f"3 food."
                )

            elif self.occupation == "Hunter":

                self.add_item(
                    "meat",
                    2
                )

                description = (
                    f"{self.name} hunted "
                    f"and produced "
                    f"2 meat."
                )

            elif self.occupation == "Blacksmith":

                self.add_item(
                    "tools",
                    1
                )

                description = (
                    f"{self.name} forged "
                    f"1 tool."
                )

            elif self.occupation == "Merchant":

                self.earn_money(5)

                description = (
                    f"{self.name} conducted "
                    f"business and earned "
                    f"5 money."
                )

            elif self.occupation == "Scholar":

                description = (
                    f"{self.name} studied "
                    f"and gained knowledge."
                )

            else:

                description = (
                    f"{self.name} worked."
                )

            self.remember({
                "type": "work",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "description": description
            })

            return description

        # ==================================================
        # PRACTICE
        # ==================================================

        elif action_type == "practice":

            self.energy = max(
                0,
                self.energy - 8
            )

            self.hunger = min(
                100,
                self.hunger + 2
            )

            self.remember({
                "type": "practice",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "description": (
                    f"{self.name} practiced "
                    f"their skills."
                )
            })

            return (
                f"{self.name} practiced "
                f"their skills."
            )

        # ==================================================
        # SOCIALIZE
        # ==================================================

        elif action_type == "socialize":

            from systems.social import (
                social_interaction
            )

            target = action.target

            if target is None:

                return (
                    f"{self.name} had nobody "
                    f"to socialize with."
                )

            self.energy = max(
                0,
                self.energy - 4
            )

            return social_interaction(
                self,
                target,
                world
            )

        # ==================================================
        # EXPLORE
        # ==================================================

        elif action_type == "explore":

            self.energy = max(
                0,
                self.energy - 8
            )

            self.hunger = min(
                100,
                self.hunger + 3
            )

            self.remember({
                "type": "exploration",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "description": (
                    f"{self.name} explored "
                    f"the surrounding area."
                )
            })

            return (
                f"{self.name} explored."
            )

        # ==================================================
        # BUY
        # ==================================================

        elif action_type == "buy":

            seller = action.target
            item = action.item
            amount = action.amount
            price = action.price

            if seller is None:

                return (
                    f"{self.name} could not "
                    f"find a seller."
                )

            total_price = (
                price * amount
            )

            if self.money < total_price:

                return (
                    f"{self.name} cannot "
                    f"afford {item}."
                )

            if not seller.has_item(
                item,
                amount
            ):

                return (
                    f"{seller.name} does not "
                    f"have {item}."
                )

            seller.remove_item(
                item,
                amount
            )

            self.add_item(
                item,
                amount
            )

            self.spend_money(
                total_price
            )

            seller.earn_money(
                total_price
            )

            self.remember({
                "type": "trade",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "other": seller.name,
                "description": (
                    f"Bought {amount} "
                    f"{item} from "
                    f"{seller.name}."
                )
            })

            seller.remember({
                "type": "trade",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "other": self.name,
                "description": (
                    f"Sold {amount} "
                    f"{item} to "
                    f"{self.name}."
                )
            })

            self.change_relationship(
                seller,
                2
            )

            return (
                f"{self.name} bought "
                f"{amount} {item} "
                f"from {seller.name} "
                f"for {total_price}."
            )

        # ==================================================
        # SELL
        # ==================================================

        elif action_type == "sell":

            buyer = action.target
            item = action.item
            amount = action.amount
            price = action.price

            if buyer is None:

                return (
                    f"{self.name} could not "
                    f"find a buyer."
                )

            total_price = (
                price * amount
            )

            if not self.has_item(
                item,
                amount
            ):

                return (
                    f"{self.name} does not "
                    f"have {item}."
                )

            if buyer.money < total_price:

                return (
                    f"{buyer.name} cannot "
                    f"afford {item}."
                )

            self.remove_item(
                item,
                amount
            )

            buyer.add_item(
                item,
                amount
            )

            self.earn_money(
                total_price
            )

            buyer.spend_money(
                total_price
            )

            self.remember({
                "type": "trade",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "other": buyer.name,
                "description": (
                    f"Sold {amount} "
                    f"{item} to "
                    f"{buyer.name}."
                )
            })

            buyer.remember({
                "type": "trade",
                "year": world.year,
                "month": world.month,
                "day": world.day,
                "hour": world.hour,
                "minute": world.minute,
                "other": self.name,
                "description": (
                    f"Bought {amount} "
                    f"{item} from "
                    f"{self.name}."
                )
            })

            self.change_relationship(
                buyer,
                2
            )

            return (
                f"{self.name} sold "
                f"{amount} {item} "
                f"to {buyer.name} "
                f"for {total_price}."
            )

        # ==================================================
        # UNKNOWN ACTION
        # ==================================================

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
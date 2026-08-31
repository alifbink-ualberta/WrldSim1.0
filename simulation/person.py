# simulation/person.py

from simulation.genetics import Genetics
from simulation.personality import Personality
from simulation.body import Body
from simulation.survival import SurvivalState
from simulation.family import Family
from simulation.emotion import EmotionalState



class Person:

    def __init__(
        self,
        first_name,
        last_name,
        age,
        sex,
        genetics=None,
        personality=None,
        body=None,
        money=0
    ):

        # =========================
        # IDENTITY
        # =========================

        self.first_name = first_name
        self.last_name = last_name

        self.age = age
        self.sex = sex
        self.family = Family(self)

        # =========================
        # BIOLOGY
        # =========================

        self.genetics = (
            genetics
            if genetics is not None
            else Genetics()
        )

        self.body = (
            body
            if body is not None
            else Body(self.genetics)
        )

        # =========================
        # PERSONALITY
        # =========================

        self.personality = (
            personality
            if personality is not None
            else Personality()
        )

        self.emotions = EmotionalState()

        # =========================
        # MIND
        # =========================

        self.memories = []
        self.beliefs = []
        self.motivations = []
        self.goals = []

        # =========================
        # DEVELOPMENT
        # =========================

        self.skills = {}
        self.knowledge = {}

        # =========================
        # SOCIAL
        # =========================

        self.relationships = {}

        # =========================
        # SURVIVAL
        # =========================

        self.survival = SurvivalState()

        # =========================
        # ECONOMY
        # =========================

        self.money = money
        self.inventory = {}

        # =========================
        # WORLD
        # =========================

        self.location = None

    # ==================================================
    # IDENTITY
    # ==================================================

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"

    # ==================================================
    # MEMORY
    # ==================================================

    def remember(
        self,
        experience,
        emotional_significance=None
    ):

        from simulation.memory import Memory

        if emotional_significance is None:

            emotional_significance = (
                experience.intensity
            )

        memory = Memory(
            person=self,
            experience=experience,
            emotional_significance=(
                emotional_significance
            )
        )

        self.memories.append(
            memory
        )

        return memory

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

    # ==================================================
    # INVENTORY
    # ==================================================

    def add_item(self, item, amount=1):

        self.inventory[item] = (
            self.inventory.get(item, 0)
            + amount
        )

    def remove_item(self, item, amount=1):

        if self.inventory.get(item, 0) < amount:
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
    # DEBUGGING
    # ==================================================

    def __str__(self):

        return (
            f"{self.full_name}, "
            f"age {self.age}, "
            f"sex {self.sex}"
        )
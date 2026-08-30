# simulation/person.py

from systems.skills import SkillSet
from systems.action_resolver import ActionResolver


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

        # =========================
        # MOTIVATIONS
        # =========================

        self.motivations = {}

        # =========================
        # SKILLS
        # =========================

        self.skills = SkillSet()

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

        # =========================
        # ACTION SYSTEM
        # =========================

        self.action_resolver = (
            ActionResolver()
        )

    # ==================================================
    # INVENTORY
    # ==================================================

    def add_item(
        self,
        item,
        amount=1
    ):

        self.inventory[item] = (
            self.inventory.get(item, 0)
            + amount
        )

    def remove_item(
        self,
        item,
        amount=1
    ):

        if not self.has_item(
            item,
            amount
        ):

            return False

        self.inventory[item] -= amount

        if self.inventory[item] <= 0:

            del self.inventory[item]

        return True

    def has_item(
        self,
        item,
        amount=1
    ):

        return (
            self.inventory.get(
                item,
                0
            )
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

    def get_relationship(
        self,
        other
    ):

        from simulation.relationship import (
            Relationship
        )

        if other == self:

            return None

        if other not in self.relationships:

            relationship = Relationship(
                self,
                other
            )

            self.relationships[other] = (
                relationship
            )

            other.relationships[self] = (
                relationship
            )

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

        relationship = (
            self.get_relationship(
                other
            )
        )

        relationship.trust_a_to_b = max(
            -100,
            min(
                100,
                relationship.trust_a_to_b
                + amount
            )
        )

        relationship.affection_a_to_b = max(
            -100,
            min(
                100,
                relationship.affection_a_to_b
                + amount
            )
        )

        relationship.trust_b_to_a = max(
            -100,
            min(
                100,
                relationship.trust_b_to_a
                + amount
            )
        )

        relationship.affection_b_to_a = max(
            -100,
            min(
                100,
                relationship.affection_b_to_a
                + amount
            )
        )

    # ==================================================
    # MEMORY
    # ==================================================

    def remember(self, memory):

        self.memories.append(
            memory
        )

    # ==================================================
    # ACTION EXECUTION
    # ==================================================

    def perform_action(
        self,
        action,
        world
    ):

        return self.action_resolver.resolve(
            self,
            action,
            world
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
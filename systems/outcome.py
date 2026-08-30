# systems/outcome.py

import random
from dataclasses import dataclass


@dataclass
class Outcome:
    """
    Result of attempting an action.
    """

    success: bool
    chance: float
    quality: float = 0.0
    description: str = ""

    @property
    def failed(self):

        return not self.success


class OutcomeModifier:
    """
    Base class for anything that modifies
    the probability of an action succeeding.
    """

    def modify(
        self,
        chance,
        person,
        action,
        world
    ):

        return chance


class BaseChance(OutcomeModifier):

    def __init__(self, chance=50):

        self.chance = chance

    def modify(
        self,
        chance,
        person,
        action,
        world
    ):

        return self.chance


class SkillModifier(OutcomeModifier):

    def __init__(
        self,
        skill,
        weight=0.5
    ):

        self.skill = skill
        self.weight = weight

    def modify(
        self,
        chance,
        person,
        action,
        world
    ):

        skill = person.skills.get(
            self.skill
        )

        return chance + (
            skill - 50
        ) * self.weight


class PersonalityModifier(OutcomeModifier):

    def __init__(
        self,
        attribute,
        weight=0.2
    ):

        self.attribute = attribute
        self.weight = weight

    def modify(
        self,
        chance,
        person,
        action,
        world
    ):

        value = getattr(
            person,
            self.attribute,
            50
        )

        return chance + (
            value - 50
        ) * self.weight


class EnergyModifier(OutcomeModifier):

    def modify(
        self,
        chance,
        person,
        action,
        world
    ):

        energy_penalty = (
            50 - person.energy
        ) * 0.2

        return chance - max(
            0,
            energy_penalty
        )


class FamiliarityModifier(OutcomeModifier):

    def modify(
        self,
        chance,
        person,
        action,
        world
    ):

        target = action.target

        if target is None:
            return chance

        relationship = (
            person.get_relationship(
                target
            )
        )

        return chance + (
            relationship.familiarity
            * 0.25
        )


class OutcomeSystem:

    def __init__(self):

        self.modifiers = []

    def add_modifier(self, modifier):

        self.modifiers.append(
            modifier
        )

    def calculate_chance(
        self,
        person,
        action,
        world
    ):

        chance = 50.0

        for modifier in self.modifiers:

            chance = modifier.modify(
                chance,
                person,
                action,
                world
            )

        return max(
            1.0,
            min(
                99.0,
                chance
            )
        )

    def resolve(
        self,
        person,
        action,
        world
    ):

        chance = self.calculate_chance(
            person,
            action,
            world
        )

        roll = random.uniform(
            0,
            100
        )

        success = (
            roll <= chance
        )

        quality = (
            roll / chance
            if chance > 0
            else 999
        )

        return Outcome(
            success=success,
            chance=chance,
            quality=quality
        )
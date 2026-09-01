# systems/consequences.py


class ConsequenceSystem:

    """
    Converts completed actions into persistent consequences.

    Pipeline:

        Action
          ↓
        Outcome
          ↓
        Consequences
          ↓
        World / Person / Relationship changes
          ↓
        Experience
          ↓
        Memory / Emotion / Motivation / Goals

    This system is deliberately modular. New action types can be
    added without changing the World simulation loop.
    """

    # ==================================================
    # RESOLVE
    # ==================================================

    @staticmethod
    def resolve(
        person,
        action,
        outcome,
        world
    ):

        if not person.is_alive:
            return []

        consequences = []

        action_type = action.action_type

        # ==============================================
        # SURVIVAL
        # ==============================================

        if action_type == "eat":

            consequences.extend(
                ConsequenceSystem._eat(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        elif action_type == "drink":

            consequences.extend(
                ConsequenceSystem._drink(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        elif action_type == "sleep":

            consequences.extend(
                ConsequenceSystem._sleep(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        # ==============================================
        # DEVELOPMENT
        # ==============================================

        elif action_type == "practice":

            consequences.extend(
                ConsequenceSystem._practice(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        # ==============================================
        # ECONOMY
        # ==============================================

        elif action_type == "work":

            consequences.extend(
                ConsequenceSystem._work(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        # ==============================================
        # SOCIAL
        # ==============================================

        elif action_type in (
            "socialize",
            "visit",
            "confront"
        ):

            consequences.extend(
                ConsequenceSystem._social(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        # ==============================================
        # EXPLORATION
        # ==============================================

        elif action_type == "explore":

            consequences.extend(
                ConsequenceSystem._explore(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        # ==============================================
        # AVOIDANCE
        # ==============================================

        elif action_type == "avoid":

            consequences.extend(
                ConsequenceSystem._avoid(
                    person,
                    action,
                    outcome,
                    world
                )
            )

        return consequences

    # ==================================================
    # EAT
    # ==================================================

    @staticmethod
    def _eat(
        person,
        action,
        outcome,
        world
    ):

        survival = person.survival

        old_hunger = survival.hunger

        survival.hunger = max(
            0.0,
            survival.hunger - 0.8
        )

        survival.energy = min(
            1.0,
            survival.energy + 0.1
        )

        return [
            {
                "type": "survival",
                "person": person,
                "effect": "hunger_reduced",
                "amount": old_hunger - survival.hunger
            }
        ]

    # ==================================================
    # DRINK
    # ==================================================

    @staticmethod
    def _drink(
        person,
        action,
        outcome,
        world
    ):

        survival = person.survival

        old_thirst = survival.thirst

        survival.thirst = max(
            0.0,
            survival.thirst - 0.8
        )

        return [
            {
                "type": "survival",
                "person": person,
                "effect": "thirst_reduced",
                "amount": old_thirst - survival.thirst
            }
        ]

    # ==================================================
    # SLEEP
    # ==================================================

    @staticmethod
    def _sleep(
        person,
        action,
        outcome,
        world
    ):

        survival = person.survival

        old_energy = survival.energy

        survival.energy = min(
            1.0,
            survival.energy + 0.8
        )

        survival.sleep = min(
            1.0,
            survival.sleep + 0.8
        )

        return [
            {
                "type": "survival",
                "person": person,
                "effect": "energy_restored",
                "amount": survival.energy - old_energy
            }
        ]

    # ==================================================
    # PRACTICE
    # ==================================================

    @staticmethod
    def _practice(
        person,
        action,
        outcome,
        world
    ):

        skill_name = (
            getattr(
                action.opportunity,
                "skill",
                None
            )
            if getattr(
                action,
                "opportunity",
                None
            )
            else None
        )

        if skill_name is None:

            skill_name = "general"

        amount = 0.05

        person.gain_skill_experience(
            skill_name,
            amount
        )

        return [
            {
                "type": "development",
                "person": person,
                "effect": "skill_experience",
                "skill": skill_name,
                "amount": amount
            }
        ]

    # ==================================================
    # WORK
    # ==================================================

    @staticmethod
    def _work(
        person,
        action,
        outcome,
        world
    ):

        amount = 10.0

        person.earn_money(
            amount
        )

        return [
            {
                "type": "economic",
                "person": person,
                "effect": "money_earned",
                "amount": amount
            }
        ]

    # ==================================================
    # SOCIAL
    # ==================================================

    @staticmethod
    def _social(
        person,
        action,
        outcome,
        world
    ):

        target = getattr(
            action,
            "target",
            None
        )

        if target is None:
            return []

        if not target.is_alive:
            return []

        interaction_type = (
            "conversation"
        )

        if action.action_type == "confront":

            interaction_type = "confrontation"

        elif action.action_type == "visit":

            interaction_type = "visit"

        intensity = 0.5

        if action.action_type == "confront":

            intensity = 0.7

        result = person.interact_with(
            target,
            interaction_type,
            world,
            intensity=intensity
        )

        return [
            {
                "type": "social",
                "person": person,
                "target": target,
                "effect": "interaction",
                "interaction": interaction_type,
                "result": result
            }
        ]

    # ==================================================
    # EXPLORE
    # ==================================================

    @staticmethod
    def _explore(
        person,
        action,
        outcome,
        world
    ):

        amount = 0.05

        person.knowledge[
            "general"
        ] = (
            person.knowledge.get(
                "general",
                0.0
            )
            + amount
        )

        return [
            {
                "type": "development",
                "person": person,
                "effect": "knowledge_gained",
                "amount": amount
            }
        ]

    # ==================================================
    # AVOID
    # ==================================================

    @staticmethod
    def _avoid(
        person,
        action,
        outcome,
        world
    ):

        target = getattr(
            action,
            "target",
            None
        )

        if target is None:
            return []

        relationship = (
            person.get_relationship(
                target
            )
        )

        relationship.familiarity[
            person
        ] = max(
            0.0,
            relationship.familiarity[person]
            - 0.01
        )

        return [
            {
                "type": "social",
                "person": person,
                "target": target,
                "effect": "avoidance"
            }
        ]
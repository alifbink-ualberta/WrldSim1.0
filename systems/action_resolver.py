# systems/action_resolver.py

from systems.outcome import (
    OutcomeSystem,
    BaseChance,
    SkillModifier,
    PersonalityModifier,
    EnergyModifier,
    FamiliarityModifier
)

from systems.action_handlers import (
    EatHandler,
    SleepHandler,
    WorkHandler,
    PracticeHandler,
    ExploreHandler,
    SocializeHandler,
    BuyHandler,
    SellHandler
)


class ActionResolver:

    def __init__(self):

        self.handlers = {}
        self.outcomes = {}

        self.register_defaults()

    # ==========================================
    # REGISTRATION
    # ==========================================

    def register_handler(
        self,
        action_type,
        handler
    ):

        self.handlers[action_type] = handler

    def register_outcome_system(
        self,
        action_type,
        outcome_system
    ):

        self.outcomes[action_type] = (
            outcome_system
        )

    # ==========================================
    # DEFAULT ACTIONS
    # ==========================================

    def register_defaults(self):

        self.register_handler(
            "eat",
            EatHandler()
        )

        self.register_handler(
            "sleep",
            SleepHandler()
        )

        self.register_handler(
            "work",
            WorkHandler()
        )

        self.register_handler(
            "practice",
            PracticeHandler()
        )

        self.register_handler(
            "explore",
            ExploreHandler()
        )

        self.register_handler(
            "socialize",
            SocializeHandler()
        )

        self.register_handler(
            "buy",
            BuyHandler()
        )

        self.register_handler(
            "sell",
            SellHandler()
        )

        self.register_social_outcome()

        self.register_basic_outcome(
            "eat"
        )

        self.register_basic_outcome(
            "sleep"
        )

        self.register_basic_outcome(
            "work"
        )

        self.register_basic_outcome(
            "practice"
        )

        self.register_basic_outcome(
            "explore"
        )

        self.register_basic_outcome(
            "buy"
        )

        self.register_basic_outcome(
            "sell"
        )

    # ==========================================
    # OUTCOME CONFIGURATION
    # ==========================================

    def register_basic_outcome(
        self,
        action_type
    ):

        system = OutcomeSystem()

        system.add_modifier(
            BaseChance(95)
        )

        system.add_modifier(
            EnergyModifier()
        )

        self.register_outcome_system(
            action_type,
            system
        )

    def register_social_outcome(self):

        system = OutcomeSystem()

        system.add_modifier(
            BaseChance(50)
        )

        system.add_modifier(
            SkillModifier(
                "conversation",
                0.6
            )
        )

        system.add_modifier(
            PersonalityModifier(
                "extraversion",
                0.20
            )
        )

        system.add_modifier(
            PersonalityModifier(
                "agreeableness",
                0.10
            )
        )

        system.add_modifier(
            FamiliarityModifier()
        )

        system.add_modifier(
            EnergyModifier()
        )

        self.register_outcome_system(
            "socialize",
            system
        )

    # ==========================================
    # RESOLUTION
    # ==========================================

    def resolve(
        self,
        person,
        action,
        world
    ):

        handler = self.handlers.get(
            action.action_type
        )

        if handler is None:

            return (
                None,
                None,
                f"{person.name} "
                f"does not know how to "
                f"{action.action_type}."
            )

        outcome_system = (
            self.outcomes.get(
                action.action_type
            )
        )

        if outcome_system is None:

            outcome_system = OutcomeSystem()

        outcome = outcome_system.resolve(
            person,
            action,
            world
        )

        if not outcome.success:

            return (
                outcome,
                None,
                f"{person.name} failed to "
                f"successfully complete "
                f"{action.action_type}."
            )

        result = handler.execute(
            person,
            action,
            world,
            outcome
        )

        return (
            outcome,
            result,
            result
        )
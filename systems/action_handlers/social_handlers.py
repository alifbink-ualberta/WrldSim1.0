# systems/action_handlers/social_handlers.py


class TalkHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        from systems.social_interaction import (
            SocialInteractionSystem
        )

        target = action.target

        result = SocialInteractionSystem.perform(
            person,
            target,
            "conversation",
            world,
            intensity=0.3
        )

        return (
            f"{person.full_name} talks "
            f"with {target.full_name}."
        )


class SpendTimeHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        from systems.social_interaction import (
            SocialInteractionSystem
        )

        target = action.target

        result = SocialInteractionSystem.perform(
            person,
            target,
            "companionship",
            world,
            intensity=0.5
        )

        return (
            f"{person.full_name} spends time "
            f"with {target.full_name}."
        )


class HelpPersonHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        from systems.social_interaction import (
            SocialInteractionSystem
        )

        target = action.target

        result = SocialInteractionSystem.perform(
            person,
            target,
            "help",
            world,
            intensity=0.5
        )

        return (
            f"{person.full_name} helps "
            f"{target.full_name}."
        )


class InsultPersonHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        from systems.social_interaction import (
            SocialInteractionSystem
        )

        target = action.target

        result = SocialInteractionSystem.perform(
            person,
            target,
            "insult",
            world,
            intensity=0.6
        )

        return (
            f"{person.full_name} insults "
            f"{target.full_name}."
        )


class ThreatenHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        from systems.social_interaction import (
            SocialInteractionSystem
        )

        target = action.target

        result = SocialInteractionSystem.perform(
            person,
            target,
            "threat",
            world,
            intensity=0.8
        )

        return (
            f"{person.full_name} threatens "
            f"{target.full_name}."
        )

from simulation.action import Action


class Behavior:

    action_type = "unknown"
    duration = 10

    def is_available(self, person, world):

        return True

    def create_action(self, person, world):

        return Action(
            actor=person,
            action_type=self.action_type
        )

    def get_duration(self, action):

        return self.duration


# ==================================================
# SURVIVAL
# ==================================================


class EatBehavior(Behavior):

    action_type = "eat"
    duration = 10

    def is_available(self, person, world):

        return (
            person.hunger >= 40
            and (
                person.has_item("food")
                or person.has_item("meat")
            )
        )


class SleepBehavior(Behavior):

    action_type = "sleep"
    duration = 8 * 60

    def is_available(self, person, world):

        return person.energy <= 30


# ==================================================
# OCCUPATION
# ==================================================


class WorkBehavior(Behavior):

    action_type = "work"
    duration = 4 * 60

    def is_available(self, person, world):

        return (
            person.occupation is not None
            and person.energy > 10
        )


# ==================================================
# DEVELOPMENT
# ==================================================


class PracticeBehavior(Behavior):

    action_type = "practice"
    duration = 2 * 60

    def is_available(self, person, world):

        return person.energy > 15


# ==================================================
# SOCIAL
# ==================================================


class SocializeBehavior(Behavior):

    action_type = "socialize"
    duration = 30

    def is_available(self, person, world):

        for other in world.people:

            if other == person:
                continue

            if other.location == person.location:
                return True

        return False

    def create_action(self, person, world):

        from systems.social import (
            choose_social_target
        )

        target = choose_social_target(
            person,
            world
        )

        if target is None:
            return None

        return Action(
            actor=person,
            action_type="socialize",
            target=target,
            reason="social_need"
        )


# ==================================================
# EXPLORATION
# ==================================================


class ExploreBehavior(Behavior):

    action_type = "explore"
    duration = 4 * 60

    def is_available(self, person, world):

        return person.energy > 15


# ==================================================
# DEFAULT REGISTRY
# ==================================================


def create_default_registry():

    from systems.behavior_registry import BehaviorRegistry

    registry = BehaviorRegistry()

    registry.register_many([
        EatBehavior(),
        SleepBehavior(),
        WorkBehavior(),
        PracticeBehavior(),
        SocializeBehavior(),
        ExploreBehavior()
    ])

    return registry
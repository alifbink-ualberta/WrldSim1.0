# systems/action_handlers.py


from simulation.event import Event
from simulation.action_result import ActionResult


# ==================================================
# BASE HANDLER
# ==================================================

class ActionHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        raise NotImplementedError


# ==================================================
# EAT
# ==================================================

class EatHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        # ------------------------------------------
        # Find food
        # ------------------------------------------

        if not person.inventory:

            event = Event(
                name="Eating",
                description=(
                    f"{person.full_name} "
                    f"attempted to eat."
                ),
                event_type="eat",
                participants=[person],
                location=person.location
            )

            return ActionResult(
                event=event,
                message=(
                    f"{person.full_name} "
                    f"has nothing to eat."
                )
            )

        # ------------------------------------------
        # Consume first available item
        # ------------------------------------------

        item = next(
            iter(person.inventory)
        )

        person.remove_item(
            item
        )

        event = Event(
            name="Eating",
            description=(
                f"{person.full_name} "
                f"ate {item}."
            ),
            event_type="eat",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"ate {item}."
            ),
            data={
                "item": item
            }
        )


# ==================================================
# SLEEP
# ==================================================

class SleepHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        event = Event(
            name="Sleeping",
            description=(
                f"{person.full_name} "
                f"went to sleep."
            ),
            event_type="sleep",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"went to sleep."
            )
        )


# ==================================================
# WORK
# ==================================================

class WorkHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        earnings = 10

        person.earn_money(
            earnings
        )

        event = Event(
            name="Working",
            description=(
                f"{person.full_name} "
                f"worked and earned "
                f"{earnings} money."
            ),
            event_type="work",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"worked and earned "
                f"{earnings}."
            ),
            data={
                "earnings": earnings
            }
        )


# ==================================================
# PRACTICE
# ==================================================

class PracticeHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        skill_name = "general"

        person.gain_skill_experience(
            skill_name,
            1.0
        )

        event = Event(
            name="Practice",
            description=(
                f"{person.full_name} "
                f"practiced {skill_name}."
            ),
            event_type="practice",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"practiced."
            ),
            data={
                "skill": skill_name
            }
        )


# ==================================================
# EXPLORE
# ==================================================

class ExploreHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        event = Event(
            name="Exploration",
            description=(
                f"{person.full_name} "
                f"explored the world."
            ),
            event_type="explore",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"explored."
            )
        )


# ==================================================
# SOCIALIZE
# ==================================================

class SocializeHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        target = action.target

        if target is None:

            event = Event(
                name="Social Interaction",
                description=(
                    f"{person.full_name} "
                    f"attempted to socialize."
                ),
                event_type="socialize",
                participants=[person],
                location=person.location
            )

            return ActionResult(
                event=event,
                message=(
                    f"{person.full_name} "
                    f"had nobody to socialize with."
                )
            )

        # ------------------------------------------
        # Interaction event
        # ------------------------------------------

        event = Event(
            name="Social Interaction",
            description=(
                f"{person.full_name} "
                f"interacted with "
                f"{target.full_name}."
            ),
            event_type="socialize",
            participants=[
                person,
                target
            ],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"socialized with "
                f"{target.full_name}."
            ),
            data={
                "target": target
            }
        )


# ==================================================
# TALK
# ==================================================

class TalkHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        target = action.target

        event = Event(
            name="Conversation",
            description=(
                f"{person.full_name} "
                f"talked with "
                f"{target.full_name}."
            ),
            event_type="talk",
            participants=[
                person,
                target
            ],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"talked with "
                f"{target.full_name}."
            ),
            data={
                "target": target
            }
        )


# ==================================================
# HELP
# ==================================================

class HelpHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        target = action.target

        event = Event(
            name="Helping Someone",
            description=(
                f"{person.full_name} "
                f"helped "
                f"{target.full_name}."
            ),
            event_type="help",
            participants=[
                person,
                target
            ],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"helped "
                f"{target.full_name}."
            ),
            data={
                "target": target
            }
        )


# ==================================================
# COMPLIMENT
# ==================================================

class ComplimentHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        target = action.target

        event = Event(
            name="Compliment",
            description=(
                f"{person.full_name} "
                f"complimented "
                f"{target.full_name}."
            ),
            event_type="compliment",
            participants=[
                person,
                target
            ],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"complimented "
                f"{target.full_name}."
            ),
            data={
                "target": target
            }
        )


# ==================================================
# INSULT
# ==================================================

class InsultHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        target = action.target

        event = Event(
            name="Insult",
            description=(
                f"{person.full_name} "
                f"insulted "
                f"{target.full_name}."
            ),
            event_type="insult",
            participants=[
                person,
                target
            ],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"insulted "
                f"{target.full_name}."
            ),
            data={
                "target": target
            }
        )


# ==================================================
# THREAT
# ==================================================

class ThreatHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        target = action.target

        event = Event(
            name="Threat",
            description=(
                f"{person.full_name} "
                f"threatened "
                f"{target.full_name}."
            ),
            event_type="threat",
            participants=[
                person,
                target
            ],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"threatened "
                f"{target.full_name}."
            ),
            data={
                "target": target
            }
        )


# ==================================================
# BUY
# ==================================================

class BuyHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        item = action.target

        price = 10

        if not person.spend_money(
            price
        ):

            event = Event(
                name="Purchase Attempt",
                description=(
                    f"{person.full_name} "
                    f"could not afford "
                    f"{item}."
                ),
                event_type="buy",
                participants=[person],
                location=person.location
            )

            return ActionResult(
                event=event,
                message=(
                    f"{person.full_name} "
                    f"could not afford "
                    f"{item}."
                )
            )

        person.add_item(
            item
        )

        event = Event(
            name="Purchase",
            description=(
                f"{person.full_name} "
                f"bought {item}."
            ),
            event_type="buy",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"bought {item}."
            ),
            data={
                "item": item,
                "price": price
            }
        )


# ==================================================
# SELL
# ==================================================

class SellHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        item = action.target

        if not person.has_item(
            item
        ):

            event = Event(
                name="Sale Attempt",
                description=(
                    f"{person.full_name} "
                    f"does not have "
                    f"{item} to sell."
                ),
                event_type="sell",
                participants=[person],
                location=person.location
            )

            return ActionResult(
                event=event,
                message=(
                    f"{person.full_name} "
                    f"does not have "
                    f"{item} to sell."
                )
            )

        person.remove_item(
            item
        )

        earnings = 5

        person.earn_money(
            earnings
        )

        event = Event(
            name="Sale",
            description=(
                f"{person.full_name} "
                f"sold {item}."
            ),
            event_type="sell",
            participants=[person],
            location=person.location
        )

        return ActionResult(
            event=event,
            message=(
                f"{person.full_name} "
                f"sold {item}."
            ),
            data={
                "item": item,
                "earnings": earnings
            }
        )

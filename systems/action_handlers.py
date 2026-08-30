# systems/action_handlers.py


class ActionHandler:

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        raise NotImplementedError


class EatHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        item = (
            "food"
            if person.has_item("food")
            else "meat"
        )

        if not person.has_item(item):

            return (
                f"{person.name} has no food."
            )

        person.remove_item(
            item,
            1
        )

        person.hunger = max(
            0,
            person.hunger - 50
        )

        person.energy = max(
            0,
            person.energy - 2
        )

        return (
            f"{person.name} ate {item}."
        )


class SleepHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        person.energy = min(
            100,
            person.energy + 60
        )

        return (
            f"{person.name} slept."
        )


class WorkHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        person.energy = max(
            0,
            person.energy - 10
        )

        person.hunger = min(
            100,
            person.hunger + 4
        )

        production = {
            "Farmer": ("food", 3),
            "Hunter": ("meat", 2),
            "Blacksmith": ("tools", 1),
        }

        result = production.get(
            person.occupation
        )

        if result:

            item, amount = result

            person.add_item(
                item,
                amount
            )

            return (
                f"{person.name} worked as "
                f"a {person.occupation} "
                f"and produced "
                f"{amount} {item}."
            )

        if person.occupation == "Merchant":

            person.earn_money(5)

            return (
                f"{person.name} conducted "
                f"business and earned 5 money."
            )

        return (
            f"{person.name} worked."
        )


class PracticeHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        person.energy = max(
            0,
            person.energy - 8
        )

        person.hunger = min(
            100,
            person.hunger + 2
        )

        return (
            f"{person.name} practiced "
            f"their skills."
        )


class ExploreHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        person.energy = max(
            0,
            person.energy - 8
        )

        person.hunger = min(
            100,
            person.hunger + 3
        )

        return (
            f"{person.name} explored."
        )


class SocializeHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        from systems.social import (
            social_interaction
        )

        target = action.target

        if target is None:

            return (
                f"{person.name} found "
                f"nobody to socialize with."
            )

        person.energy = max(
            0,
            person.energy - 4
        )

        return social_interaction(
            person,
            target,
            world,
            outcome
        )


class BuyHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        seller = action.target

        if seller is None:

            return (
                f"{person.name} "
                f"could not buy anything."
            )

        total_price = (
            action.price
            * action.amount
        )

        if person.money < total_price:

            return (
                f"{person.name} "
                f"cannot afford "
                f"{action.item}."
            )

        if not seller.has_item(
            action.item,
            action.amount
        ):

            return (
                f"{seller.name} "
                f"does not have "
                f"{action.item}."
            )

        seller.remove_item(
            action.item,
            action.amount
        )

        person.add_item(
            action.item,
            action.amount
        )

        person.spend_money(
            total_price
        )

        seller.earn_money(
            total_price
        )

        person.change_relationship(
            seller,
            2
        )

        return (
            f"{person.name} bought "
            f"{action.amount} "
            f"{action.item} from "
            f"{seller.name} for "
            f"{total_price}."
        )


class SellHandler(ActionHandler):

    def execute(
        self,
        person,
        action,
        world,
        outcome
    ):

        buyer = action.target

        if buyer is None:

            return (
                f"{person.name} "
                f"could not sell anything."
            )

        total_price = (
            action.price
            * action.amount
        )

        if not person.has_item(
            action.item,
            action.amount
        ):

            return (
                f"{person.name} "
                f"does not have "
                f"{action.item}."
            )

        if buyer.money < total_price:

            return (
                f"{buyer.name} "
                f"cannot afford "
                f"{action.item}."
            )

        person.remove_item(
            action.item,
            action.amount
        )

        buyer.add_item(
            action.item,
            action.amount
        )

        person.earn_money(
            total_price
        )

        buyer.spend_money(
            total_price
        )

        person.change_relationship(
            buyer,
            2
        )

        return (
            f"{person.name} sold "
            f"{action.amount} "
            f"{action.item} to "
            f"{buyer.name} for "
            f"{total_price}."
        )
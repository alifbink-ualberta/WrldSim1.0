from simulation.opportunity import Opportunity


RESOURCE_PRICES = {

    "food": 5,
    "meat": 7,
    "tools": 15
}


def get_people_nearby(person, world):

    nearby = []

    for other in world.people:

        if other is person:
            continue

        if (
            other.location == person.location
        ):

            nearby.append(other)

    return nearby


def generate_trade_opportunities(
    person,
    world
):

    opportunities = []

    nearby_people = get_people_nearby(
        person,
        world
    )

    # =====================================
    # SELLING
    # =====================================

    for item, amount in person.inventory.items():

        if amount <= 0:
            continue

        if item not in RESOURCE_PRICES:
            continue

        price = RESOURCE_PRICES[item]

        for other in nearby_people:

            # Other person must actually
            # be able to afford the item.

            if other.money < price:
                continue

            opportunities.append(
                Opportunity(
                    actor=person,
                    action_type="sell",
                    target=other,
                    item=item,
                    amount=1,
                    price=price,
                    reason="has_surplus"
                )
            )

    # =====================================
    # BUYING
    # =====================================

    for other in nearby_people:

        for item, amount in other.inventory.items():

            if amount <= 0:
                continue

            if item not in RESOURCE_PRICES:
                continue

            price = RESOURCE_PRICES[item]

            if person.money < price:
                continue

            opportunities.append(
                Opportunity(
                    actor=person,
                    action_type="buy",
                    target=other,
                    item=item,
                    amount=1,
                    price=price,
                    reason="needs_resource"
                )
            )

    return opportunities
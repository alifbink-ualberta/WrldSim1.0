# systems/opportunities.py


from simulation.opportunity import Opportunity


def generate_opportunities(person, world):

    opportunities = []

    # ==========================================
    # BASIC PERSONAL OPPORTUNITIES
    # ==========================================

    opportunities.append(
        Opportunity("eat")
    )

    opportunities.append(
        Opportunity("sleep")
    )

    opportunities.append(
        Opportunity("practice")
    )

    opportunities.append(
        Opportunity("explore")
    )

    # ==========================================
    # SOCIAL OPPORTUNITIES
    # ==========================================

    for other in world.people:

        if other == person:
            continue

        # People in the same location can interact.

        if (
            person.location is not None
            and other.location == person.location
        ):

            opportunities.append(
                Opportunity(
                    "socialize",
                    target=other
                )
            )

    # ==========================================
    # WORK
    # ==========================================

    # For now, work is available everywhere.
    #
    # Later this will come from actual workplaces,
    # employers, contracts and occupations.

    opportunities.append(
        Opportunity("work")
    )

    # ==========================================
    # FILTER
    # ==========================================

    available = []

    for opportunity in opportunities:

        if opportunity.is_available(
            person,
            world
        ):

            available.append(
                opportunity
            )

    return available
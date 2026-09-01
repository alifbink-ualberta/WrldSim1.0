# systems/opportunities.py


from simulation.opportunity import Opportunity


def generate_opportunities(
    person,
    world
):

    opportunities = []

    # ==========================================
    # SURVIVAL
    # ==========================================

    opportunities.append(
        Opportunity("eat")
    )

    opportunities.append(
        Opportunity("sleep")
    )

    # ==========================================
    # PERSONAL DEVELOPMENT
    # ==========================================

    opportunities.append(
        Opportunity("practice")
    )

    opportunities.append(
        Opportunity("explore")
    )

    # ==========================================
    # WORK
    # ==========================================

    opportunities.append(
        Opportunity("work")
    )

    # ==========================================
    # SOCIAL INTERACTIONS
    # ==========================================

    for other in world.people:

        if other == person:
            continue

        if not other.is_alive:
            continue

        # --------------------------------------
        # Must be co-located
        # --------------------------------------

        if (
            person.location is None
            or other.location != person.location
        ):

            continue

        # --------------------------------------
        # Conversation
        # --------------------------------------

        opportunities.append(
            Opportunity(
                "talk",
                target=other
            )
        )

        # --------------------------------------
        # Help
        # --------------------------------------

        opportunities.append(
            Opportunity(
                "help",
                target=other
            )
        )

        # --------------------------------------
        # Compliment
        # --------------------------------------

        opportunities.append(
            Opportunity(
                "compliment",
                target=other
            )
        )

        # --------------------------------------
        # Insult
        # --------------------------------------

        opportunities.append(
            Opportunity(
                "insult",
                target=other
            )
        )

        # --------------------------------------
        # Threaten
        # --------------------------------------

        opportunities.append(
            Opportunity(
                "threat",
                target=other
            )
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
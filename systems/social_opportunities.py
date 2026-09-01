# systems/social_opportunities.py


from simulation.opportunity import Opportunity


class SocialOpportunitySystem:

    """
    Creates social opportunities involving people
    currently accessible to the person.
    """

    @staticmethod
    def generate(
        person,
        world
    ):

        opportunities = []

        if person.location is None:
            return opportunities

        # ==========================================
        # PEOPLE AT LOCATION
        # ==========================================

        people = getattr(
            person.location,
            "people",
            []
        )

        for other in people:

            if other is person:
                continue

            if not other.is_alive:
                continue

            relationship = (
                person.get_relationship(
                    other
                )
            )

            feelings = relationship.get_feelings(
                person
            )

            # ==========================================
            # TALK
            # ==========================================

            opportunities.append(
                Opportunity(
                    action_type="talk",
                    target=other,
                    location=person.location
                )
            )

            # ==========================================
            # HELP
            # ==========================================

            opportunities.append(
                Opportunity(
                    action_type="help_person",
                    target=other,
                    location=person.location
                )
            )

            # ==========================================
            # SPEND TIME
            # ==========================================

            if feelings["affection"] > 30:

                opportunities.append(
                    Opportunity(
                        action_type="spend_time",
                        target=other,
                        location=person.location
                    )
                )

            # ==========================================
            # INSULT
            # ==========================================

            if feelings["resentment"] > 40:

                opportunities.append(
                    Opportunity(
                        action_type="insult_person",
                        target=other,
                        location=person.location
                    )
                )

            # ==========================================
            # THREATEN
            # ==========================================

            if feelings["resentment"] > 70:

                opportunities.append(
                    Opportunity(
                        action_type="threaten",
                        target=other,
                        location=person.location
                    )
                )

        return opportunities

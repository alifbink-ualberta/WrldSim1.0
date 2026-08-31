# systems/interpretation.py


from simulation.interpretation import Interpretation
from simulation.intent import PerceivedIntent


def interpret_event(person, perception):

    # ==========================================
    # PERCEPTION
    # ==========================================

    event = perception["event"]

    clarity = perception["clarity"]

    if not perception["noticed"]:

        interpretation = Interpretation(
            person=person,
            event=event,
            meaning=(
                f"{person.full_name} did not "
                f"notice the event."
            ),
            emotional_impact=0.0
        )

        interpretation.perceived_intent = None

        return interpretation

    event_type = event.event_type

    # ==========================================
    # BASIC INTERPRETATION
    # ==========================================

    if event_type == "insult":

        meaning = "I have been disrespected."
        impact = 0.5

    elif event_type == "compliment":

        meaning = "I have been appreciated."
        impact = 0.3

    elif event_type == "help":

        meaning = "Someone has helped me."
        impact = 0.3

    elif event_type == "threat":

        meaning = "I am in danger."
        impact = 0.7

    elif event_type == "gift":

        meaning = "Someone has given me something."
        impact = 0.3

    elif event_type == "betrayal":

        meaning = (
            "Someone I trusted has betrayed me."
        )

        impact = 0.8

    elif event_type == "death":

        meaning = "Someone has died."
        impact = 0.8

    else:

        meaning = event.description
        impact = event.significance

    # ==========================================
    # PERCEPTION CLARITY
    # ==========================================

    # Someone who only partially perceives an
    # event should generally experience less
    # certainty and emotional impact.

    impact *= clarity

    # ==========================================
    # FIND OTHER PERSON
    # ==========================================

    other = None

    for participant in event.participants:

        if participant != person:

            other = participant
            break

    # ==========================================
    # PERSONALITY
    # ==========================================

    if event_type == "insult":

        impact += (
            person.personality.narcissism
            * 0.3
        )

        impact += (
            person.personality.neuroticism
            * 0.2
        )

    if event_type == "compliment":

        impact += (
            person.personality.narcissism
            * 0.15
        )

    if event_type == "threat":

        impact += (
            person.personality.neuroticism
            * 0.3
        )

    # ==========================================
    # RELATIONSHIP
    # ==========================================

    relationship = None
    feelings = None

    if other is not None:

        relationship = person.get_relationship(
            other
        )

        feelings = relationship.get_feelings(
            person
        )

        # --------------------------------------
        # INSULT
        # --------------------------------------

        if event_type == "insult":

            if feelings["trust"] > 50:

                meaning = (
                    "Someone I trust has insulted me."
                )

                impact -= 0.15

            if feelings["affection"] > 50:

                impact -= 0.10

            if feelings["resentment"] > 50:

                meaning = (
                    "Someone I resent is deliberately "
                    "disrespecting me."
                )

                impact += 0.15

            if feelings["respect"] > 50:

                impact += 0.05

            if feelings["fear"] > 50:

                meaning = (
                    "Someone I fear has "
                    "disrespected me."
                )

                impact += 0.10

        # --------------------------------------
        # HELP
        # --------------------------------------

        elif event_type == "help":

            if feelings["trust"] > 50:

                meaning = (
                    "Someone I trust has helped me."
                )

            if feelings["affection"] > 50:

                impact += 0.10

        # --------------------------------------
        # GIFT
        # --------------------------------------

        elif event_type == "gift":

            if feelings["trust"] > 50:

                meaning = (
                    "Someone I trust has given "
                    "me something."
                )

            if feelings["resentment"] > 50:

                meaning = (
                    "Someone I resent has given "
                    "me something."
                )

                impact += 0.10

        # --------------------------------------
        # THREAT
        # --------------------------------------

        elif event_type == "threat":

            if feelings["fear"] > 50:

                meaning = (
                    "Someone I fear has "
                    "threatened me."
                )

                impact += 0.20

            if feelings["trust"] > 50:

                impact -= 0.10

    # ==========================================
    # PERCEIVED INTENT
    # ==========================================

    perceived_intent = None

    if other is not None:

        intention = "interact with me"
        confidence = 0.5

        # --------------------------------------
        # INSULT
        # --------------------------------------

        if event_type == "insult":

            if feelings["trust"] > 50:

                intention = (
                    "tease or provoke me without "
                    "serious hostility"
                )

                confidence = 0.6

            elif feelings["resentment"] > 50:

                intention = (
                    "deliberately disrespect me"
                )

                confidence = 0.8

            elif feelings["fear"] > 50:

                intention = (
                    "intimidate me"
                )

                confidence = 0.7

            else:

                intention = (
                    "humiliate or disrespect me"
                )

                confidence = 0.5

        # --------------------------------------
        # HELP
        # --------------------------------------

        elif event_type == "help":

            if feelings["trust"] > 50:

                intention = (
                    "help me because they care"
                )

                confidence = 0.7

            else:

                intention = (
                    "help me for some reason"
                )

                confidence = 0.5

        # --------------------------------------
        # GIFT
        # --------------------------------------

        elif event_type == "gift":

            if feelings["trust"] > 50:

                intention = (
                    "give me something sincerely"
                )

                confidence = 0.7

            elif feelings["resentment"] > 50:

                intention = (
                    "manipulate or influence me"
                )

                confidence = 0.6

            else:

                intention = (
                    "gain something from me"
                )

                confidence = 0.4

        # --------------------------------------
        # THREAT
        # --------------------------------------

        elif event_type == "threat":

            intention = (
                "harm or intimidate me"
            )

            confidence = 0.8

        # --------------------------------------
        # PERCEPTION UNCERTAINTY
        # --------------------------------------

        # Poor perception means weaker confidence
        # in the interpretation.

        confidence *= clarity

        perceived_intent = PerceivedIntent(
            person=person,
            other=other,
            event=event,
            intention=intention,
            confidence=round(
                confidence,
                2
            )
        )

    # ==========================================
    # LIMIT IMPACT
    # ==========================================

    impact = max(
        0.0,
        min(1.0, impact)
    )

    # ==========================================
    # CREATE INTERPRETATION
    # ==========================================

    interpretation = Interpretation(
        person=person,
        event=event,
        meaning=meaning,
        emotional_impact=round(
            impact,
            2
        )
    )

    # Attach perceived intent.

    interpretation.perceived_intent = (
        perceived_intent
    )

    return interpretation
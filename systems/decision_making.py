import random


def choose_action(person, world):

    # Critical needs override everything else.

    if person.hunger >= 80:
        return "EAT"

    if person.energy <= 15:
        return "SLEEP"

    if person.social <= 20:
        return "TALK"

    # Personality influences behavior.

    choices = []

    # Everyone needs to work.
    choices += ["WORK"] * 5

    # Sociable people talk more.
    choices += [
        "TALK"
    ] * max(
        1,
        person.sociability // 20
    )

    # Curious people explore.
    if person.curiosity >= 60:

        choices += [
            "EXPLORE"
        ] * 2

    # Sometimes people rest.
    choices += [
        "REST"
    ] * 2

    return random.choice(choices)
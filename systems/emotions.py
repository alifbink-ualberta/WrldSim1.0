def process_interaction_emotion(
    person,
    interaction
):

    interaction_type = (
        interaction.interaction_type
    )

    # ==========================================
    # INSULT
    # ==========================================

    if interaction_type == "insult":

        person.emotions.change(
            "anger",
            0.25
        )

        person.emotions.change(
            "embarrassment",
            0.15
        )

    # ==========================================
    # COMPLIMENT
    # ==========================================

    elif interaction_type == "compliment":

        person.emotions.change(
            "joy",
            0.15
        )

        person.emotions.change(
            "pride",
            0.10
        )

    # ==========================================
    # HELP
    # ==========================================

    elif interaction_type == "help":

        person.emotions.change(
            "joy",
            0.10
        )

        person.emotions.change(
            "love",
            0.03
        )

    # ==========================================
    # THREAT
    # ==========================================

    elif interaction_type == "threaten":

        person.emotions.change(
            "fear",
            0.30
        )

        person.emotions.change(
            "anger",
            0.10
        )
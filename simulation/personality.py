# simulation/personality.py


class Personality:

    def __init__(
        self,
        openness=0.5,
        conscientiousness=0.5,
        extraversion=0.5,
        agreeableness=0.5,
        neuroticism=0.5,
        machiavellianism=0.5,
        narcissism=0.5,
        psychopathy=0.5,
        sadism=0.5
    ):

        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

        self.machiavellianism = machiavellianism
        self.narcissism = narcissism
        self.psychopathy = psychopathy
        self.sadism = sadism

    # ==================================================
    # DEVELOPMENT
    # ==================================================

    def modify_trait(
        self,
        trait,
        amount
    ):

        if not hasattr(
            self,
            trait
        ):
            return False

        value = getattr(
            self,
            trait
        )

        value += amount

        value = max(
            0.0,
            min(1.0, value)
        )

        setattr(
            self,
            trait,
            value
        )

        return True
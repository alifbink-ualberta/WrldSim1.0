# simulation/interaction.py


class Interaction:

    def __init__(
        self,
        interaction_type,
        actor,
        target=None,
        intensity=0.5,
        subject=None
    ):

        self.interaction_type = interaction_type

        self.actor = actor
        self.target = target

        # 0.0 - 1.0
        self.intensity = max(
            0.0,
            min(1.0, intensity)
        )

        # Optional third-party subject.
        #
        # Example:
        # Arthur gossips with Thomas about Edward.
        #
        self.subject = subject

    def participants(self):

        people = [self.actor]

        if (
            self.target is not None
            and self.target not in people
        ):

            people.append(
                self.target
            )

        if (
            self.subject is not None
            and self.subject not in people
        ):

            people.append(
                self.subject
            )

        return people

    def __str__(self):

        if self.target is None:

            return (
                f"{self.actor.full_name} "
                f"{self.interaction_type}"
            )

        return (
            f"{self.actor.full_name} "
            f"{self.interaction_type} "
            f"{self.target.full_name}"
        )

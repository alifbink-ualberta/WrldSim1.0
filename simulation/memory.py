# simulation/memory.py


class Memory:

    def __init__(
        self,
        person,
        experience,
        emotional_significance=0.5
    ):

        self.person = person
        self.experience = experience

        # How important this memory is
        self.emotional_significance = (
            emotional_significance
        )

        # How accurately it is currently remembered
        self.accuracy = 1.0

        # Number of times this memory has been recalled
        self.recall_count = 0

    def recall(self):

        self.recall_count += 1

        return self.experience.description
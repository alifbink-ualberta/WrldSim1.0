# simulation/relationship.py


class Relationship:

    def __init__(self, person_a, person_b):

        self.person_a = person_a
        self.person_b = person_b

        # Emotional dimensions

        self.affection = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.trust = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.respect = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.fear = {
            person_a: 0.0,
            person_b: 0.0
        }

        self.resentment = {
            person_a: 0.0,
            person_b: 0.0
        }

        # Connections

        self.connections = set()

        # Shared history

        self.memories = []
from dataclasses import dataclass, field


@dataclass
class Person:

    # -------------------------
    # IDENTITY
    # -------------------------

    name: str
    age: int
    species: str

    # -------------------------
    # PERSONALITY
    # -------------------------

    openness: int
    conscientiousness: int
    extraversion: int
    agreeableness: int
    neuroticism: int

    machiavellianism: int
    narcissism: int
    psychopathy: int
    sadism: int

    # -------------------------
    # CIRCUMSTANCE
    # -------------------------

    occupation: str = "Unemployed"
    money: int = 50

    health: int = 100
    energy: int = 80
    hunger: int = 20

    location: str = "Home"

    # -------------------------
    # PSYCHOLOGICAL STATE
    # -------------------------

    goals: list = field(default_factory=list)

    # Things the person personally remembers
    memories: list = field(default_factory=list)

    # What this person thinks about other people
    relationships: dict = field(default_factory=dict)

    # What other people generally think about this person
    reputation: dict = field(default_factory=dict)

    # -------------------------
    # HISTORY
    # -------------------------

    life_events: list = field(default_factory=list)

    # -------------------------
    # METHODS
    # -------------------------

    def remember(self, memory):

        self.memories.append(memory)

        if len(self.memories) > 100:
            self.memories.pop(0)

    def add_life_event(self, event):

        self.life_events.append(event)

    def relationship_with(self, person_name):

        return self.relationships.get(
            person_name,
            50
        )

    def change_relationship(
        self,
        person_name,
        amount
    ):

        current = self.relationship_with(
            person_name
        )

        new_value = max(
            0,
            min(
                100,
                current + amount
            )
        )

        self.relationships[
            person_name
        ] = new_value

    def perform_action(self, action):

        if action == "eat":

            self.hunger = max(
                0,
                self.hunger - 50
            )

            self.energy -= 5

            return f"{self.name} ate a meal."

        elif action == "sleep":

            self.energy = min(
                100,
                self.energy + 60
            )

            return f"{self.name} went to sleep."

        elif action == "work":

            self.energy -= 15
            self.hunger += 5
            self.money += 5

            return (
                f"{self.name} worked as a "
                f"{self.occupation}."
            )

        elif action == "socialize":

            self.energy -= 5

            return (
                f"{self.name} spent time "
                f"socializing."
            )

        elif action == "practice":

            self.energy -= 10

            return (
                f"{self.name} practiced "
                f"their skills."
            )

        elif action == "explore":

            self.energy -= 10

            return (
                f"{self.name} explored "
                f"the surrounding area."
            )

        return f"{self.name} did nothing."
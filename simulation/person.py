from dataclasses import dataclass, field


@dataclass
class Person:

    name: str
    age: int
    species: str
    occupation: str
    money: int

    # Personality
    ambition: int
    aggression: int
    sociability: int
    curiosity: int
    loyalty: int

    # Needs
    hunger: int = 20
    energy: int = 80
    social: int = 50
    safety: int = 80

    location: str = "Home"

    # Social information
    relationships: dict = field(default_factory=dict)

    # Things this person remembers
    memories: list = field(default_factory=list)

    # Current personal objectives
    goals: list = field(default_factory=list)

    def remember(self, memory: str):

        self.memories.append(memory)

        # Keep the prototype manageable
        if len(self.memories) > 50:
            self.memories.pop(0)

    def relationship_with(self, other_name: str):

        return self.relationships.get(other_name, 50)

    def change_relationship(self, other_name: str, amount: int):

        current = self.relationship_with(other_name)

        current += amount

        self.relationships[other_name] = max(
            0,
            min(100, current)
        )
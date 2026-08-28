class Location:

    def __init__(self, name):

        self.name = name
        self.people = []

    def enter(self, person):

        if person not in self.people:
            self.people.append(person)

        person.location = self.name

    def leave(self, person):

        if person in self.people:
            self.people.remove(person)

    def __str__(self):

        return (
            f"{self.name} "
            f"({len(self.people)} people)"
        )
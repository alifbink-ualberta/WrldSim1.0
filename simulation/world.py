from simulation.person import Person
from simulation.event import Event
from systems.needs import update_needs
from systems.decision_making import choose_action

class World:

    def __init__(self):

        self.year = 1
        self.month = 1
        self.day = 1

        self.people = []
        self.events = []

    # -------------------------
    # PEOPLE
    # -------------------------

    def add_person(self, person):

        self.people.append(person)

    # -------------------------
    # EVENTS
    # -------------------------

    def create_event(
        self,
        description,
        participants=None,
        location="",
        importance=50
    ):

        if participants is None:
            participants = []

        event = Event(
            year=self.year,
            month=self.month,
            day=self.day,
            description=description,
            participants=participants,
            location=location,
            importance=importance
        )

        self.events.append(event)

        return event

    # -------------------------
    # TIME
    # -------------------------

    def advance_day(self):

        self.day += 1

        if self.day > 30:

            self.day = 1
            self.month += 1

        if self.month > 12:

            self.month = 1
            self.year += 1

            for person in self.people:
                person.age += 1

    # -------------------------
    # SIMULATION
    # -------------------------

    def simulate_day(self):

        for person in self.people:

            update_needs(person)

            action = choose_action(person)

            result = person.perform_action(
                action
            )

            print(result)

        self.advance_day()

    def run(self, years):

        total_days = years * 360

        for _ in range(total_days):

            self.simulate_day()
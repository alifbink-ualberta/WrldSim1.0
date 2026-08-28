from simulation.person import Person
from simulation.event import Event
from systems.needs import update_needs
from systems.decision_making import choose_action
from systems.routines import get_routine_location

class World:

    def __init__(self):

        self.year = 1
        self.month = 1
        self.day = 1

        self.people = []
        self.events = []

        self.locations = {}

    def add_location(self, location):

        self.locations[location.name] = location

    def add_person(self, person):

        self.people.append(person)

    def move_person(self, person, location_name):

        if location_name not in self.locations:
            return

        # Remove them from their current location
        for location in self.locations.values():

            location.leave(person)

        # Move them
        location = self.locations[location_name]

        location.enter(person)

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

    def check_encounters(self):

        for location in self.locations.values():

            if len(location.people) < 2:
                continue

            for i in range(
                len(location.people)
            ):

                for j in range(
                    i + 1,
                    len(location.people)
                ):

                    person_a = location.people[i]
                    person_b = location.people[j]

                    self.create_event(
                        description=(
                            f"{person_a.name} "
                            f"encountered "
                            f"{person_b.name}."
                        ),
                        participants=[
                            person_a.name,
                            person_b.name
                        ],
                        location=location.name,
                        importance=10
                    )


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

    def simulate_day(self):

        for person in self.people:

            update_needs(person)

            action = choose_action(person)

            person.perform_action(action)

            routine = get_routine_location(person)

            location_index = (
                self.day - 1
            ) % len(routine)

            destination = routine[location_index]

            self.move_person(
                person,
                destination
            )

        self.check_encounters()

        for event in self.events[-10:]:
            print(event)

        self.advance_day()

    def run(self, years):

        total_days = years * 360

        for _ in range(total_days):

            self.simulate_day()
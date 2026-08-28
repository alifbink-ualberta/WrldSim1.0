import random

from simulation.person import Person
from simulation.event import Event
from systems.needs import update_needs
from systems.decision_making import choose_action


class World:

    def __init__(self):

        self.day = 1
        self.hour = 6

        self.people = []
        self.events = []

        self.locations = [
            "Home",
            "Market",
            "Tavern",
            "Farm",
            "Blacksmith",
            "Town Hall",
            "Forest",
        ]

        self.resources = {
            "food": 500,
            "wood": 300,
            "iron": 100,
        }

    # ---------------------------------------------------------
    # PEOPLE
    # ---------------------------------------------------------

    def add_person(self, person):

        self.people.append(person)

    # ---------------------------------------------------------
    # EVENTS
    # ---------------------------------------------------------

    def log_event(self, description):

        event = Event(
            day=self.day,
            hour=self.hour,
            description=description
        )

        self.events.append(event)

        print(event)

    # ---------------------------------------------------------
    # SETUP
    # ---------------------------------------------------------

    def setup(self):

        people = [

            Person(
                "Mariam", 34, "Human", "Farmer", 100,
                70, 30, 80, 60, 75
            ),

            Person(
                "Hassan", 41, "Human", "Merchant", 180,
                85, 20, 70, 75, 50
            ),

            Person(
                "Ahmed", 27, "Human", "Guard", 90,
                60, 70, 45, 40, 80
            ),

            Person(
                "Elira", 22, "Human", "Scholar", 120,
                55, 10, 60, 95, 40
            ),

            Person(
                "Gorak", 31, "Goblin", "Hunter", 70,
                65, 75, 40, 85, 70
            ),

            Person(
                "Mira", 19, "Goblin", "Laborer", 45,
                80, 45, 85, 70, 60
            ),

            Person(
                "Thorin", 58, "Dwarf", "Blacksmith", 160,
                40, 50, 35, 55, 90
            ),

            Person(
                "Borin", 36, "Dwarf", "Miner", 110,
                50, 60, 40, 45, 85
            ),
        ]

        for person in people:
            self.add_person(person)

        self.create_relationships()

    # ---------------------------------------------------------
    # RELATIONSHIPS
    # ---------------------------------------------------------

    def create_relationships(self):

        for person in self.people:

            others = [
                other
                for other in self.people
                if other != person
            ]

            for other in random.sample(
                others,
                min(3, len(others))
            ):

                person.relationships[
                    other.name
                ] = random.randint(30, 80)

    # ---------------------------------------------------------
    # SIMULATION
    # ---------------------------------------------------------

    def simulate_hour(self):

        people = self.people.copy()

        random.shuffle(people)

        for person in people:

            update_needs(person)

            action = choose_action(
                person,
                self
            )

            self.perform_action(
                person,
                action
            )

        self.hour += 1

        if self.hour >= 24:

            self.hour = 0
            self.end_day()

    # ---------------------------------------------------------
    # ACTIONS
    # ---------------------------------------------------------

    def perform_action(self, person, action):

        if action == "WORK":

            self.work(person)

        elif action == "EAT":

            self.eat(person)

        elif action == "SLEEP":

            self.sleep(person)

        elif action == "REST":

            self.rest(person)

        elif action == "TALK":

            self.talk(person)

        elif action == "EXPLORE":

            self.explore(person)

    # ---------------------------------------------------------
    # WORK
    # ---------------------------------------------------------

    def work(self, person):

        person.location = "Work"

        person.energy -= 15
        person.hunger += 10

        earnings = random.randint(5, 15)

        person.money += earnings

        self.log_event(
            f"{person.name} worked as a "
            f"{person.occupation} and earned "
            f"{earnings} coins."
        )

    # ---------------------------------------------------------
    # EAT
    # ---------------------------------------------------------

    def eat(self, person):

        if person.money < 3:

            self.log_event(
                f"{person.name} could not afford food."
            )

            person.hunger += 10

            return

        person.money -= 3

        person.hunger = max(
            0,
            person.hunger - 40
        )

        self.resources["food"] -= 1

        self.log_event(
            f"{person.name} bought food."
        )

    # ---------------------------------------------------------
    # SLEEP
    # ---------------------------------------------------------

    def sleep(self, person):

        person.location = "Home"

        person.energy = min(
            100,
            person.energy + 40
        )

        person.hunger += 5

    # ---------------------------------------------------------
    # REST
    # ---------------------------------------------------------

    def rest(self, person):

        person.energy = min(
            100,
            person.energy + 10
        )

    # ---------------------------------------------------------
    # TALK
    # ---------------------------------------------------------

    def talk(self, person):

        others = [
            other
            for other in self.people
            if other != person
        ]

        other = random.choice(others)

        person.social = min(
            100,
            person.social + 30
        )

        relationship_change = random.randint(
            -5,
            8
        )

        person.change_relationship(
            other.name,
            relationship_change
        )

        person.remember(
            f"Spoke with {other.name}."
        )

        self.log_event(
            f"{person.name} spoke with {other.name}."
        )

    # ---------------------------------------------------------
    # EXPLORE
    # ---------------------------------------------------------

    def explore(self, person):

        person.energy -= 10
        person.hunger += 5

        discoveries = [
            "found nothing interesting",
            "found wild berries",
            "found an abandoned campsite",
            "discovered a small iron deposit",
            "found strange tracks",
        ]

        discovery = random.choice(
            discoveries
        )

        person.remember(
            f"Explored the forest and {discovery}."
        )

        self.log_event(
            f"{person.name} explored the forest and "
            f"{discovery}."
        )

    # ---------------------------------------------------------
    # END DAY
    # ---------------------------------------------------------

    def end_day(self):

        self.log_event(
            f"Day {self.day} has ended."
        )

        self.day += 1

    # ---------------------------------------------------------
    # RUN
    # ---------------------------------------------------------

    def run(self, days):

        total_hours = days * 24

        for _ in range(total_hours):

            self.simulate_hour()
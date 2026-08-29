from simulation.world import World
from simulation.person import Person
from simulation.location import Location


def main():

    world = World()

    # =========================
    # CREATE PEOPLE
    # =========================

    mariam = Person(
        name="Mariam",
        age=24,
        species="Human",

        openness=70,
        conscientiousness=85,
        extraversion=30,
        agreeableness=40,
        neuroticism=60,

        machiavellianism=65,
        narcissism=50,
        psychopathy=15,
        sadism=10,

        occupation="Farmer",
        money=100
    )

    hassan = Person(
        name="Hassan",
        age=29,
        species="Human",

        openness=45,
        conscientiousness=60,
        extraversion=85,
        agreeableness=70,
        neuroticism=35,

        machiavellianism=40,
        narcissism=55,
        psychopathy=10,
        sadism=5,

        occupation="Merchant",
        money=200
    )

    gorak = Person(
        name="Gorak",
        age=31,
        species="Goblin",

        openness=80,
        conscientiousness=35,
        extraversion=45,
        agreeableness=30,
        neuroticism=45,

        machiavellianism=75,
        narcissism=45,
        psychopathy=60,
        sadism=40,

        occupation="Hunter",
        money=70
    )

    elira = Person(
        name="Elira",
        age=22,
        species="Human",

        openness=95,
        conscientiousness=65,
        extraversion=60,
        agreeableness=75,
        neuroticism=50,

        machiavellianism=20,
        narcissism=30,
        psychopathy=5,
        sadism=2,

        occupation="Scholar",
        money=120
    )

    thorin = Person(
        name="Thorin",
        age=58,
        species="Dwarf",

        openness=35,
        conscientiousness=90,
        extraversion=25,
        agreeableness=45,
        neuroticism=30,

        machiavellianism=35,
        narcissism=40,
        psychopathy=10,
        sadism=8,

        occupation="Blacksmith",
        money=200
    )

    # =========================
    # PERSONAL GOALS
    # =========================

    mariam.goals = [
        "Become financially secure",
        "Protect her family"
    ]

    hassan.goals = [
        "Become wealthy",
        "Become respected in the merchant community"
    ]

    gorak.goals = [
        "Become a respected hunter",
        "Build a strong reputation"
    ]

    elira.goals = [
        "Learn about the world",
        "Become a respected scholar"
    ]

    thorin.goals = [
        "Master his craft",
        "Teach his knowledge to someone worthy"
    ]

    # =========================
    # ADD PEOPLE TO WORLD
    # =========================

    people = [
        mariam,
        hassan,
        gorak,
        elira,
        thorin
    ]

    for person in people:
        world.add_person(person)

    # =========================
    # STARTING RESOURCES
    # =========================

    mariam.add_item("food", 40)

    gorak.add_item("meat", 10)

    thorin.add_item("tools", 5)

    # =========================
    # CREATE LOCATIONS
    # =========================

    world.add_location(
        Location("Home")
    )

    world.add_location(
        Location("Market")
    )

    world.add_location(
        Location("Tavern")
    )

    world.add_location(
        Location("Workshop")
    )

    world.add_location(
        Location("Farm")
    )

    world.add_location(
        Location("Library")
    )

    world.add_location(
        Location("Forest")
    )

    # =========================
    # PLACE PEOPLE IN WORLD
    # =========================

    world.move_person(
        mariam,
        "Market"
    )

    world.move_person(
        hassan,
        "Market"
    )

    world.move_person(
        gorak,
        "Market"
    )

    world.move_person(
        elira,
        "Market"
    )

    world.move_person(
        thorin,
        "Market"
    )

    # =========================
    # INITIAL WORLD STATE
    # =========================

    print("WORLD CREATED")
    print()

    for person in world.people:
        print(person)

    print()
    print(
        f"Simulation date: "
        f"Year {world.year}, "
        f"Month {world.month}, "
        f"Day {world.day}, "
        f"{world.hour:02d}:00"
    )

    print()

    # =========================
    # RUN SIMULATION
    # =========================

    world.run_hours(30)

    # =========================
    # FINAL STATE
    # =========================

    print()
    print("SIMULATION COMPLETE")
    print()

    print(
        f"Simulation date: "
        f"Year {world.year}, "
        f"Month {world.month}, "
        f"Day {world.day}, "
        f"{world.hour:02d}:00"
    )

    print()

    for person in world.people:

        print(
            f"{person.name}: "
            f"${person.money} | "
            f"Inventory: {person.inventory} | "
            f"Hunger: {person.hunger} | "
            f"Energy: {person.energy}"
        )


if __name__ == "__main__":
    main()
# test.py


from simulation.world import World
from simulation.person import Person

from systems.event_system import EventSystem
from systems.consequence_system import ConsequenceSystem


# ==========================================
# WORLD
# ==========================================

world = World()


# ==========================================
# PEOPLE
# ==========================================

edward = Person(
    first_name="Edward",
    last_name="Stirling",
    age=55,
    sex="male"
)

arthur = Person(
    first_name="Arthur",
    last_name="Stirling",
    age=25,
    sex="male"
)

thomas = Person(
    first_name="Thomas",
    last_name="Stirling",
    age=22,
    sex="male"
)


# ==========================================
# ADD PEOPLE TO WORLD
# ==========================================

world.add_person(edward)
world.add_person(arthur)
world.add_person(thomas)


# ==========================================
# FAMILY
# ==========================================

arthur.family.add_parent(edward)
thomas.family.add_parent(edward)


# ==========================================
# RELATIONSHIPS
# ==========================================

arthur.get_relationship(edward)
thomas.get_relationship(edward)


# ==========================================
# SHOW FAMILY
# ==========================================

print("Edward's children:")

for person in edward.family.children:

    print(
        f"  - {person.full_name}"
    )


print()

print("Arthur's siblings:")

for person in arthur.family.get_siblings():

    print(
        f"  - {person.full_name}"
    )


# ==========================================
# CREATE DEATH EVENT
# ==========================================

event = EventSystem.create_event(
    world=world,
    name="Death of Edward Stirling",
    description="Edward Stirling has died.",
    event_type="death",
    participants=[edward]
)


print()
print(event.name)
print(event.description)

# ==========================================
# OBSERVE EVENT
# ==========================================

from systems.event_observation import (
    EventObservationSystem
)


observations = (
    EventObservationSystem.observe_all(
        event,
        world
    )
)


for observation in observations:

    person = observation["person"]

    print()
    print(
        f"{person.full_name} experiences the event."
    )

    print(
        "Interpretation:",
        observation["interpretation"]
    )


# ==========================================
# APPLY CONSEQUENCES
# ==========================================

print()

consequences = ConsequenceSystem.apply(
    event,
    world
)


for consequence in consequences:

    print(consequence)


# ==========================================
# CHECK WORLD STATE
# ==========================================

print()

print(
    "Edward alive:",
    edward.is_alive
)

print(
    "Arthur alive:",
    arthur.is_alive
)

print(
    "Thomas alive:",
    thomas.is_alive
)

print(
    "Arthur memories:",
    len(arthur.memories)
)

print(
    "Thomas memories:",
    len(thomas.memories)
)

print(
    "Event resolved:",
    event.resolved
)

# ==========================================
# PROCESS EVENT
# ==========================================

from systems.experience_system import (
    ExperienceSystem
)

experiences = (
    ExperienceSystem.process_event(
        event,
        world
    )
)

for experience in experiences:

    person = experience["person"]

    print()

    print(
        f"{person.full_name}"
    )

    print(
        "Interpretation:",
        experience["interpretation"]
    )

    print(
        "Emotional significance:",
        round(
            experience["significance"],
            2
        )
    )

    print(
        "Memory created:",
        len(person.memories)
    )
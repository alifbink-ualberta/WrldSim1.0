from simulation.world import World
from simulation.person import Person
from systems.event_system import EventSystem
from systems.consequence_system import ConsequenceSystem


world = World()

arthur = Person(
    first_name="Arthur",
    last_name="Stirling",
    age=25,
    sex="male"
)

world.add_person(arthur)


event = EventSystem.create_event(
    world,
    name="Father's Death",
    description="Arthur's father has died.",
    participants=[arthur]
)


print(event.name)
print(event.description)

print()

consequences = ConsequenceSystem.apply(
    event,
    world
)

for consequence in consequences:

    print(consequence)

print()

print(
    "Memories:",
    len(arthur.memories)
)

print(
    "Event resolved:",
    event.resolved
)
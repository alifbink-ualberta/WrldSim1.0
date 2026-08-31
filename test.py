from simulation.world import World
from simulation.person import Person
from simulation.event import Event
from systems.interpretation import interpret_event


world = World()


# ==========================================
# PEOPLE
# ==========================================

arthur = Person(
    first_name="Arthur",
    last_name="Stirling",
    age=30,
    sex="male"
)

thomas = Person(
    first_name="Thomas",
    last_name="Stirling",
    age=30,
    sex="male"
)

marcus = Person(
    first_name="Marcus",
    last_name="Black",
    age=30,
    sex="male"
)


# ==========================================
# PERSONALITY
# ==========================================

arthur.personality.narcissism = 0.9
arthur.personality.neuroticism = 0.2

thomas.personality.narcissism = 0.1
thomas.personality.neuroticism = 0.8


# ==========================================
# RELATIONSHIP: ARTHUR ↔ MARCUS
# ==========================================

arthur_marcus = arthur.get_relationship(
    marcus
)

arthur_marcus.affection[arthur] = 80
arthur_marcus.trust[arthur] = 90
arthur_marcus.respect[arthur] = 70
arthur_marcus.familiarity[arthur] = 90


# ==========================================
# RELATIONSHIP: THOMAS ↔ MARCUS
# ==========================================

thomas_marcus = thomas.get_relationship(
    marcus
)

thomas_marcus.affection[thomas] = -50
thomas_marcus.trust[thomas] = 10
thomas_marcus.respect[thomas] = 20
thomas_marcus.resentment[thomas] = 80
thomas_marcus.familiarity[thomas] = 90


arthur.update_goals(world)
thomas.update_goals(world)

print()
print("ARTHUR'S GOALS")

for goal in arthur.goals:
    print(goal)

print()
print("THOMAS'S GOALS")

for goal in thomas.goals:
    print(goal)
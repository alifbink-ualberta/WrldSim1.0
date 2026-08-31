from simulation.person import Person
from simulation.reproduction import reproduce


father = Person(
    "Robert",
    "Stirling",
    42,
    "male"
)

mother = Person(
    "Elena",
    "Stirling",
    39,
    "female"
)


william = reproduce(
    father,
    mother,
    "William",
    "Stirling"
)

anne = reproduce(
    father,
    mother,
    "Anne",
    "Stirling"
)

henry = reproduce(
    father,
    mother,
    "Henry",
    "Stirling"
)


print("\nFAMILY")

print(
    father.full_name,
    "children:",
    [
        child.full_name
        for child in father.family.children
    ]
)

print(
    william.full_name,
    "siblings:",
    [
        sibling.full_name
        for sibling in william.family.get_siblings()
    ]
)

print(
    anne.full_name,
    "siblings:",
    [
        sibling.full_name
        for sibling in anne.family.get_siblings()
    ]
)

print(
    henry.full_name,
    "siblings:",
    [
        sibling.full_name
        for sibling in henry.family.get_siblings()
    ]
)
import random

from simulation.person import Person
from simulation.genetics import Genetics


def reproduce(
    parent_a,
    parent_b,
    first_name,
    last_name
):

    # ==================================================
    # GENETICS
    # ==================================================

    genetics = Genetics.inherit(
        parent_a.genetics,
        parent_b.genetics
    )

    # ==================================================
    # SEX
    # ==================================================

    sex = random.choice([
        "male",
        "female"
    ])

    # ==================================================
    # CHILD
    # ==================================================

    child = Person(
        first_name=first_name,
        last_name=last_name,
        age=0,
        sex=sex,
        genetics=genetics
    )

    # ==================================================
    # FAMILY
    # ==================================================

    child.family.add_parent(parent_a)
    child.family.add_parent(parent_b)

    # ==================================================
    # RELATIONSHIPS
    # ==================================================

    relationship_a = parent_a.get_relationship(child)
    relationship_b = parent_b.get_relationship(child)

    relationship_a.connections.add("parent")
    relationship_b.connections.add("parent")

    child_relationship_a = child.get_relationship(parent_a)
    child_relationship_b = child.get_relationship(parent_b)

    child_relationship_a.connections.add("child")
    child_relationship_b.connections.add("child")

    # ==================================================
    # SIBLING RELATIONSHIPS
    # ==================================================

    for sibling in child.family.get_siblings():

        relationship = child.get_relationship(
            sibling
        )

        relationship.connections.add(
            "sibling"
        )

        sibling_relationship = sibling.get_relationship(
            child
        )

        sibling_relationship.connections.add(
            "sibling"
        )

    # ==================================================
    # BIRTH MEMORIES
    # ==================================================

    parent_a.remember({
        "type": "birth",
        "person": child,
        "description": f"{child.full_name} was born."
    })

    parent_b.remember({
        "type": "birth",
        "person": child,
        "description": f"{child.full_name} was born."
    })

    child.remember({
        "type": "birth",
        "parents": [parent_a, parent_b],
        "description": (
            f"{child.full_name} was born "
            f"to {parent_a.full_name} and "
            f"{parent_b.full_name}."
        )
    })

    return child
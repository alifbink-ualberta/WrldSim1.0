def update_needs(person):

    # Hunger increases every day
    person.hunger += 5

    # Energy decreases throughout the day
    person.energy -= 10

    # Keep values within bounds
    person.hunger = min(person.hunger, 100)
    person.energy = max(person.energy, 0)
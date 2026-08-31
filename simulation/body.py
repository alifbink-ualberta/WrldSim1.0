# simulation/body.py


class Body:

    def __init__(self, genetics):

        self.height = genetics.traits["height"]
        self.strength = genetics.traits["strength"]
        self.agility = genetics.traits["agility"]
        self.stamina = genetics.traits["stamina"]
        self.constitution = genetics.traits["constitution"]
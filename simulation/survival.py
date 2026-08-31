# simulation/survival.py


class SurvivalState:

    def __init__(self):

        self.hunger = 0.0
        self.thirst = 0.0
        self.energy = 1.0
        self.sleep = 1.0

        self.health = 1.0
        self.injuries = []
        self.illnesses = []
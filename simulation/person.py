# simulation/person.py

from simulation.genetics import Genetics
from simulation.personality import Personality
from simulation.body import Body
from simulation.survival import SurvivalState
from simulation.family import Family
from simulation.emotion import EmotionalState


class Person:

    def __init__(
        self,
        first_name,
        last_name,
        age,
        sex,
        genetics=None,
        personality=None,
        body=None,
        money=0
    ):

        # ==========================================
        # IDENTITY
        # ==========================================

        self.first_name = first_name
        self.last_name = last_name

        self.age = age
        self.sex = sex
        self.is_alive = True

        self.family = Family(self)

        # ==========================================
        # BIOLOGY
        # ==========================================

        self.genetics = (
            genetics
            if genetics is not None
            else Genetics()
        )

        self.body = (
            body
            if body is not None
            else Body(self.genetics)
        )

        # ==========================================
        # PERSONALITY
        # ==========================================

        self.personality = (
            personality
            if personality is not None
            else Personality()
        )

        self.emotions = EmotionalState()

        # ==========================================
        # MIND
        # ==========================================

        self.memories = []
        self.beliefs = []
        self.motivations = []
        self.goals = []

        # ==========================================
        # DEVELOPMENT
        # ==========================================

        self.skills = {}
        self.knowledge = {}

        self.experiences = []

        self.development_stage = (
            "adult"
            if age >= 18
            else "child"
        )

        # ==========================================
        # SOCIAL
        # ==========================================

        self.relationships = {}

        # ==========================================
        # PERSONAL CIRCUMSTANCES
        # ==========================================

        self.circumstances = []

        # ==========================================
        # SURVIVAL
        # ==========================================

        self.survival = SurvivalState()

        # ==========================================
        # ECONOMY
        # ==========================================

        self.money = money
        self.inventory = {}

        # ==========================================
        # WORLD
        # ==========================================

        self.location = None

        # ==========================================
        # CURRENT ACTIVITY
        # ==========================================

        self.current_activity = None

    # ==============================================
    # IDENTITY
    # ==============================================

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"

    # Backward compatibility for older systems.

    @property
    def name(self):

        return self.full_name

    # ==============================================
    # MEMORY
    # ==============================================

    def remember(
        self,
        experience,
        emotional_significance=None
    ):

        from simulation.memory import Memory

        if emotional_significance is None:

            emotional_significance = (
                experience.intensity
            )

        memory = Memory(
            person=self,
            experience=experience,
            emotional_significance=(
                emotional_significance
            )
        )

        self.memories.append(memory)

        return memory

    # ==============================================
    # DEVELOPMENT
    # ==============================================

    def add_experience(
        self,
        experience
    ):

        self.experiences.append(
            experience
        )

        from systems.development import (
            DevelopmentSystem
        )

        DevelopmentSystem.process_experience(
            self,
            experience
        )

    def gain_skill_experience(
        self,
        skill_name,
        amount
    ):

        from systems.development import (
            DevelopmentSystem
        )

        return DevelopmentSystem.gain_skill_experience(
            self,
            skill_name,
            amount
        )

    def get_skill(
        self,
        skill_name
    ):

        from systems.development import (
            DevelopmentSystem
        )

        return DevelopmentSystem.get_skill(
            self,
            skill_name
        )

    def update_development_stage(self):

        if self.age < 5:
            self.development_stage = "infant"

        elif self.age < 13:
            self.development_stage = "child"

        elif self.age < 18:
            self.development_stage = "adolescent"

        else:
            self.development_stage = "adult"

    # ==============================================
    # RELATIONSHIPS
    # ==============================================

    def get_relationship(self, other):

        from simulation.relationship import Relationship

        if other == self:
            return None

        if other not in self.relationships:

            relationship = Relationship(
                self,
                other
            )

            self.relationships[other] = relationship
            other.relationships[self] = relationship

        return self.relationships[other]

    # ==============================================
    # SOCIAL INTERACTION
    # ==============================================

    def interact_with(
        self,
        other,
        interaction_type,
        world,
        intensity=0.5
    ):

        from systems.social_interaction import (
            SocialInteractionSystem
        )

        return SocialInteractionSystem.perform(
            self,
            other,
            interaction_type,
            world,
            intensity
        )

    # ==============================================
    # PERCEPTION
    # ==============================================

    def perceive_event(self, event):

        from systems.perception import (
            PerceptionSystem
        )

        return PerceptionSystem.perceive(
            self,
            event
        )

    # ==================================================
    # PSYCHOLOGICAL RESPONSE
    # ==================================================

    def respond_to_interpretation(
        self,
        interpretation
    ):

        from systems.psychological_response import (
            PsychologicalResponseSystem
        )

        response = (
            PsychologicalResponseSystem.process(
                self,
                interpretation
            )
        )

        from systems.motivation_dynamics import (
            MotivationDynamicsSystem
        )

        MotivationDynamicsSystem.process(
            self,
            interpretation.event,
            interpretation,
            response
        )

        return response

    # ==============================================
    # GOALS
    # ==============================================

    def update_goals(self, world):

        from systems.goal_generation import (
            GoalGenerationSystem
        )

        self.goals = GoalGenerationSystem.generate(
            self,
            world
        )

        return self.goals

    # ==============================================
    # INVENTORY
    # ==============================================

    def add_item(
        self,
        item,
        amount=1
    ):

        self.inventory[item] = (
            self.inventory.get(item, 0)
            + amount
        )

    def remove_item(
        self,
        item,
        amount=1
    ):

        if self.inventory.get(item, 0) < amount:
            return False

        self.inventory[item] -= amount

        if self.inventory[item] <= 0:
            del self.inventory[item]

        return True

    def has_item(
        self,
        item,
        amount=1
    ):

        return (
            self.inventory.get(item, 0)
            >= amount
        )

    # ==============================================
    # ECONOMY
    # ==============================================

    def earn_money(self, amount):

        self.money += amount

    def spend_money(self, amount):

        if self.money < amount:
            return False

        self.money -= amount

        return True

    # ==============================================
    # DEBUGGING
    # ==============================================

    def __str__(self):

        return (
            f"{self.full_name}, "
            f"age {self.age}, "
            f"sex {self.sex}"
        )
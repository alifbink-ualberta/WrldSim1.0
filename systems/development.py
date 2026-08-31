# systems/development.py

from simulation.skill import Skill


class DevelopmentSystem:

    @staticmethod
    def get_skill(person, skill_name):

        if skill_name not in person.skills:

            person.skills[skill_name] = Skill(
                skill_name
            )

        return person.skills[skill_name]

    @staticmethod
    def gain_skill_experience(
        person,
        skill_name,
        amount
    ):

        skill = (
            DevelopmentSystem.get_skill(
                person,
                skill_name
            )
        )

        skill.add_experience(
            amount
        )

        return skill

    @staticmethod
    def practice(
        person,
        skill_name,
        minutes,
        effectiveness=1.0
    ):

        # Diminishing returns will eventually
        # be handled here.
        #
        # For now:
        # 60 minutes = 1 XP

        experience = (
            minutes / 60
        ) * effectiveness

        return (
            DevelopmentSystem
            .gain_skill_experience(
                person,
                skill_name,
                experience
            )
        )

    @staticmethod
    def decay_skill(
        person,
        skill_name,
        amount
    ):

        if skill_name not in person.skills:
            return None

        skill = person.skills[
            skill_name
        ]

        skill.experience = max(
            0.0,
            skill.experience - amount
        )

        return skill



    @staticmethod
    def process_experience(
        person,
        experience
    ):

        """
        Converts an experience into developmental effects.

        This is the bridge between:

            LIFE EVENTS

        and:

            THE PERSON THEY BECOME
        """

        category = experience.category

        intensity = experience.intensity

        # ==========================================
        # WORK
        # ==========================================

        if category == "work":

            skill_name = experience.source

            if skill_name is not None:

                DevelopmentSystem.gain_skill_experience(
                    person,
                    skill_name,
                    intensity * 5
                )

        # ==========================================
        # EDUCATION
        # ==========================================

        elif category == "education":

            subject = experience.source

            if subject is not None:

                person.knowledge[subject] = (
                    person.knowledge.get(
                        subject,
                        0.0
                    )
                    + intensity
                )

        # ==========================================
        # GENERAL EXPERIENCE
        # ==========================================

        elif category == "social":

            # Social experiences currently have
            # no direct developmental effect.

            pass
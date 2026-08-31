# systems/social_interaction.py

from simulation.interaction import Interaction
from simulation.experience import Experience


class SocialInteractionSystem:

    # ==================================================
    # PERFORM INTERACTION
    # ==================================================

    @staticmethod
    def perform(
        initiator,
        target,
        interaction_type,
        world,
        intensity=0.5
    ):

        relationship = (
            initiator.get_relationship(
                target
            )
        )

        description = (
            SocialInteractionSystem
            .generate_description(
                initiator,
                target,
                interaction_type
            )
        )

        interaction = Interaction(
            initiator=initiator,
            target=target,
            interaction_type=interaction_type,
            description=description,
            intensity=intensity
        )

        # ==========================================
        # RELATIONSHIP EFFECT
        # ==========================================

        SocialInteractionSystem.update_relationship(
            relationship,
            initiator,
            target,
            interaction_type,
            intensity
        )

        # ==========================================
        # EXPERIENCE
        # ==========================================

        initiator.add_experience(
            Experience(
                category="social",
                description=description,
                intensity=intensity,
                source=interaction_type
            )
        )

        target.add_experience(
            Experience(
                category="social",
                description=description,
                intensity=intensity,
                source=interaction_type
            )
        )

        # ==========================================
        # SHARED HISTORY
        # ==========================================

        relationship.add_history(
            interaction
        )

        return interaction

    # ==================================================
    # RELATIONSHIP EFFECTS
    # ==================================================

    @staticmethod
    def update_relationship(
        relationship,
        initiator,
        target,
        interaction_type,
        intensity
    ):

        # ------------------------------------------
        # FRIENDLY
        # ------------------------------------------

        if interaction_type == "friendly":

            relationship.affection[
                initiator
            ] += 0.03 * intensity

            relationship.affection[
                target
            ] += 0.03 * intensity

            relationship.trust[
                initiator
            ] += 0.01 * intensity

            relationship.trust[
                target
            ] += 0.01 * intensity

        # ------------------------------------------
        # CONVERSATION
        # ------------------------------------------

        elif interaction_type == "conversation":

            relationship.familiarity[
                initiator
            ] += 0.02 * intensity

            relationship.familiarity[
                target
            ] += 0.02 * intensity

        # ------------------------------------------
        # INSULT
        # ------------------------------------------

        elif interaction_type == "insult":

            relationship.resentment[
                target
            ] += 0.08 * intensity

            relationship.affection[
                target
            ] -= 0.05 * intensity

            relationship.respect[
                target
            ] -= 0.03 * intensity

        # ------------------------------------------
        # HELP
        # ------------------------------------------

        elif interaction_type == "help":

            relationship.trust[
                target
            ] += 0.05 * intensity

            relationship.affection[
                target
            ] += 0.03 * intensity

            relationship.respect[
                target
            ] += 0.02 * intensity

        # ------------------------------------------
        # THREAT
        # ------------------------------------------

        elif interaction_type == "threat":

            relationship.fear[
                target
            ] += 0.08 * intensity

            relationship.trust[
                target
            ] -= 0.05 * intensity

            relationship.resentment[
                target
            ] += 0.03 * intensity

        # ------------------------------------------
        # CONFLICT
        # ------------------------------------------

        elif interaction_type == "conflict":

            relationship.resentment[
                initiator
            ] += 0.04 * intensity

            relationship.resentment[
                target
            ] += 0.04 * intensity

            relationship.affection[
                initiator
            ] -= 0.02 * intensity

            relationship.affection[
                target
            ] -= 0.02 * intensity

    # ==================================================
    # DESCRIPTION
    # ==================================================

    @staticmethod
    def generate_description(
        initiator,
        target,
        interaction_type
    ):

        if interaction_type == "friendly":

            return (
                f"{initiator.full_name} spent "
                f"time being friendly with "
                f"{target.full_name}."
            )

        if interaction_type == "conversation":

            return (
                f"{initiator.full_name} had a "
                f"conversation with "
                f"{target.full_name}."
            )

        if interaction_type == "insult":

            return (
                f"{initiator.full_name} insulted "
                f"{target.full_name}."
            )

        if interaction_type == "help":

            return (
                f"{initiator.full_name} helped "
                f"{target.full_name}."
            )

        if interaction_type == "threat":

            return (
                f"{initiator.full_name} threatened "
                f"{target.full_name}."
            )

        if interaction_type == "conflict":

            return (
                f"{initiator.full_name} got into "
                f"a conflict with "
                f"{target.full_name}."
            )

        return (
            f"{initiator.full_name} interacted "
            f"with {target.full_name}."
        )
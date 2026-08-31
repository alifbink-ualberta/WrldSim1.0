# systems/perception.py


class PerceptionSystem:

    @staticmethod
    def perceive(
        person,
        event
    ):

        # ==========================================
        # BASIC VISIBILITY
        # ==========================================

        clarity = 1.0

        # ==========================================
        # DISTANCE
        # ==========================================

        # Later this will use actual world
        # locations and distances.

        if hasattr(event, "distance"):

            distance = event.distance

            if distance > 100:
                clarity *= 0.3

            elif distance > 50:
                clarity *= 0.6

            elif distance > 20:
                clarity *= 0.8

        # ==========================================
        # EVENT VISIBILITY
        # ==========================================

        if hasattr(event, "visibility"):

            clarity *= event.visibility

        # ==========================================
        # ATTENTION
        # ==========================================

        # Later this can depend on:
        #
        # personality
        # current activity
        # fatigue
        # emotional state
        # relationship
        # familiarity
        # importance
        #
        # For now everyone gets full attention.

        attention = 1.0

        clarity *= attention

        # ==========================================
        # DETERMINE WHETHER EVENT WAS NOTICED
        # ==========================================

        noticed = clarity > 0.1

        source = None

        if hasattr(event, "actor"):

            source = event.actor

        return {
            "observer": person,
            "event": event,
            "noticed": noticed,
            "clarity": clarity,
            "source": source
        }
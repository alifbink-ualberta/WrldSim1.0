# systems/consequence_system.py


class ConsequenceSystem:

    @staticmethod
    def apply(event, world):

        consequences = []

        # ==========================================
        # DEATH
        # ==========================================

        if event.event_type == "death":

            for person in event.participants:

                if not person.is_alive:
                    continue

                # ----------------------------------
                # CHANGE WORLD STATE
                # ----------------------------------

                person.is_alive = False

                consequences.append(
                    f"{person.full_name} has died."
                )

        # ==========================================
        # RESOLVE EVENT
        # ==========================================

        event.resolve()

        return consequences
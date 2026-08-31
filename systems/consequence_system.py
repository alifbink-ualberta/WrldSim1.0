# systems/consequence_system.py


class ConsequenceSystem:

    @staticmethod
    def apply(event, world):

        consequences = []

        # ==========================================
        # PROCESS EVENT
        # ==========================================

        if event.name == "Father's Death":

            for person in event.participants:

                # ----------------------------------
                # MEMORY
                # ----------------------------------

                person.remember(
                    event,
                    emotional_significance=1.0
                )

                consequences.append(
                    f"{person.full_name} remembers "
                    f"the death of their father."
                )

        # ==========================================
        # RESOLVE EVENT
        # ==========================================

        event.resolve()

        return consequences
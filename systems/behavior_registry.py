class BehaviorRegistry:

    def __init__(self):

        self.behaviors = []

    # ==========================================
    # REGISTRATION
    # ==========================================

    def register(self, behavior):

        self.behaviors.append(behavior)

    def register_many(self, behaviors):

        for behavior in behaviors:
            self.register(behavior)

    # ==========================================
    # GENERATION
    # ==========================================

    def generate_actions(self, person, world):

        actions = []

        for behavior in self.behaviors:

            if not behavior.is_available(
                person,
                world
            ):
                continue

            action = behavior.create_action(
                person,
                world
            )

            if action is not None:
                actions.append(action)

        return actions
class Behavior:

    name = "Unnamed Behavior"

    def get_actions(self, person, world):
        """
        Return a list of possible Actions.

        A behavior may return zero, one, or many actions.
        """

        return []

    def can_perform(self, person, action, world):
        """
        Determines whether this behavior can resolve
        the given action.
        """

        return True

    def resolve(self, person, action, world):
        """
        Resolves the action.

        Must return an ActionResult.
        """

        raise NotImplementedError(
            "Behavior subclasses must implement resolve()."
        )
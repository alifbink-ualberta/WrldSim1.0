class Opportunity:

    def __init__(
        self,
        actor,
        action_type,
        target=None,
        item=None,
        amount=1,
        price=0,
        reason=None
    ):

        self.actor = actor
        self.action_type = action_type
        self.target = target
        self.item = item
        self.amount = amount
        self.price = price
        self.reason = reason

    def __str__(self):

        target = ""

        if self.target:
            target = f" → {self.target.name}"

        item = ""

        if self.item:
            item = (
                f" ({self.amount} "
                f"{self.item})"
            )

        return (
            f"{self.actor.name}: "
            f"{self.action_type}"
            f"{target}"
            f"{item}"
        )
class World:

    def __init__(
        self,
        decision_system=None,
        behavior_registry=None,
        action_resolver=None
    ):

        # =====================================
        # TIME
        # =====================================

        self.year = 1
        self.month = 1
        self.day = 1
        self.hour = 0
        self.minute = 0

        # =====================================
        # WORLD ENTITIES
        # =====================================

        self.people = []
        self.events = []
        self.locations = {}

        # =====================================
        # SYSTEMS
        # =====================================

        from systems.decision_making import (
            DecisionSystem
        )

        from systems.behaviors import (
            create_default_registry
        )

        from systems.action_resolver import (
            ActionResolver
        )

        self.decision_system = (
            decision_system
            or DecisionSystem()
        )

        self.behavior_registry = (
            behavior_registry
            or create_default_registry()
        )

        self.action_resolver = (
            action_resolver
            or ActionResolver()
        )

    # =====================================
    # PEOPLE
    # =====================================

    def add_person(self, person):

        self.people.append(person)

    # =====================================
    # LOCATIONS
    # =====================================

    def add_location(self, location):

        self.locations[
            location.name
        ] = location

    def move_person(
        self,
        person,
        location_name
    ):

        if location_name not in self.locations:
            return

        for location in self.locations.values():

            location.leave(person)

        location = self.locations[
            location_name
        ]

        location.enter(person)

    # =====================================
    # TIME
    # =====================================

    def advance_minute(self):

        self.minute += 1

        if self.minute >= 60:

            self.minute = 0
            self.hour += 1

        if self.hour >= 24:

            self.hour = 0
            self.day += 1

            self.daily_update()

        if self.day > 30:

            self.day = 1
            self.month += 1

            self.monthly_update()

        if self.month > 12:

            self.month = 1
            self.year += 1

            self.yearly_update()

    # =====================================
    # SIMULATION
    # =====================================

    def simulate_minute(self):

        from systems.needs import update_needs

        from simulation.activity import (
            Activity
        )

        for person in self.people:

            # =================================
            # NEEDS
            # =================================

            update_needs(
                person,
                1
            )

            # =================================
            # CURRENT ACTIVITY
            # =================================

            if person.current_activity is not None:

                activity = (
                    person.current_activity
                )

                activity.advance(1)

                if activity.is_finished():

                    self.finish_activity(
                        person
                    )

                continue

            # =================================
            # DECISION
            # =================================

            action, score = (
                self.decision_system.choose_action(
                    person,
                    self,
                    self.behavior_registry
                )
            )

            if action is None:
                continue

            # =================================
            # START ACTIVITY
            # =================================

            from systems.actions import (
                get_action_duration
            )

            duration = (
                get_action_duration(
                    action.action_type
                )
            )

            person.current_activity = (
                Activity(
                    action=action,
                    remaining_minutes=duration
                )
            )

            # =================================
            # LOG
            # =================================

            print(
                f"[Y{self.year} "
                f"M{self.month} "
                f"D{self.day} "
                f"{self.hour:02d}:"
                f"{self.minute:02d}] "
                f"{person.name} begins "
                f"{action.action_type} "
                f"(score={score:.1f}, "
                f"duration={duration}m)"
            )

    # =====================================
    # ACTIVITY COMPLETION
    # =====================================

    def finish_activity(self, person):

        activity = (
            person.current_activity
        )

        action = activity.action

        outcome = (
            self.action_resolver.resolve(
                action,
                self
            )
        )

        # =================================
        # APPLY RESULT
        # =================================

        if outcome.success:

            result = person.perform_action(
                action,
                self
            )

            print(
                f"    → {result}"
            )

        else:

            print(
                f"    → {outcome.description}"
            )

        print(
            f"       Success chance: "
            f"{outcome.probability:.1f}%"
        )

        person.current_activity = None

    # =====================================
    # DAILY
    # =====================================

    def daily_update(self):

        pass

    # =====================================
    # MONTHLY
    # =====================================

    def monthly_update(self):

        print(
            f"\n=== MONTH "
            f"{self.month}, "
            f"YEAR {self.year} ===\n"
        )

    # =====================================
    # YEARLY
    # =====================================

    def yearly_update(self):

        print(
            f"\n######## YEAR "
            f"{self.year} ########\n"
        )

        for person in self.people:

            person.age += 1

    # =====================================
    # RUN
    # =====================================

    def run_minutes(self, minutes):

        for _ in range(minutes):

            self.simulate_minute()

            self.advance_minute()

    def run_hours(self, hours):

        self.run_minutes(
            hours * 60
        )

    def run_days(self, days):

        self.run_minutes(
            days * 24 * 60
        )

    def run_years(self, years):

        self.run_minutes(
            years * 365 * 24 * 60
        )
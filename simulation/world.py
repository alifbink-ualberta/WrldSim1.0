# simulation/world.py

from simulation.activity import Activity

from systems.behavior_registry import BehaviorRegistry
from systems.decision_making import choose_action
from systems.action_resolver import ActionResolver
from systems.actions import get_action_duration
from systems.needs import update_needs


class World:

    def __init__(self):

        # ==========================================
        # TIME
        # ==========================================

        self.year = 1
        self.month = 1
        self.day = 1

        self.hour = 0
        self.minute = 0

        self.current_time_minutes = 0

        # ==========================================
        # ENTITIES
        # ==========================================

        self.people = []
        self.events = []
        self.locations = {}

        # ==========================================
        # CIRCUMSTANCES
        # ==========================================

        self.circumstances = []

        # ==========================================
        # SIMULATION SYSTEMS
        # ==========================================

        self.behavior_registry = (
            BehaviorRegistry()
        )

        self.action_resolver = (
            ActionResolver()
        )

        # ==========================================
        # STATE
        # ==========================================

        self.running = True

    # ==============================================
    # PEOPLE
    # ==============================================

    def add_person(self, person):

        if person not in self.people:

            self.people.append(person)

    # ==============================================
    # LOCATIONS
    # ==============================================

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
            return False

        for location in self.locations.values():

            location.leave(person)

        location = self.locations[
            location_name
        ]

        location.enter(person)

        person.location = location

        return True

    # ==============================================
    # TIME
    # ==============================================

    def advance_minute(self):

        self.minute += 1

        self.current_time_minutes += 1

        # ------------------------------------------
        # HOUR
        # ------------------------------------------

        if self.minute >= 60:

            self.minute = 0
            self.hour += 1

        # ------------------------------------------
        # DAY
        # ------------------------------------------

        if self.hour >= 24:

            self.hour = 0
            self.day += 1

            self.daily_update()

        # ------------------------------------------
        # MONTH
        # ------------------------------------------

        if self.day > 30:

            self.day = 1
            self.month += 1

            self.monthly_update()

        # ------------------------------------------
        # YEAR
        # ------------------------------------------

        if self.month > 12:

            self.month = 1
            self.year += 1

            self.yearly_update()

    # ==============================================
    # TIME DISPLAY
    # ==============================================

    def timestamp(self):

        return (
            f"[Y{self.year} "
            f"M{self.month} "
            f"D{self.day} "
            f"{self.hour:02d}:"
            f"{self.minute:02d}]"
        )

    # ==============================================
    # START ACTIVITY
    # ==============================================

    def start_activity(
        self,
        person,
        action,
        score
    ):

        duration = get_action_duration(
            action.action_type
        )

        person.current_activity = Activity(
            action=action,
            remaining_minutes=duration
        )

        target_text = ""

        if action.target is not None:

            target_text = (
                f" with {action.target.full_name}"
            )

        print(
            f"{self.timestamp()} "
            f"{person.full_name} begins "
            f"{action.action_type}"
            f"{target_text} "
            f"(score={score:.2f}, "
            f"duration={duration}m)"
        )

    # ==============================================
    # CHOOSE ACTION
    # ==============================================

    def choose_action(self, person):

        return choose_action(
            person,
            self
        )

    # ==============================================
    # UPDATE ACTIVITY
    # ==============================================

    def update_activity(self, person):

        activity = person.current_activity

        if activity is None:
            return

        activity.advance(1)

        if activity.is_finished():

            self.finish_activity(person)

    # ==============================================
    # FINISH ACTIVITY
    # ==============================================

    def finish_activity(self, person):

        activity = person.current_activity

        if activity is None:
            return

        action = activity.action

        outcome, result, message = (
            self.action_resolver.resolve(
                person,
                action,
                self
            )
        )

        print(
            f"{self.timestamp()} "
            f"    → {message}"
        )

        if outcome is not None:

            print(
                f"       Success chance: "
                f"{outcome.chance:.1f}%"
            )

        person.current_activity = None

    # ==============================================
    # SIMULATE ONE MINUTE
    # ==============================================

    def simulate_minute(self):

        if not self.running:
            return

        # ==========================================
        # NEEDS
        # ==========================================

        for person in self.people:

            if not person.is_alive:
                continue

            update_needs(
                person,
                minutes=1
            )

        # ==========================================
        # PEOPLE
        # ==========================================

        for person in self.people:

            if not person.is_alive:
                continue

            # --------------------------------------
            # EXISTING ACTIVITY
            # --------------------------------------

            if person.current_activity is not None:

                self.update_activity(
                    person
                )

                continue

            # --------------------------------------
            # GOALS
            # --------------------------------------

            if not person.goals:

                person.update_goals(
                    self
                )

            # --------------------------------------
            # DECISION
            # --------------------------------------

            action, score = (
                self.choose_action(person)
            )

            if action is None:
                continue

            # --------------------------------------
            # START
            # --------------------------------------

            self.start_activity(
                person,
                action,
                score
            )

        # ==========================================
        # CLOCK
        # ==========================================

        self.advance_minute()

    # ==============================================
    # DAILY UPDATE
    # ==============================================

    def daily_update(self):

        # Reconsider goals every day.

        for person in self.people:

            if not person.is_alive:
                continue

            person.update_goals(
                self
            )

            person.update_development_stage()

    # ==============================================
    # MONTHLY UPDATE
    # ==============================================

    def monthly_update(self):

        print(
            f"\n=== MONTH "
            f"{self.month}, "
            f"YEAR {self.year} ===\n"
        )

    # ==============================================
    # YEARLY UPDATE
    # ==============================================

    def yearly_update(self):

        print(
            f"\n######## YEAR "
            f"{self.year} "
            f"########\n"
        )

        for person in self.people:

            if not person.is_alive:
                continue

            person.age += 1

            person.update_development_stage()

    # ==============================================
    # RUN MINUTES
    # ==============================================

    def run_minutes(self, minutes):

        for _ in range(minutes):

            if not self.running:
                break

            self.simulate_minute()

    # ==============================================
    # RUN HOURS
    # ==============================================

    def run_hours(self, hours):

        self.run_minutes(
            hours * 60
        )

    # ==============================================
    # RUN DAYS
    # ==============================================

    def run_days(self, days):

        self.run_minutes(
            days * 24 * 60
        )

    # ==============================================
    # RUN YEARS
    # ==============================================

    def run_years(self, years):

        self.run_minutes(
            years * 365 * 24 * 60
        )

    # ==============================================
    # CONTROL
    # ==============================================

    def stop(self):

        self.running = False

    def start(self):

        self.running = True
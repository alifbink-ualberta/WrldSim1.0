class World:

    def __init__(self):

        # =========================
        # TIME
        # =========================

        self.year = 1
        self.month = 1
        self.day = 1
        self.hour = 0

        # =========================
        # WORLD ENTITIES
        # =========================

        self.people = []
        self.events = []
        self.locations = {}

    # =============================
    # PEOPLE
    # =============================

    def add_person(self, person):

        self.people.append(person)

    # =============================
    # LOCATIONS
    # =============================

    def add_location(self, location):

        self.locations[location.name] = location

    def move_person(self, person, location_name):

        if location_name not in self.locations:
            return

        # Remove from previous location
        for location in self.locations.values():

            location.leave(person)

        # Enter new location
        location = self.locations[location_name]

        location.enter(person)

    # =============================
    # TIME
    # =============================

    def advance_hour(self):

        self.hour += 1

        if self.hour >= 24:

            self.hour = 0
            self.day += 1

            self.daily_update()

        # 30-day months for now
        if self.day > 30:

            self.day = 1
            self.month += 1

            self.monthly_update()

        if self.month > 12:

            self.month = 1
            self.year += 1

            self.yearly_update()

    # =============================
    # HOURLY SIMULATION
    # =============================

    def simulate_hour(self):

        from systems.needs import update_needs
        from systems.decision_making import choose_action
        from simulation.activity import Activity
        from systems.actions import get_action_duration

        for person in self.people:

            # -----------------------------
            # UPDATE NEEDS
            # -----------------------------

            update_needs(person)

            # -----------------------------
            # CONTINUE CURRENT ACTIVITY
            # -----------------------------

            if person.current_activity is not None:

                activity = person.current_activity

                print(
                    f"[Y{self.year} "
                    f"M{self.month} "
                    f"D{self.day} "
                    f"{self.hour:02d}:00] "
                    f"{person.name} continues "
                    f"{activity.action_type}."
                )

                activity.advance_hour()

                # Activity finished
                if activity.is_finished():

                    print(
                        f"    → {person.name} "
                        f"finished "
                        f"{activity.action_type}."
                    )

                    person.current_activity = None

                continue

            # -----------------------------
            # MAKE A NEW DECISION
            # -----------------------------

            action, score = choose_action(
                person,
                self
            )

            if action is None:
                continue

            duration = get_action_duration(
                action.action_type
            )

            person.current_activity = Activity(
                action=action,
                remaining_hours=duration
            )

            # Execute the initial effects
            result = person.perform_action(
                action,
                self
            )

            print(
                f"[Y{self.year} "
                f"M{self.month} "
                f"D{self.day} "
                f"{self.hour:02d}:00] "
                f"{result} "
                f"(score={score:.1f}, "
                f"duration={duration}h)"
            )

        self.advance_hour()

    # =============================
    # DAILY UPDATE
    # =============================

    def daily_update(self):

        pass

    # =============================
    # MONTHLY UPDATE
    # =============================

    def monthly_update(self):

        print(
            f"\n=== MONTH {self.month}, "
            f"YEAR {self.year} ===\n"
        )

    # =============================
    # YEARLY UPDATE
    # =============================

    def yearly_update(self):

        print(
            f"\n######## YEAR "
            f"{self.year} ########\n"
        )

        for person in self.people:

            person.age += 1

    # =============================
    # RUN SIMULATION
    # =============================

    def run_hours(self, hours):

        for _ in range(hours):

            self.simulate_hour()

    def run_days(self, days):

        self.run_hours(
            days * 24
        )

    def run_years(self, years):

        self.run_hours(
            years * 365 * 24
        )
# simulation/family.py


class Family:

    def __init__(self, person):

        self.person = person

        # ==========================================
        # IMMEDIATE FAMILY
        # ==========================================

        self.parents = []

        self.children = []

        self.siblings = []

    # ==============================================
    # PARENTS
    # ==============================================

    def set_parents(
        self,
        parent_a,
        parent_b
    ):

        self.parents = []

        if parent_a is not None:
            self.parents.append(
                parent_a
            )

        if parent_b is not None:
            self.parents.append(
                parent_b
            )

        self.update_siblings()

    # ==============================================
    # CHILDREN
    # ==============================================

    def add_child(
        self,
        child
    ):

        if child not in self.children:

            self.children.append(
                child
            )

        # Every existing child of this parent
        # becomes a sibling of the new child.

        for existing_child in self.children:

            if existing_child == child:
                continue

            if existing_child not in child.family.siblings:

                child.family.siblings.append(
                    existing_child
                )

            if child not in existing_child.family.siblings:

                existing_child.family.siblings.append(
                    child
                )

    # ==============================================
    # SIBLINGS
    # ==============================================

    def update_siblings(self):

        for parent in self.parents:

            for sibling in parent.family.children:

                if sibling == self.person:
                    continue

                if sibling not in self.siblings:

                    self.siblings.append(
                        sibling
                    )

                if self.person not in sibling.family.siblings:

                    sibling.family.siblings.append(
                        self.person
                    )

    # ==============================================
    # RELATIONSHIPS
    # ==============================================

    def is_parent_of(
        self,
        person
    ):

        return person in self.children

    def is_child_of(
        self,
        person
    ):

        return person in self.parents

    def is_sibling_of(
        self,
        person
    ):

        return person in self.siblings
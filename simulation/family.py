class Family:

    def __init__(self, person):

        self.person = person

        # Biological parents
        self.parents = []

        # Children
        self.children = []

    # ==================================================
    # PARENTS
    # ==================================================

    def add_parent(self, parent):

        if parent not in self.parents:

            self.parents.append(parent)

            if self.person not in parent.family.children:
                parent.family.children.append(self.person)

    # ==================================================
    # CHILDREN
    # ==================================================

    def add_child(self, child):

        if child not in self.children:

            self.children.append(child)

            if self.person not in child.family.parents:
                child.family.parents.append(self.person)

    # ==================================================
    # SIBLINGS
    # ==================================================

    def get_siblings(self):

        siblings = set()

        for parent in self.parents:

            for child in parent.family.children:

                if child != self.person:
                    siblings.add(child)

        return list(siblings)
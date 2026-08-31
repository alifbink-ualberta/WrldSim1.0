# simulation/family.py


class Family:

    def __init__(self, person):

        self.person = person

        # ==========================================
        # PARENTS
        # ==========================================

        self.parents = []

        # ==========================================
        # CHILDREN
        # ==========================================

        self.children = []

        # ==========================================
        # PARTNERS
        # ==========================================

        self.partners = []

    # ==============================================
    # PARENTS
    # ==============================================

    def add_parent(self, parent):

        if parent is self.person:
            return

        if parent not in self.parents:

            self.parents.append(parent)

        if self.person not in parent.family.children:

            parent.family.children.append(
                self.person
            )

    # ==============================================
    # CHILDREN
    # ==============================================

    def add_child(self, child):

        if child is self.person:
            return

        if child not in self.children:

            self.children.append(child)

        if self.person not in child.family.parents:

            child.family.parents.append(
                self.person
            )

    # ==============================================
    # PARTNERS
    # ==============================================

    def add_partner(self, partner):

        if partner is self.person:
            return

        if partner not in self.partners:

            self.partners.append(partner)

        if self.person not in partner.family.partners:

            partner.family.partners.append(
                self.person
            )

    # ==============================================
    # SIBLINGS
    # ==============================================

    def get_siblings(self):

        siblings = []

        for parent in self.parents:

            for child in parent.family.children:

                if (
                    child is not self.person
                    and child not in siblings
                ):

                    siblings.append(child)

        return siblings

    # ==============================================
    # FAMILY MEMBERS
    # ==============================================

    def get_family_members(self):

        members = []

        for parent in self.parents:

            if parent not in members:
                members.append(parent)

        for child in self.children:

            if child not in members:
                members.append(child)

        for partner in self.partners:

            if partner not in members:
                members.append(partner)

        for sibling in self.get_siblings():

            if sibling not in members:
                members.append(sibling)

        return members
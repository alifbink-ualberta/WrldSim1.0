class Consideration:

    name = "Unnamed Consideration"

    def score(self, person, action, world):

        return 0


class NeedConsideration(Consideration):

    name = "Needs"

    def score(self, person, action, world):

        score = 0

        if action.action_type == "eat":

            score += person.hunger ** 1.7

        elif action.action_type == "sleep":

            fatigue = 100 - person.energy

            score += fatigue ** 1.7

        return score


class GoalConsideration(Consideration):

    name = "Goals"

    def score(self, person, action, world):

        score = 0

        for goal in person.goals:

            goal = goal.lower()

            if (
                "financial" in goal
                or "secure" in goal
            ):

                if action.action_type == "work":
                    score += 25

                elif action.action_type == "sell":
                    score += 20

            if "wealth" in goal:

                if action.action_type == "work":
                    score += 25

                elif action.action_type == "sell":
                    score += 30

            if (
                "respect" in goal
                or "reputation" in goal
            ):

                if action.action_type == "work":
                    score += 15

                elif action.action_type == "socialize":
                    score += 20

            if (
                "learn" in goal
                or "knowledge" in goal
                or "scholar" in goal
            ):

                if action.action_type == "practice":
                    score += 30

                elif action.action_type == "explore":
                    score += 25

            if "master" in goal:

                if action.action_type == "practice":
                    score += 35

                elif action.action_type == "work":
                    score += 20

            if "family" in goal:

                if action.action_type == "socialize":
                    score += 15

                elif action.action_type == "work":
                    score += 15

        return score


class PersonalityConsideration(Consideration):

    name = "Personality"

    def score(self, person, action, world):

        score = 0

        if action.action_type == "work":

            score += (
                person.conscientiousness * 0.5
            )

            score += (
                person.machiavellianism * 0.1
            )

        elif action.action_type == "practice":

            score += (
                person.conscientiousness * 0.4
            )

            score += (
                person.openness * 0.4
            )

        elif action.action_type == "socialize":

            score += (
                person.extraversion * 0.7
            )

            score += (
                person.agreeableness * 0.2
            )

        elif action.action_type == "explore":

            score += (
                person.openness * 0.7
            )

            score += (
                person.extraversion * 0.2
            )

            score -= (
                person.neuroticism * 0.3
            )

        return score

class CircumstanceConsideration(Consideration):

    name = "Circumstances"

    def score(self, person, action, world):

        score = 0

        if action.action_type == "eat":

            if (
                person.has_item("food")
                or person.has_item("meat")
            ):

                score += 20

            else:

                score -= 100

        elif action.action_type == "work":

            if person.energy < 20:

                score -= 80

        elif action.action_type == "sleep":

            if person.energy < 40:

                score += 30

        return score
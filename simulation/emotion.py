# simulation/emotion.py


class EmotionalState:

    def __init__(self):

        # All values are 0.0 - 1.0

        self.happiness = 0.0
        self.sadness = 0.0
        self.anger = 0.0
        self.fear = 0.0
        self.disgust = 0.0
        self.surprise = 0.0

        # More persistent psychological states.

        self.grief = 0.0
        self.shame = 0.0
        self.guilt = 0.0
        self.loneliness = 0.0
        self.pride = 0.0
        self.contentment = 0.0

    # ==================================================
    # SET
    # ==================================================

    def set(self, emotion, value):

        if not hasattr(self, emotion):
            return

        setattr(
            self,
            emotion,
            max(0.0, min(1.0, value))
        )

    # ==================================================
    # CHANGE
    # ==================================================

    def change(self, emotion, amount):

        if not hasattr(self, emotion):
            return

        current = getattr(
            self,
            emotion
        )

        self.set(
            emotion,
            current + amount
        )

    # ==================================================
    # GET
    # ==================================================

    def get(self, emotion):

        return getattr(
            self,
            emotion,
            0.0
        )

    # ==================================================
    # DECAY
    # ==================================================

    def decay(self, minutes=1):

        # Emotional states gradually return toward
        # baseline rather than disappearing instantly.

        rate = 0.001 * minutes

        persistent_rate = 0.0003 * minutes

        temporary = [
            "happiness",
            "sadness",
            "anger",
            "fear",
            "disgust",
            "surprise",
            "shame",
            "guilt",
            "pride",
            "contentment"
        ]

        persistent = [
            "grief",
            "loneliness"
        ]

        for emotion in temporary:

            value = self.get(emotion)

            if value > 0:
                self.set(
                    emotion,
                    value - rate
                )

        for emotion in persistent:

            value = self.get(emotion)

            if value > 0:
                self.set(
                    emotion,
                    value - persistent_rate
                )

    # ==================================================
    # DOMINANT EMOTION
    # ==================================================

    def dominant_emotion(self):

        emotions = {
            "happiness": self.happiness,
            "sadness": self.sadness,
            "anger": self.anger,
            "fear": self.fear,
            "disgust": self.disgust,
            "surprise": self.surprise,
            "grief": self.grief,
            "shame": self.shame,
            "guilt": self.guilt,
            "loneliness": self.loneliness,
            "pride": self.pride,
            "contentment": self.contentment
        }

        return max(
            emotions,
            key=emotions.get
        )

    # ==================================================
    # OVERALL DISTRESS
    # ==================================================

    def distress(self):

        return min(
            1.0,
            (
                self.sadness
                + self.anger
                + self.fear
                + self.grief
                + self.shame
                + self.loneliness
            ) / 6
        )

    # ==================================================
    # DEBUGGING
    # ==================================================

    def summary(self):

        return {
            "happiness": round(self.happiness, 2),
            "sadness": round(self.sadness, 2),
            "anger": round(self.anger, 2),
            "fear": round(self.fear, 2),
            "grief": round(self.grief, 2),
            "shame": round(self.shame, 2),
            "guilt": round(self.guilt, 2),
            "loneliness": round(self.loneliness, 2),
            "pride": round(self.pride, 2),
            "contentment": round(
                self.contentment,
                2
            )
        }
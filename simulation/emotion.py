# simulation/emotion.py


class EmotionalState:

    def __init__(self):

        # =========================
        # PRIMARY EMOTIONS
        # =========================

        self.joy = 0.0
        self.sadness = 0.0
        self.anger = 0.0
        self.fear = 0.0
        self.disgust = 0.0
        self.surprise = 0.0

        # =========================
        # SOCIAL / SELF-CONSCIOUS
        # =========================

        self.love = 0.0
        self.shame = 0.0
        self.guilt = 0.0
        self.pride = 0.0
        self.envy = 0.0
        self.embarrassment = 0.0

    # =========================
    # CHANGE EMOTION
    # =========================

    def change(self, emotion, amount):

        if not hasattr(self, emotion):
            return

        current = getattr(
            self,
            emotion
        )

        value = current + amount

        value = max(
            0.0,
            min(1.0, value)
        )

        setattr(
            self,
            emotion,
            value
        )

    # =========================
    # DECAY
    # =========================

    def decay(self, amount=0.05):

        for emotion in vars(self):

            value = getattr(
                self,
                emotion
            )

            value = max(
                0.0,
                value - amount
            )

            setattr(
                self,
                emotion,
                value
            )

    # =========================
    # STRONGEST EMOTION
    # =========================

    def strongest(self):

        emotions = {
            name: value
            for name, value
            in vars(self).items()
        }

        if not emotions:
            return None

        return max(
            emotions,
            key=emotions.get
        )
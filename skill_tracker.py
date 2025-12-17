class SkillTracker:
    def __init__(self):
        self.history = []

    def update(self, features):
        self.history.append(features)

    def mastery_score(self):
        if not self.history:
            return 0.0
        return max(0, 1 - (self.history[-1]["complexity"] / 20))

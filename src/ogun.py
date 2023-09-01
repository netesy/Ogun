class Ogun:
    def __init__(self):
        self.user_id = None
        self.data = None
        self.weights = {}

    def user(self, user_id):
        self.user_id = user_id
        return self

    def data(self, array_data):
        self.data = array_data
        return self

    def score(self, category, weight):
        self.weights[category] = weight
        return self

    def get(self):
        total_score = 0
        for category, weight in self.weights.items():
            if category in self.data:
                total_score += self.data[category] * weight
        return RiskResult(total_score)


class RiskResult:
    def __init__(self, total_score):
        self.total_score = total_score

    @property
    def rating(self):
        if self.total_score <= 30:
            return "Low Risk"
        elif self.total_score <= 60:
            return "Moderate Risk"
        else:
            return "High Risk"

    @property
    def status(self):
        return "Approved" if self.rating == "Low Risk" else "Denied"
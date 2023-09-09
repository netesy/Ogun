from .engine import Engine


class Default(Engine):
    def calculate(self):
        total_score = 0
        for category, weight in self.weights.items():
            if category in self.data:
                total_score += self.data[category] * weight
        return total_score

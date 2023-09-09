from .engine import Engine


# Conditional Value at Risk (CVaR)
class CVaR(Engine):
    def calculate(self):
        confidence_level = 0.95
        data_points = list(self.data.values())
        var = self.calculate_risk(method="var")
        cvar_data = [
            data * weight
            for data, weight in zip(data_points, self.weights.values())
            if data < var
        ]
        return (1 / (1 - confidence_level)) * sum(cvar_data)

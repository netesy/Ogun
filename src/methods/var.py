from .engine import Engine


# Value at Risk (VaR) risk calculation method
class VaR(Engine):
    def calculate(self):
        confidence_level = 0.95
        data_points = list(self.data.values())
        portfolio_value = sum(
            [data * weight for data, weight in zip(data_points, self.weights.values())]
        )
        sorted_returns = sorted(data_points)
        var_index = int((1 - confidence_level) * len(data_points))
        return sorted_returns[var_index] * portfolio_value

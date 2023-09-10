from .engine import Engine
import statistics


class SharpeRatio(Engine):
    def calculate(self):
        portfolio_returns = list(self.data.values())
        risk_free_rate = 0.03
        excess_returns = [r - risk_free_rate for r in portfolio_returns]
        sharpe_ratio = statistics.mean(excess_returns) / statistics.stdev(
            excess_returns
        )
        return sharpe_ratio

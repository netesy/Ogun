from .engine import Engine  # Import the `Engine` class from a relative module
import statistics  # Import the `statistics` module for statistical calculations


# Define a class called `SharpeRatio` that inherits from the `Engine` class
class SharpeRatio(Engine):
    def calculate(self) -> float:
        """
        Calculate the Sharpe Ratio for a portfolio.

        Returns:
        - float: The calculated Sharpe Ratio.
        """
        # None safety checks
        if data is None:
            raise ValueError("Data cannot be None.")
        if weights is None:
            raise ValueError("Weights cannot be None.")
        portfolio_returns = list(
            self.data.values()
        )  # Extract portfolio returns from the data

        risk_free_rate = 0.03  # Define the risk-free rate

        # Calculate excess returns by subtracting the risk-free rate from portfolio returns
        excess_returns = [r - risk_free_rate for r in portfolio_returns]

        # Calculate the Sharpe Ratio as the mean of excess returns divided by the standard deviation of excess returns
        sharpe_ratio = statistics.mean(excess_returns) / statistics.stdev(
            excess_returns
        )

        return sharpe_ratio  # Return the calculated Sharpe Ratio

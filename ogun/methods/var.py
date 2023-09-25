from .engine import Engine  # Import the `Engine` class from a relative module


# Define a class called `VaR` that inherits from the `Engine` class
class VaR(Engine):
    def calculate(self) -> float:
        """
        Calculate the Value at Risk (VaR) as a risk measurement.

        Returns:
        - float: The calculated VaR.
        """
        confidence_level = 0.95  # Define the confidence level for VaR calculation
        data_points = list(
            self.data.values()
        )  # Extract data points from the data dictionary

        # Calculate the portfolio value by summing weighted data points
        portfolio_value = sum(
            [data * weight for data, weight in zip(data_points, self.weights.values())]
        )

        # Sort the data points in ascending order
        sorted_returns = sorted(data_points)

        # Calculate the index corresponding to the VaR at the specified confidence level
        var_index = int((1 - confidence_level) * len(data_points))

        # Calculate VaR as the data point at the computed index multiplied by the portfolio value
        var = sorted_returns[var_index] * portfolio_value

        return var  # Return the calculated VaR

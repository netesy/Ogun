from .engine import Engine  # Import the `Engine` class from a relative module


# Define a class called `CVaR` that inherits from the `Engine` class
class CVaR(Engine):
    def calculate(self) -> float:
        """
        Calculate Conditional Value at Risk (CVaR) using a specified confidence level.

        Returns:
        - float: The calculated CVaR.
        """
        confidence_level = 0.95  # Define the confidence level for CVaR calculation
        data_points = list(
            self.data.values()
        )  # Extract data points from the data dictionary

        # Calculate Value at Risk (VaR) using the 'var' method
        var = self.calculate_risk(method="var")

        # Calculate CVaR data points by filtering data points below VaR
        cvar_data = [
            data * weight
            for data, weight in zip(data_points, self.weights.values())
            if data < var
        ]

        # Calculate CVaR using the formula
        cvar = (1 / (1 - confidence_level)) * sum(cvar_data)

        return cvar

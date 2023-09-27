from .engine import Engine  # Import the `Engine` class from a relative module
import statistics  # Import the `statistics` module for statistical calculations


# Define a class called `StandardDeviation` that inherits from the `Engine` class
class StandardDeviation(Engine):
    def calculate(self) -> float:
        """
        Calculate the standard deviation as a risk measurement.

        Returns:
        - float: The calculated standard deviation.
        """
        # None safety checks
        if data is None:
            raise ValueError("Data cannot be None.")
        if weights is None:
            raise ValueError("Weights cannot be None.")
        data_points = list(
            self.data.values()
        )  # Assuming self.data is a Dict[str, float] containing data points

        # Calculate the standard deviation of the data points using the statistics module
        return statistics.stdev(data_points)

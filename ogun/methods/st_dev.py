from .engine import Engine
import statistics


# Standard Deviation risk calculation method
class StandardDeviation(Engine):
    def calculate(self) -> float:
        data_points = list(
            self.data.values()
        )  # Assuming self.data is a Dict[str, float]
        return statistics.stdev(data_points)

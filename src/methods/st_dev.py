from .engine import Engine
import statistics


# Standard Deviation risk calculation method
class StandardDeviation(Engine):
    def calculate(self):
        data_points = list(self.data.values())
        return statistics.stdev(data_points)

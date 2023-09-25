from typing import Any, Type, Optional
from ogun.methods.st_dev import StandardDeviation


# Define a class called Ogun
class Ogun:
    def __init__(self) -> None:
        """
        Constructor for the Ogun class.

        Initializes instance variables:
        - data: Holds the data used for risk calculation (initialized as None)
        - method: Holds the risk calculation method (initialized as None)
        - weights: Holds a dictionary of category weights
        - risk_method: Holds the default risk calculation method (StandardDeviation)
        """
        self.data = None
        self.method = None
        self.weights = {}
        self.risk_method = StandardDeviation

    def set_data(self, data: Any) -> "Ogun":
        """
        Set the data for risk calculation.

        Args:
        - data (Any): The data to be used for risk calculation.

        Returns:
        - self (Ogun): Returns the Ogun instance for method chaining.
        """
        self.data = data
        return self

    def using(self, risk_method: Optional[Type[StandardDeviation]] = None) -> "Ogun":
        """
        Set the risk calculation method.

        Args:
        - risk_method (Optional[Type[StandardDeviation]]): The risk calculation method to use.
          If None, it raises a ValueError.

        Returns:
        - self (Ogun): Returns the Ogun instance for method chaining.
        """
        if risk_method:
            self.risk_method = risk_method
        else:
            raise ValueError(
                "Please specify a risk calculation method using the 'using' method."
            )
        return self

    def score(self, category: str, weight: float) -> "Ogun":
        """
        Assign a weight to a risk category.

        Args:
        - category (str): The risk category.
        - weight (float): The weight assigned to the category.

        Returns:
        - self (Ogun): Returns the Ogun instance for method chaining.
        """
        self.weights[category] = weight
        return self

    def get(self) -> "RiskResult":
        """
        Get the risk result using the specified risk calculation method and weights.

        Returns:
        - RiskResult: Returns a RiskResult instance containing the total risk score.
        """
        if self.risk_method is None:
            raise ValueError(
                "Please specify a risk calculation method using the 'using' method."
            )
        try:
            risk_calculator = self.risk_method(self.data, self.weights)
            return RiskResult(risk_calculator.calculate())
        except Exception as e:
            raise RuntimeError(f"An error occurred during risk calculation: {str(e)}")


# Define a class called RiskResult
class RiskResult:
    def __init__(self, total_score: float) -> None:
        """
        Constructor for the RiskResult class.

        Initializes an instance variable:
        - total_score: Holds the total risk score.

        Args:
        - total_score (float): The total risk score.
        """
        self.total_score = total_score

    @property
    def rating(self) -> str:
        """
        Calculate and return a risk rating based on the total score.

        Returns:
        - str: The risk rating (Low Risk, Moderate Risk, or High Risk).
        """
        if self.total_score <= 30:
            return "Low Risk"
        elif self.total_score <= 60:
            return "Moderate Risk"
        else:
            return "High Risk"

    @property
    def status(self) -> str:
        """
        Determine the status based on the risk rating.

        Returns:
        - str: The status (Approved or Denied).
        """
        return "Approved" if self.rating == "Low Risk" else "Denied"

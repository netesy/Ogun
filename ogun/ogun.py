from typing import Any, Type, Optional
from ogun.methods.st_dev import StandardDeviation


class Ogun:
    def __init__(self) -> None:
        self.data = None
        self.method = None
        self.weights = {}
        self.risk_method = StandardDeviation

    def set_data(self, data: Any) -> "Ogun":
        self.data = data
        return self

    def using(self, risk_method: Optional[Type[StandardDeviation]] = None) -> "Ogun":
        if risk_method:
            self.risk_method = risk_method
        else:
            raise ValueError(
                "Please specify a risk calculation method using the 'using' method."
            )
        return self

    def score(self, category: str, weight: float) -> "Ogun":
        self.weights[category] = weight
        return self

    def get(self) -> "RiskResult":
        if self.risk_method is None:
            raise ValueError(
                "Please specify a risk calculation method using the 'using' method."
            )
        try:
            risk_calculator = self.risk_method(self.data, self.weights)
            return RiskResult(risk_calculator.calculate())
        except Exception as e:
            raise RuntimeError(f"An error occurred during risk calculation: {str(e)}")


class RiskResult:
    def __init__(self, total_score: float) -> None:
        self.total_score = total_score

    @property
    def rating(self) -> str:
        if self.total_score <= 30:
            return "Low Risk"
        elif self.total_score <= 60:
            return "Moderate Risk"
        else:
            return "High Risk"

    @property
    def status(self) -> str:
        return "Approved" if self.rating == "Low Risk" else "Denied"

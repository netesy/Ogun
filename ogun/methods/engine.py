from typing import Any, Dict


class Engine:
    def __init__(self, data: Any, weights: Dict[str, float]) -> None:
        self.data = data
        self.weights = weights

    def calculate(self) -> Any:
        # Common logic for recommendation methods
        pass

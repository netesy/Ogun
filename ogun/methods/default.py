from .engine import Engine  # Import the `Engine` class from a relative module


# Define a class called `Default` that inherits from the `Engine` class
class Default(Engine):
    def calculate(self) -> float:
        """
        Calculate the total score using the default recommendation method.

        Returns:
        - float: The total score calculated using the default method.
        """
        # None safety checks
        if data is None:
            raise ValueError("Data cannot be None.")
        if weights is None:
            raise ValueError("Weights cannot be None.")
        total_score = 0

        # Iterate through category-weight pairs in the weights dictionary
        for category, weight in self.weights.items():
            # Check if the category is present in the data
            if category in self.data:
                # Add the product of category data and weight to the total score
                total_score += self.data[category] * weight

        return total_score

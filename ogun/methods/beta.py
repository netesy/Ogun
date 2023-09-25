from .engine import Engine  # Import the `Engine` class from a relative module
import statistics  # Import the `statistics` module for statistical calculations


# Define a class called `Beta` that inherits from the `Engine` class
class Beta(Engine):
    def calculate(self) -> float:
        """
        Calculate the beta of a portfolio.

        Returns:
        - float: The calculated beta.
        """
        # Extract portfolio returns from the data dictionary
        portfolio_returns = list(self.data.values())

        # Replace this list with your actual benchmark data
        benchmark_returns = [0.05, 0.07, 0.03]

        # Calculate the covariance matrix between portfolio and benchmark returns
        covariance_matrix = self.calculate_covariance_matrix(
            portfolio_returns, benchmark_returns
        )

        # Extract specific elements from the covariance matrix
        portfolio_variance = covariance_matrix[0][0]
        portfolio_benchmark_covariance = covariance_matrix[0][1]
        benchmark_variance = covariance_matrix[1][1]

        # Calculate beta as the ratio of portfolio-benchmark covariance to benchmark variance
        beta = portfolio_benchmark_covariance / benchmark_variance

        return beta

    def calculate_covariance_matrix(self, portfolio_returns, benchmark_returns):
        """
        Calculate the covariance matrix between portfolio and benchmark returns.

        Args:
        - portfolio_returns (list): List of portfolio returns.
        - benchmark_returns (list): List of benchmark returns.

        Returns:
        - list of lists: A 2x2 matrix representing the covariance matrix.
        """
        # Calculate the mean (average) of portfolio and benchmark returns
        portfolio_mean = statistics.mean(portfolio_returns)
        benchmark_mean = statistics.mean(benchmark_returns)

        # Initialize a variable to accumulate the covariance sum
        cov_sum = 0

        # Iterate over the returns and calculate the covariance
        for i in range(len(portfolio_returns)):
            cov_sum += (portfolio_returns[i] - portfolio_mean) * (
                benchmark_returns[i] - benchmark_mean
            )

        # Calculate portfolio and benchmark variances
        portfolio_variance = statistics.variance(portfolio_returns)
        benchmark_variance = statistics.variance(benchmark_returns)

        # Calculate the covariance and create a 2x2 covariance matrix
        covariance = cov_sum / (len(portfolio_returns) - 1)
        return [[portfolio_variance, covariance], [covariance, benchmark_variance]]

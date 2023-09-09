from .engine import Engine
import statistics


class Beta(Engine):
    def calculate(self):
        portfolio_returns = list(self.data.values())
        benchmark_returns = [0.05, 0.07, 0.03]  # Replace with your benchmark data
        covariance_matrix = self.calculate_covariance_matrix(
            portfolio_returns, benchmark_returns
        )
        portfolio_variance = covariance_matrix[0][0]
        portfolio_benchmark_covariance = covariance_matrix[0][1]
        benchmark_variance = covariance_matrix[1][1]
        beta = portfolio_benchmark_covariance / benchmark_variance
        return beta

    def calculate_covariance_matrix(self, portfolio_returns, benchmark_returns):
        portfolio_mean = statistics.mean(portfolio_returns)
        benchmark_mean = statistics.mean(benchmark_returns)
        cov_sum = 0
        for i in range(len(portfolio_returns)):
            cov_sum += (portfolio_returns[i] - portfolio_mean) * (
                benchmark_returns[i] - benchmark_mean
            )
        portfolio_variance = statistics.variance(portfolio_returns)
        benchmark_variance = statistics.variance(benchmark_returns)
        covariance = cov_sum / (len(portfolio_returns) - 1)
        return [[portfolio_variance, covariance], [covariance, benchmark_variance]]

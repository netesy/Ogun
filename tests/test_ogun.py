import unittest
from ogun import Ogun, RiskResult


class TestOgun(unittest.TestCase):
    def test_risk_calculation(self):
        # Create an instance of the Ogun class
        ogun_instance = (
            Ogun()
            .set_user(user_id="123")
            .set_data(
                array_data={
                    "account_balance": 10,
                    "account_age": 5,
                    "work_status": 4,
                    "Salary": 10,
                }
            )
            .score(category="account_balance", weight=10)
            .score(category="account_age", weight=20)
            .score(category="work_status", weight=10)
            .score(category="Salary", weight=10)
        )

        # Get the risk result
        risk = ogun_instance.get()

        # Verify the result using assertions
        self.assertIsInstance(risk, RiskResult)
        self.assertIn(risk.rating, ["Low Risk", "Moderate Risk", "High Risk"])
        self.assertIn(risk.status, ["Approved", "Denied"])


if __name__ == "__main__":
    unittest.main()

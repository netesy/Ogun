from ogun import Ogun

risk = (
    Ogun()
    .user(user_id="123")
    .data(array_data={
        "account_balance": 10,
        "account_age": 5,
        "work_status": 4,
        "Salary": 10,
    })
    .score(category="account_balance", weight=10)
    .score(category="account_age", weight=5)
    .score(category="work_status", weight=4)
    .score(category="Salary", weight=10)
    .get()
)

print("Risk Rating:", risk.rating)
print("Status:", risk.status)
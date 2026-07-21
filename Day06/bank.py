from account_factory import AccountFactory

from observers import SMSAlert
from observers import AuditLog
from bank_config import BankConfig


print("=" * 60)
print("BANK MANAGEMENT SYSTEM")
print("=" * 60)

config = BankConfig()

print("Interest Rate :", config.interest_rate)
print("Overdraft :", config.overdraft_limit)

print()

acc1 = AccountFactory.create(
    "savings",
    "Surafel",
    "ACC001",
    5000
)

acc2 = AccountFactory.create(
    "current",
    "Abebe",
    "ACC002",
    3000
)

sms = SMSAlert()
log = AuditLog()

acc1.subscribe(sms)
acc1.subscribe(log)

acc2.subscribe(sms)
acc2.subscribe(log)

print("\nSavings Account")

acc1.deposit(1000)

acc1.withdraw(2000)

print()

print("Interest Earned")

print(acc1.calculate_interest())

print()

print("Current Account")

acc2.deposit(2000)

acc2.withdraw(5500)
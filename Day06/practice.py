from bank_config import BankConfig

from account_factory import AccountFactory
from observers import SMSAlert, AuditLog

print("=" * 60)
print("Singleton Demo")
print("=" * 60)

config1 = BankConfig()
config2 = BankConfig()

print(config1 is config2)

print()

print("=" * 60)
print("Factory Demo")
print("=" * 60)

acc = AccountFactory.create(
    "savings",
    "Almaz",
    "CBE001",
    4000
)

print(type(acc))

print()

print("=" * 60)
print("Observer Demo")
print("=" * 60)

sms = SMSAlert()
audit = AuditLog()

acc.subscribe(sms)
acc.subscribe(audit)

acc.deposit(1000)

acc.withdraw(500)

print()

print("Balance")

print(acc.balance)
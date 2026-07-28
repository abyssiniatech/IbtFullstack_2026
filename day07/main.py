from account_factory import AccountFactory
from observers import SMSAlert, AuditLog
from bank_config import BankConfig
from account_registry import AccountRegistry
from transfer import Transfer
from transfer_queue import TransferQueue


print("=" * 60)
print("BANK MANAGEMENT SYSTEM - DAY 07")
print("=" * 60)


# -------------------------------------------------
# Singleton Configuration
# -------------------------------------------------

config = BankConfig()

print("\nBank Configuration")

print(
    "Interest Rate:",
    config.interest_rate
)

print(
    "Overdraft Limit:",
    config.overdraft_limit
)


# -------------------------------------------------
# Create Accounts Using Factory Pattern
# -------------------------------------------------

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


# -------------------------------------------------
# Observer Pattern
# -------------------------------------------------

sms = SMSAlert()

audit = AuditLog()


acc1.subscribe(sms)
acc1.subscribe(audit)

acc2.subscribe(sms)
acc2.subscribe(audit)


# -------------------------------------------------
# Account Registry (Dictionary)
# -------------------------------------------------

registry = AccountRegistry()


registry.add(acc1)

registry.add(acc2)


registry.show_all()


# -------------------------------------------------
# Deposit and Withdraw
# -------------------------------------------------

print("\n===== Account Transactions =====")


acc1.deposit(1000)

acc1.withdraw(2000)


acc2.deposit(2000)

acc2.withdraw(3500)



# -------------------------------------------------
# Search Account O(1)
# -------------------------------------------------

print("\n===== Account Search =====")


found = registry.find("ACC001")


if found:

    print(
        "Found:",
        found.owner
    )

    print(
        "Balance:",
        found.balance
    )



# -------------------------------------------------
# Stack: Transaction History
# -------------------------------------------------

print("\n===== Transaction History =====")


acc1.show_history()



# -------------------------------------------------
# Stack: Undo Last Transaction
# -------------------------------------------------

print("\n===== Undo Transaction =====")


acc1.undo_last_transaction()


acc1.show_history()



# -------------------------------------------------
# Queue: Pending Transfers
# -------------------------------------------------

print("\n===== Transfer Queue =====")


transfer_queue = TransferQueue()


transfer1 = Transfer(
    acc1,
    acc2,
    500
)


transfer2 = Transfer(
    acc2,
    acc1,
    300
)


transfer_queue.enqueue(
    transfer1
)


transfer_queue.enqueue(
    transfer2
)



transfer_queue.show_pending()



# -------------------------------------------------
# Process Queue
# -------------------------------------------------

print("\n===== Processing Transfers =====")


transfer_queue.process()

transfer_queue.process()



# -------------------------------------------------
# Final Result
# -------------------------------------------------

print("\n===== Final Balances =====")


print(
    acc1.owner,
    ":",
    acc1.balance,
    "ETB"
)


print(
    acc2.owner,
    ":",
    acc2.balance,
    "ETB"
)


print("\nBANK SYSTEM FINISHED")
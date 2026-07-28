from account_factory import AccountFactory
from account_registry import AccountRegistry



print("="*60)

print("DAY 08 BANK SEARCH AND SORT SYSTEM")

print("="*60)



# Create registry

registry = AccountRegistry()



# Create accounts

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
    8000
)



acc3 = AccountFactory.create(
    "savings",
    "Marta",
    "ACC003",
    12000
)



acc4 = AccountFactory.create(
    "current",
    "Dawit",
    "ACC004",
    3000
)



# Add accounts

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)
registry.add(acc4)



# -----------------------------------
# Leaderboard
# -----------------------------------

print("\n===== TOP BALANCES =====")


top = registry.top_by_balance(3)



for account in top:

    print(
        account.owner,
        account.balance
    )



# -----------------------------------
# Binary Search
# -----------------------------------

print("\n===== BINARY SEARCH =====")


result = registry.find_by_number(
    "ACC003"
)



if result:

    print(
        "Found:",
        result.owner,
        result.balance
    )


else:

    print(
        "Account not found"
    )



# -----------------------------------
# Missing account
# -----------------------------------

missing = registry.find_by_number(
    "ACC999"
)


print(
    "Missing:",
    missing
)



# -----------------------------------
# Recursive transaction total
# -----------------------------------


print(
    "\n===== TRANSACTION TOTAL ====="
)


acc1.deposit(1000)

acc1.withdraw(500)



total = registry.total_transactions(
    "ACC001"
)


print(
    "Total transactions:",
    total
)
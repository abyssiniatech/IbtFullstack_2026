from account import Account


def main():

    # Create two accounts
    account1 = Account("Surafel Mengist", "ACC1001", 10000)
    account2 = Account("Almaz", "ACC1002", 5000)

    print("\nInitial Account Information")
    account1.statement()
    account2.statement()

    print("\nPerforming Transactions...\n")

    # Deposit
    account1.deposit(2500)

    # Withdraw
    account1.withdraw(1500)

    account2.deposit(1000)
    account2.withdraw(2000)

    print("\nUpdated Account Information")
    account1.statement()
    account2.statement()

    print("\nTesting Validation\n")

    try:
        account1.deposit(-500)
    except ValueError as error:
        print("Deposit Error:", error)

    try:
        account2.withdraw(100000)
    except ValueError as error:
        print("Withdrawal Error:", error)

    print("\nTesting Read-Only Property")

    print("Current Balance:", account1.balance)

    try:
        account1.balance = 999999
    except AttributeError as error:
        print("Property Error:", error)


if __name__ == "__main__":
    main()
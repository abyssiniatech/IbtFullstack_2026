class Account:
    """
    Addis Bank Account Management System (Version 2)
    Base Account Class
    """

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        """Read-only balance property."""
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount
        print(f"Deposit Successful: {amount:.2f} ETB")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        self.__balance -= amount
        print(f"Withdrawal Successful: {amount:.2f} ETB")

    def statement(self):
        """Display account information."""
        print("\n" + "=" * 40)
        print("        ADDIS BANK ACCOUNT")
        print("=" * 40)
        print(f"Owner           : {self.owner}")
        print(f"Account Number  : {self.account_number}")
        print(f"Current Balance : {self.__balance:.2f} ETB")
        print("=" * 40)


# ---------------------------------------------------
# Savings Account
# ---------------------------------------------------

class SavingsAccount(Account):
    """
    Savings Account inherits from Account.
    Adds interest functionality.
    """

    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        """Add interest to the account balance."""
        interest = self.balance * self.rate
        self.deposit(interest)
        print(f"Interest Added: {interest:.2f} ETB")


# ---------------------------------------------------
# Current Account
# ---------------------------------------------------

class CurrentAccount(Account):
    """
    Current Account inherits from Account.
    Allows overdraft.
    """

    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        """
        Override the withdraw() method.
        Allow withdrawal using overdraft.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded.")

        # Accessing the private variable using name mangling
        self._Account__balance -= amount

        print(f"Withdrawal Successful: {amount:.2f} ETB")
# Demonstration (Polymorphism)
# Create different account types

bank = [
    SavingsAccount("Almaz", "CBE-1001", 5000, 0.08),
    CurrentAccount("Dawit", "CBE-1002", 2000, 3000)
]

print("\n=== Initial Statements ===")

for account in bank:
    account.statement()

print("\n=== Deposit 500 ETB into Every Account ===")

for account in bank:
    account.deposit(500)

print("\n=== Add Interest to Savings Account ===")

bank[0].add_interest()

print("\n=== Withdraw from Current Account ===")

bank[1].withdraw(4500)

print("\n=== Final Statements ===")

for account in bank:
    account.statement()



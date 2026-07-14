class Account:
    """
    Addis Bank Account Management System (Version 1)
    """

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        """Read-only property for account balance."""
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount
        print(f"Deposit Successful: {amount} ETB")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        self.__balance -= amount
        print(f"Withdrawal Successful: {amount} ETB")

    def statement(self):
        """Display account information."""

        print("\n" + "=" * 40)
        print("      ADDIS BANK ACCOUNT")
        print("=" * 40)
        print(f"Owner           : {self.owner}")
        print(f"Account Number  : {self.account_number}")
        print(f"Current Balance : {self.__balance:.2f} ETB")
        print("=" * 40)
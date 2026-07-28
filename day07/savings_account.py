from account import Account
from bank_config import BankConfig


class SavingsAccount(Account):
    """
    Savings Account
    - No overdraft allowed.
    - Earns interest.
    """

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        self.interest_rate = BankConfig().interest_rate

    def withdraw(self, amount):
        """
        Withdraw money from the savings account.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        # Access the private balance from the parent class
        self._Account__balance -= amount

        # Save transaction to the stack
        self.history.append(
            f"Withdraw: {amount:.2f} ETB"
        )

        print(f"Withdrawal Successful: {amount:.2f} ETB")

        # Notify observers
        self._notify(
            f"{self.owner} withdrew {amount:.2f} ETB"
        )

    def calculate_interest(self):
        """
        Calculate the interest earned.
        """
        return self.balance * self.interest_rate

    def display_account(self):
        """
        Display account information.
        """
        print("\n===== Savings Account =====")
        print(f"Owner         : {self.owner}")
        print(f"Account No.   : {self.number}")
        print(f"Balance       : {self.balance:.2f} ETB")
        print(f"Interest Rate : {self.interest_rate * 100:.1f}%")
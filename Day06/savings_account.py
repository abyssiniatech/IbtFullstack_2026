from account import Account
from bank_config import BankConfig


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(owner, number, balance)

        self.interest_rate = BankConfig().interest_rate

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self._Account__balance -= amount

        print(f"Withdrawal Successful: {amount:.2f} ETB")

        self._notify(f"{self.owner} withdrew {amount:.2f} ETB")

    def calculate_interest(self):

        return self.balance * self.interest_rate
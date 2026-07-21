from bank_config import BankConfig
import account
from account import Account

class CurrentAccount(account.Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(owner, number, balance)

        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded.")

        self._Account__balance -= amount

        print(f"Withdrawal Successful: {amount:.2f} ETB")

        self._notify(f"{self.owner} withdrew {amount:.2f} ETB")
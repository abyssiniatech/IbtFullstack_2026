from account import Account
from bank_config import BankConfig


class CurrentAccount(Account):
    """
    Current Account

    Features:
    - Allows overdraft
    - Keeps transaction history
    - Sends observer notifications
    """

    def __init__(self, owner, number, balance=0):

        super().__init__(
            owner,
            number,
            balance
        )

        # Get overdraft limit from Singleton
        self.overdraft = BankConfig().overdraft_limit


    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )


        available_balance = (
            self.balance +
            self.overdraft
        )


        if amount > available_balance:

            raise ValueError(
                "Overdraft limit exceeded."
            )


        # Update private balance from parent class
        self._Account__balance -= amount


        # Add transaction to Stack
        self.history.append(
            f"Withdraw: {amount:.2f} ETB"
        )


        print(
            f"Withdrawal Successful: {amount:.2f} ETB"
        )


        # Notify observers
        self._notify(
            f"{self.owner} withdrew {amount:.2f} ETB"
        )


    def display_account(self):

        print("\n===== Current Account =====")

        print(
            "Owner:",
            self.owner
        )

        print(
            "Account Number:",
            self.number
        )

        print(
            "Balance:",
            self.balance,
            "ETB"
        )

        print(
            "Overdraft:",
            self.overdraft,
            "ETB"
        )
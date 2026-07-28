from account import Account
from bank_config import BankConfig


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(
            owner,
            number,
            balance
        )


        self.overdraft = (
            BankConfig()
            .overdraft_limit
        )


    def withdraw(self, amount):

        if amount <= 0:

            raise ValueError(
                "Amount must be positive"
            )


        if amount > (
            self.balance +
            self.overdraft
        ):

            raise ValueError(
                "Overdraft exceeded"
            )


        self._Account__balance -= amount


        self.history.append(
            f"Withdraw: {amount:.2f} ETB"
        )


        self._notify(
            f"{self.owner} withdrew {amount:.2f} ETB"
        )
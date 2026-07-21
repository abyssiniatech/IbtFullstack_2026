from current_account import CurrentAccount
from savings_account import SavingsAccount

class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        kind = kind.lower()

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        raise ValueError("Unknown account type.")
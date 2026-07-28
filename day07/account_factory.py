from savings_account import SavingsAccount
from current_account import CurrentAccount


class AccountFactory:
    """
    Factory Pattern
    Creates different types of bank accounts.
    """

    @staticmethod
    def create(kind, owner, number, balance=0):

        kind = kind.lower()

        if kind == "savings":

            return SavingsAccount(
                owner,
                number,
                balance
            )

        elif kind == "current":

            return CurrentAccount(
                owner,
                number,
                balance
            )

        else:

            raise ValueError(
                "Unknown account type. "
                "Use 'savings' or 'current'."
            )
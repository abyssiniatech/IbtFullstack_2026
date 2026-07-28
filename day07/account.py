from abc import ABC, abstractmethod


class Account(ABC):
    """
    Abstract base class for all bank accounts.
    """

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.__balance = balance

        # Observer pattern
        self._observers = []

        # Stack (list) for transaction history
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount

        # Push transaction onto stack
        self.history.append(f"Deposit: {amount:.2f} ETB")

        print(f"Deposit Successful: {amount:.2f} ETB")

        self._notify(
            f"{self.owner} deposited {amount:.2f} ETB"
        )

    @abstractmethod
    def withdraw(self, amount):
        """
        Withdraw money.
        Must be implemented by subclasses.
        """
        pass

    def subscribe(self, observer):
        """
        Register an observer.
        """
        self._observers.append(observer)

    def _notify(self, message):
        """
        Notify all observers.
        """
        for observer in self._observers:
            observer.update(message)

    def show_history(self):
        """
        Display transaction history.
        Newest transaction appears first.
        """
        print("\nTransaction History")

        if not self.history:
            print("No transactions.")
            return

        for transaction in reversed(self.history):
            print(transaction)

    def undo_last_transaction(self):
        """
        Remove the most recent transaction from history.
        (Demonstrates stack behavior.)
        """
        if not self.history:
            print("Nothing to undo.")
            return

        last = self.history.pop()
        print(f"Undo -> {last}")
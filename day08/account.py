from abc import ABC, abstractmethod


class Account(ABC):
    """
    Abstract Base Class

    Parent class for:
    - SavingsAccount
    - CurrentAccount

    Features:
    - Encapsulation
    - Observer Pattern
    - Transaction Stack
    """


    def __init__(self, owner, number, balance=0):

        self.owner = owner

        self.number = number


        # Private balance (Encapsulation)
        self.__balance = balance


        # Observer list
        self._observers = []


        # Stack for transaction history
        self.history = []



    @property
    def balance(self):

        return self.__balance



    def deposit(self, amount):
        """
        Deposit money.
        """


        if amount <= 0:

            raise ValueError(
                "Amount must be positive."
            )


        self.__balance += amount


        # Stack push
        self.history.append(
            f"Deposit: {amount:.2f} ETB"
        )


        print(
            f"Deposit Successful: {amount:.2f} ETB"
        )


        # Notify observers
        self._notify(
            f"{self.owner} deposited {amount:.2f} ETB"
        )



    @abstractmethod
    def withdraw(self, amount):
        """
        Child classes must implement.
        """

        pass



    def subscribe(self, observer):
        """
        Add observer.
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
        Display transactions.
        """

        print("\n===== Transaction History =====")


        if not self.history:

            print(
                "No transactions."
            )

            return



        for item in reversed(self.history):

            print(item)



    def undo_last_transaction(self):
        """
        Stack pop operation.
        """

        if not self.history:

            print(
                "Nothing to undo."
            )

            return



        last = self.history.pop()


        print(
            f"Undo -> {last}"
        )
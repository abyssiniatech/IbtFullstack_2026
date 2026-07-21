from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.__balance = balance

        self._observers = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount

        print(f"Deposit Successful: {amount:.2f} ETB")

        self._notify(f"{self.owner} deposited {amount:.2f} ETB")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):

        for observer in self._observers:
            observer.update(message)
class Transfer:
    """
    Represents a money transfer between two accounts.
    """

    def __init__(self, sender, receiver, amount):

        self.sender = sender
        self.receiver = receiver
        self.amount = amount


    def execute(self):
        """
        Execute the transfer.

        Steps:
        1. Withdraw from sender
        2. Deposit to receiver
        """

        if self.amount <= 0:
            raise ValueError(
                "Transfer amount must be positive."
            )


        # Remove money from sender
        self.sender.withdraw(
            self.amount
        )


        # Add money to receiver
        self.receiver.deposit(
            self.amount
        )


        print(
            f"""
Transfer Successful

From   : {self.sender.owner}
To     : {self.receiver.owner}
Amount : {self.amount:.2f} ETB
"""
        )


    def details(self):

        return (
            f"{self.sender.owner} -> "
            f"{self.receiver.owner} : "
            f"{self.amount:.2f} ETB"
        )
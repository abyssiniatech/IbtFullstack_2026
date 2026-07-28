class AccountRegistry:
    """
    Account Registry

    Uses dictionary for fast account lookup.

    Key:
        Account number

    Value:
        Account object

    Example:
        ACC001 -> SavingsAccount object
    """

    def __init__(self):

        # Dictionary:
        # account_number -> Account
        self.accounts = {}


    def add(self, account):
        """
        Add an account to the registry.
        """

        self.accounts[account.number] = account

        print(
            f"Account {account.number} registered successfully."
        )


    def find(self, number):
        """
        Find account by account number.

        Time Complexity:
            O(1)
        """

        return self.accounts.get(number)


    def remove(self, number):
        """
        Remove an account from registry.
        """

        if number in self.accounts:

            del self.accounts[number]

            print(
                f"Account {number} removed."
            )

        else:

            print(
                "Account not found."
            )


    def show_all(self):
        """
        Display all registered accounts.
        """

        print("\n===== Registered Accounts =====")

        if not self.accounts:

            print("No accounts registered.")
            return


        for number, account in self.accounts.items():

            print(
                f"""
Account Number : {number}
Owner          : {account.owner}
Balance        : {account.balance:.2f} ETB
------------------------------
"""
            )
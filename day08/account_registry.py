from binary_search import binary_search


class AccountRegistry:
    """
    Day 08 Account Registry

    New Features:
    - Balance leaderboard
    - Binary search account lookup
    - Recursive transaction total
    """

    def __init__(self):

        self.by_number = {}


    def add(self, account):
        """
        Add account.
        """

        self.by_number[account.number] = account

        print(
            f"{account.number} added successfully."
        )


    def find(self, number):
        """
        Normal dictionary lookup.

        Complexity:
        O(1)
        """

        return self.by_number.get(number)



    # -----------------------------------------
    # Day 08 Feature 1
    # Leaderboard
    # -----------------------------------------

    def top_by_balance(self, n=5):
        """
        Return highest balance accounts.

        Uses sorting.
        """

        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )


        return accounts[:n]



    # -----------------------------------------
    # Day 08 Feature 2
    # Binary Search
    # -----------------------------------------

    def find_by_number(self, number):
        """
        Search account number using binary search.
        """

        numbers = sorted(
            self.by_number.keys()
        )


        index = binary_search(
            numbers,
            number
        )


        if index >= 0:

            account_number = numbers[index]

            return self.by_number[account_number]


        return None



    # -----------------------------------------
    # Day 08 Feature 3
    # Recursive Transaction Total
    # -----------------------------------------

    def total_transactions(self, number):

        account = self.by_number.get(number)


        if account is None:

            return 0


        return self.calculate_total(
            account.history,
            0
        )



    def calculate_total(self, history, index):

        """
        Recursive helper function.

        Base case:
        when index reaches end.
        """

        if index == len(history):

            return 0



        transaction = history[index]


        amount = float(
            transaction.split(":")[1]
            .replace("ETB","")
        )


        return (
            amount +
            self.calculate_total(
                history,
                index + 1
            )
        )



    def show_all(self):

        print(
            "\n===== All Accounts ====="
        )


        for number, account in self.by_number.items():

            print(
                number,
                account.owner,
                account.balance
            )
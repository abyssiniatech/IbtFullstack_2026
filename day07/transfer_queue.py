from collections import deque


class TransferQueue:
    """
    Queue for pending bank transfers.

    Uses FIFO:
    First transfer added
    is the first transfer processed.
    """

    def __init__(self):

        # Queue storage
        self.queue = deque()


    def enqueue(self, transfer):
        """
        Add a transfer to the queue.

        Complexity:
            O(1)
        """

        self.queue.append(transfer)

        print(
            "Transfer added to queue:"
        )

        print(
            transfer.details()
        )


    def process(self):
        """
        Process the next transfer.

        Complexity:
            O(1)
        """

        if not self.queue:

            print(
                "No pending transfers."
            )

            return


        # Remove first transfer
        transfer = self.queue.popleft()


        # Execute transfer
        transfer.execute()


    def show_pending(self):
        """
        Display waiting transfers.
        """

        print(
            "\n===== Pending Transfers ====="
        )


        if not self.queue:

            print(
                "No pending transfers."
            )

            return


        for transfer in self.queue:

            print(
                transfer.details()
            )


    def size(self):
        """
        Return number of pending transfers.
        """

        return len(self.queue)
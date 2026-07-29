"""
File: payment_heap.py
Description: Priority Queue for bank payments implemented using a Min-Heap.
"""

import heapq


class PaymentQueue:
    """Priority queue where lower priority numbers are processed first."""

    def __init__(self):
        self._heap = []

    def push_payment(self, priority: int, name: str):
        """Pushes a payment tuple (priority, description) into the heap."""
        heapq.heappush(self._heap, (priority, name))

    def pop_payment(self) -> tuple:
        """Removes and returns the highest-priority payment (smallest priority number)."""
        if self._heap:
            return heapq.heappop(self._heap)
        return None

    def is_empty(self) -> bool:
        """Returns True if there are no pending payments."""
        return len(self._heap) == 0


# --- Execution Example ---
if __name__ == "__main__":
    queue = PaymentQueue()

    # Insert items in arbitrary order
    queue.push_payment(1, "Rent — Bole landlord")
    queue.push_payment(4, "Airtime — Ethio Telecom")
    queue.push_payment(2, "School fees — AAU")

    print("=== PAYMENT QUEUE PROCESSING ===")
    order = 1
    while not queue.is_empty():
        priority, task = queue.pop_payment()
        print(f"#{order} [Priority {priority}] Processing: {task}")
        order += 1
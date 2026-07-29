"""
File: day09_banking_system.py
Description: Complete Day 9 Non-Linear Data Structures implementation.
             Includes Branch Tree, Transfer Graph, and Payment Priority Heap.
"""

import heapq
from collections import deque


# ==========================================
# 1. BRANCH HIERARCHY AS A TREE
# ==========================================
class Account:

    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance


class Branch:

    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.accounts = []

    def add_child(self, branch: "Branch"):
        self.children.append(branch)

    def add_account(self, account: Account):
        self.accounts.append(account)

    def total_balance(self) -> float:
        total = sum(acc.balance for acc in self.accounts)
        for child in self.children:
            total += child.total_balance()
        return total


# ==========================================
# 2. TRANSFERS AS A GRAPH (BFS)
# ==========================================
def bfs_reachable(graph: dict, start_node: str) -> set:
    visited = {start_node}
    queue = deque([start_node])

    while queue:
        curr = queue.popleft()
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


# ==========================================
# 3. PRIORITY QUEUE FOR PAYMENTS (HEAP)
# ==========================================
class PaymentPriorityQueue:

    def __init__(self):
        self._queue = []

    def schedule(self, priority: int, name: str):
        heapq.heappush(self._queue, (priority, name))

    def process_all(self):
        step = 1
        while self._queue:
            prio, name = heapq.heappop(self._queue)
            print(f"   {step}. [Priority {prio}] {name}")
            step += 1


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("==================================================")
    print("   DAY 9 PROJECT: NON-LINEAR DATA STRUCTURES")
    print("==================================================\n")

    # --- Part 1: Tree ---
    print("--- 1. Bank Branch Tree Hierarchy ---")
    head_office = Branch("Head Office - Addis Ababa")
    bole = Branch("Bole Branch")
    piazza = Branch("Piazza Branch")

    bole.add_account(Account("CBE-101", 12000.00))
    piazza.add_account(Account("CBE-202", 8500.00))
    head_office.add_account(Account("CBE-001", 50000.00))

    head_office.add_child(bole)
    head_office.add_child(piazza)

    print(f"Bole Branch Total:   ETB {bole.total_balance():,.2f}")
    print(f"Piazza Branch Total: ETB {piazza.total_balance():,.2f}")
    print(f"Total Bank System:   ETB {head_office.total_balance():,.2f}\n")

    # --- Part 2: Graph ---
    print("--- 2. Money Transfer Graph (BFS) ---")
    transfers = {
        "CBE-1": ["CBE-2", "CBE-3"],
        "CBE-2": ["CBE-4"],
        "CBE-3": ["CBE-4"],
        "CBE-4": [],
    }
    start_account = "CBE-1"
    reachable = bfs_reachable(transfers, start_account)
    print(f"Accounts reachable from {start_account}: {sorted(list(reachable))}\n")

    # --- Part 3: Priority Queue ---
    print("--- 3. Pending Payment Priority Queue ---")
    payments = PaymentPriorityQueue()
    payments.schedule(1, "Rent — Bole landlord")
    payments.schedule(4, "Airtime — Ethio Telecom")
    payments.schedule(2, "School fees — AAU")
    payments.process_all()

    print("\n==================================================")
    print("   DAY 9 COMPLETED - READY FOR DAY 10 REVIEW")
    print("==================================================")
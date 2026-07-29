"""
File: transfer_graph.py
Description: Money transfer connections modeled as a Graph using BFS reachability.
"""

from collections import deque


def find_reachable_accounts(graph: dict, start_account: str) -> set:
    """
    Uses Breadth-First Search (BFS) to discover all accounts that can be reached
    from a starting account through transfer links.
    """
    visited = set()
    queue = deque([start_account])

    # Mark the initial starting account as visited
    visited.add(start_account)

    while queue:
        current_account = queue.popleft()

        # Get adjacent accounts that received direct transfers
        neighbors = graph.get(current_account, [])

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


# --- Execution Example ---
if __name__ == "__main__":
    # Graph represented as an Adjacency List
    transfers = {
        "CBE-1": ["CBE-2", "CBE-3"],
        "CBE-2": ["CBE-4"],
        "CBE-3": ["CBE-4"],
        "CBE-4": [],
    }

    start = "CBE-1"
    reachable = find_reachable_accounts(transfers, start)

    print("=== TRANSFER GRAPH REACHABILITY ===")
    print(f"Starting Account: {start}")
    print(f"Reachable Accounts ({len(reachable)}): {sorted(list(reachable))}")
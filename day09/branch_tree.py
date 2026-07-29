"""
File: branch_tree.py
Description: Bank Branch Hierarchy modeled as a Tree data structure.
"""


class Account:
    """Represents an individual bank account."""

    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance


class Branch:
    """Represents a bank branch in a hierarchical tree structure."""

    def __init__(self, name: str):
        self.name = name
        self.children = []  # List of sub-branches (child nodes)
        self.accounts = []  # List of direct accounts under this branch

    def add_child(self, branch: "Branch"):
        """Attach a sub-branch to this branch."""
        self.children.append(branch)

    def add_account(self, account: Account):
        """Add a direct bank account to this branch."""
        self.accounts.append(account)

    def total_balance(self) -> float:
        """
        Recursively calculates the total balance of this branch
        and all nested sub-branches beneath it.
        """
        # Base step: sum balances of direct accounts at this branch level
        total = sum(account.balance for account in self.accounts)

        # Recursive step: add balances from every child sub-branch
        for child in self.children:
            total += child.total_balance()

        return total


# --- Execution Example ---
if __name__ == "__main__":
    # Create branches (tree nodes)
    head_office = Branch("Head Office - Addis Ababa")
    region_north = Branch("Northern Regional Office")
    bole_branch = Branch("Bole Branch")
    piazza_branch = Branch("Piazza Branch")

    # Add accounts to specific branches
    bole_branch.add_account(Account("CBE-101", 5000.00))
    bole_branch.add_account(Account("CBE-102", 2500.00))
    piazza_branch.add_account(Account("CBE-201", 3000.00))
    head_office.add_account(Account("CBE-001", 10000.00))

    # Build hierarchy: Head Office -> Regional -> Local Branches
    region_north.add_child(bole_branch)
    region_north.add_child(piazza_branch)
    head_office.add_child(region_north)

    # Calculate total balances
    print("=== BRANCH BALANCE CALCULATIONS ===")
    print(f"Bole Branch Total:   ETB {bole_branch.total_balance():,.2f}")
    print(f"Northern Region:     ETB {region_north.total_balance():,.2f}")
    print(f"Head Office (Total): ETB {head_office.total_balance():,.2f}")
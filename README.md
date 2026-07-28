#  Day 08 - Bank Management System
## Search & Sort Account Registry

A Python Object-Oriented Bank Management System that extends the Day 07 project by adding advanced searching, sorting, and recursive algorithms.

This project demonstrates practical use of:

- Object-Oriented Programming (OOP)
- Abstract Classes
- Encapsulation
- Factory Design Pattern
- Singleton Design Pattern
- Observer Design Pattern
- Dictionary Data Structure
- Sorting Algorithms
- Binary Search
- Recursion
- Big-O Complexity Analysis


---

##  Features

### Account Management

The system supports:

- Savings Accounts
- Current Accounts
- Deposits
- Withdrawals
- Transaction History


### Account Registry

Accounts are stored using a dictionary:

```
Account Number → Account Object
```

Example:

```
ACC001 → SavingsAccount
ACC002 → CurrentAccount
```


### Balance Leaderboard

Find the highest balance accounts:

```python
top_by_balance(3)
```

Example output:

```
Marta      12000 ETB
Abebe       8000 ETB
Surafel     5000 ETB
```


### Binary Search Account Lookup

Search accounts efficiently by account number:

```python
find_by_number("ACC003")
```

Algorithm:

```
1. Sort account numbers
2. Find middle element
3. Compare target
4. Search left or right half
```

Complexity:

```
O(log n)
```


### Recursive Transaction Total

Calculate total transactions using recursion:

Example:

```
Deposit: 1000 ETB
Withdraw: 500 ETB

Total: 1500 ETB
```

Complexity:

```
O(n)
```


---

#  Project Structure

```
day08/
│
├── account.py
├── account_factory.py
├── account_registry.py
├── bank_config.py
├── binary_search.py
├── current_account.py
├── savings_account.py
└── practice.py
```


---

# 🛠️ Requirements

- Python 3.10+

Check Python version:

```bash
python --version
```


---

#  How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd day08
```

Run:

```bash
python practice.py
```


---

# 🧪 Testing

Test Account module:

```bash
python -c "from account import Account; print('Account OK')"
```

Test Registry:

```bash
python -c "from account_registry import AccountRegistry; print('Registry OK')"
```

Test Binary Search:

```bash
python -c "from binary_search import binary_search; print(binary_search(['ACC001','ACC002','ACC003'],'ACC002'))"
```


---

#  Complexity Analysis

| Operation | Algorithm | Complexity |
|---|---|---|
| Add Account | Dictionary | O(1) |
| Find Account | Dictionary | O(1) |
| Balance Ranking | Sorting | O(n log n) |
| Account Search | Binary Search | O(log n) |
| Transaction Total | Recursion | O(n) |


---

# 📚 Concepts Practiced

✅ Python Classes and Objects  
✅ Abstract Base Classes  
✅ Inheritance  
✅ Encapsulation  
✅ Design Patterns  
✅ Searching Algorithms  
✅ Sorting Algorithms  
✅ Recursive Functions  
✅ Data Structures  


---

#  Next Module

Day 09 will introduce:

- Trees
- Graphs
- Hierarchical Data
- Connected Data Models


---

#  Author

**Surafel Mengist**

IBT College Canada  
CodeOps Program

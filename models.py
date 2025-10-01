from dataclasses import dataclass

@dataclass
class User:
    """
    Represents a user in the expense tracker.
    """
    name: str           # User name
    email: str = ""     # Optional email for notifications

@dataclass
class Expense:
    """
    Represents an expense entry.
    """
    amount: float
    category: str
    expense_date: str      # Format YYYY-MM-DD
    description: str = ""
    user: str = "self"     # Default user name

@dataclass
class Budget:
    """
    Represents monthly budget per category.
    """
    category: str
    month: int
    year: int
    amount: float

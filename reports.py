import sqlite3
from database import DB_NAME

def total_spending(month, year):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    target = f"{year}-{month:02d}"
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', expense_date)=?", (target,))
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total

def spending_vs_budget(month, year):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    target = f"{year}-{month:02d}"
    cursor.execute('''
        SELECT b.category, b.amount, SUM(e.amount)
        FROM budgets b LEFT JOIN expenses e
        ON b.category=e.category AND strftime('%Y-%m', e.expense_date)=?
        WHERE b.month=? AND b.year=?
        GROUP BY b.category
    ''', (target, month, year))
    rows = cursor.fetchall()
    conn.close()
    result = []
    for cat, budget, spent in rows:
        spent = spent or 0
        percent = spent/budget*100 if budget else 0
        result.append((cat,budget,spent,percent))
    return result

def group_expense_summary(month, year):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    target = f"{year}-{month:02d}"
    cursor.execute('''
        SELECT user, SUM(amount) FROM expenses
        WHERE strftime('%Y-%m', expense_date)=?
        GROUP BY user
    ''', (target,))
    rows = cursor.fetchall()
    conn.close()
    return {u or "Unassigned": total for u,total in rows}

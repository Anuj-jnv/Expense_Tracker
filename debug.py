# debug_check.py
import sqlite3
from database import reset_db, create_tables, get_all_expenses

DB_NAME = "expense_tracker.db"

def print_expenses():
    rows = get_all_expenses()
    if not rows:
        print("No expenses in DB.")
        return
    print("\nCurrent expenses in DB:")
    print("ID | Amount | Category | Date       | Description   | User")
    print("------------------------------------------------------------")
    for r in rows:
        print(r)

def print_duplicates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT amount, category, expense_date, description, user, COUNT(*)
        FROM expenses
        GROUP BY amount, category, expense_date, description, user
        HAVING COUNT(*) > 1
    ''')
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("\n⚠️ Duplicate entries found:")
        for r in rows:
            print(r)
    else:
        print("\n✅ No duplicate entries.")

if __name__ == "__main__":
    # Reset DB for a clean state (comment out if you don't want to wipe data)
    reset_db()
    create_tables()
    print("Database reset and tables created.")

    print_expenses()
    print_duplicates()

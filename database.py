import sqlite3

DB_NAME = "expense_tracker.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            email TEXT
        )
    ''')

    # Expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            expense_date TEXT,
            description TEXT,
            user TEXT
        )
    ''')

    # Budgets table (category + month + year)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            month INTEGER,
            year INTEGER,
            amount REAL
        )
    ''')

    # Groups table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    ''')

    # Group members
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS group_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            user_name TEXT
        )
    ''')

    conn.commit()
    conn.close()

def reset_db():
    """Drop all tables and recreate."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS expenses')
    cursor.execute('DROP TABLE IF EXISTS budgets')
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('DROP TABLE IF EXISTS groups')
    cursor.execute('DROP TABLE IF EXISTS group_members')
    conn.commit()
    conn.close()
    create_tables()
    print("✅ Database reset complete.")

# Add a user
def add_user(name, email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (name,email) VALUES (?,?)', (name,email))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

# Add expense (idempotent)
def add_expense(amount, category, date, description, user="Unassigned"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Skip if duplicate
    cursor.execute('''
        SELECT id FROM expenses WHERE amount=? AND category=? AND expense_date=? AND description=? AND user=?
    ''', (amount, category, date, description, user))
    if cursor.fetchone():
        conn.close()
        return
    cursor.execute('''
        INSERT INTO expenses (amount, category, expense_date, description, user)
        VALUES (?,?,?,?,?)
    ''', (amount, category, date, description, user))
    conn.commit()
    conn.close()

# Set budget for month/year
def set_budget(category, month, year, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM budgets WHERE category=? AND month=? AND year=?',
                   (category, month, year))
    r = cursor.fetchone()
    if r:
        cursor.execute('UPDATE budgets SET amount=? WHERE id=?', (amount, r[0]))
    else:
        cursor.execute('INSERT INTO budgets (category, month, year, amount) VALUES (?,?,?,?)',
                       (category, month, year, amount))
    conn.commit()
    conn.close()

# Get all expenses
def get_all_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, category, expense_date, description, user FROM expenses ORDER BY id')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Add group
def add_group(name, members):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))
        group_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        cursor.execute('SELECT id FROM groups WHERE name=?', (name,))
        group_id = cursor.fetchone()[0]
    for m in members:
        cursor.execute('SELECT id FROM group_members WHERE group_id=? AND user_name=?', (group_id, m))
        if not cursor.fetchone():
            cursor.execute('INSERT INTO group_members (group_id, user_name) VALUES (?,?)', (group_id, m))
    conn.commit()
    conn.close()
    return group_id

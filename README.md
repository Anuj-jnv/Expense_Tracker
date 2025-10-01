# 💰 Python Expense Tracker

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **command-line Python application** to help users manage daily expenses, track budgets, and monitor shared group spending efficiently. The project uses **SQLite** for data storage and is fully **Docker-ready** for easy deployment.

---

## 📌 Features

- Log daily expenses with **categories** (Food, Transport, Entertainment, etc.).
- Set **monthly budgets** for each category, including **different budgets for different months**.
- Receive **alerts** when approaching or exceeding budgets.
- Track **shared expenses** among multiple users (Splitwise-like).
- Generate reports: **total monthly spending** and **spending vs. budget per category**.
- Database resets on fresh start for clean test runs.
- Fully **Dockerized** for simple setup and execution.

---

## 📂 Project Structure

expense-tracker/
├── main.py # Entry point of the application
├── database.py # Handles SQLite database operations
├── expense.py # Expense class and logic
├── alerts.py # Budget alert handling
├── utils.py # Helper functions for calculations and summaries
├── expenses.db # SQLite database file (auto-created)
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build file
└── README.md # Project documentation


---

## ⚙️ Setup & Run

### 🔹 1. Run Locally

1. Clone the repository:  
```bash
git clone https://github.com/Anuj-jnv/Expense_Tracker.git
cd Expense_Tracker

2. Install dependencies (if any):
pip install -r requirements.txt

3.  Run the application:
 python main.py

---

### 🔹 2. Run with Docker

1. Build Docker Image
    docker build -t Expense_Tracker .

2. Run the Application
    docker run --rm -it Expense_Tracker

✅ Test Steps

   1. Run the app → database resets automatically.

   2. Add users and expenses → verify they are stored in SQLite.

   3. Set budgets → confirm alerts appear when thresholds are reached.

   4. Add group/shared expenses → verify totals per user.

   5. Restart → database should reset.

   6. Run via Docker → confirm same behavior.

🗃️ Database & SQL

The project uses SQLite for persistence.

Tables include users and expenses.

Examples SQL

   CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
    );

   CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TEXT DEFAULT CURRENT_TIMESTAMP
    );

📝 Documentation in Code

    database.py → functions for users, expenses, budgets.

    alerts.py → handles budget alerts.

    utils.py → helper functions for calculations and summaries.

    main.py → runs the program and links all modules.

    All functions include docstrings and inline comments for clarity.






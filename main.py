from database import reset_db, create_tables, add_user, add_expense, set_budget, add_group
from reports import total_spending, spending_vs_budget, group_expense_summary
from alerts import check_alert

# 1️⃣ Reset DB
reset_db()
create_tables()

# 2️⃣ Users
add_user("Alice","alice@example.com")
add_user("Bob","bob@example.com")
add_user("Charlie","charlie@example.com")

# 3️⃣ Expenses
add_expense(2000,"Food","2025-09-05","Groceries","Alice")
add_expense(2000,"Food","2025-09-10","Restaurant","Alice")
add_expense(1000,"Transport","2025-09-07","Taxi","Bob")
add_expense(500,"Entertainment","2025-09-20","Concert","Alice")
add_expense(1000,"Entertainment","2025-09-22","Event","Bob")


# Shared group dinner $600 split between Alice & Charlie
for u in ["Alice","Charlie"]:
    add_expense(300,"Food","2025-09-25","Group Dinner",u)

# 4️⃣ Budgets (different months)
set_budget("Food",9,2025,1000)
set_budget("Transport",9,2025,500)
set_budget("Entertainment",9,2025,400)
set_budget("Food",10,2025,1200)  # Different month budget

# 5️⃣ Group
add_group("Friends", ["Alice","Bob","Charlie"])

# 6️⃣ Reports
month, year = 9, 2025
print("\nTotal Spending:", total_spending(month,year))

print("\nSpending vs Budget:")
for cat,budget,spent,percent in spending_vs_budget(month,year):
    print(f"{cat}: Spent {spent} / Budget {budget} ({percent:.1f}%)")

print("\nAlerts:")
for a in check_alert(month,year,alert_threshold_percent=90,low_budget_threshold_percent=10):
    print(a)

print("\nGroup Expense Summary:")
for u,total in group_expense_summary(month,year).items():
    print(f"{u} spent: {total}")

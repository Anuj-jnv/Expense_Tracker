from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# -----------------------------
# Constants
# -----------------------------
CATEGORIES = ["Food", "Transport", "Entertainment", "Utilities", "Others"]

# -----------------------------
# Validation Functions
# -----------------------------
def validate_amount(amount):
    """
    Check if the amount is a positive number.
    Returns float if valid, None otherwise.
    """
    try:
        amt = float(amount)
        if amt <= 0:
            print("Amount must be positive!")
            return None
        return amt
    except ValueError:
        print("Invalid amount! Enter a number.")
        return None

def validate_category(category):
    """
    Check if the category is allowed.
    Returns category if valid, None otherwise.
    """
    if category not in CATEGORIES:
        print(f"Invalid category! Choose from {CATEGORIES}")
        return None
    return category

def parse_date(date_str):
    """
    Convert string YYYY-MM-DD to a datetime.date object.
    Returns None if format is invalid.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        return None

# -----------------------------
# Calculation Helpers
# -----------------------------
def calculate_percentage(spent, budget):
    """
    Calculate percentage spent relative to budget.
    """
    if budget == 0:
        return 0
    return (spent / budget) * 100

# -----------------------------
# Email Helper
# -----------------------------
def send_email_alert(to_email, subject, message, from_email="youremail@gmail.com", password="yourpassword"):
    """
    Sends an email alert to the user.
    Make sure Gmail App Password is used or 'Less secure apps' enabled.
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print("Error sending email:", e)

# -----------------------------
# Helper: Format money
# -----------------------------
def format_currency(amount):
    """
    Format number as currency string
    """
    return f"${amount:.2f}"

# -----------------------------
# Optional: User helpers
# -----------------------------
def validate_user_name(name):
    """
    Validate a user name is non-empty
    """
    if not name or len(name.strip()) == 0:
        print("User name cannot be empty!")
        return None
    return name.strip()

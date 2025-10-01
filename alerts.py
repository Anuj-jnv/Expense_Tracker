from reports import spending_vs_budget

def check_alert(month, year, alert_threshold_percent=90, low_budget_threshold_percent=10):
    from reports import spending_vs_budget
    alerts = []
    for cat, budget, spent, percent in spending_vs_budget(month, year):
        if percent >= alert_threshold_percent:
            alerts.append(f"⚠️ ALERT! {cat} reached {percent:.1f}% of budget ({spent}/{budget})")
        elif spent >= budget * (100 - low_budget_threshold_percent)/100:
            alerts.append(f"⚠️ LOW BUDGET! {cat} only {budget-spent} left")
    return alerts

request_spending = {
    "mehek": {
        "balance": 3000.00,
        "transaction": [
            {"amount": -9000.00, "category": "creatives"},
            {"amount": 7000.00, "category": "sponsor"},
            {"amount": -2000.00, "category": "Prize-money"}
        ]
    },
    "arham": {
        "balance": 5000.00,
        "transaction": [
            {"amount": 8000.00, "category": "stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "unnati": {
        "balance": 3500.00,
        "transaction": [
            {"amount": -5000.00, "category": "Attractions"},
            {"amount": 2500.00, "category": "promo"},
            {"amount": -900.00, "category": "lighting"},
            {"amount": -3000.00, "category": "games"}
        ]
    },
    "gaurang": {
        "balance": 2000.00,
        "transaction": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}

def total_spending(request_spending, account_id: str, category: str):
    account = request_spending.get(account_id.lower())
    if not account:
        return 0.0
    total = 0.0
    for transaction in account['transaction']:
        if transaction['category'].lower() == category.lower():
            total += transaction['amount']
    return total

def account_balance(request_spending, account_id: str):
    account = request_spending.get(account_id)
    if not account:
        return 0.0

    balance = account.get("balance", 0.0)
    for transaction in account['transaction']:
        balance -= transaction['amount']

    return balance

def money_owed(request_spending, account_id: str):
    balance = account_balance(request_spending, account_id)
    return max(0.0, -balance)

name=input('Enter the name of the account holder:')
category=input('Enter the category:')
print("Total spending in category:", total_spending(request_spending, name.lower(), category))
print("Account balance:", account_balance(request_spending, name.lower()))                  
print("Money owed:", money_owed(request_spending, name.lower()))                          


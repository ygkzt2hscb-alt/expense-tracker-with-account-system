# Expense Tracker

A command-line expense tracking system with persistent JSON storage and user accounts.

## Features

- **User Accounts** — Create an account and log in securely
- **Add Transactions** — Record expenses with amount, category, and automatic date
- **Transaction History** — View all past transactions in chronological order
- **Monthly Summary** — See total spending broken down by category for any month
- **Data Persistence** — All data saved to `expense_tracker.json` automatically

## How It Works

The program stores data in JSON format:

```json
{
  "username": {
    "password": "userpassword",
    "transactions": [
      {
        "amount": 45.50,
        "category": "Groceries",
        "date": "2026-05-19"
      }
    ]
  }
}

## How To Run

python expense_tracker.py

## Example Session

--- Expense Tracker ---

1. Add a transaction
2. View transaction history
3. View monthly summary
4. Log out

Choose an option: 1
How much was spent on this transaction? $42.50
Category: Groceries
Expense added.

--- Expense Tracker ---

Choose an option: 3
Which month and year are you looking for? (Format: YYYY-MM)
2026-05

Groceries: $42.50
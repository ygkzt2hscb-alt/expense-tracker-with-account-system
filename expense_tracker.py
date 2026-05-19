import json
import os
from datetime import date
print(str(date.today()))

USER_FILE = "expense_tracker.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}
    
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


account = load_users()

def not_got_account():
    while True:
        ask = input("Do you already have an account? (yes/no) ").lower().strip().replace(" ", "")
        if ask == "no":
            return True
        elif ask == "yes":
            return False
        else:
            print("Please respond with either yes or no.")
        

def create_account():
    while True:
        create = input("Would you like to create an account? (yes/no) ").lower().strip().replace(" ", "")
        if create == "yes":
            break
        elif create == "no":
            print("Alright, maybe next time.")
            quit()
        else:
            print("Either respond with yes or no.")
    while True:
        username = input("Please create a username. ").strip().replace(" ", "")
        if len(username) < 3:
            print("Please create a username with at least 3 characters.")
            continue
        elif username in account:
            print("This username has already been taken, please choose another one.")
            continue
        else:
            while True:
                password = input(f"Please create a password, {username}. ").strip()
                if len(password) < 6:
                    print("Please make it so your password is at least 6 characters.")
                    continue
                else:
                    print(f"Your password is: {password}.")
                    break
        break
    account[username] = {
        "password": password,
        "transactions": []
    }
    save_users(account)
    print("Account created successfully.")



def login():
    while True:
        login = input("Would you like to log into an account? (yes/no) ").lower().strip().replace(" ", "")
        if login == "yes":
            while True:
                username = input("Please enter you username. ").strip()
                password = input("Please enter your password. ").strip()
                if username in account:
                    if account[username]["password"] == password:
                        print(f"You are logged in, {username}.")
                        return username
                    else:
                        print("Your password is incorrect.")
                else:
                    print("This username does not exist.")
                
        elif login == "no":
            print("Maybe next time.")
            quit()
        else:
            print("Please answer with either yes or no.")
            continue

def add_transaction(username):
    while True:
        try:
            amount = float(input("How much was spent on this transaction? $"))
            if amount <= 0:
                print("Please put in a value larger than 0.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue
        category = input("Category: ").strip().replace(" ", "")
        if len(category) < 3:
            print("Please enter a valid category.")
            continue
        today = str(date.today())

        transaction = {
            "amount": amount,
            "category": category,
            "date": today
        }
        account[username]["transactions"].append(transaction)
        save_users(account)
        print("Expense added.")
        break

def view_transactions(username):
    transactions = account[username]["transactions"]
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(transactions):
            print(f"{i+1}. {transaction['date']} | {transaction['category']} | ${transaction['amount']}")
        
def monthly_summary(username):
    while True:
        user_date = input("Which month and year are you looking for?"
                          "\nFormat: YYYY-MM"
                          )
        totals = {}
        for transaction in account[username]["transactions"]:
            transaction_month = transaction["date"][:7]
            if transaction_month == user_date:
                category = transaction["category"]
                amount = transaction["amount"]
                if category not in totals:
                    totals[category] = 0
                totals[category] += amount
        if len(totals) == 0:
            print("No transactions found within this month.")
        else:
            for category, total in totals.items():
                print(f"{category}: ${total}")

def menu(username):
    while True:
        print("\n--- Expense Tracker ---")
        print("\n1. Add a transaction.")
        print("2. View a transaction.")
        print("3. View a monthly summary.")
        print("4. Log out.")
        choice = input("Choose an option. ")
        if choice == "1":
            add_transaction(username)
        elif choice == "2":
            view_transactions(username)
        elif choice == "3":
            monthly_summary(username)
        elif choice == "4":
            print("Successfully logged out.")
            break
        else:
            print("Please choose an option from 1-4.")


if not_got_account():
    create_account()
logged_in_user = login()
menu(logged_in_user)
    

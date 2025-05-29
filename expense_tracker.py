import json
import os
import datetime as dt
import pandas as pd
from tabulate import tabulate
expenses = []
total_budget = None
def show_menu():
    print("\n=============Expense Tracker=============")
    print("1. Set Total Budget")
    print("2. Add New Expenses")
    print("3. View All Expenses")
    print("4. View Expenses in Table Format")
    print("5. Show Remaining Balance")
    print("6. Save to TXT file")
    print("7. Save to CSV file")
    print("8. Exit")

def set_budget():
    global total_budget
    try:
        total_budget = float(input("Please enter your budget: Rs. "))
        print(f"Total budget set to Rs. {total_budget: .2f}")
    except ValueError:
        print("Invalid amount. Please enter a valid number")

def add_expenses():
    global total_budget
    if total_budget is None:
        print("⚠ No budget is added. Please add a budget first from choice 1")
        return
    try:
        category = input("Enter the category: ")
        amount = float(input("Enter the amount spent: "))
        total_expenses = sum(exp['Amount'] for exp in expenses)
        if total_expenses + amount > total_budget:
            print(f"❌ Cannot add expense. It exceeds your budget")
            print(f"Current expenses: Rs.{total_expenses:.2f}, Budget: Rs. {total_budget:.2f}")
            return
        description = input("Enter the description: ")
        date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expense = {
            'Category': category,
            'Amount' : amount,
            'Description' : description,
            'Date' : date
        }
        expenses.append(expense)
        print("Expense is added successfully")
    except ValueError:
        print("Invalid data, Please enter valid data")

def view_expenses():
    if not expenses:
        print("No expenses recorded")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"\n{i}. Category: {exp['Category']}, Amount: {exp['Amount']}, Description: {exp['Description']}, Date: {exp['Date']}")

def view_table():
    if not expenses:
        print("No expenses to show")
        return
    df = pd.DataFrame(expenses)
    print(f"\n {name}, Here's your Expenses Table: ")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))

def show_balance():
    spent = sum(exp['Amount'] for exp in expenses)
    remaining = total_budget - spent
    print(f"\n Total Budget : Rs. {total_budget: .2f}")
    print(f"\n Spent Amount : Rs. {spent: .2f}")
    print(f"\n Remaining Balance: Rs. {remaining: .2f}")

def save_txt():
    if not expenses:
        print("No expenses to save")
        return
    filename = f"{name}.txt"
    with open(filename, "a") as f:
        for exp in expenses:
            f.write(f"{exp['Date']} | {exp['Category']} | {exp['Amount']} | {exp['Description']}")
    print(f"Expenses saved to {filename}")

def save_csv():
    if not expenses:
        print("No expenses to save")
        return
    filename = f"{name}.csv"
    file_exists = os.path.exists(filename)
    df = pd.DataFrame(expenses)
    df.index += 1
    df.to_csv(filename,mode='a',header = not file_exists, index = False)
    print(f"Expenses saved to {filename}")


print("Welcome to the expense tracker")
name = input("Enter your name: ").strip().lower()
print(f"\n Hello, {name}. Lets see your expenses.")
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        set_budget()
    elif choice == 2:
        add_expenses()
    elif choice == 3:
        view_expenses()
    elif choice == 4:
        view_table()
    elif choice == 5:
        show_balance()
    elif choice == 6:
        save_txt()
    elif choice == 7:
        save_csv()
    elif choice == 8:
        print("BYE BYEEEE")
        break
    else:
        print("Invalid choice. Please try again")




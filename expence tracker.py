import os
import json
from datetime import datetime

# Initialize the expense file if it doesn't exist
expense_file = "expenses.json"
if not os.path.exists(expense_file):
    with open(expense_file, 'w') as file:
        json.dump([], file)

# Function to add a new expense
def add_expense():
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD, leave empty for today): ")
    
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    
    expense = {
        "description": description,
        "amount": amount,
        "date": date
    }
    
    # Load existing expenses and append the new one
    with open(expense_file, 'r') as file:
        expenses = json.load(file)
    expenses.append(expense)
    
    # Save the updated expenses list
    with open(expense_file, 'w') as file:
        json.dump(expenses, file, indent=4)
    
    print(f"Expense of {amount} added successfully.")

# Function to view all expenses
def view_expenses():
    with open(expense_file, 'r') as file:
        expenses = json.load(file)
    
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\nExpense Records:")
        print("Description | Amount | Date")
        print("-" * 40)
        for expense in expenses:
            print(f"{expense['description']} | {expense['amount']} | {expense['date']}")
    
# Function to calculate total expenses
def calculate_total_expenses():
    with open(expense_file, 'r') as file:
        expenses = json.load(file)
    
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: {total}")

# Main program loop
def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()

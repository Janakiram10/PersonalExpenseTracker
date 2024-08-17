import csv
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
from datetime import datetime

# Global list to store expenses and budget
expenses = []
budget = 0

# Function to add an expense
def add_expense(date, amount, category, description):
    expense = {
        'date': date,
        'amount': float(amount),
        'category': category,
        'description': description
    }
    expenses.append(expense)
    print(f"Added expense: {expense}")

# Function to save expenses to a CSV file
def save_expenses_to_csv(filename='C:\\Users\\janak\\Downloads\\PersonalExpenseTracker\\expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}")

# Function to load expenses from a CSV file
def load_expenses_from_csv(filename='C:\\Users\\janak\\Downloads\\PersonalExpenseTracker\\expenses.csv'):
    global expenses
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print(f"Expenses loaded from {filename}")
    except FileNotFoundError:
        print(f"No file named {filename} found. Starting with an empty list.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to display expenses
def display_expenses():
    if not expenses:
        print("No expenses to display.")
        return

    for expense in expenses:
        print(f"{expense['date']}: ₹{expense['amount']:.2f} - {expense['category']} ({expense['description']})")

# Function to plot expenses by category
def plot_expenses_by_category():
    if not expenses:
        print("No expenses to plot.")
        return

    categories = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    plt.bar(categories.keys(), categories.values(), color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Spending (₹)')
    plt.title('Spending by Category')
    plt.show()

# Function to plot expenses over time
def plot_expenses_over_time():
    if not expenses:
        print("No expenses to plot.")
        return

    dates = [expense['date'] for expense in expenses]
    amounts = [expense['amount'] for expense in expenses]

    plt.plot(dates, amounts, marker='o', linestyle='-', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Amount Spent (₹)')
    plt.title('Spending Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to filter expenses by category
def filter_expenses_by_category(category):
    filtered_expenses = [expense for expense in expenses if expense['category'] == category]
    if not filtered_expenses:
        print("No expenses found for this category.")
        return
    for expense in filtered_expenses:
        print(f"{expense['date']}: ₹{expense['amount']:.2f} - {expense['description']}")

# Function to filter expenses by date range
def filter_expenses_by_date(start_date, end_date):
    filtered_expenses = [expense for expense in expenses if start_date <= expense['date'] <= end_date]
    if not filtered_expenses:
        print("No expenses found for this date range.")
        return
    for expense in filtered_expenses:
        print(f"{expense['date']}: ₹{expense['amount']:.2f} - {expense['category']} ({expense['description']})")

# Function to filter expenses by amount range
def filter_expenses_by_amount(min_amount, max_amount):
    filtered_expenses = [expense for expense in expenses if min_amount <= expense['amount'] <= max_amount]
    if not filtered_expenses:
        print("No expenses found for this amount range.")
        return
    for expense in filtered_expenses:
        print(f"{expense['date']}: ₹{expense['amount']:.2f} - {expense['category']} ({expense['description']})")

# Function to generate a monthly summary
def monthly_summary():
    monthly_expenses = defaultdict(float)
    for expense in expenses:
        month_year = datetime.strptime(expense['date'], '%Y-%m-%d').strftime('%Y-%m')
        monthly_expenses[month_year] += expense['amount']

    for month, total in monthly_expenses.items():
        print(f"{month}: ₹{total:.2f}")

# Function to export expenses to an Excel file
def export_to_excel(filename='expenses.xlsx'):
    df = pd.DataFrame(expenses)
    df.to_excel(filename, index=False)
    print(f"Expenses exported to {filename}")

# Function to import expenses from an Excel file
def import_from_excel(filename='expenses.xlsx'):
    global expenses
    try:
        df = pd.read_excel(filename)
        expenses = df.to_dict(orient='records')
        print(f"Expenses imported from {filename}")
    except FileNotFoundError:
        print(f"No file named {filename} found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to set the budget
def set_budget(amount):
    global budget
    budget = amount
    print(f"Budget set to ₹{budget:.2f}")

# Function to track the remaining budget
def track_budget():
    if budget <= 0:
        print("No budget set.")
        return
    total_expense = sum(expense['amount'] for expense in expenses)
    remaining_budget = budget - total_expense
    print(f"Total expenses: ₹{total_expense:.2f}")
    print(f"Remaining budget: ₹{remaining_budget:.2f}")

# Main function to run the command-line interface
def main():
    load_expenses_from_csv()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Plot Expenses by Category")
        print("4. Plot Expenses Over Time")
        print("5. Filter Expenses by Category")
        print("6. Filter Expenses by Date Range")
        print("7. Filter Expenses by Amount Range")
        print("8. Monthly Summary")
        print("9. Export to Excel")
        print("10. Import from Excel")
        print("11. Set Budget")
        print("12. Track Budget")
        print("13. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            plot_expenses_by_category()
        elif choice == '4':
            plot_expenses_over_time()
        elif choice == '5':
            category = input("Enter category to filter by: ")
            filter_expenses_by_category(category)
        elif choice == '6':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            filter_expenses_by_date(start_date, end_date)
        elif choice == '7':
            min_amount = float(input("Enter minimum amount: "))
            max_amount = float(input("Enter maximum amount: "))
            filter_expenses_by_amount(min_amount, max_amount)
        elif choice == '8':
            monthly_summary()
        elif choice == '9':
            export_to_excel()
        elif choice == '10':
            import_from_excel()
        elif choice == '11':
            amount = float(input("Enter budget amount: "))
            set_budget(amount)
        elif choice == '12':
            track_budget()
        elif choice == '13':
            save_expenses_to_csv()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

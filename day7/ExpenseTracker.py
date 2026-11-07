
expenses = []

def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def show_expenses():
    if len(expenses) == 0:
        print("\nNo expenses found!")
        return

    print("\n------- All Expenses -------")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} : ₹{expense['amount']:.2f}"
        )


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total:.2f}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Calculate Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")

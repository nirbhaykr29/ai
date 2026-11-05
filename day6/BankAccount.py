class BankAccount:

    # Constructor
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")

    # Check Balance Method
    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Available Balance: ₹{self.balance}")


# Create Object
account = BankAccount("Nirbhay", 5000)

# Menu
while True:

    print("\n===== BANK ACCOUNT =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using Bank Account!")
        break

    else:
        print("Invalid choice! Try again.")
from datetime import datetime, date

# Current Date and Time
now = datetime.now()

print("===== DATE CALCULATOR =====")

print("Current Date:", now.strftime("%d-%m-%Y"))
print("Current Time:", now.strftime("%H:%M:%S"))

# Take Future Date from User
target_input = input("\nEnter target date (DD-MM-YYYY): ")

try:
    target_date = datetime.strptime(target_input, "%d-%m-%Y").date()

    # Calculate Remaining Days
    today = date.today()
    remaining_days = (target_date - today).days

    if remaining_days > 0:
        print("Remaining Days:", remaining_days)

    elif remaining_days == 0:
        print("Today is your target date!")

    else:
        print("This date has already passed!")

except ValueError:
    print("Invalid date! Please enter DD-MM-YYYY format.")
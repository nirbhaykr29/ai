try:
    # Take user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Division
    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

except Exception as e:
    print("Something went wrong:", e)
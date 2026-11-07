import random
import string

# Take password length from user
length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a valid password length!")

else:
    # Characters for password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
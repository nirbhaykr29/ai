secret_number = 25

while True:
    guess = int(input("Guess the secret number: "))

    if guess > secret_number:
        print("Too High! Try Again.")

    elif guess < secret_number:
        print("Too Low! Try Again.")

    else:
        print("Congratulations! Correct Guess 🎉")
        break
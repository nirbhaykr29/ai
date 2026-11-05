while True:

    print("\n===== NOTES APPLICATION =====")
    print("1. Add Note")
    print("2. Read Saved Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add Note
    if choice == "1":

        note = input("Enter your note: ")

        with open("note.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    # Read Notes
    elif choice == "2":

        try:
            with open("note.txt", "r") as file:
                notes = file.read()

                if notes:
                    print("\n===== SAVED NOTES =====")
                    print(notes)
                else:
                    print("No notes found!")

        except FileNotFoundError:
            print("No saved notes available!")

    # Exit
    elif choice == "3":
        print("Thank you for using Notes Application!")
        break

    else:
        print("Invalid choice! Try again.")
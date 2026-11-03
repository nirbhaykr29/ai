inventory = {
    "Laptop": 10,
    "Mobile": 20,
    "Keyboard": 15
}

while True:

    print("\n===== INVENTORY MANAGER =====")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display Products")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        if product in inventory:
            print("Product already exists!")
        else:
            inventory[product] = quantity
            print("Product added successfully!")

    # Update Product
    elif choice == "2":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Product updated successfully!")
        else:
            print("Product not found!")

    # Delete Product
    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted successfully!")
        else:
            print("Product not found!")

    # Display Products
    elif choice == "4":
        print("\n----- Product List -----")

        if inventory:
            for product, quantity in inventory.items():
                print(f"{product}: {quantity}")
        else:
            print("Inventory is empty!")

    # Exit
    elif choice == "5":
        print("Thank you for using Inventory Manager!")
        break

    else:
        print("Invalid choice! Try again.")
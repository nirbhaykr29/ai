contacts = {
    "Rahul": "9876543210",
    "Amit": "9876543211",
    "Priya": "9876543212",
    "Neha": "9876543213"
}

name = input("Enter contact name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact Not Found!")
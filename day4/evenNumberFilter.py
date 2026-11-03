numbers = [10, 15, 20, 25, 30, 35, 40, 45]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
#bill_generator

item1 = input("enter name of item 1 : ")
price1 = float(input(f"enter price of {item1} : "))
quantity1 = int(input(f"enter quantity of {item1} : "))

item2 = input("enter name of item 2 : ")
price2 = float(input(f"enter price of {item2} : "))
quantity2 = int(input(f"enter quantity of {item2} : "))

item3 = input("enter name of item 3 : ")
price3 = float(input(f"enter price of {item3} : "))
quantity3 = int(input(f"enter quantity of {item3} : "))

#calculate total for each item
total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

#calculate grand total
grand_total = total1 + total2 + total3

#calculate gst (assuming 18% gst)
gst = grand_total * 0.18

#output
print("\n---------- Bill -------")
print(f"{item1}\t{price1}\t{quantity1}\t{total1}")
print(f"{item2}\t{price2}\t{quantity2}\t{total2}")
print(f"{item3}\t{price3}\t{quantity3}\t{total3}")
print("----------------------------------------")
print(f"Grand Total:\t\t\t{grand_total}")
print(f"GST (18%):\t\t\t{gst}")
print(f"Total Amount:\t\t\t{grand_total + gst}")

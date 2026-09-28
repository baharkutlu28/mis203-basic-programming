
item1 = input("Enter first item name: ")
quantity1 = int(input("Enter quantity for first item: "))
price1 = float(input("Enter unit price for first item: "))

item2 = input("Enter second item name: ")
quantity2 = int(input("Enter quantity for second item: "))
price2 = float(input("Enter unit price for second item: "))

delivery_fee = float(input("Enter delivery fee: "))
tax_percentage = float(input("Enter tax percentage: "))

subtotal1 = quantity1 * price1
subtotal2 = quantity2 * price2

subtotal = subtotal1 + subtotal2
tax = subtotal * (tax_percentage / 100)
final_total = subtotal + tax + delivery_fee

print("\nPurchase Quote")
print("--------------------")
print(f"{item1}: {quantity1} x {price1:.2f} = {subtotal1:.2f} TRY")
print(f"{item2}: {quantity2} x {price2:.2f} = {subtotal2:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax: {tax:.2f} TRY")
print(f"Delivery: {delivery_fee:.2f} TRY")
print(f"Final Total: {final_total:.2f} TRY")

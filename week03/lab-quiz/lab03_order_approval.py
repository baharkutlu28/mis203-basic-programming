order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member = input("Is the customer a member? (yes/no): ").lower()

if requested_quantity <= 0:
    print("Order rejected: Invalid quantity.")
elif requested_quantity > available_stock:
    print("Order rejected: Insufficient stock.")
else:
    print("Order approved: Stock is available and quantity is valid.")

    final_price = order_amount

    if is_member == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Member discount applied: 10%")
    
    print(f"Final price: {final_price:.2f} TRY")

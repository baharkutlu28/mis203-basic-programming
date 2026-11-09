
def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_discount_rate(subtotal):
    if subtotal >= 1000:
        return 0.10
    elif subtotal >= 500:
        return 0.05
    else:
        return 0.0


def calculate_shipping_fee(subtotal):
    if subtotal >= 1000:
        return 0.0
    else:
        return 50.0


def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount = subtotal * discount_rate
    return subtotal - discount + shipping_fee


# Tests
assert calculate_subtotal(100, 2) == 200
assert calculate_discount_rate(499) == 0.0
assert calculate_discount_rate(500) == 0.05
assert calculate_discount_rate(1000) == 0.10
assert calculate_shipping_fee(1000) == 0.0

print("All tests passed!")


# Sample order 1
price1 = 200
quantity1 = 3

subtotal1 = calculate_subtotal(price1, quantity1)
discount_rate1 = calculate_discount_rate(subtotal1)
shipping_fee1 = calculate_shipping_fee(subtotal1)
final_total1 = calculate_final_total(
    subtotal1, discount_rate1, shipping_fee1
)

print("\n--- Order 1 ---")
print(f"Subtotal: {subtotal1:.2f} TRY")
print(f"Discount rate: {discount_rate1:.0%}")
print(f"Shipping fee: {shipping_fee1:.2f} TRY")
print(f"Final total: {final_total1:.2f} TRY")


# Sample order 2
price2 = 300
quantity2 = 4

subtotal2 = calculate_subtotal(price2, quantity2)
discount_rate2 = calculate_discount_rate(subtotal2)
shipping_fee2 = calculate_shipping_fee(subtotal2)
final_total2 = calculate_final_total(
    subtotal2, discount_rate2, shipping_fee2
)

print("\n--- Order 2 ---")
print(f"Subtotal: {subtotal2:.2f} TRY")
print(f"Discount rate: {discount_rate2:.0%}")
print(f"Shipping fee: {shipping_fee2:.2f} TRY")
print(f"Final total: {final_total2:.2f} TRY")


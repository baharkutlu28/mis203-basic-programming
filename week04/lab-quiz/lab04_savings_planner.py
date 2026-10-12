
print("Savings Goal Planner")

while True:
    starting_balance = float(input("Enter starting balance: "))
    if starting_balance >= 0:
        break
    print("Starting balance cannot be negative.")

while True:
    monthly_deposit = float(input("Enter monthly deposit: "))
    if monthly_deposit > 0:
        break
    print("Monthly deposit must be positive.")

while True:
    interest_rate = float(input("Enter monthly interest rate (%): "))
    if interest_rate >= 0:
        break
    print("Interest rate cannot be negative.")

while True:
    savings_goal = float(input("Enter savings goal: "))
    if savings_goal > 0:
        break
    print("Savings goal must be positive.")

balance = starting_balance
total_interest = 0
month = 0

print("\nSavings Plan")
print("-" * 45)

if balance >= savings_goal:
    print("Goal already reached!")
else:
    print(f"{'Month':<10}{'Interest':<15}{'Balance':<15}")

    while month < 60:
        month += 1

        interest = balance * interest_rate / 100
        balance += interest
        total_interest += interest

        balance += monthly_deposit

        print(f"{month:<10}{interest:<15.2f}{balance:<15.2f}")

        if balance >= savings_goal:
            break

if balance >= savings_goal:
    print(f"\nGoal reached in {month} months!")
else:
    print("\nGoal not reached within 60 months.")

print(f"Final balance: {balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")


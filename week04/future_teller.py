import random
import datetime

print("=" * 40)
print("       THE FUTURE TELLER")
print("       Your Destiny Awaits!")
print("=" * 40)

name = input("\nWhat is your name? ")

today = datetime.date.today()

print(f"\nHello, {name}!")
print("Today's date:", today)
print("\nLet's discover your future!")

print("\nChoose your mood:")
print("1. Happy")
print("2. Tired")
print("3. Sad")
print("4. Excited")

mood = input("\nEnter your choice (1-4): ")

predictions = [
    "A wonderful opportunity is coming your way!",
    "You may meet someone interesting soon!",
    "A small surprise will make you smile!",
    "Your hard work may bring good results!",
    "An exciting new chapter may begin soon!"
]

lucky_colours = ["Purple", "Blue", "Pink", "Green", "Gold"]

advice = [
    "Believe in yourself and never give up!",
    "Take a chance and try something new!",
    "Be patient. Good things take time!",
    "Smile more and enjoy the little things!",
    "Trust yourself and follow your dreams!"
]

if mood == "1":
    print("\nYour positive energy is shining!")
elif mood == "2":
    print("\nTake a break and give yourself some rest!")
elif mood == "3":
    print("\nRemember, difficult days do not last forever!")
elif mood == "4":
    print("\nYour excitement may lead you to new adventures!")
else:
    print("\nThe universe has a mysterious message for you!")

print("\n" + "=" * 40)
print("          YOUR FUTURE READING")
print("=" * 40)

lucky_number = random.randint(1, 100)
prediction = random.choice(predictions)
colour = random.choice(lucky_colours)
daily_advice = random.choice(advice)

print(f"\nYour lucky number is: {lucky_number}")
print(f"Your lucky colour is: {colour}")
print(f"\nYour prediction: {prediction}")
print(f"Your advice: {daily_advice}")

print("\nRemember: Your future is in your hands!")
print(f"See you again, {name}!")
print("=" * 40)
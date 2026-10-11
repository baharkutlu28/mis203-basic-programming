# mis203-basic-programming
Name: Bahar[Kutlu]

Student Number: [2404109011]

Department: Management Information Systems

Course Name: MIS203 Basic Programming

## AI Tool Information

AI Tool Used: ChatGPT

Prompt Used: Create a simple Python program that asks the user for their name, department, age, and career goal, and then prints a student profile.

What did you change?
I checked the code and made sure it works correctly. I also kept the code simple and easy to understand.



 #week02#
## Week 02

* **AI Tool Used:** ChatGPT

* **Prompt Used:** Create a Python grade calculator program using a while True loop and break. Ask for a student name and score, validate the score between 0 and 100, calculate the letter grade, and print the total number of students and average score.

* **What did you change?** I checked the code and made sure it follows the assignment requirements. I also used `student_name.lower()` so that the user can type `q` or `Q` to quit.

* **What does break do in your program?** It stops the loop when the user enters q.



## Week 03

* **AI Tool Used:** ChatGPT

* **Prompt Used:** This week you will combine everything you have learned so far: input, type conversion, f-strings, loops, and this week's new topic: conditions (if / elif / else, and / or, boundaries and input validation). Create a folder named week03 and write a Python program named ticket_office.py. The program sells cinema tickets and keeps running until the user wants to stop. It should ask for the customer name, age, day, and student status, validate the inputs, apply the correct ticket price and discount rules, print the ticket result, and print a summary after the loop ends.

* **What did you change?** I created the ticket office program and added input validation, discount rules, and a sales summary.

* **Tests:**

  1. Age 5, weekend, no → 0.00 TRY (Free)
  2. Age 12, weekday, yes → 120.00 TRY (Child)
  3. Age 65, weekday, no → 100.00 TRY (Senior)

* **Why does the order of the rules matter?** The program uses the first rule that matches. For example, a 10-year-old student must get the Child discount, so the Child rule must come before the Student rule.

 
## Week 04

### Project: Future Teller

**AI Tool Used:** ChatGPT

**What does the program do?**
The Future Teller is a Python program that gives users random future predictions. It asks for the user's name and mood, then shows a lucky number, a lucky colour, a prediction, and advice.

**Libraries Used:**
- random
- datetime

**What did I learn?**
I practised using variables, input, conditions, lists, functions from libraries, and random choices in Python.

**Testing:**
I ran the program and tested it with my name and different mood choices. The program worked successfully.
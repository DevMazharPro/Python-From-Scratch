# PRACTICE EXERCISES FOR CONDITIONAL STATEMENTS
"""
Practice exercises to master if-else, if-elif-else, and nested conditions.
"""

print("=== Conditional Statements Practice ===")

# Exercise 1: Simple if-else
print("\nExercise 1: Even or Odd Checker")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Exercise 2: If-elif-else chain
print("\nExercise 2: Grade Calculator")
marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# Write a program to find the greatest number of four numbers entered by user.
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
num_4 = int(input("Enter fourth number: "))

if num_1 > num_2 and num_1 > num_3 and num_1 > num_4:
    print(num_1, "is greater among these.")
elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4:
    print(num_2, "is greater among these.")
elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4:
    print(num_3, "is greater among these.")
elif num_4 > num_1 and num_4 > num_2 and num_4 > num_3:
    print(num_4, "is greater among these.")
else:
    print("All numbers are equal")



# Write a program to find out whether a student has passed or failed if it requires total of 40% and at least 33% in each subject out of 100. Assume user will enter marks for 3 subjects.

marks = []
total = 300
mark_1 = int(input("Enter marks for subject 1: "))  
mark_2 = int(input("Enter marks for subject 2: "))
mark_3 = int(input("Enter marks for subject 3: "))
marks.append(mark_1)
marks.append(mark_2)
marks.append(mark_3)
total_percentage = (sum(marks) / total) * 100
if total_percentage >= 40:
    if mark_1 >= 33 and mark_2 >= 33 and mark_3 >= 33:
        print("Student has passed in all subjects.")
    else:
        print("Student has failed in one or more subjects.")
else:
    print("Student has failed in all subjects.")

# A spam comment is defined as text containing following keywords: make a lot of money, buy now, subscribe this, click this. Write a program to detect these spams.

comment = input("Enter a comment: ")
if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("Spam comment detected!")
else:
    print("Not a spam comment.")

# Write a program to find out whether a given username contains less than 10 characters or not.
username = input("Enter a username: ")
if len(username) < 10:
    print("Correct Username - less than 10 characters")
else:
    print("Incorrect Username - more than 10 characters")


# Write a program to find whether name is in the list or not?
names_list = ["Mazhar", "Azhar", "Hasnain", "Abbas"]
inp_name = input("Enter your name: ")
if inp_name in names_list:
    print("Name is in the list")
else:
    print("Name is not in the list")

# Write a program to find out whether a given post is talking about "Mazhar" or not
post = input("Enter a post: ").lower()
if "mazhar" in post:
    print("Post is talking about Mazhar")
else:
    print("Post is not talking about Mazhar")

# Write a program to find out whether password is strong or not
password = input("Enter a password: ")
if len(password) >= 8 and "@" in password or "#" in password or "$" in password or "!" in password or "*" in password or "&" in password:
    print("Strong password")
else:
    print("Weak password")
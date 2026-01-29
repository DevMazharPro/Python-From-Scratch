# Conditional Statements - If else and elif in Python
"""
Conditional statements allow us to control the flow of our program
based on different conditions. Python provides if, elif, and else statements.
"""

# BASIC IF-ELSE STATEMENTS

print("=== Basic If-Else Examples ===")

condition1 = True

if condition1:
    print("Condition 1 is True") # This will be printed
else:
    print("Condition 1 is False")

# IF-ELIF-ELSE CHAINS

print("\n=== If-Elif-Else Chains ===")

cond_1 = False
cond_2 = True

if cond_1:
    print("Condition 1 is True")
elif cond_2:
    print("Condition 2 is True") # This will be printed
else:
    print("Both conditions are False")

# When cond_1 is False and cond_2 is True, the elif block will be executed
# If both cond_1 and cond_2 are False, the else block will be executed

# MULTIPLE IF STATEMENTS VS IF-ELIF-ELSE

print("\n=== Multiple If vs If-Elif-Else ===")

print("Multiple independent if statements:")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are adult, you can vote.")
if age >= 60:
    print("You are senior citizen too.")
else:
    print("You are under 18.")

# If we want to run multiple conditions we use multiple if statements
# Each if statement is evaluated independently

# Example 2: If-elif-else chain (mutually exclusive)
print("\nIf-elif-else chain (mutually exclusive):")
age = 25

if age <= 18:
    print("You are 18, or under 18.")
elif age <= 30:
    print("You are 30 or under 30.")
elif age <= 40:
    print("You are 40 or under 40.")
elif age <= 50:
    print("You are 50 or under 50.")
elif age <= 60:
    print("You are 60 or under 60.")
else:
    print("You are senior citizen aged 60+")

# In if-elif-else, only one block executes and program exits the conditional structure

# COMPLEX CONDITIONS WITH LOGICAL OPERATORS

print("\n=== Complex Conditions with Logical Operators ===")

temperature = 25
is_raining = False

# Using AND operator
if temperature > 20 and not is_raining:
    print("Perfect weather for a walk!")
elif temperature > 20 and is_raining:
    print("Warm but rainy - bring an umbrella!")
elif temperature <= 20 and not is_raining:
    print("Cool weather - wear a jacket!")
else:
    print("Cool and rainy - stay indoors!")

# Using OR operator
day = "Saturday"
is_holiday = True

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("It's the weekend or holiday! Time to relax!")
else:
    print("It's a weekday - time to work!")

# TERNARY OPERATOR (CONDITIONAL EXPRESSION)

print("\n=== Ternary Operator ===")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Another example
number = 15
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")


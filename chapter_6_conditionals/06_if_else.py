# IF-ELSE STATEMENTS
"""
If-else statements allow us to execute different blocks of code
based on whether a condition is True or False.
"""

print("=== Basic If-Else Examples ===")

# Example 1: Simple condition
age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 2: Even or odd number
number = 15

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example 3: Temperature check
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot")

# Example 4: Login validation
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials")

# Example 5: Grade pass/fail
marks = 75

if marks >= 50:
    print("You passed the exam!")
else:
    print("You failed the exam")

# Example 6: Positive/negative number
num = -5

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Example 7: User input with if-else
print("\n--- Interactive Examples ---")
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote")
    if user_age >= 60:
        print("You are also a senior citizen")
else:
    print("You are not eligible to vote")

# Example 8: Number comparison
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"Both numbers are equal: {num1}")

print("\n=== If-Else Statements Complete! ===")

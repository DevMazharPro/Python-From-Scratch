# IF-ELIF-ELSE STATEMENTS
"""
If-elif-else statements allow us to check multiple conditions in sequence.
Only one block will execute - the first condition that evaluates to True.
"""

print("=== If-Elif-Else Examples ===")

# Example 1: Grade classification
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")

# Example 2: Age categories
age = 25

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"Age: {age}, Category: {category}")

# Example 3: Temperature description
temp = 15

if temp < 0:
    description = "Freezing"
elif temp < 10:
    description = "Cold"
elif temp < 20:
    description = "Cool"
elif temp < 30:
    description = "Warm"
else:
    description = "Hot"

print(f"Temperature: {temp}°C, Description: {description}")

# Example 4: Traffic light system
light = "yellow"

if light == "red":
    action = "STOP"
elif light == "yellow":
    action = "PREPARE TO STOP"
elif light == "green":
    action = "GO"
else:
    action = "INVALID SIGNAL"

print(f"Light: {light}, Action: {action}")

# Example 5: BMI Calculator
weight = 70
height = 1.75
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f}, Category: {category}")

# Example 6: Letter grade with plus/minus
score = 87

if score >= 97:
    grade = "A+"
elif score >= 93:
    grade = "A"
elif score >= 90:
    grade = "A-"
elif score >= 87:
    grade = "B+"
elif score >= 83:
    grade = "B"
elif score >= 80:
    grade = "B-"
elif score >= 77:
    grade = "C+"
elif score >= 73:
    grade = "C"
elif score >= 70:
    grade = "C-"
elif score >= 67:
    grade = "D+"
elif score >= 65:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Example 7: Time of day greeting
current_hour = 14

if 5 <= current_hour < 12:
    greeting = "Good morning!"
elif 12 <= current_hour < 17:
    greeting = "Good afternoon!"
elif 17 <= current_hour < 21:
    greeting = "Good evening!"
else:
    greeting = "Good night!"

print(f"Hour: {current_hour}, Greeting: {greeting}")

# Example 8: Calculator with if-elif-else
print("\n--- Interactive Calculator ---")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator!")

print("\n=== If-Elif-Else Statements Complete! ===")

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


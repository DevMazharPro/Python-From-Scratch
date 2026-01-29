# NESTED CONDITIONAL STATEMENTS
"""
Nested conditional statements are conditions inside other conditions.
This allows for more complex decision-making logic.
"""

print("=== Nested Conditional Examples ===")

# Example 1: Exam grading with nested conditions
score = 85

if score >= 60:
    print("You passed the exam!")
    if score >= 90:
        print("Excellent! You got an A grade.")
        if score >= 95:
            print("Outstanding! You're in the top 5%!")
    elif score >= 80:
        print("Good job! You got a B grade.")
    elif score >= 70:
        print("You got a C grade.")
    else:
        print("You got a D grade.")
else:
    print("You failed the exam. Please try again.")

# Example 2: Age and license check
age = 25
has_license = True

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You have a license - you can drive!")
    else:
        print("You need to get a license first")
else:
    print("You are too young to drive")

# Example 3: Login with role-based access
username = "admin"
password = "12345"
role = "admin"

if username == "admin" and password == "12345":
    print("Login successful!")
    if role == "admin":
        print("You have admin access")
        print("You can: create, read, update, delete")
    elif role == "editor":
        print("You have editor access")
        print("You can: read, update")
    else:
        print("You have basic access")
        print("You can: read only")
else:
    print("Invalid credentials")

# Example 4: Shopping discount system
purchase_amount = 150
is_member = True

if purchase_amount > 100:
    print("You qualify for bulk purchase discount")
    if is_member:
        print("Additional member discount applied")
        final_discount = 20
    else:
        print("Standard bulk discount applied")
        final_discount = 10
elif purchase_amount > 50:
    print("You qualify for standard discount")
    if is_member:
        final_discount = 15
    else:
        final_discount = 5
else:
    print("No discount available")
    final_discount = 0

print(f"Final discount: {final_discount}%")

# Example 5: Weather activity suggestion
temperature = 22
is_raining = False
is_weekend = True

if temperature > 15:
    print("Weather is pleasant")
    if not is_raining:
        print("It's not raining")
        if is_weekend:
            print("Perfect weather for a picnic!")
        else:
            print("Great weather for a walk in the park")
    else:
        print("It's raining - indoor activities recommended")
else:
    print("Weather is cold")
    if is_raining:
        print("Cold and rainy - stay indoors with hot chocolate")
    else:
        print("Cold but dry - dress warmly for outdoor activities")

# Example 6: Student performance evaluation
marks = 78
attendance = 85
assignments_completed = 90

if marks >= 70:
    print("Academic performance: Good")
    if attendance >= 80:
        print("Attendance: Excellent")
        if assignments_completed >= 85:
            print("Assignments: Excellent")
            print("Overall: Outstanding student!")
        else:
            print("Assignments: Needs improvement")
            print("Overall: Good student, focus on assignments")
    else:
        print("Attendance: Needs improvement")
        print("Overall: Attend classes regularly")
else:
    print("Academic performance: Needs improvement")
    if attendance >= 80:
        print("Attendance: Good - keep it up!")
    else:
        print("Attendance: Also needs improvement")
    print("Overall: Significant improvement needed")

print("\n=== Nested Conditional Statements Complete! ===")
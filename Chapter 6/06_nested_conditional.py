# NESTED CONDITIONAL STATEMENTS
# A condition under another condition

print("\n=== Nested Conditional Statements ===")

score = 85

if score >= 60:
    print("You passed the exam!")
    if score >= 90:
        print("Excellent! You got an A grade.")
    elif score >= 80:
        print("Good job! You got a B grade.")
    elif score >= 70:
        print("You got a C grade.")
    else:
        print("You got a D grade.")
else:
    print("You failed the exam. Please try again.")
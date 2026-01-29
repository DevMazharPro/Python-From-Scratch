"""
========================================
ROUND FUNCTION AND NUMBER FORMATTING
========================================

The round() function is used to round numbers to a specified number of decimal places.
"""

# =============================================================================
# BASIC ROUND FUNCTION
# =============================================================================

print("=== Basic Round Function ===")

# Round to nearest integer (default)
print("round(3.7) =", round(3.7))      # Output: 4
print("round(3.2) =", round(3.2))      # Output: 3
print("round(3.5) =", round(3.5))      # Output: 4 (rounds .5 up)

# Round to specific decimal places
print("round(3.14159, 2) =", round(3.14159, 2))    # Output: 3.14
print("round(3.14159, 3) =", round(3.14159, 3))    # Output: 3.142
print("round(2.675, 2) =", round(2.675, 2))        # Output: 2.67

# Round negative numbers
print("round(-3.7) =", round(-3.7))    # Output: -4
print("round(-3.2) =", round(-3.2))    # Output: -3

print("\n" + "="*50 + "\n")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("=== Practical Examples ===")

# Currency calculations
price = 19.99
tax_rate = 0.08
tax = price * tax_rate
total = price + tax

print(f"Price: ${price}")
print(f"Tax (8%): ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")

# Grade calculations
score = 87.6
rounded_score = round(score)
print(f"Original score: {score}")
print(f"Rounded score: {rounded_score}")

# Average calculations
grades = [85.5, 92.3, 78.9, 91.2]
average = sum(grades) / len(grades)
print(f"Grades: {grades}")
print(f"Average: {round(average, 2)}")

print("\n" + "="*50 + "\n")

# =============================================================================
# ROUND WITH F-STRINGS
# =============================================================================

print("=== Round with F-Strings ===")

# Formatting in f-strings
pi = 3.14159265359
print(f"Pi (default): {pi}")
print(f"Pi (2 decimal places): {pi:.2f}")
print(f"Pi (3 decimal places): {pi:.3f}")
print(f"Pi rounded: {round(pi, 4)}")

# Currency formatting
amount = 1234.567
print(f"Amount: ${amount:.2f}")
print(f"Amount rounded: ${round(amount, 2)}")

print("\n" + "="*50 + "\n")

# =============================================================================
# COMMON USE CASES
# =============================================================================

print("=== Common Use Cases ===")

# Temperature conversion
celsius = 25.7
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {round(fahrenheit, 1)}°F")

# Percentage calculations
correct_answers = 17
total_questions = 20
percentage = (correct_answers / total_questions) * 100
print(f"Score: {round(percentage, 1)}%")

# BMI calculation
weight = 70.5  # kg
height = 1.75  # m
bmi = weight / (height ** 2)
print(f"BMI: {round(bmi, 1)}")

print("\n" + "="*50 + "\n")

# =============================================================================
# IMPORTANT NOTES
# =============================================================================

print("""
📚 IMPORTANT NOTES ABOUT ROUND():

1. **Banker's Rounding**: Python 3 uses "banker's rounding" - .5 rounds to nearest even number
   - round(2.5) = 2 (rounds down to even)
   - round(3.5) = 4 (rounds up to even)

2. **Floating Point Precision**: Some numbers can't be represented exactly
   - round(2.675, 2) = 2.67 (not 2.68 due to floating point precision)

3. **Negative Numbers**: Round works the same way with negative numbers
   - round(-3.5) = -4

4. **Decimal Places**: Second parameter specifies decimal places
   - round(3.14159, 0) = 3.0
   - round(3.14159, 1) = 3.1
   - round(3.14159, 2) = 3.14

💡 TIP: For financial calculations, consider using the decimal module for exact precision.
""")

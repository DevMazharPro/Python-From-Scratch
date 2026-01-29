"""
F-Strings: Formatted String Literals in Python
===============================================

F-strings (formatted string literals) were introduced in Python 3.6 and provide 
a concise, readable way to embed expressions inside string literals.

Syntax: f"string {expression} string"
"""

# ========================================
# BASIC F-STRING USAGE
# ========================================

name = "Alice"
age = 25
city = "New York"

print("=== Basic F-String Examples ===")
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city}.")
print()

# ========================================
# EXPRESSIONS IN F-STRINGS
# ========================================

print("=== Expressions in F-Strings ===")
x = 10
y = 5

print(f"The sum of {x} and {y} is {x + y}")
print(f"The product is {x * y}")
print(f"The division result is {x / y:.2f}")  # Formatted to 2 decimal places
print()

# ========================================
# FORMATTING OPTIONS
# ========================================

print("=== Formatting Options ===")

# Number formatting
price = 49.99
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:.0f}")  # No decimal places

# Percentage
score = 0.8765
print(f"Score: {score:.1%}")    # Percentage with 1 decimal

# Scientific notation
large_number = 1234567.89
print(f"Scientific: {large_number:.2e}")
print()

# ========================================
# ALIGNMENT AND PADDING
# ========================================

print("=== Alignment and Padding ===")

text = "Python"
number = 42

# Left alignment
print(f"'{text:<10}'")  # Left align, width 10
print(f"'{number:<10}'")  # Left align number

# Right alignment
print(f"'{text:>10}'")   # Right align
print(f"'{number:>10}'")  # Right align

# Center alignment
print(f"'{text:^10}'")   # Center align
print(f"'{number:^10}'")  # Center align

# With padding character
print(f"'{text:*^10}'")  # Center with * padding
print()

# ========================================
# DICTIONARIES AND OBJECTS
# ========================================

print("=== Dictionaries in F-Strings ===")

person = {
    "name": "Bob Smith",
    "age": 32,
    "occupation": "Developer"
}

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Occupation: {person['occupation']}")
print()

# ========================================
# DATE AND TIME FORMATTING
# ========================================

print("=== Date and Time Formatting ===")

from datetime import datetime

now = datetime.now()
print(f"Current time: {now}")
print(f"Formatted date: {now:%Y-%m-%d}")
print(f"Formatted time: {now:%H:%M:%S}")
print(f"Full format: {now:%B %d, %Y at %I:%M %p}")
print()

# ========================================
# ADVANCED FEATURES
# ========================================

print("=== Advanced Features ===")

# Conditional expressions
status = "pass" if score >= 0.7 else "fail"
print(f"Student status: {status}")

# Calling methods
message = "hello world"
print(f"Uppercase: {message.upper()}")
print(f"Title case: {message.title()}")

# Using functions
def format_currency(amount):
    return f"${amount:,.2f}"

salary = 75000
print(f"Annual salary: {format_currency(salary)}")
print()

# ========================================
# DEBUGGING WITH F-STRINGS (Python 3.8+)
# ========================================

print("=== Debugging with F-Strings ===")

debug_var = "test value"
debug_num = 123

print(f"{debug_var=}")  # Prints: debug_var='test value'
print(f"{debug_num=}")  # Prints: debug_num=123
print(f"{x + y=}")      # Prints: x + y=15
print()

print("=== F-String Mastery Complete! ===")
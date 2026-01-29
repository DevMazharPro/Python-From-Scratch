"""
========================================
TYPE CONVERSION (TYPE CASTING)
========================================

Type conversion is the process of converting one data type to another.
Python has built-in functions for type conversion.
"""

# =============================================================================
# INTEGER CONVERSION
# =============================================================================

print("=== Integer Conversion ===")

# String to integer
str_num = "123"
int_num = int(str_num)
print(f"String '{str_num}' to integer: {int_num}")
print(f"Type: {type(int_num)}")

# Float to integer (truncates decimal part)
float_num = 45.67
int_from_float = int(float_num)
print(f"Float {float_num} to integer: {int_from_float}")  # 45 (truncated)

# Boolean to integer
bool_true = True
bool_false = False
print(f"True to integer: {int(bool_true)}")   # 1
print(f"False to integer: {int(bool_false)}")  # 0

print("\n" + "="*50 + "\n")

# =============================================================================
# FLOAT CONVERSION
# =============================================================================

print("=== Float Conversion ===")

# Integer to float
int_num = 42
float_num = float(int_num)
print(f"Integer {int_num} to float: {float_num}")
print(f"Type: {type(float_num)}")

# String to float
str_float = "3.14159"
float_from_str = float(str_float)
print(f"String '{str_float}' to float: {float_from_str}")

# Boolean to float
print(f"True to float: {float(True)}")   # 1.0
print(f"False to float: {float(False)}")  # 0.0

print("\n" + "="*50 + "\n")

# =============================================================================
# STRING CONVERSION
# =============================================================================

print("=== String Conversion ===")

# Integer to string
int_val = 100
str_from_int = str(int_val)
print(f"Integer {int_val} to string: '{str_from_int}'")
print(f"Type: {type(str_from_int)}")

# Float to string
float_val = 99.99
str_from_float = str(float_val)
print(f"Float {float_val} to string: '{str_from_float}'")

# Boolean to string
print(f"True to string: '{str(True)}'")
print(f"False to string: '{str(False)}'")

print("\n" + "="*50 + "\n")

# =============================================================================
# BOOLEAN CONVERSION
# =============================================================================

print("=== Boolean Conversion ===")

# Numbers to boolean
print(f"bool(0): {bool(0)}")        # False
print(f"bool(1): {bool(1)}")        # True
print(f"bool(-5): {bool(-5)}")      # True
print(f"bool(0.0): {bool(0.0)}")    # False
print(f"bool(3.14): {bool(3.14)}")  # True

# String to boolean
print(f"bool(''): {bool('')}")              # False (empty string)
print(f"bool('hello'): {bool('hello')}")      # True
print(f"bool('0'): {bool('0')}")              # True
print(f"bool('False'): {bool('False')}")      # True

# None to boolean
print(f"bool(None): {bool(None)}")            # False

print("\n" + "="*50 + "\n")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("=== Practical Examples ===")

# Example 1: User input calculation
print("Example 1: User Input Calculation")
age_input = "25"
height_input = "1.75"

age = int(age_input)
height = float(height_input)

print(f"Age: {age} years (type: {type(age).__name__})")
print(f"Height: {height} m (type: {type(height).__name__})")

# Example 2: String formatting with numbers
print("\nExample 2: String Formatting")
price = 49.99
quantity = 3
total = price * quantity

print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${round(total, 2)}")

# Example 3: Boolean checks
print("\nExample 3: Boolean Checks")
user_input = "hello"
if user_input:  # Converts to boolean automatically
    print("User provided input!")
else:
    print("No input provided.")

number = 0
if number:  # 0 converts to False
    print("Number is non-zero")
else:
    print("Number is zero")

print("\n" + "="*50 + "\n")

# =============================================================================
# COMMON ERRORS AND SOLUTIONS
# =============================================================================

print("=== Common Errors and Solutions ===")

# Error: Invalid string conversion
try:
    invalid_str = "abc"
    result = int(invalid_str)
except ValueError as e:
    print(f"Error converting '{invalid_str}' to int: {e}")

# Solution: Check if string is numeric before conversion
str_to_check = "123"
if str_to_check.isdigit():
    print(f"'{str_to_check}' can be converted to integer: {int(str_to_check)}")
else:
    print(f"'{str_to_check}' cannot be converted to integer")

# Safe float conversion
float_str = "3.14"
try:
    float_result = float(float_str)
    print(f"Successfully converted '{float_str}' to float: {float_result}")
except ValueError:
    print(f"Cannot convert '{float_str}' to float")

print("\n" + "="*50 + "\n")

# =============================================================================
# SUMMARY
# =============================================================================

print("""
📚 TYPE CONVERSION SUMMARY:

1. **int()**: Convert to integer
   - int("123") → 123
   - int(45.67) → 45 (truncates decimal)
   - int(True) → 1, int(False) → 0

2. **float()**: Convert to float
   - float("3.14") → 3.14
   - float(42) → 42.0
   - float(True) → 1.0, float(False) → 0.0

3. **str()**: Convert to string
   - str(123) → "123"
   - str(45.67) → "45.67"
   - str(True) → "True"

4. **bool()**: Convert to boolean
   - False values: 0, 0.0, "", None, False
   - True values: Any non-zero number, non-empty string, True

💡 IMPORTANT:
- Always validate user input before conversion
- Use try-except blocks for safe conversion
- Boolean conversion follows "truthiness" rules
- String to int only works with numeric strings
""")

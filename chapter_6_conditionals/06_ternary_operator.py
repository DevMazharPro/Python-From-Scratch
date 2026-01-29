"""
========================================
TERNARY OPERATOR (CONDITIONAL EXPRESSIONS)
========================================

The ternary operator provides a concise way to write simple if-else statements.
It's also called a conditional expression.
"""

# =============================================================================
# BASIC TERNARY OPERATOR SYNTAX
# =============================================================================

print("=== Basic Ternary Operator ===")

# Traditional if-else
age = 20
if age >= 18:
    message = "Adult"
else:
    message = "Minor"

print("Traditional if-else:")
print(f"Age: {age}, Status: {message}")

# Ternary operator
message_ternary = "Adult" if age >= 18 else "Minor"
print("\nTernary operator:")
print(f"Age: {age}, Status: {message_ternary}")

print("\n" + "="*50 + "\n")

# =============================================================================
# MORE EXAMPLES
# =============================================================================

print("=== More Examples ===")

# Number classification
number = 7
classification = "Even" if number % 2 == 0 else "Odd"
print(f"Number {number} is {classification}")

# Temperature classification
temperature = 25
temp_status = "Warm" if temperature > 20 else "Cold"
print(f"Temperature {temperature}°C is {temp_status}")

# Grade classification
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"Score {score}: {grade}")

# Price check
price = 50
price_category = "Expensive" if price > 100 else "Affordable" if price > 50 else "Cheap"
print(f"Price ${price} is {price_category}")

print("\n" + "="*50 + "\n")

# =============================================================================
# TERNARY WITH FUNCTIONS
# =============================================================================

print("=== Ternary with Functions ===")

def get_discount_status(price):
    return "Discount Available" if price > 100 else "No Discount"

def calculate_price(price, is_member):
    return price * 0.9 if is_member else price

# Test functions
item_price = 120
print(f"Item price: ${item_price}")
print(f"Status: {get_discount_status(item_price)}")

member_price = calculate_price(50, True)
non_member_price = calculate_price(50, False)
print(f"Member price: ${member_price}")
print(f"Non-member price: ${non_member_price}")

print("\n" + "="*50 + "\n")

# =============================================================================
# TERNARY IN F-STRINGS
# =============================================================================

print("=== Ternary in F-Strings ===")

name = "John"
age = 25
city = "New York"

# Using ternary inside f-string
info = f"{name} is {'an adult' if age >= 18 else 'a minor'} from {city}"
print(info)

# Multiple ternary conditions
score = 85
result = f"Score: {score} ({'Excellent' if score >= 90 else 'Good' if score >= 80 else 'Average' if score >= 70 else 'Poor'})"
print(result)

# Weather example
weather = "sunny"
temperature = 28
advice = f"It's {weather} and {'hot' if temperature > 25 else 'pleasant' if temperature > 15 else 'cold'} at {temperature}°C"
print(advice)

print("\n" + "="*50 + "\n")

# =============================================================================
# TERNARY WITH LISTS AND DATA STRUCTURES
# =============================================================================

print("=== Ternary with Lists ===")

# Create list based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_or_odd = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print("Numbers:", numbers)
print("Even/Odd:", even_or_odd)

# Filter with ternary
grades = [85, 92, 78, 65, 95, 72]
status = ["Pass" if grade >= 70 else "Fail" for grade in grades]
print("Grades:", grades)
print("Status:", status)

# Create price categories
prices = [25, 150, 75, 200, 50, 120]
categories = ["High" if price > 100 else "Medium" if price > 50 else "Low" for price in prices]
print("Prices:", prices)
print("Categories:", categories)

print("\n" + "="*50 + "\n")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("=== Practical Examples ===")

# Example 1: User authentication
print("Example 1: User Authentication")
is_logged_in = True
username = "JohnDoe"
welcome_message = f"Welcome back, {username}!" if is_logged_in else "Please log in"
print(welcome_message)

# Example 2: Product availability
print("\nExample 2: Product Availability")
stock = 15
product_status = f"In Stock ({stock} available)" if stock > 0 else "Out of Stock"
print(f"Product Status: {product_status}")

# Example 3: File size formatting
print("\nExample 3: File Size Formatting")
file_size_bytes = 2048
size_category = "Large" if file_size_bytes > 1000000 else "Medium" if file_size_bytes > 1000 else "Small"
print(f"File size: {file_size_bytes} bytes ({size_category})")

# Example 4: Time of day greeting
print("\nExample 4: Time Greeting")
current_hour = 14  # 2 PM
greeting = ("Good Morning" if current_hour < 12 else 
           "Good Afternoon" if current_hour < 18 else 
           "Good Evening")
print(f"Current hour: {current_hour}")
print(f"Greeting: {greeting}")

print("\n" + "="*50 + "\n")

# =============================================================================
# COMPARISON: TRADITIONAL VS TERNARY
# =============================================================================

print("=== Traditional If-Else vs Ternary ===")

# Traditional approach
print("Traditional If-Else:")
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score}: Grade {grade}")

# Ternary approach (for simple cases)
print("\nTernary (simple case):")
status = "Pass" if score >= 60 else "Fail"
print(f"Score {score}: {status}")

print("\n" + "="*50 + "\n")

# =============================================================================
# BEST PRACTICES AND WHEN TO USE
# =============================================================================

print("""
📚 TERNARY OPERATOR BEST PRACTICES:

✅ GOOD USE CASES:
- Simple if-else conditions
- Assigning values based on conditions
- Inside f-strings for formatting
- List comprehensions with conditions
- Function return values

❌ AVOID WHEN:
- Complex conditions with multiple elif
- Nested ternary operators (hard to read)
- Long expressions
- When readability suffers

SYNTAX:
value_if_true if condition else value_if_false

NESTED TERNARY:
value1 if condition1 else value2 if condition2 else value3

💡 TIPS:
- Keep it simple and readable
- Use parentheses for complex conditions
- Consider traditional if-else for complex logic
- Great for one-liners and simple assignments
""")

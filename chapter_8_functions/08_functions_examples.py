"""
========================================
CHAPTER 8: FUNCTIONS - SIMPLE EXAMPLES
========================================

Simple examples showing how functions solve common problems.
Using only concepts we've covered so far.
"""

# =============================================================================
# 1. MATHEMATICAL OPERATIONS
# =============================================================================

def add_numbers(num1, num2):
    """Add two numbers and return the result"""
    return num1 + num2

def calculate_average(*numbers):
    """Calculate average of multiple numbers"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print("=== 1. Mathematical Operations ===")
print("10 + 20 =", add_numbers(10, 20))
print("Average of [10, 20, 30, 40, 50] =", calculate_average(10, 20, 30, 40, 50))

print("\n" + "="*50 + "\n")

# =============================================================================
# 2. STRING OPERATIONS
# =============================================================================

def count_spaces(text):
    """Count the number of spaces in a string"""
    return text.count(" ")

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def space_remover(text):
    """Remove spaces from a string"""
    return text.replace(" ", "")

def space_replacer(text, replacement):
    """Replace spaces with a specified character"""
    return text.replace(" ", replacement)

print("=== 2. String Operations ===")
test_string = "Hello World I AM Here"
print("Original:", test_string)
print("Spaces:", count_spaces(test_string))
print("Reversed:", reverse_string(test_string))
print("Without spaces:", space_remover(test_string))
print("With hyphens:", space_replacer(test_string, "-"))
print("With asterisks:", space_replacer(test_string, "*"))
print("\n" + "="*50 + "\n")

# =============================================================================
# 3. NUMBER ANALYSIS
# =============================================================================

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def get_number_type(number):
    """Get information about a number"""
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive" + (" Even" if is_even(number) else " Odd")
    else:
        return "Negative" + (" Even" if is_even(number) else " Odd")

print("=== 3. Number Analysis ===")
test_numbers = [0, 5, 8, -3, -10]
for num in test_numbers:
    print(num, ":", get_number_type(num))

print("\n" + "="*50 + "\n")

# =============================================================================
# 4. BUSINESS CALCULATIONS
# =============================================================================

def apply_discount(price, discount_percentage):
    """Apply discount to a price and return final price"""
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price

print("=== 4. Business Calculations ===")
original_price = 1000
discount = 10  # 10%

print("Original Price: $", original_price)
print("After", discount, "% discount: $", apply_discount(original_price, discount))

print("\n" + "="*50 + "\n")

# =============================================================================
# 5. SIMPLE INPUT/OUTPUT
# =============================================================================

def greeting_name(name):
    """Greet a person by name"""
    print("Hello", name)

print("=== 5. Simple Input/Output ===")
greeting_name("Alice")
greeting_name("Bob")

# Example with user input (uncomment to test):
# user_name = input("Enter your name: ")
# greeting_name(user_name)

print("\n" + "="*50 + "\n")

# =============================================================================
# 6. LIST OPERATIONS
# =============================================================================

def find_even_numbers(numbers):
    """Find all even numbers in a list"""
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def square_list_numbers(numbers):
    """Square all numbers in a list"""
    squared = []
    for num in numbers:
        squared.append(num * num)
    return squared

print("=== 6. List Operations ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original list:", numbers)
print("Even numbers:", find_even_numbers(numbers))
print("Squared numbers:", square_list_numbers(numbers))

print("\n" + "="*50 + "\n")

# =============================================================================
# 7. UTILITY FUNCTIONS
# =============================================================================

def square(number):
    """Calculate square of a number"""
    return number * number

def cube(number):
    """Calculate cube of a number"""
    return number * number * number

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

print("=== 7. Utility Functions ===")
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))

print("\n" + "="*50 + "\n")

# =============================================================================
# SUMMARY
# =============================================================================

print("""
📚 SUMMARY - Simple Examples:

1. **Mathematical Operations**: Addition, average calculation
2. **String Operations**: Counting spaces, reversing strings
3. **Number Analysis**: Even/odd, positive/negative
4. **Business Calculations**: Simple discount calculations
5. **Input/Output**: Basic greeting functions
6. **List Operations**: Finding even numbers, squaring numbers
7. **Utility Functions**: Math operations, temperature conversion

🎯 KEY TAKEAWAYS:
- Functions solve specific, reusable problems
- Good functions have single responsibilities
- Return values make functions flexible
- Functions can work with different data types
- Start simple and build up complexity
""")

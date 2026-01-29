"""
========================================
CHAPTER 8: FUNCTIONS - BASICS
========================================

What is a Function?
- A block of code that performs a specific task
- Makes code reusable
- Must be defined before called

Basic Syntax:
def function_name():
    # code block
    pass

function_name()  # Calling the function
"""

# =============================================================================
# 1. BASIC FUNCTION - NO PARAMETERS
# =============================================================================

def say_hello():
    """Simple function that prints a greeting"""
    print("Hello, World!")

print("=== 1. Basic Function ===")
say_hello()  # Output: Hello, World!
say_hello()  # Can be called multiple times

print("\n" + "="*50 + "\n")

# =============================================================================
# 2. FUNCTION WITH PARAMETERS
# =============================================================================

def greet_person(name):
    """Function that takes a name parameter"""
    print("Hello", name)

print("=== 2. Function with Parameters ===")
greet_person("Alice")   # Output: Hello Alice
greet_person("Bob")     # Output: Hello Bob

# What happens if we call without argument?
# greet_person()  # This would raise: TypeError: missing 1 required positional argument

print("\n" + "="*50 + "\n")

# =============================================================================
# 3. FUNCTION WITH DEFAULT PARAMETERS
# =============================================================================

def greet_with_default(name="Guest"):
    """Function with default parameter value"""
    print("Hello", name)

print("=== 3. Function with Default Parameters ===")
greet_with_default()        # Output: Hello Guest (uses default)
greet_with_default("John")   # Output: Hello John (uses provided value)

print("\n" + "="*50 + "\n")

# =============================================================================
# 4. FUNCTION WITH MULTIPLE PARAMETERS
# =============================================================================

def introduce_person(name, age):
    """Function with multiple parameters"""
    print("Hello", name, "you are", age, "years old")

print("=== 4. Function with Multiple Parameters ===")
introduce_person("Sarah", 25)
introduce_person("Mike", 30)

print("\n" + "="*50 + "\n")

# =============================================================================
# 5. FUNCTION WITH ARBITRARY NUMBER OF PARAMETERS (*args)
# =============================================================================

def sum_all(*numbers):
    """Function that accepts any number of arguments"""
    print("Numbers:", numbers)
    total = sum(numbers)
    print("Sum:", total)
    return total

print("=== 5. Function with *args ===")
result1 = sum_all(1, 2, 3)           # Numbers: (1, 2, 3), Sum: 6
result2 = sum_all(10, 20, 30, 40)    # Numbers: (10, 20, 30, 40), Sum: 100

print("\n" + "="*50 + "\n")

# =============================================================================
# 6. FUNCTION WITH RETURN VALUES
# =============================================================================

def add_numbers(a, b):
    """Function that returns a value"""
    result = a + b
    return result

def multiply_numbers(a, b):
    """Function that returns multiplication result"""
    return a * b

print("=== 6. Functions with Return Values ===")
sum_result = add_numbers(5, 3)
product_result = multiply_numbers(4, 7)

print("Sum:", sum_result)        # Output: Sum: 8
print("Product:", product_result) # Output: Product: 28

print("\n" + "="*50 + "\n")

# =============================================================================
# SUMMARY
# =============================================================================

print("""
📚 SUMMARY - Function Basics:

1. **Basic Function**: No parameters, simple execution
2. **Parameters**: Pass values to functions for customization
3. **Default Parameters**: Provide fallback values
4. **Multiple Parameters**: Handle multiple inputs
5. ***args**: Accept unlimited positional arguments
6. **Return Values**: Send results back to caller

🎯 KEY POINTS:
- Functions must be defined before called
- Parameters are variables in function definition
- Arguments are actual values passed to function
- Use return to send values back
- Functions make code reusable and organized
""")

"""
========================================
CHAPTER 8: FUNCTIONS - PRACTICE EXERCISES
========================================

Practice exercises to reinforce your understanding of Python functions.
Try to solve these problems on your own first!
"""

# =============================================================================
# EXERCISE 1: BASIC FUNCTION CREATION
# =============================================================================

# TODO: Create a function called 'print_welcome' that prints "Welcome to Python!"
def print_welcome():
    print("Weclome to Python!")

# TODO: Create a function called 'print_goodbye' that prints "Goodbye!"
def print_goodbye():
    print("Goodbye!")

print("=== Exercise 1: Basic Function Creation ===")
print("Testing your functions:")
print_welcome()  # Uncomment to test
print_goodbye()  # Uncomment to test

print("\n" + "="*50 + "\n")

# =============================================================================
# EXERCISE 2: FUNCTIONS WITH PARAMETERS
# =============================================================================

# TODO: Create a function that takes a name and prints "Hello, [name]!"
def greet_user(name):
    print(f"Hello, {name}!")

# TODO: Create a function that takes two numbers and prints their sum
def add_and_print(a, b):
    print(f"{a} + {b} = {a + b}")

# TODO: Create a function that takes a number and prints its square
def print_square(number):
    print(f"{number} squared = {number * number}")

print("=== Exercise 2: Functions with Parameters ===")
print("Testing your functions:")
greet_user("Alice")  # Uncomment to test
add_and_print(5, 3)   # Uncomment to test
print_square(4)       # Uncomment to test

print("\n" + "="*50 + "\n")

# =============================================================================
# EXERCISE 3: FUNCTIONS WITH RETURN VALUES
# =============================================================================

# TODO: Create a function that takes two numbers and returns their sum
def add_numbers(a, b):
    return a + b

# TODO: Create a function that takes a number and returns its square
def square_number(number):
    return number * number

# TODO: Create a function that takes a string and returns its length
def string_length(text):
    return len(text)

print("=== Exercise 3: Functions with Return Values ===")
print("Testing your functions:")
result1 = add_numbers(10, 20)        # Uncomment to test
result2 = square_number(5)          # Uncomment to test
result3 = string_length("Hello")    # Uncomment to test
print("10 + 20 =", result1)       # Uncomment to test
print("5 squared =", result2)      # Uncomment to test
print("Length of 'Hello' =", result3)  # Uncomment to test

print("\n" + "="*50 + "\n")

# =============================================================================
# EXERCISE 4: FUNCTIONS WITH DEFAULT PARAMETERS
# =============================================================================

# TODO: Create a function that greets with a default name "Guest"
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

# TODO: Create a function that calculates area with default width=10
def calculate_area(length, width=10):
    return length * width

print("=== Exercise 4: Functions with Default Parameters ===")
print("Testing your functions:")
greet_with_default()           # Uncomment to test
greet_with_default("John")     # Uncomment to test
area1 = calculate_area(5)      # Uncomment to test
area2 = calculate_area(5, 3)    # Uncomment to test
print("Area 1:", area1)      # Uncomment to test
print("Area 2:", area2)      # Uncomment to test

print("\n" + "="*50 + "\n")

# =============================================================================
# EXERCISE 5: FUNCTIONS WITH *args
# =============================================================================

# TODO: Create a function that takes any number of arguments and returns their sum
def sum_all(*numbers):
    return sum(numbers)

# TODO: Create a function that takes any number of arguments and returns the maximum
def find_max(*numbers):
    return max(numbers)

print("=== Exercise 5: Functions with *args ===")
print("Testing your functions:")
sum_result = sum_all(1, 2, 3, 4, 5)           # Uncomment to test
max_result = find_max(10, 5, 20, 15)           # Uncomment to test
print("Sum:", sum_result)                    # Uncomment to test
print("Max:", max_result)                    # Uncomment to test

print("\n" + "="*50 + "\n")

# =============================================================================
# EXERCISE 6: SIMPLE PRACTICAL PROBLEMS
# =============================================================================

# TODO: Create a function that checks if a number is even and returns True/False
def is_even(number):
    return number % 2 == 0

# TODO: Create a function that converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# TODO: Create a function that counts spaces in a string
def count_spaces(text):
    pass  # Remove 'pass' and add your code

# TODO: Create a function that reverses a string
def reverse_string(text):
    pass  # Remove 'pass' and add your code

print("=== Exercise 6: Simple Practical Problems ===")
print("Testing your functions:")
even_check = is_even(4)                    # Uncomment to test
temp_f = celsius_to_fahrenheit(25)        # Uncomment to test
space_count = count_spaces("Hello World") # Uncomment to test
reversed_text = reverse_string("Python")  # Uncomment to test
print("Is 4 even?", even_check)          # Uncomment to test
print("25°C =", temp_f, "°F")                # Uncomment to test
print("Spaces in 'Hello World':", space_count)  # Uncomment to test
print("Reversed 'Python':", reversed_text)      # Uncomment to test

print("\n" + "="*50 + "\n")

# =============================================================================
# SOLUTIONS (Check your answers here)
# =============================================================================

print("""
🎯 SOLUTIONS (for reference only - try to solve yourself first!)

Exercise 1:
def print_welcome():
    print("Welcome to Python!")

def print_goodbye():
    print("Goodbye!")

Exercise 2:
def greet_user(name):
    print("Hello", name)

def add_and_print(a, b):
    print(a + b)

def print_square(number):
    print(number * number)

Exercise 3:
def add_numbers(a, b):
    return a + b

def square_number(number):
    return number * number

def string_length(text):
    return len(text)

Exercise 4:
def greet_with_default(name="Guest"):
    print("Hello", name)

def calculate_area(length, width=10):
    return length * width

Exercise 5:
def sum_all(*numbers):
    return sum(numbers)

def find_max(*numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

Exercise 6:
def is_even(number):
    return number % 2 == 0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def count_spaces(text):
    return text.count(" ")

def reverse_string(text):
    return text[::-1]
""")

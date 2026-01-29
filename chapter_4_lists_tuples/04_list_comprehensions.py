"""
========================================
LIST COMPREHENSIONS
========================================

List comprehensions provide a concise way to create lists.
They are more readable and often faster than using loops.
"""

# =============================================================================
# BASIC LIST COMPREHENSION SYNTAX
# =============================================================================

print("=== Basic List Comprehension ===")

# Traditional way with loop
numbers = []
for i in range(1, 6):
    numbers.append(i * 2)
print("Traditional loop:", numbers)

# List comprehension way
numbers_comp = [i * 2 for i in range(1, 6)]
print("List comprehension:", numbers_comp)

print("\n" + "="*50 + "\n")

# =============================================================================
# MORE EXAMPLES
# =============================================================================

print("=== More Examples ===")

# Squares of numbers
squares = [x ** 2 for x in range(1, 11)]
print("Squares 1-10:", squares)

# Cube of numbers
cubes = [x ** 3 for x in range(1, 6)]
print("Cubes 1-5:", cubes)

# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print("Uppercase:", uppercase)

# Calculate prices with tax
prices = [10, 20, 30, 40]
with_tax = [price * 1.08 for price in prices]  # 8% tax
print("Prices:", prices)
print("With 8% tax:", [round(price, 2) for price in with_tax])

print("\n" + "="*50 + "\n")

# =============================================================================
# LIST COMPREHENSION WITH CONDITIONS
# =============================================================================

print("=== List Comprehension with Conditions ===")

# Even numbers only
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers 1-20:", even_numbers)

# Odd numbers only
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print("Odd numbers 1-20:", odd_numbers)

# Numbers greater than 5
numbers = [1, 3, 5, 7, 9, 11, 13]
greater_than_5 = [x for x in numbers if x > 5]
print("Numbers > 5:", greater_than_5)

# Words longer than 4 characters
words = ["cat", "dog", "elephant", "bird", "python"]
long_words = [word for word in words if len(word) > 4]
print("Long words:", long_words)

print("\n" + "="*50 + "\n")

# =============================================================================
# IF-ELSE IN LIST COMPREHENSIONS
# =============================================================================

print("=== If-Else in List Comprehensions ===")

# Classify numbers as even or odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
classification = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Numbers:", numbers)
print("Classification:", classification)

# Grade classification
scores = [85, 92, 78, 65, 95, 72]
grades = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" for score in scores]
print("Scores:", scores)
print("Grades:", grades)

# Temperature classification
temperatures = [15, 25, 35, 45, 5]
temp_classification = ["Cold" if temp < 20 else "Warm" if temp < 30 else "Hot" for temp in temperatures]
print("Temperatures:", temperatures)
print("Classification:", temp_classification)

print("\n" + "="*50 + "\n")

# =============================================================================
# NESTED LIST COMPREHENSIONS
# =============================================================================

print("=== Nested List Comprehensions ===")

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Matrix:", matrix)
print("Flattened:", flattened)

# Create multiplication table
multiplication_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table 3x3:")
for row in multiplication_table:
    print(row)

print("\n" + "="*50 + "\n")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("=== Practical Examples ===")

# Example 1: Process student grades
print("Example 1: Student Grades")
student_grades = [85, 92, 78, 65, 95, 88, 72, 90]

# Filter passing grades (>= 70)
passing_grades = [grade for grade in student_grades if grade >= 70]
print(f"All grades: {student_grades}")
print(f"Passing grades: {passing_grades}")
print(f"Average: {round(sum(passing_grades) / len(passing_grades), 2)}")

# Example 2: Filter and transform products
print("\nExample 2: Product Processing")
products = [
    {"name": "Laptop", "price": 999, "category": "Electronics"},
    {"name": "Book", "price": 25, "category": "Education"},
    {"name": "Coffee", "price": 5, "category": "Food"},
    {"name": "Mouse", "price": 25, "category": "Electronics"}
]

# Get names of products under $50
affordable_products = [product["name"] for product in products if product["price"] < 50]
print(f"Products under $50: {affordable_products}")

# Example 3: Text processing
print("\nExample 3: Text Processing")
sentence = "Python is a powerful and versatile programming language"
words = sentence.split()
word_lengths = [len(word) for word in words]
print(f"Sentence: '{sentence}'")
print(f"Words: {words}")
print(f"Word lengths: {word_lengths}")

# Words longer than 4 characters
long_words = [word for word in words if len(word) > 4]
print(f"Long words (>4 chars): {long_words}")

print("\n" + "="*50 + "\n")

# =============================================================================
# COMPARISON: TRADITIONAL VS COMPREHENSION
# =============================================================================

print("=== Traditional Loop vs List Comprehension ===")

# Traditional approach
print("Traditional Loop:")
traditional_result = []
for i in range(1, 11):
    if i % 2 == 0:
        traditional_result.append(i ** 2)
print("Result:", traditional_result)

# List comprehension approach
print("List Comprehension:")
comprehension_result = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("Result:", comprehension_result)

print("Both methods produce the same result!")

print("\n" + "="*50 + "\n")

# =============================================================================
# SUMMARY
# =============================================================================

print("""
📚 LIST COMPREHENSION SUMMARY:

**Basic Syntax:**
[expression for item in iterable]

**With Condition:**
[expression for item in iterable if condition]

**With If-Else:**
[expression_if_true if condition else expression_if_false for item in iterable]

**Nested:**
[expression for outer in outer_iterable for inner in inner_iterable]

**Common Use Cases:**
- Transform data: [x * 2 for x in numbers]
- Filter data: [x for x in numbers if x > 5]
- Both: [x * 2 for x in numbers if x > 5]
- Classification: ["Even" if x % 2 == 0 else "Odd" for x in numbers]

💡 BENEFITS:
- More concise and readable
- Often faster than loops
- Expressive and Pythonic
- Less code, same functionality

⚠️ WHEN TO USE:
- Simple transformations and filters
- When logic is straightforward
- For readability and maintainability
- Avoid complex nested comprehensions
""")

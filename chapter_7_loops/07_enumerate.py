"""
========================================
ENUMERATE FUNCTION
========================================

The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
This is useful when you need both the index and the value when looping.
"""

# =============================================================================
# BASIC ENUMERATE USAGE
# =============================================================================

print("=== Basic Enumerate Usage ===")

fruits = ["apple", "banana", "cherry", "orange"]

# Traditional way with range
print("Traditional way with range:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Using enumerate
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n" + "="*50 + "\n")

# =============================================================================
# ENUMERATE WITH START PARAMETER
# =============================================================================

print("=== Enumerate with Start Parameter ===")

# Start counting from 1 instead of 0
print("Starting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Start from any number
print("\nStarting from 100:")
for index, fruit in enumerate(fruits, start=100):
    print(f"{index}: {fruit}")

print("\n" + "="*50 + "\n")

# =============================================================================
# ENUMERATE WITH DIFFERENT DATA TYPES
# =============================================================================

print("=== Enumerate with Different Data Types ===")

# With string
word = "PYTHON"
print("String characters:")
for index, char in enumerate(word):
    print(f"Position {index}: '{char}'")

# With tuple
numbers = (10, 20, 30, 40, 50)
print("\nTuple elements:")
for index, num in enumerate(numbers):
    print(f"Index {index}: {num}")

# With dictionary (iterates over keys)
student = {"name": "John", "age": 25, "grade": "A"}
print("\nDictionary keys:")
for index, key in enumerate(student):
    print(f"{index}: {key} -> {student[key]}")

print("\n" + "="*50 + "\n")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("=== Practical Examples ===")

# Example 1: Numbered list
print("Example 1: Numbered List")
tasks = ["Buy groceries", "Clean house", "Study Python", "Call mom"]
print("To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# Example 2: Find index of specific item
print("\nExample 2: Find Index")
numbers = [5, 12, 8, 3, 15, 9, 20]
target = 15
found_index = -1

for index, num in enumerate(numbers):
    if num == target:
        found_index = index
        break

if found_index != -1:
    print(f"Found {target} at index {found_index}")
else:
    print(f"{target} not found in the list")

# Example 3: Process with index
print("\nExample 3: Process with Index")
scores = [85, 92, 78, 65, 95, 88]
print("Score Analysis:")
for i, score in enumerate(scores):
    status = "Pass" if score >= 70 else "Fail"
    print(f"Student {i+1}: {score} - {status}")

# Example 4: Create numbered output
print("\nExample 4: Numbered Output")
ingredients = ["flour", "sugar", "eggs", "milk", "butter"]
print("Recipe Ingredients:")
for i, ingredient in enumerate(ingredients, start=1):
    print(f"{i}. {ingredient.capitalize()}")

print("\n" + "="*50 + "\n")

# =============================================================================
# ENUMERATE WITH LIST COMPREHENSIONS
# =============================================================================

print("=== Enumerate with List Comprehensions ===")

# Create numbered list
words = ["python", "is", "awesome"]
numbered_words = [f"{i}: {word}" for i, word in enumerate(words, start=1)]
print("Numbered words:", numbered_words)

# Create index-value pairs
numbers = [10, 20, 30, 40]
index_value_pairs = [(i, num) for i, num in enumerate(numbers)]
print("Index-value pairs:", index_value_pairs)

# Filter with enumerate
scores = [85, 92, 78, 65, 95, 88]
high_scores = [(i, score) for i, score in enumerate(scores) if score >= 90]
print("High scores (>=90):", high_scores)

print("\n" + "="*50 + "\n")

# =============================================================================
# ENUMERATE VS TRADITIONAL METHODS
# =============================================================================

print("=== Enumerate vs Traditional Methods ===")

data = ["A", "B", "C", "D"]

# Method 1: Using range and len
print("Method 1: range + len")
for i in range(len(data)):
    print(f"{i}: {data[i]}")

# Method 2: Using enumerate
print("\nMethod 2: enumerate")
for i, item in enumerate(data):
    print(f"{i}: {item}")

# Method 3: Manual counter
print("\nMethod 3: Manual counter")
counter = 0
for item in data:
    print(f"{counter}: {item}")
    counter += 1

print("\nEnumerate is the most Pythonic and readable!")

print("\n" + "="*50 + "\n")

# =============================================================================
# ADVANCED EXAMPLES
# =============================================================================

print("=== Advanced Examples ===")

# Example 1: Find all indices of a value
print("Example 1: Find All Indices")
text = "hello world, hello python"
search_char = "l"
indices = [i for i, char in enumerate(text) if char == search_char]
print(f"Character '{search_char}' found at positions: {indices}")

# Example 2: Parallel processing with enumerate
print("\nExample 2: Parallel Processing")
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35, 28]
print("People:")
for i, name in enumerate(names):
    if i < len(ages):
        print(f"{i+1}. {name} - {ages[i]} years old")

# Example 3: Create dictionary with enumerate
print("\nExample 3: Create Dictionary")
words = ["first", "second", "third", "fourth"]
word_dict = {i: word for i, word in enumerate(words, start=1)}
print("Dictionary:", word_dict)

print("\n" + "="*50 + "\n")

# =============================================================================
# SUMMARY
# =============================================================================

print("""
📚 ENUMERATE FUNCTION SUMMARY:

**Basic Syntax:**
for index, value in enumerate(iterable):
    # code

**With Start Parameter:**
for index, value in enumerate(iterable, start=1):
    # code

**Common Use Cases:**
- Need both index and value in loop
- Creating numbered lists
- Finding positions of items
- Processing with position information
- Creating dictionaries from lists

**Works With:**
- Lists
- Tuples
- Strings
- Dictionaries (iterates over keys)
- Any iterable object

**Benefits:**
- More readable than range(len())
- Automatic index management
- Flexible starting index
- Pythonic and efficient
- Reduces code complexity

💡 REMEMBER:
- enumerate() returns (index, value) pairs
- Default start is 0
- Use start parameter to change beginning number
- Great for numbered output and position-based processing
""")

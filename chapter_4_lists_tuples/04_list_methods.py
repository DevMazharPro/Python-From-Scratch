# List methods

# Add elements
fruits = ["apple", "banana", "orange"]
print("Original list:", fruits)

# Add element to the end
fruits.append("grape")
print("After append:", fruits)

# Add element at specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# Remove elements
fruits.remove("banana")
print("After remove:", fruits)

# Remove element by index
fruits.pop(0)
print("After pop:", fruits)

# Clear all elements
fruits.clear()
print("After clear:", fruits) 

# Sorting
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)

# Sort in ascending order
numbers.sort()
print("Sorted list (ascending):", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Sorted list (descending):", numbers)

# Slice
print(numbers[1:4]) # [34, 25, 12] - Same like string slicing

# Reverse
numbers.reverse()
print("Reversed list:", numbers)

# 3. Finding elements
fruits = ["apple", "banana", "orange", "apple", "grape"]
print("Fruits list:", fruits)

# Find index of an element
index = fruits.index("orange")
print("Index of 'orange':", index)

# Count occurrences of an element
count = fruits.count("apple")
print("Count of 'apple':", count)



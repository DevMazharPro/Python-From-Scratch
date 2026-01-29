# Set Methods

numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
print(numbers)
print(fruits)

# Length of set
print(len(numbers))
print(len(fruits))

# Add an element to the set
numbers.add(6) # If set contain numbers then it will be added in sorted order
print(numbers)

fruits.add("orange") # If set contain strings then it will be added in random order
print(fruits)

# Remove an element from the set
numbers.remove(6)
print(numbers)

# Clear the set
numbers.clear()
print(numbers)


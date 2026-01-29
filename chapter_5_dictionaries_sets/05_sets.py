# Set - Unordered, unchangeable, and do not allow duplicate values
# Set items are unchangeable, but you can remove items and add new items

numbers = {1, 2, 3, 4, 5}
print(numbers)
print(type(numbers))

fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits))

# To create an empty set
empty_set = set()
print(empty_set)
print(type(empty_set))
# empty_set = {} # This is not an empty set, it is an empty dictionary

# Duplicate values are ignored
numbers_with_duplicates = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(numbers_with_duplicates)

# Mixed data types
mixed_set = {1, "apple", 3.14, True}
print(mixed_set)



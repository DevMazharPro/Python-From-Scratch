# Tuple - Immutable list - cannot be changed after creation

# Create a tuple
coordinates = (10, 20)
print(coordinates)

# Access elements
print(coordinates[0])  # 10
print(coordinates[1])  # 20

# Tuples are immutable
# coordinates[0] = 30  # This will raise an error

# Tuple with different data types
mixed_tuple = (1, "hello", True, 3.14)
print(mixed_tuple)

# Tuple with one element
single_tuple = (1,)
print(single_tuple)

# Tuple unpacking
x, y = coordinates
print(x, y)

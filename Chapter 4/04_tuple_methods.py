# Tuple methods

coordinates = (10, 20, 30, 20)
print(len(coordinates))  # 4 - return length of tuple
print(coordinates.count(20))  # 2 - counts how many times 20 appears
print(coordinates.index(30))  # 2 - returns index of first occurrence of 30

# Tuple methods are limited compared to lists
# Common methods: count(), index()

# Other tuple operations
print(min(coordinates))  # 10 - returns minimum value
print(max(coordinates))  # 30 - returns maximum value

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# Repetition
tuple4 = (1, 2) * 3
print(tuple4)  # (1, 2, 1, 2, 1, 2)

# Membership testing
print(20 in coordinates)  # True
print(40 in coordinates)  # False

# Tuple unpacking
x, y, z = (10, 20, 30)
print(x, y, z)  # 10 20 30

# Tuple packing
person = "John", 30, "Engineer"
print(person)  # ('John', 30, 'Engineer')

# Converting between tuple and list
list_from_tuple = list(coordinates)
print(list_from_tuple)  # [10, 20, 30, 20]

tuple_from_list = tuple(list_from_tuple)
print(tuple_from_list)  # (10, 20, 30, 20)

# Tuple with single element (note the comma)
single_tuple = (5,)
print(single_tuple)  # (5,)

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # ()


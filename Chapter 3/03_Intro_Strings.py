# String is data type in Python. Basically a sequence of characters written in quotation marks. 
name = "Mazhar"
number = '123'
print(type(name))
print(type(number))
# Both are same, single or double quotation marks can be used.
# Strings are immutable, i.e., once created, they cannot be changed.
# String indexing starts from 0 from the left and -1 from the right.
print(name[0])
print(name[-1])

# Immutability means that once a string is created, it cannot be changed.
# name[0] = "A" This will raise an error.

# However, we can create a new string by concatenating the old string with another string.
new_name = name + " Ali"
print(new_name)

# String methods
# 1. Slice = Extracting a part of the string [start:stop:step]
# start is inclusive, stop is exclusive, step is optional.
print(name[1:3])  # az
print(name[1:3:2]) # a
print(name[-4:-1]) #zha
print(name[:4]) # Mazh same as name[0:4] 
print(name[2:]) #zahr same as name[2:6] 

# String functions

# len() function
string = "hello World"
print(len(string)) # This returns the length of the string, including spaces, in this case "11".

# upper() function
print(string.upper()) # This returns the string in uppercase.

# lower() function
print(string.lower()) # This returns the string in lowercase.

# capitalize() function
print(string.capitalize()) # This returns the string with the first character in uppercase and the rest in lowercase.

# find() function
print(string.find("World")) # This returns the index of the first occurrence of the substring.

# replace() function
print(string.replace("World", "Universe")) # This returns the string with the first occurrence of the substring replaced with the second argument.

# split() function
print(string.split(" ")) # This returns a list of words in the string.

# endswith() function
print(string.endswith("World")) # This returns True if the string ends with the specified value, otherwise False.

# startswith() function
print(string.startswith("hello")) # This returns True if the string starts with the specified value, otherwise False.

# strip() function
print(string.strip()) # This returns the string with leading and trailing whitespace removed.

# count() function
print(string.count("l")) # This returns the number of occurrences of the substring.

# index() function
print(string.index("World")) # This returns the index of the first occurrence of the substring.

# isalpha() function
print(string.isalpha()) # This returns True if all characters in the string are alphabets, otherwise False.

# isdigit() function
print(string.isdigit()) # This returns True if all characters in the string are digits, otherwise False.

# isalnum() function
print(string.isalnum()) # This returns True if all characters in the string are alphanumeric, otherwise False.



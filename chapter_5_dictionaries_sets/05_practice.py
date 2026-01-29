# Write a program in which you have dictionary of urdu words with values as their english translation
# Provide user with an option to look it up

urdu_to_english = {
    "kitab": "book",
    "kursi": "chair",
    "dost": "friend",
    "dil": "heart",
    "zindagi": "life"
}

word = input("Enter a urdu word: ")
print(urdu_to_english.get(word, "Word not found"))

# Write a program to input eight numbers from the user and display all the unique numbers (once)
numbers = set()
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))
num_4 = int(input("Enter number 4: "))
num_5 = int(input("Enter number 5: "))
num_6 = int(input("Enter number 6: "))
num_7 = int(input("Enter number 7: "))
num_8 = int(input("Enter number 8: "))
numbers.add(num_1)
numbers.add(num_2)
numbers.add(num_3)
numbers.add(num_4)
numbers.add(num_5)
numbers.add(num_6)
numbers.add(num_7)
numbers.add(num_8)
print(numbers)

# Can we have a set with 18 (int) and "18" (str) as a value in it?
set_with_mixed_types = {18, "18"}
print(set_with_mixed_types)

# What will be the length of following set S:
# S = set()
# S.add(20)
# S.add(20.0)
# S.add("20")
# What is S.length?

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) 

"""What is the difference between S.add(20) and S.add(20.0)?
S.add(20) adds an integer 20
S.add(20.0) adds a float 20.0
=> Since 20 == 20.0 in Python, they are considered the same value in the set"""

"""s ={} - What is the type of s?
s = {}
print(type(s)) # Dictionary"""

s = {}
print(type(s)) # Dictionary

# Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
favorite_languages = {}
name_1 = input("Enter friend 1 name: ")
language_1 = input("Enter friend 1 favorite language: ")
name_2 = input("Enter friend 2 name: ")
language_2 = input("Enter friend 2 favorite language: ")
name_3 = input("Enter friend 3 name: ")
language_3 = input("Enter friend 3 favorite language: ")
name_4 = input("Enter friend 4 name: ")
language_4 = input("Enter friend 4 favorite language: ")
favorite_languages[name_1] = language_1
favorite_languages[name_2] = language_2
favorite_languages[name_3] = language_3
favorite_languages[name_4] = language_4
print(favorite_languages)

"""If names of 2 friends are same; what will happen to the program in problem 6?
=> The program will overwrite the value of the first friend with the value of the second friend."""

"""If languages of two friends are same; what will happen to the program in problem 6?
=> The program will not overwrite the value of the first friend with the value of the second friend."""

"""Can you change the values inside a list which is contained in set S?
S = {8, 7, 12, "Harry", [1, 2]}
=> No, you cannot change the values inside a list which is contained in set S because lists are mutable and cannot be elements of a set."""

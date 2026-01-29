# Practice Program 1
print("Twinke Twinke little star")
print("How I wonder what you are")
print("Up above the world so high")
print("Like a diamond in the sky")

# Practice Program 2
# Use REPL and print the table of 5 using it

# Practice Program 3
# Install a external module and use it
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, how are you?")
engine.runAndWait()


# Practice Program 4
# Write a python program to print the contents of a directory using the os module
# Search on google: python module for os 
import os


# Specify the directory path (empty string for current directory)
directory_path = "/"

# Get the list of all files and directories
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)


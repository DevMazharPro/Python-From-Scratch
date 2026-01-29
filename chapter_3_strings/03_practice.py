# Write a program to display a user entered name followed by good afternoon using input function
name = input('Enter your name: ')
print('Good afternoon, ' + name + '!')

# Write a program to fill in a letter template given below with name and date
letter = '''Dear <|name|>,
You are selected!
<date>'''
name = input('Enter your name: ')
date = input('Enter date: ')
print(letter.replace('<|name|>', name).replace('<date>', date))

# Write a program to detect double spaces in a string 
sampleString = "This is a string with double  spaces"
doubleSpaces = sampleString.find("  ")
print(doubleSpaces)

# Write a program to replace double spaces with single space in a string
sampleString = sampleString.replace("  ", " ")
print(sampleString)

# Write a program to format a letter using escape sequence characters
sample = "Hello How are you?"
sampleString = "Hello\nHow are you?"
print(sampleString)


# Practice program for f string
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


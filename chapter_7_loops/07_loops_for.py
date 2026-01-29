# FOR LOOP => it is used when we know how many times we want to execute a block of code - brother of while.

# Syntax => for i in range(start, end, step): => end is exclusive

for i in range(5): # range(5) will generate numbers from 0 to 4
    print(i)

for i in range(1, 11): # range(1, 11) will generate numbers from 1 to 10
    print(i)

for i in range(1, 11, 2): # range(1, 11, 2) odd numbers from 1 to 10
    print(i)
    print("Done")


# List accessing by for-loop

names = ["Mazhar", "Azhar", "Hasnain", "Ayan"]

# Two ways to access list elements

for name in names:
    print(name)


for i in range(len(names)):
    print(names[i])

# If we want to access index and value both 

# Syntax => for i, name in enumerate(names): => i is index and name is value. Enumerate is a built-in function that returns index and value both

for i, name in enumerate(names):
    print(i, name)


# We can access characters of a string by for-loop
for char in "Mazhar":
    print(char)


# for-loop in reverse order
for i in range(5, 0, -1):
    print(i)
    
# for loop with else 
for i in range(5):
    print(i)
else:
    print("Done") # else will execute when the loop is finished
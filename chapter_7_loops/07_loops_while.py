# Loops in Python - used to perform a task multiple times
# 2 types of loops in Python - for loop and while loop

# While Loop => while a condition is true, it will keep on executing and it is used when we don't know how many times we want to execute a block of code 

# Example 1

i = 1 # 1 is starting number which will be printed first - this is important to initialize the value of i
while i <= 10:
    print(i)
    i += 1 # Here += is used to increment the value of i by 1 if we don't use this, the loop will run infinite times
else:
    print("Done") # This will be executed when the condition is false

# if we want to execute a block of code infinite times, we can use while True - 

# Example 2 - print 100 numbers
i = 1 
while i <= 100:
    print(i)
    i += 1
else:
    print("Done")


fruits = ["apple", "banana", "cherry", "orange", "mango"]

i = 0 
n = len(fruits)
while i < n:
    print(fruits[i])
    i += 1
else:
    print("Done")
    
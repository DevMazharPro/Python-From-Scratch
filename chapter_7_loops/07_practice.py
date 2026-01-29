# Write a program to write a multiplication table of a number given by user
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)  

# Write a program to greet all the names in a list, names which start with A
names = ["Mazhar", "Azhar", "Hasnain", "Ayan"]
for name in names:
    if name.startswith("A"):
        print("Hello", name)

# Attempt question 1 by while
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1


# Write a program to find whether the given number is prime or not
n = int(input("Enter a number to check for prime: "))
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

# Write a program to find the sum of first n natural numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum of first", n, "natural numbers is", sum)

# Write a program to find the factorial of a number
n = int(input("Enter a number: "))
factorial = 1 
for i in range(1, n+1):
    factorial *= i   
print("Factorial of", n, "is", factorial) 

# Write a program to print the following pattern
"""
    *
   ***
  *****
 """

nmb = int(input("Enter a number: "))
for i in range(1, nmb+1):
    print(" " * (nmb - i) + "*" * (2 * i - 1))

for i in range(0 , nmb + 1):
    print("*"*i)

for i in range(1, nmb + 1):
    if i == 1  or i == nmb:
        print("*"*nmb)
    else:
        print("*" + " "*(nmb-2) + "*")

# Write a program to print a multiplication table of n but in reverse order
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(n, "x", i, "=", n * i)
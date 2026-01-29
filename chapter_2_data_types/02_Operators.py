# Operators in Python
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators


# Arithmetic contain +, -, *, /, %, **, //
a = 10
b = 20
print(a + b) # 30 (addition)
print(a - b) # -10 (subtraction)
print(a * b) # 200 (multiplication)
print(a / b) # 0.5 (division)
print(a % b) # 10 (modulo = remainder)
print(a ** b) # 10^20 (exponentiation)
print(a // b) # 0 (floor division = quotient)

# Assignment Operator =, +=, -=, *=, /=, %=, //=, **=
x = 5 # assignment
print(x) # 5
x += 3 # addition assignment
print(x) # 8
x -= 3 # subtraction assignment
print(x) # 5
x *= 3 # multiplication assignment
print(x) # 15
x /= 3 # division assignment
print(x) # 5.0
x %= 3 # modulo assignment
print(x) # 2.0
x //= 3 # floor division assignment
print(x) # 0.0
x **= 3 # exponentiation assignment
print(x) # 0.0

# Comparison Operators ==, !=, >, <, >=, <=. These operators returns boolean values (True or False)
a = 10
b = 20
print(a == b) # False (equal)
print(a != b) # True (not equal)
print(a > b) # False (greater than)
print(a < b) # True (less than)
print(a >= b) # False (greater than or equal)
print(a <= b) # True (less than or equal)

# Logical Operators and, or, not
x = True
y = False
print(x and y) # False (logical and "Both Must be True") 
print(x or y) # True (logical or "At least one must be True")
print(not x) # False (logical not "Negation")
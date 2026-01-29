# We can assign types to values
num = "4"
print(num, type(num)) # This is string not a integer

# But we can convert it into integer or float too
integer_type = int(num)
print(integer_type, type(integer_type)) # This is now integer
float_type = float(integer_type)
print(float_type, type(float_type)) # This is now float 
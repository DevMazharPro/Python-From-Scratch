# Dictionary in Python - Key-Value pairs, Unordered, Mutable, Indexed, No duplicate keys

user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }

print(user, type(user))
print(user["name"]) # Accessing value by key
print(user["age"]) # Accessing value by key
print(user["isPaid"]) # Accessing value by key

# Dictionary is mutable - we can change the values, 
user["name"] = "Mazhar Khan"
print(user)

user["age"] = 25
print(user)

# We can add new key-value pairs
user["city"] = "Karachi"
print(user)

# We can delete key-value pairs
del user["city"]
print(user)

# We can check if a key exists in the dictionary
if "name" in user:
    print("Name exists in the dictionary")
else:
    print("Name does not exist in the dictionary")

# We can get all the keys in the dictionary
print(user.keys())

# We can get all the values in the dictionary
print(user.values())

# We can get all the key-value pairs in the dictionary
print(user.items())



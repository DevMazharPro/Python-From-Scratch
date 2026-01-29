# Dictionary Methods

# clear() - Removes all the elements from the dictionary
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
user.clear()
print(user)

# copy() - Returns a copy of the dictionary
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
user_copy = user.copy()
print(user_copy)

# fromkeys() - Returns a dictionary with the specified keys and value
keys = ["name", "age", "isPaid"]
value = "Unknown"
user_fromkeys = dict.fromkeys(keys, value)
print(user_fromkeys)

# get() - Returns the value of the specified key if it exists, otherwise returns None or a default value
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
print(user.get("name"))

# items() - Returns a list containing a tuple for each key value pair
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
print(user.items())

# keys() - Returns a list containing the dictionary's keys
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
print(user.keys())

# pop() - Removes the element with the specified key
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
user.pop("name")
print(user)

# popitem() - Removes the last inserted key-value pair
user = {
    "name" : "Mazhar",
    "age" : 24,
    "isPaid" : True
    }
print(user)
user.popitem()
print(user)

# setdefault() - Returns the value of the specified key if it exists, otherwise inserts the key with the specified value
print(user.setdefault("name", "Unknown"))


# update() - Updates the dictionary with the specified key-value pairs
user.update({"name": "Azhar"})
print(user)

# values() - Returns a list of all the values in the dictionary
print(user.values())

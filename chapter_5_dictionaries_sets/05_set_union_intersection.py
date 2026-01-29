# Set Union and Intersection

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Union of two sets
print(s1.union(s2)) # All elements from both sets

# Intersection of two sets
print(s1.intersection(s2)) # Common elements from both sets

# Difference of two sets
print(s1.difference(s2)) # Elements in s1 but not in s2

# Symmetric difference of two sets
print(s1.symmetric_difference(s2)) # Elements in either set but not in both

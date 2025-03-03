myTuple = (1, "Hello", True, 3.14, [1, 2, 3])
print(myTuple)

# Accessing values in tuple
print("\nAccessing values in tuple")
print(myTuple[0])   # Output : 1, zero-based indexing
print(myTuple[3])   # Output : 3.14
print(myTuple[-1])  # Output : [1, 2, 3], Print tuple from last

# Deleting values in tuple
print("\nDeleting values in tuple")
# del myTuple[0]      # this will raise an error
# myTuple.remove(3.14) # this alse will raise an error

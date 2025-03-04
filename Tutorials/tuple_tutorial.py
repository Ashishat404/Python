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
# Instead you can reasign the value in the tuple
myTuple = (2, True, 3.14, [1, 2, 3])

# Updating tuple
print("\nUpdating tuple")
# can bedone by converting the tuple to list and then updating the list
myTuple = list(myTuple)
myTuple[1] = "Welcome"
myTuple = tuple(myTuple)
print(myTuple)       # Output : (2, "Welcome", 3.14, [1, 2, 3])
# Basic tuple operations
print("\nBasic tuple operations")
print("Length of tuple : ", len(myTuple))    # Output : 4
print("\n Adding Tuple: ")
print(myTuple + (4, 5, 6))  # Output : (2, "Welcome", 3.14, [1, 2, 3], 4, 5, 6)
print("\n Repetation of Tuple: ")
print(myTuple * 3)   # Output : (2, "Welcome", 3.14, [1, 2, 3], 2, "Welcome", 3.14, [1, 2, 3], 2, "Welcome", 3.14, [1, 2, 3])
print("\n Membership check: ")
print(3.14 in myTuple)   # Output : True
print(3 in myTuple)      # Output : False
#Tuple packing and unpacking
print("\nTuple packing and unpacking")
myTuple = (1, "Hello", True, 3.14, [1, 2, 3])
x, y, z, w, v = myTuple
print(x, y, z, w, v)    # Output : 1 Hello True 3.14 [1, 2, 3]
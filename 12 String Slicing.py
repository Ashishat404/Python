names = "harry,ashish"
fruit = "mango"
print(names[0:5])       # prints the length including 0 but not 5 
print(len(names))       # Gives the length of a string 
print(fruit[0:4])       # prints the length including 0 but not 4

#Negative slicing 
print(fruit[:-3])                 #Python always includes len(fruit) -3 automatically
print(fruit[0:len(fruit)-3])

print(fruit[-3:-1])

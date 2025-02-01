
# strings are immutable in python
a="!Ashish!!! Ashish"
b="John"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))  # The Exclamation marks are stripped (Trailing characters only)

# replace -> Replacing of Characters (all teh occurance are changed)
print(a.replace("Ashish","John"))
print(a.replace("Ashish",b))

# split -> splits the lists into parts as per the no. of spaces present in it.
print(a.split(" "))

# capitalize -> the first character of string is converted to an uppercase and the others are turned into lowercase
# if first is already an uppercase then no effect
boldheading="introduction to pYthon"
print(boldheading.capitalize())

# center -> The center meathod aligns the strings to the center as the parameter given
str1 = "Welcome to Console!!!"
print(len(str1))
print(len(str1.center(50)))

# count -> The Count meathod returns the number of times the given value has occured within the string
print(a.count("Ashish"))

# endswith -> It checks weather the given string ends with a given value 
# replies with either true or false
str1 = "Welcome to Console"
print(str1.endswith("!!!"))


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

str1 = "Welcome to Console"
print(str1.endswith("to",4,10))

# find -> this searches for the first occurrence
str1 = "He,s name is dan. he is a honest man"
print(str1.find("is"))

# index -> if not found it raises an exception
#  ValueError: substring not found 
str1 = "He,s name is dan. he is a honest man"
# print(str1.index("iss"))    # will surely give error iss not present 

# isalnum -> to check weather the series is alpha numeric A-Z , a-z , 0-9 , if any other are present it returns false
str1= "WelcomeToTheConsole"
print(str1.isalnum())

# isalpha -> if the entire string only consists of A-Z , a-z 
# if the punctuations like(0-9) are present then returns false
str1 = "Welcome"
print(str1.isalpha())

# islower -> returns true if all characters are in smallcase , Otherwise False
str1 = "Welcome"
print(str1.islower())

# isprintable -> returns true if all the values given string are printable , if not then return false
str1 = "Happy New Year\n"   # \n is not a printable character  
print(str1.isprintable())

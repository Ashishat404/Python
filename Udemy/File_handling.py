#creating a file

f= open("test.txt" , "w") 
f.write("Welcome to python programming") 
f.close() 

# reading a file
f = open("test.txt", "r")
print(f.read())
f.close()

# appending a file
f = open("test.txt", "a")
f.write("\nHello World")
f.close()

# deleting a file
import os
os.remove("test.txt")

# checking if a file exists
import os

if os.path.exists("test.txt"):
    print("File exists")
else:
    print("File does not exist")
    
#Renaming a File
import os 
if os.path.exists("test"):
    print("file exists")
else:
    print("file does not exist")

#Renaming a file 

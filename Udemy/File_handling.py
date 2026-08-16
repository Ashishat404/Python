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


# renaming a file
import os
os.rename("test.txt", "test1.txt")

# copying a file
import shutil
shutil.copy("test1.txt", "test2.txt")

# moving a file
import shutil
shutil.move("test2.txt", "test3.txt")

# creating a directory
import os
os.mkdir("test4")

# removing files in a directory
import os 
os.mkdir("test4")

#listening files in directory 
import os
files = os.listendir()
print(files)

#getting the current working directory

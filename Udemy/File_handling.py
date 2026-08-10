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

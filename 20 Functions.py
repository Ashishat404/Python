def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
   if(a>b):
    print("First number is greater")
   else:
    print("Second number is greater")
         
def isLesser(a,b):
    pass      # The pass resolves the indentation error which can also be defined later , it's a user-defined function

a= 3
b= 5
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater")  --> This prints the greater number but instead of this we can write this
    
# gmean1 = a*b/(a+b)
# print(gmean1)         --> Instead of writing this we can write 
calculateGmean(a,b)
isGreater(a,b)

c=8
d=7
# if(c>d):
#     print("FIrst number is greater")
# else:
#     print("Second number is greater")

# gmean2= c*d/(c+d)
# print(gmean2)
calculateGmean(c,d)
isGreater(c,d)

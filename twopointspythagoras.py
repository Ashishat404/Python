# Online Python - IDE, Editor, Compiler, Interpreter
import math as m
def dis(a, b):
    xdiff=a[0]-b[0]
    ydiff=a[1]-b[1]
    dis=m.sqrt(xdiff*2 + ydiff*2)
    return dis

a = eval(input('Enter cordinatea number: '))
b = eval(input('Enter 2nd number: '))

print(f'distance of {a} and {b} is {dis(a, b)}')
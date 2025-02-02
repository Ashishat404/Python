
# not completed
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)


timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

if  time.strftime('%H') < 12:
    print("Good Morning")
    
else:
    print("Good Afternoon")

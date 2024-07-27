# Age calculator
# Please enter your birth year

try:
    birth = int(input())
    
    if birth < 1000 or birth > 2024:
        print("Please enter valid birth year.")
    else:
        age = 2024 - birth
        result = "You are " + str(age) + " years old."
        print(result)
except ValueError:
    print("Looks like you enter alphabet, please enter numbers.")

print("\nThank you!")
#Design a simple calculator which has the following functionality:
#add, sub, mul, div, mod, sqrt, log

import math

print("What do you want to do? ")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. mod")
print("6. sqrt")
print("7. log")
choice = int(input('Your choice -> '))

if(choice == 1):
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    res = x + y
elif(choice == 2):
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    res = x - y
elif(choice == 3):
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    res = x * y
elif(choice == 4):
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    res = x / y
elif(choice == 5):
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    res = x % y
elif(choice == 6):
    x = int(input("Enter the number"))
    res = math.sqrt(x)
elif(choice == 7):
    x = int(input("Enter the number"))
    res = math.log(x)

print(res)


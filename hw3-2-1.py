# Author: Nolan (AMDG) 10/6/2021

x = int(input("Input numerical average for quarter 1: "))

if x >= 93:
    print("you got an A!")
elif x <= 92.999 and x >= 90:
    print("you got an A-")
elif x <= 89.999 and x >= 87:
    print("you got a B+")
elif x <= 86.999 and x >= 83:
    print("you got a B")
elif x <= 82.999 and x >= 80:
    print("you got a B-")
elif x <= 79.999 and x >= 77:
    print("you got a C+")
elif x <= 76.999 and x >= 73:
    print("you got a C")
elif x <= 72.999 and x >= 70:
    print("C-")
elif x <= 69.999 and x >= 65:
    print("you got a D+")
elif x <= 64.999 and x >= 60:
    print("you got a D")
elif x <= 59.999:
    print(" you got an F")
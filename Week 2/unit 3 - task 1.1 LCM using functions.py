import math

number1 = int(input("enter number"))
number2 = int(input("enter number"))

def findlcm(number1,number2):
    return(math.lcm(number1,number2))


print(findlcm(number1,number2))
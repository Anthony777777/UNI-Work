#using the python built in modules.
import math
number1 = int(input("enter number"))
number2 = int(input("enter number"))
print(math.lcm(number1,number2))



# using while loops
n = int(input("enter number 1: "))
m = int(input("enter number 2: "))

lcmFound = False
count = 1
while lcmFound == False:
    currentMultiple = count * n
    if (currentMultiple % m) == 0:
        lcm = currentMultiple
        lcmFound = True
    else:
        count += 1

print("The LCM is: ", lcm)
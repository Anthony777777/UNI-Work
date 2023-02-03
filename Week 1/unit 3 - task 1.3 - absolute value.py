#this is the easy way
#absolute value just means how close a number is to zero is can never be negative.
#example -5 is 5 away from 0 : 5 is also 5 away from 0

integer = input("enter a number: ")
print('Absolute value of', int(integer), 'is:', abs(int(integer)))

#this is the way uni wnated us to do it using if statements
number = int(input("Number please: "))
#if number is less than zero run this
if (number) < 0:
#number entered multiplied by -1
    print(number * -1)
else:
#if number is above 0 do this instead
    print(number)

#this is a check agaisnt the 2nd part
print(abs(number))
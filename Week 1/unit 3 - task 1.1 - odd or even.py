# odd or even enter a number and the if statement determines if odd or even
#if a number is divisible by 2 and leaves 0 remainder this is even
# the % is the modulas symbol and shows any remainder is there is any

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(num, "is Even")
else:
   print(num, "is Odd")
number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))

#uses the modulas function to check if any remainders
if (number_1%number_2) == 0:
    print(number_1, "is a multiple of ", number_2 )
else:
    print(number_1, "is not a multiple of ", number_2)
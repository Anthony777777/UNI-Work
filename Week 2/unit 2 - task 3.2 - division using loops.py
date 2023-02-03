numberN = int(input("big number: "))
numberM = int(input("divide by smaller number "))

numberNSubtract = numberN
numberOfSubtractions = 0


while numberNSubtract > 0:
    numberNSubtract = numberNSubtract - numberM
    numberOfSubtractions += 1


print(numberOfSubtractions)
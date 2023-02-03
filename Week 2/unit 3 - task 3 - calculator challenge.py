userentry = str(input("what calculation would you like to process: "))
calculationList = [entries for entries in userentry]
operators = ["+", "-", "/", "*", " "]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


if any(value not in (numbers+operators) for value in calculationList):
    print("error")
else:
    print(eval(userentry))
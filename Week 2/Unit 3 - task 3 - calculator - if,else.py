# this uses if and else and while loops to implement a claculator

extra = []
Operation = int(input("Please select a operator: "
                         "\n 1: Addition "
                         "\n 2: Subtraction "
                         "\n 3: Multiplication "
                         "\n 4: Division "
                         "\n"))

while Operation > 4:
    print("Please Select a value shown below")
    Operation = int(input("Please select a operator: "
                            "\n 1: Addition "
                            "\n 2: Subtraction "
                            "\n 3: Multiplication "
                            "\n 4: Division "
                            "\n"))
firstnumber = input("please enter the first number ")
secondnumber = input("please enter a second number ")
addition = int(firstnumber) + int(secondnumber)
subtraction = int(firstnumber) - int(secondnumber)
Multiplication = int(firstnumber) ** int(secondnumber)
division = int(firstnumber) // int(secondnumber)

if Operation == int("1"):
    print(addition)
elif Operation == int("2"):
    print(subtraction)
elif Operation == int("3"):
    print(Multiplication)
elif Operation == int("4"):
    print(division)
else:
    print("error")

extra = input("would you like to do another eqaution? (y/n)")
while extra == "y":
    Operation = int(input("Please select a operator: "
                          "\n 1: Addition "
                          "\n 2: Subtraction "
                          "\n 3: Multiplication "
                          "\n 4: Division "
                          "\n"))
    while Operation > 4:
        print("Please Select a value shown below")
        Operation = int(input("Please select a operator: "
                              "\n 1: Addition "
                              "\n 2: Subtraction "
                              "\n 3: Multiplication "
                              "\n 4: Division "
                              "\n"))

    firstnumber = input("please enter the first number ")
    secondnumber = input("please enter a second number ")

    if Operation == int("1"):
        print(addition)
    elif Operation == int("2"):
        print(subtraction)
    elif Operation == int("3"):
        print(Multiplication)
    elif Operation == int("4"):
        print(division)
    else:
        print("error")
    extra = input("would you like to do another eqaution? (y/n)")
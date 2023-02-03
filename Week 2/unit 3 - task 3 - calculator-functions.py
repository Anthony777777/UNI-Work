# addition function
def addition(number1,number2):
    return (number1+number2)

#subtration function
def subtraction(number1,number2):
    return (number1-number2)

#multiplication
def multiplication(number1,number2):
    return (number1*number2)

#division
def division (number1,number2):
    return (number1/number2)
extra= []
number1 = float(input("first number "))
number2 = float(input("second number "))

function = int(input("Please select a operator: "
                            "\n 1: Addition "
                            "\n 2: Subtraction "
                            "\n 3: Multiplication "
                            "\n 4: Division "
                            "\n"))
while function > 4:
        print("Please Select a value shown below")
        function = int(input("Please select a operator: "
                              "\n 1: Addition "
                              "\n 2: Subtraction "
                              "\n 3: Multiplication "
                              "\n 4: Division "
                              "\n"))

if function == 1:
    print("Total for ", number1, " + ", number2, "= ",addition(number1,number2))
if function == 2:
    print("Total for ", number1, " - ", number2, "= ",subtraction(number1, number2))
if function == 3:
    print("Total for ", number1, " * ", number2, "= ",multiplication(number1,number2))
if function == 4:
    print ("Total for ", number1, " / ", number2, "= ",division(number1,number2))

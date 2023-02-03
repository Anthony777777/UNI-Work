correctCount = 0
q1 = input("What is the capital of the United Kingdom?\nA. London\nB. Paris\nC. Washington\nD. Madrid\n")

if q1.upper() == "A":
    print("Correct!")
    correctCount = correctCount + 1
else:
    print("Incorrect. The correct answer was A. London")

q2 = input("What is the most widely used currency in the European continent?\nA. Pound\nB. Euro\nC. Dollar\nD. Rand\n")

if q2.upper() == "B":
    print("Correct!")
    correctCount = correctCount + 1
else:
    print("Incorrect. The correct answer was B. Euro")

q3 = input("Which country won the world cup in 1966?\nA. England\nB. Germany\nC. Spain\nD. Portugal\n")

if q3.upper() == "A":
    print("Correct!")
    correctCount = correctCount + 1
else:
    print("Incorrect. The correct answer was A. England")

q4 = input("Which country won the world cup in 1966?\nA. England\nB. Portugal\nC. France\nD. Italy\n")

if q4.upper() == "B":
    print("Correct!")
    correctCount = correctCount + 1
else:
    print("Incorrect. The correct answer was B. Portugal")

print("You scored ", str(correctCount), " out of 4.")
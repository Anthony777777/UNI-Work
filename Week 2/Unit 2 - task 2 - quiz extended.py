correctCount = 0

attempts = 3
while attempts != 0:
    q1 = input("What is the capital of the United Kingdom?\nA. London\nB. Paris\nC. Washington\nD. Madrid\n")
    if q1.upper() == "A":
        print("Correct!")
        correctCount += 1
        attempts = 0
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect. You have ", attempts, "attempts left. \n")
        else:
            print("You are out of attempts. The correct answer was A. London.\n")

attempts = 3
while attempts != 0:
    q2 = input("What is the most widely used currency in the European continent?\nA. Pound\nB. Euro\nC. Dollar\nD. Rand\n")
    if q2.upper() == "B":
        print("Correct!")
        correctCount += 1
        attempts = 0
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect. You have ", attempts, "attempts left. \n")
        else:
            print("You are out of attempts. The correct answer was B. Euro.\n")

attempts = 3
while attempts != 0:
    q3 = input("Which country won the world cup in 1966?\nA. England\nB. Germany\nC. Spain\nD. Portugal\n")
    if q3.upper() == "A":
        print("Correct!")
        correctCount += 1
        attempts = 0
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect. You have ", attempts, "attempts left. \n")
        else:
            print("You are out of attempts. The correct answer was A. England.\n")

attempts = 3
while attempts != 0:
    q4 = input("Which country won the world cup in 1966?\nA. England\nB. Portugal\nC. France\nD. Italy\n")
    if q4.upper() == "B":
        print("Correct!")
        correctCount += 1
        attempts = 0
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect. You have ", attempts, "attempts left. \n")
        else:
            print("You are out of attempts. The correct answer was B. Portugal.\n")

if correctCount == 4:
    print("You got them all correct ", correctCount,"/4")
else:
    print("You only got ", correctCount, "/4 ", "try again")
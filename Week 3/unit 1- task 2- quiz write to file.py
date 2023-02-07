import datetime

name = input("Give us yer name: ")
print("Great name ", name, ". Alright quiz time.")

quizFile = open("quiz.txt", "r")
correctCount = 0
questionCount = 0
for line in quizFile.readlines():
    if line[0:8] == "correct:":
        questionCount += 1
        correct = line[8:9]
        attempts = 3

        while attempts != 0:
            answer = input("What's your answer?? ")
            if answer.upper() == correct:
                print("Correct!")
                correctCount += 1
                attempts = 0
            else:
                attempts -= 1
                if attempts > 0:
                    if attempts > 1:
                        print("Incorrect. You have ", attempts, "attempts left. DON'T PANIC!!! \n")
                    else:
                        print("Incorrect. This is your last attempt. Here's a hint: the answer is ", correct, ".\n")
                else:
                    print("You are simply out of attempts. The correct answer was ", correct, ".\n")
    else:
        print(line)

quizFile.close()

print("I'm sorry to say the quiz is over, but I hope you had the time of your life.")
print("You scored ", correctCount, " out of ", questionCount, ".")

scoresFile = open("quizScores.txt", "a")
scoresFileText = str(datetime.datetime.now()) + ": " + str(name) + " scored " + str(correctCount) + " out of " + str(questionCount) + ".\n"
scoresFile.writelines(scoresFileText)
scoresFile.close()
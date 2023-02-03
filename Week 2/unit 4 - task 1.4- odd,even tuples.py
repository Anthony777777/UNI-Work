#This function takes a list of integers and returns if they are even or odd numbers
#
def OddEvenCheck(userInput):
    userInputList = userInput
    evenOddList = []
    Counter = 0
    for i in userInputList:
        if int(userInputList[Counter]) % 2 == 0:
            evenOddList.append('({}, even)'.format(userInputList[Counter]))
        if int(userInputList[Counter]) % 2 != 0:
            evenOddList.append('({}, odd)'.format(userInputList[Counter]))
        Counter += 1
    return(evenOddList)

list1 = ([1, 2, 3, 2, "2", "6", "7"])
list2 = ["1", "2", "3", "2", "2", "4", "5", "6", "7"]


print(OddEvenCheck(list1))
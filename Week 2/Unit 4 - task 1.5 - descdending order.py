# Example: descending (2, 4) should return [4, 3, 2]
def numberRange(x, y):
    rangeCounter = x
    numberRangeList = []
# y+1 to be inclusive of final number in range
    for numbers in range(x, y+1):
        numberRangeList.append(rangeCounter)
        rangeCounter += 1
    numberRangeList.reverse()
    print(numberRangeList)

numberRange(2,4)
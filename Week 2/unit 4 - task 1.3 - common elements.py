#This function returns common elements between two lists
def commonElements(list1, list2):
    commonElementsList = []
    counterElementInList = 0
    for i in list1:
        if list1[counterElementInList] in list2:
            commonElementsList.append(list1[counterElementInList])
            counterElementInList += 1
    distinctList = []
    [distinctList.append(anyvalue) for anyvalue in commonElementsList]
    # use this code to get the distinct elements rather than multiples if they exsist
    # [distinctList.append(anynumber) for anynumber in list if anynumber not in distinctList]
    #
    return(distinctList)

list1 = [1, "2", "3", "2", "2", "6", "7","bird"]
list2 = [1, "2", "3", "2", "2", "6", "7","bird","teacup"]

# finds any of the same details in the two list
print(commonElements(list1,list2))
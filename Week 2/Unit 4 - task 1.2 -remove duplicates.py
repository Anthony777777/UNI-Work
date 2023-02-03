#This function removes
def removeFromList(input, list):
    while (input in list):
        list.remove(input)

# lists are defined by [] they can be altered and changed
#lists allow duplicate values and are indexed from 0 to end
#lists are ordered
list1 = [1, "2", "3", "2", "2", "6", "7","bird"]
list2 = [1, "2", "3", "2", "2", "6", "7","bird"]

# entries need to match completely to be found ie 2 needs to be input as "2"
# carnt cross reference lists on values
removeFromList(1,list2)
# new list is printed without the first value from remove from list
#example if value entered is 2 then the new print would take away all the 2's
# as long as the input was an exact match eg "2" rather than 2
print(list2)

#This function removes duplicates from a list
def removeDuplicates(list):
    # creates a new temporary list with a blank value
    distinctList = []
    # adds old list into temp lists refencing temp list to see if number allready
    # exsists and if not adds to end
    [distinctList.append(anynumber) for anynumber in list if anynumber not in distinctList]
    return(distinctList)

print(removeDuplicates(list2))
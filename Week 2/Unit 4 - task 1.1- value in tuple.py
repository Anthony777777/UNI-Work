#This function checks if the input is in a list
def crossReference (input, list):
    if input in list:
        print(True)
    else:
        print(False)

#tuples are written in () they are ordered and unchangeable from original form they allow duplicates
# tuple items are indexed from 0-finish number
list1 = (1, "2", "3", "2", "2", "6", "7","bird")
list2 = (1, "2", "3", "2", "2", "6", "7","bird")

# entries need to match completely to be found ie 2 needs to be input as "2"
# carnt cross reference lists on values
crossReference(list1,list2)
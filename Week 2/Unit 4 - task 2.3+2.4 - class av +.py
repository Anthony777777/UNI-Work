def class_average_grade(average):
#0-0.9 = zero
    if int(average) == 0 or float(average) in (x/10 for x in range(0, 1-1)):
        return ("Classes Average Grade is: zero")
#1 - 3.9 = fail
    elif int(average) in range (1,3) or float(average) in (x/10 for x in range(1, 4-1)):
        return("Classes Average Grade is: fail")
#4-6.9 = mid fail
    elif int(average) in range (4,6) or float(average) in (x/10 for x in range(4, 7-1)):
        return ("Classes Average Grade is: 3rd")
#7 -9.9 = 2:2
    elif int(average) in range (7,9) or float(average) in (x/10 for x in range(7, 10-1)):
        return ("Classes Average Grade is: 2:2")
#10 - 13.9 = 2:1
    elif int(average) in range (10,13)or float(average) in (x/10 for x in range(10, 13-1)):
        return("Classes Average Grade is: 2:1")
#13- 15.9 = first
    elif int(average) in range (13,15) or float(average) in (x/10 for x in range(13, 16+1)):
        return  ("Classes Average Grade is: First")
#16 = perfect scores for everyone
    elif int(average) == 16:
        return ("perfect scores all round")
#anything else incorrect entries
    else:
        return ("invalid")

def classAverage(gradesinput):
    totalSum = sum([float(totals) for totals in gradesinput])
    average = totalSum / len(gradesinput)
    return float(average)

def classTotal(gradesinput):
    totalSum = sum([float(totals) for totals in gradesinput])
    return float(totalSum)

numberOfStudents = int(input("Number of Students: "))
studentGrade = []
count = 0
for studentGradeLoop in range(numberOfStudents):
    count += 1
    studentGrade.append(input("Grade for student" + str([count]) + ": "))

print("The total scores are :", classTotal(studentGrade))
print("The Average score is :", classAverage(studentGrade))
print("The class average grade equits too: ", class_average_grade(classAverage(studentGrade)))
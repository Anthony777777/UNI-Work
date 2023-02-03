def classAverage(gradesinput):
    totalSum = sum([float(totals) for totals in gradesinput])
    average = totalSum / len(gradesinput)
    return ("The total scores is: ", totalSum,
    "The Average is: ", average)

numberOfStudents = int(input("Number of Students: "))
studentGrade = []
count = 0
for studentGradeLoop in range(numberOfStudents):
    count += 1
    studentGrade.append(input("Grade for student" + str([count]) + ": "))

print(classAverage(studentGrade))
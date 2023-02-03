numberOfStudents = int(input("Number of Students: "))
studentGrade = []
count = 0

for studentGradeLoop in range(numberOfStudents):
    count += 1
    studentGrade.append(input("Grade for student" + str([count]) + ": "))

average = (sum([float(x) for x in studentGrade])) / count

print("The total scores is: ", sum([float(x) for x in studentGrade]))
print("The Average is: ", average)
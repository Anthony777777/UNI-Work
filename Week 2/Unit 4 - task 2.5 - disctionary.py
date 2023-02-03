teacher = input("Are you a teacher? ")
password = "University"
class_grades = {
    "101" : "2:1",
    "102" : "fail",
    "103" : "zero"
}
if teacher.upper() == "YES":
    test = input("Please enter password ")
    if password == test.capitalize():
        print("Thank you! you have passed Security ")
        operation = int(input("Please select how you wish to proceed:"
                          "\n 1. Input new grade"
                          "\n 2. View all grades"
                          "\n 3. Amend grades"
                          "\n"))
        if operation == 1:
            student_id = input("Please enter the studnet id: ")
            grade = input("Please enter the students grade: ")
            class_grades[student_id] = grade
            print("these are the new class values ")
            for key, value in class_grades.items():
                print("student id: ", key)
                print("grade : ", value)
        if operation == 2:
            for key, value in class_grades.items():
                print("student id: ", key)
                print("grade : ", value)
        if operation == 3:
            student_id = input("Please enter student id of grade to change : ")
            new_grade = input("please enter new grade ")
            class_grades[student_id] = new_grade
            for key, value in class_grades.items():
                print("student id: ", key)
                print("grade : ", value)
else:
    student_id = input("please enter your student id: ")
    print("your grade is: ", class_grades[student_id])


first_number = int(input("please enter the first number: "))
second_number = int(input("please enter the second number: "))
total = 0

for i in range(second_number):
    total += first_number

print("The multiplication by addition only is: ", total)
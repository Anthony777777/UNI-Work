loop = int(input("Number of Expenses: "))
expenses_name = []
expenses_list = []
# -1 this is due to how the count works on the loop ie 2 expenses is 0,1 in python -
# the -1 allows the count to run the correct amount of times.
count = -1
for expen_name_list in range(loop):
    count+=1
    expenses_name.append(input("Name of Expenditure: "))
    expenses_list.append(input("Cost of " + str(expenses_name[count]) + ": " ))

print("Total cost of all expenditure ", sum([float(x) for x in expenses_list]))
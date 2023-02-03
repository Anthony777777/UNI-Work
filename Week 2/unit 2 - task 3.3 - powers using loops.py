n = int(input("Initial number "))
m = int(input("power multiplied: "))

total = n
# has to start at 1 so it counts correctly 1,2,3 rather than 0,1,2,3
for i in range(1,m):
    total = total * n

print("the total of ",n," to the power of ", m , " : ", total)
score = int(input("Please enter your score? "))

# this stops people entering nothing
#no mesures in place to stop people entering a word currently will error
while score == "":
    score = input("Please enter your score? ")

if score == 0:
        print("your Grade is: zero")
elif score in range(1,3):
        print("fail")
elif score in range(4,6):
        print("your Grade is: 3rd")
elif score in range(7, 9):
        print("your Grade is: 2:2")
elif score in range(10, 13):
        print("your Grade is: 2:1")
elif score in range(14, 16):
        print("your Grade is: First")
else:
        print ("invalid entry")
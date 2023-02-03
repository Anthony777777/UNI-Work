import random

# sets the condition for name stops blank values
name = ""
while not name.capitalize():
    name = input("Please enter your name: ")
# generates a random number in range 0,100
number = random.randrange(0, 100)
player_geuss = int(input("Please enter a number between 0 and 100: "))
# sets attempt counter to 1
attempts = 1

# while player geuss the incorrect number
# if geuss is more than number print lower
# if geuss is higher print higher
# each time increase the attempts counter
while player_geuss != number:
    if player_geuss > number:
        print('\n' + "Guess a number that is lower than: ", player_geuss)
    else:
        print('\n' + "Guess a number that is higher than: ", player_geuss)
    player_geuss = int(input("Please enter a number between 0 and 100: "))
    attempts += 1

print("Congratulations ", name)
print("It took you ", attempts, "tries to get this correct")

print(number)

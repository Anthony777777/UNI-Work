import math


def square_root(x : int):
    if x < 0:
        raise ValueError("The given width %d is negative" %x)
    return math.sqrt(x)


try:
    print("Let's calculate the square root!")
    x = int(input("Enter a number: "))
    p = square_root(x)
    print("The squoot is: %d" %p)
except ValueError as err:
    print("Invalid input: %s" %err)
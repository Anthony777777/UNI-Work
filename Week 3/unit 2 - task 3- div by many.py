def div_by_many(p, qs):
    r = []
    try:
        for q in qs:
            r.append(p/q)
    except ZeroDivisionError:
        r = []
    return r

import math

def div_bm(w : int):
    if w < 0:
        raise ValueError("The given number %d is negative" %w)
    return div_bm(w)

try:
    print("Let's calculate the sqre root!")
    w = int(input("Enter the number to be rooted:"))
    print("The root is: " , (w))
except ValueError as err:
    print('Invalid input: %s' %err)


def div_by_many(p: int, qs: list):
    div = []
    for q in qs:
            if q == 0:
                raise ValueError("Index " + str(qs.index(q)) + " in list is 0")
                div.append(p / q)
                print(div)
                return divdiv_by_many(150, [1, 2, 15, 25, 50, 75, 74])


    div_by_many(100, [1, 2, 4, 25, 0])
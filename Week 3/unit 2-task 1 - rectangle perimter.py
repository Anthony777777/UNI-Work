def perimeter_rectangle(w : int, h : int):
    if w < 0:
        raise ValueError("The given width %d is negative" %w)
    if h < 0:
        raise ValueError("The given height %d is negative" %h)
    return 2*(w+h)

try:
    print("Let's calculate the perimeter of a rectangle!")
    w = int(input("Enter the width:"))
    h = int(input("Enter the height:"))
    p = perimeter_rectangle(w, h)
    print("The perimeter is: %d" %p)
except ValueError as err:
    print('Invalid input: %s' %err)
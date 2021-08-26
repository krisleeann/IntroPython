# Write a function named my_min that accepts 3 integers as parameters 
def my_min(x, y, z):
    ls = [x, y, z]

    list.sort(ls)
    minimum = ls[0]
    integer = int(minimum)

    # returns the smallest of the three values, such that the call my_min(3, -2, 7) would return -2
    return integer

def main():
    # Returns and prints -2 and -27, respectively 
    my_min(3, -2, 7)
    print(my_min)

    my_min(19+3, 6, -9*3)
    print(my_min)

    # BUG: No errors raised but the output is in not in int form.

main()
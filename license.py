from random import randint, choices
from string import ascii_uppercase

def plate():

    ltr_list = []
    num_list = []

    for i in range(3):
        l = chr(randint(65, 90))
        ltr_list.append(l)

        n = randint(1, 9)
        num_list.append(n)

    print(*num_list, " ", *ltr_list, sep="")

def main():
    plate()

main()
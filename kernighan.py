def print4x() :
    print ("Controlling complexity is the essence of programming!")
    print ("Controlling complexity is the essence of programming!") 
    print ("Controlling complexity is the essence of programming!") 
    print ("Controlling complexity is the essence of programming!")

def print64():
    i = 64
    n = True
    # Prints 32 times 
    if ((i % i == 0) or (i % 2 == 0) or (i % 4 == 0) or (i % 8 == 0) == n):
        print4x()
        print4x()
        print4x()
        print4x()
    if ((i % 3 == 1) or (i % 7 == 1)== n):
        print4x()
        print4x()
    if ((i % 5 == 4) or (i % 6 == 4) == n):
        print4x()
        print4x()

def main():
    # Prints 64 times when called twice
    print64()
    print64()

main()
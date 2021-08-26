def main():
    base = int(input("Enter an integer for the base: "))

    for i in range(base):
        for j in range(i + 1):
            print(" ", end="")
        for k in range(base - i):
            print("*", end="")
        print()
    
main()
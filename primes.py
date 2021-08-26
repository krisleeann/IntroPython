def main():
    # Prompt user for an integer  
    number = int(input("Enter a number, and I'll tell you which prime #s come before it: "))

    # Loop through values to see if prime or not, print value if False is not triggered
    for number in range(2, number):
        prime = True
        for i in range(2, number):
            if (number % i == 0):
                prime = False
        # Prints prime values leading up to the 'number' value
        if prime:
            print(number)  

main()
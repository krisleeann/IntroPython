def print_range(x, y):
    # Handle cases where values are the same
    if x == y:
        print(x)
    # Sort values in ascending order if they differ
    else:
        n = [x, y]
        n = list.sort(n)

    for i in range(x, y + 1):
        print(i, end=" ")
        i += 1
    print()

def main():
    # Bug: could not wrap the output in brackets
    print_range(2, 7)
    
main()
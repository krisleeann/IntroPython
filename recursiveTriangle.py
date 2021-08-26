def print_triangle(sideLength):
    if sideLength > 0:
        print("[]" * sideLength)
        print_triangle(sideLength-1)
    return
        
def main():
    print_triangle(4)

main()

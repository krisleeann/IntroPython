def months(n):
    m =  {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    
    print(m[n])

def main():
    n = int(input("Please enter a month in integer form: "))
    months(n)

main()
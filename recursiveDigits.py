def digit_sum(n):
    # base case
    if n < 10: 
        return 1
    # recursive case
    else: 
        return n % 10 + digit_sum(n / 10)
    
def main():
    print(int(digit_sum(3456))) # off by 1
    print(int(digit_sum(1234))) # correct
    
main()

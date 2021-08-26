# i. 
def power (x, n):                           
    # raise x to the n'th power 
    if n == 0:
        return 1.0                                  # base case
    elif n > 0 and n % 2 == 0:                      # evens case
        y = power(x, n / 2)
        return power(y, 2)
    elif n > 0:             
        return x * power(x, n-1)                    # odds case
    else:                                   
        return 1.0 / power (x, -n)                  # less than 0 case

def main():
    print(power(2, 2))

main()


# ii. None; NameError, as foobar is not defined and I believe cannot be performed on a string. 
# Solution: assign foobar an int value before calling it in this context.
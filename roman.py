# SUBMITTED FOR EXTRA CREDIT 
# BUG: DOES NOT ACCOUNT FOR SUBTRACTION CASES 

def convert(number):
    # Read in a string of characters that represent a Roman numeral and convert it to Arabic form (an integer).
    x = 0
    
    for i in range(len(number)):
        if number[i] == ('M'):
            x += 1000
        elif number[i] == ('D'):
            x += 500
        elif number[i] == ('C'):
            x += 100
        elif number[i] == ('L'):
            x += 50
        elif number[i] == ('X'):
            x += 10
        elif number[i] == ('V'):
            x += 5
        elif number[i] == ('I'):
            x += 1
        else:
            pass
        
        # ADD SUBTRACTION CASES 

    return x

def main():    
    print("a.) LXXXVII becomes: \t{}".format(convert("LXXXVII")))           # 87    OK
    print("b.) CCXIX becomes: \t{}".format(convert("CCXIX")))               # 219   Off by 3: missing subtraction logic
    print("c.) MCCCLIV becomes: \t{}".format(convert("MCCCLIV")))           # 1354  Off by 2: missing subtraction logic
    print("d.) MMDCLXXIII becomes: {}".format(convert("MMDCLXXIII")))     # 2673  OK
    print("e.) MCDLXXVI becomes: \t{}".format(convert("MCDLXXVI")))         # 1476  Off by 200: missing subtraction logic

main()

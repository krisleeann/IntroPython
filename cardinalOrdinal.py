def create_ordinal_form(n):

    ending = ["th", "st", "nd", "rd"]
    ordinal = ""
    
    if n == 111 or n == 112 or n == 113:
        ordinal = ending[0]
    elif n == 11 or n == 12 or n == 13:
        ordinal = ending[0]
    elif n == '1' or (n % 10 == 1):
        ordinal = ending[1]
    elif n == '2' or (n % 10 == 2):
        ordinal = ending[2]
    elif n == '3' or (n % 10 == 3):
        ordinal = ending[3]
    else: 
        ordinal = ending[0]
    
    # Return formatting found via: https://docs.python.org/3.4/library/string.html#string-formatting
    return "{}{}".format(n, ordinal)

def main():
    # For example, your method should return the following values:
    print(create_ordinal_form (1))
    print(create_ordinal_form (2))
    print(create_ordinal_form (3))
    print(create_ordinal_form (10))
    print(create_ordinal_form(11))
    print(create_ordinal_form(12))
    print(create_ordinal_form (21))
    print(create_ordinal_form (42))
    print(create_ordinal_form (101))
    print(create_ordinal_form (111))

main()

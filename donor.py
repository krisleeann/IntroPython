def sorting(x):
    # A certain charity designates donors who give $10,000.00 or more as Benefactors; 
    if 10000.00 <= x:
        print("Benefactor")
    # those who give $1,000.00 or more but less than $10,000.00 as Patrons; 
    elif (1000.00 <= x < 10000.00):
        print("Patrons")
    # those who give $200.00 or more but less than $1,000.00 as Supporters; 
    elif (200.00 <= x < 1000.00):
        print("Supporters")
    # those who give $15.00 but less than $200.00 as Friends; 
    elif (15.00 <= x < 200.00):
        print("Friends")
    # and those who give less than $15 as Cheapskates.  
    elif (0.01 <= x < 15.00):
        print("Cheapskate")
    else:
        print("Error: cannot make a negative donation.")

def main():
    donation = float(input("Enter the amount of a contribution: "))
    sorting(donation)

main()
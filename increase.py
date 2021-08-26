# A single constant variable can be changed 
# Example prices: 48  54  49  47  62  64  59  70  75  82
DAYS = 3

def compare():
    global DAYS
    # Using an array instead of a list
    prices = [input("Please enter your stock prices, followed by the enter key: ") for i in range(DAYS)]
    print()

    highest = 0
    lowest = 0
    increase = 0
    day = 0 
    
    for i in prices:
        i = 0
        prices = str(prices)
        if prices[i] < prices[i+1]:
            highest = prices[i+1]
            lowest = prices[i]
            increase = prices[i+1] - prices[i]
            day = i
            price += 1
            i += 1
        elif price[i] == price[i-1]:
            pass
        elif price[i] < price[i-1]:
            # Handles cases where the new price is less than the old price
            pass
        else:
            # Handles cases where the price does not change
            print("No increase found.")

    # BUG: doesn't print updated values
    print(f"The largest increase was %i" % increase)
    print(f"on day %i" % day) 
    print(f"of %i to %i" % (lowest, highest))
    
    
def main():
    compare()

main()
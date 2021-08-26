def check(num):
    card = num

    # Check if user's input is valid 
    if len(card) < 8 or len(card) > 8:
        print("Please only enter 8 integer digits. Try again.")
        main()
    else:
        pass
    
    # Starting from the righmost digit, form the sum of every other digit
    card = card.reverse()
    card = int(card)
    checked_values = []
    values = list(enumerate(card, start=1))

    for i, value in values:
        # Double each of the digits that were not included in the previous step
        if i % 2 == 0:
            checked_values.append(value * 2)
        else:
            checked_values.append(value)

            # Handle double digits cases
            if value > 9:
                doubled = value - 9

                checked_values.append(doubled)
            else:
                checked_values.append(value)

    total = sum(checked_values)

    # Final validity check
    if total % 10 == 0:
        print("The value %i is valid" % total)
    else:
        print("%i is not a valid sequence" % total)

def main():
    card = list(input("Please enter an eight digit sequence of numbers: ").strip())

    check(card)

main()
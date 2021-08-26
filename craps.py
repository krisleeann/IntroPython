from random import randint

def roll():
    first_die = randint(1, 6)
    second_die = randint(1, 6)
    point = first_die + second_die

    # Establish point boundaries of (4-6, 8-10)
    if (point > 3 and point < 7) or (point > 8 and point < 11):
        print(f"Computer rolls a %i and a %i, for a total of %i" % (first_die, second_die, point))
    
    return point

def play():
    point = roll()
    print(f"%i IS THE ESTABLISHED POINT" % point)
    
    # Enter matching phase of game
    new_roll = roll()

    while new_roll != 7 and new_roll != point:
        new_roll = roll()    
        
    if new_roll == 7:
        print("YOU LOSE!")
        exit
    elif new_roll == point:
        print("YOU WIN!")
        exit
    else:
        roll()
        
def main():
    play()

main()
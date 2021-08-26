import random

def play(comp_num, user_num):
    if comp_num == user_num:
        return True
    else:
        return False

def comp_generated():
    comp_num = []

    while len(comp_num) < 4:
        num = random.sample(range(1, 9), 4)
        if num not in comp_num:
            comp_num.append(num)
            
        comp_num.sort()

    return comp_num

def user_input():
    user_num = []

    while len(user_num) < 4:
        num = int(input("Pick 4 unique integer values: (enter 1 # followed by enter): "))

        if num not in user_num:
            user_num.append(num)
        else:
            input("Please select another number. Values may not repeat.")

        user_num.sort()
    
    return user_num

def main():
    comp_num = comp_generated()
    user_num =  user_input()
    play(comp_num, user_num)

    if play:
        print("YOU WIN!")
    else:
        print("Better luck next time...")

main()
import random

N = 5

def drunk_walk(N):
        # The student starts at 6th St., and randomly wanders one block up or down Main St. with probability 0.5 for each; 
        current_step = 6
        step_count = 0
        result = ""

        while (current_step > 0 and current_step < 12):
            prob = random.random()
            if (prob >= 0.5): 
                current_step += 1
            else:
                current_step -= 1
            step_count += 1

            if current_step == 11:
                result = "IN JAIL!"
            elif current_step == 1:
                result = "AT HOME!"

        print("Took " + str(step_count) + " steps, and ")
        print(f"Landed %s" % result + "\n")

        return step_count

def main():
    i = 0
    total_steps = 0

    while (N >= i): 
        i += 1
        print("Here we go again... time for a walk!")

        steps_taken = drunk_walk(N)
        total_steps += steps_taken

    print("Average number of steps: " + str(float(total_steps / N)))

main()
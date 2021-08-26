import sys 

def read_and_format():
    # Usage logic was buggy, commented it out for testing purposes
    # if len(sys.argv != 2):
    #     sys.exit("USAGE: python3 authorship.py your_file.txt")
    
    with open(sys.argv[1], "r") as file:
        line = file.readline()

        while line != "":
            word_list = line.split()

            for word in word_list:
                word = word.lower().rstrip(",.!;?:;[]-")

            line = file.readline()
    
    x = reader(line)
    word_count = len(word_list)
    proportion = (x / word_count) * 100
    
    for i in range(12):
        if i < 13:
            print(f"Proportion of {i}- letter words: {proportion}% ({word_count})")
        else:
            print("Proportion of 13- (or more) letter words: {proportion}% ({word_count})")

def reader(file):
    if reader(file) == "":              # Base case: empty files
        return 0
    else:                               # Recursive case
        return 1 + reader(file[1:])

def main():
    read_and_format()

main()

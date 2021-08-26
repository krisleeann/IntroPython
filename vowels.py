def vowel_count(sentence):
    
    ls = list(sentence)
    
    total = []
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    
    # Iterate through string and count vowels 
    # If vowel is in current position, add it to the list
    for i in range(len(ls)):
        if ls[i] == ('a') or ls[i] == ('A'):
            a_count += 1
        elif ls[i] == ('e') or ls[i] == ('E'):
            e_count += 1
        elif ls[i] == ('i') or ls[i] == ('I'):
            i_count += 1
        elif ls[i] == ('o') or ls[i] == ('O'):
            o_count += 1
        elif ls[i] == ('u') or ls[i] == ('U'):
            u_count += 1
        else: 
            pass
            
    total = [a_count, e_count, i_count, o_count, u_count]
        
    return total

def main():
    # For testing/grading purposes
    # x = str(input("Enter a sentence: "))
    print(" A  E  I  O  U")
    
    print(vowel_count("I think, therefore I am"))
    # Expected output: [1, 3, 3, 1, 0]
    
    print(vowel_count("Welcome to the United States of America"))
    # Expected output: [3, 6, 2, 3, 1]
    
    print(vowel_count("CSCI E-7 is all about the FUNdamentals!"))
    # Expected output: [4, 3, 2, 1, 2]

main()

# BUG: Output is correct but doesn't maintain the the set's original order. 

def split():
    
    # Phrase is capitalized, stripped, and converted into a list
    phrase_set = "Now is the time"
    p = phrase_set.upper()
    stripped = {char for char in p if char.strip()}
    
    print(letter_set(stripped))

def letter_set(phrase):
    
    l_set = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', ' X', 'Y', 'Z'}
        
    return list(l_set - phrase)
    
def main():
    split()

main()

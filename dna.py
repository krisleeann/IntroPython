# NOTE: Did not finish. "Implemented" with pseudo-code

def dna_errors(first_string, second_string):
    error_count = 0
    # Set lists that account for lower/upper cases of DNA; I realize this doesn't account for a-a/c-c/etc error pairs.
    a_pairs = ["a", "A"] 
    t_pairs = ["t", "T"]
    c_pairs = ["c", "C"]
    g_pairs = ["g", "G"]
    
    # Compare each element[i] with its counterpart to check if it's matched with its proper pair
    for i in range(first_string):
        for j in range(first_string):
            if ((i == a_pairs and j == t_pairs) or (i == a_pairs and j == t_pairs)):
                pass
            else:
                error_count += 1
                
    return error_count

def main():
    """ A is paired with T and vice-versa. C is paired with G and vice-versa.
    
    The task of your function is to find two particular kinds of errors:
    Unmatched nucleotides, in which one strand contains a dash ('-') at a given index, or does not contain a nucleotide at the given index 
    (if the strings are not the same length). Each of these counts as 1 error.
    Permutations, in which a letter from one strand is matched against the wrong letter in the other strand. 
    
    For example, A might accidentally pair with C, or G might pair with G. Each of these counts as 2 errors.
    
    For example, consider these two DNA strands:
    "GGGA-GAATCTCTGGACT" 
    "CTCTACTTA-AGACCGGTACAGG"
    This pair of strands has three permutations (at indexes 1, 15, and 17), 
    and seven unmatched nucleotides (dashes at indexes 4 and 9, and nucleotides in the second string with no match at indexes 18-22). 
    The permutations count as a total of 3 * 2 = 6 errors, and the unmatched nucleotides count as 7 * 1 = 7 errors, so your function
    would return an error count of 6+7 = 13 total errors if passed the two above strands.
    
    You may assume that each string consists purely of the characters A, C, T, G, and – (the dash character), 
    but the letters could appear in either upper or lowercase. 
    The strings might be the same length, or the first or second might be longer than the other. 
    Either string could be very long, very short, or even the empty string. 
    
    """
    print(dna_errors("GGGA-GAATCTCTGGACT", "CTCTACTTA-AGACCGGTACAGG"))

main()

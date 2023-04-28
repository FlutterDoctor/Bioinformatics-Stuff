# Problem
# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.


# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def find_reverse_palindromes(dna_string):
    # Define the reverse complement mapping
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    reverse_palindromes = []
    
    # Iterate through the DNA string
    for i in range(len(dna_string)):
        # Check palindromes of lengths between 4 and 12
        for length in range(4, 13):
            if i + length > len(dna_string):
                break  # Stop if substring exceeds DNA string length
            
            substring = dna_string[i:i+length]
            reverse_complement = ''.join(complement_map[base] for base in substring[::-1])
            
            # Check if the substring is a reverse palindrome
            if substring == reverse_complement:
                reverse_palindromes.append((i+1, length))
    
    return reverse_palindromes

# Test the function with the sample dataset
dna_string = """ATATATCCCATTGAGAGCTTGCTCTCATAGACTCCGGAATTTCGGGGGTGAGGCATCACACGGGATTCCCCAACGCCCAGGACTAAAACACAAATGATACGTGGATCTACCGTCACAGCATTCACAAGGATTGTTACCACTGTTTAGTTGCTGCATTGCTGGCCTCAATCTTCTCCACTCGCCGTCTTCTTCGGTGACCCGGTATGCATACACAAACGGCTAGACATTGCGCTGAAATACTTCTTGTAACTCAGCGTCTTTGGAAGGATAACTATCTATAACTAACGATTAAGGAGGGTAAGGTGAGGCGTCGTAGGGCGAATAACATCTGTGATCGACGCCTAGAGTTTCCACATAACTTTCTATCTAGCTACTAGGCGTGGCTATGTAGGAGGCGGCGTTATGTGACATCGTCTAGATCGCGCGCCATCACCCATCTACATCGTAGAACAGAGGACCCACCGCGGATATATCCGCGGGACGTGGGATCTGCAATACATGATATTCGAAACATCTGACTATCACAGAGTCGAACACTAGAACTGCTGTAGTGACGCAGCAGATGGACGCACCGTAACCTCGTGCTCCCTCCACGTATCGACATTCAGGTTGAGCGCTATACACGATACATAAGTTTCTAAACCACGAAGCCCACACATTGAACTCAGAAGAAAGTTGGCTCCATAAGACGCAACTGCGGAACTCGGCCATAACCTTCTGGGAGGCTACCCTTTTTGGATCAAAACAGCAAGTAACTGACACGTGAAAGTGTCGTTGAGAATCTCTTGCCCAGTAGTTGCTGTCCGGAGTAGGCGGGATGGCATGTCGCTTAACCTACTTAGCAATTCGCCATTGAGTCCCCTCGGTGTATCCTGGGCGACCGCTTGAGGCTGAGGTGAAGCTCAACGGCGCGCACAGTTGCTGGCCGGAGGAGATGCGC"""
reverse_palindromes = find_reverse_palindromes(dna_string)
for position, length in reverse_palindromes:
    print(position, length)

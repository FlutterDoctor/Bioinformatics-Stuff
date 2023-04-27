# Problem

# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def read_fasta_strings(file_path):
    with open(file_path, 'r') as file:
        fasta_strings = {}
        for line in file:
            if line[0] == '>':
                header = line[1:].strip()
                fasta_strings[header] = ''
            else:
                fasta_strings[header] += line.strip()
    return list(fasta_strings.values())

def longest_common_substring(dna_strings):
    substr = ''
    if len(dna_strings) > 1 and len(dna_strings[0]) > 0:
        for i in range(len(dna_strings[0])):
            for j in range(len(dna_strings[0])-i+1):
                if j > len(substr) and all(dna_strings[0][i:i+j] in x for x in dna_strings):
                    substr = dna_strings[0][i:i+j]
    return substr

# Read the input data
dna_strings = read_fasta_strings('/content/rosalind_lcsm-2.txt')

# Find the longest common substring
result = longest_common_substring(dna_strings)

# Print the result
print(result)

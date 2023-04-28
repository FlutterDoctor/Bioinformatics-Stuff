# Problem

# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

#             A T C C A G C T
#             G G G C A A C T
#             A T G G A T C T
# DNA Strings	A A G C A A C C
#             T T G G A A C T
#             A T G C C A T T
#             A T G G C A C T
            
#         A   5 1 0 0 5 5 0 0
# Profile	C   0 0 1 4 2 0 6 1
#         G   1 1 6 3 0 1 0 0
#         T   1 5 0 0 0 1 1 6
        
# Consensus	A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
from collections import Counter

def read_fasta_file(filename):
    with open(filename, 'r') as f:
        content = f.read().split('>')[1:]
        sequences = []
        for c in content:
            parts = c.split('\n', 1)
            name, sequence = parts[0], parts[1].replace('\n', '')
            sequences.append(sequence)
    return sequences

def compute_profile_matrix(sequences):
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    for i in range(len(sequences[0])):
        column = [sequence[i] for sequence in sequences]
        counts = Counter(column)
        profile['A'].append(counts['A'])
        profile['C'].append(counts['C'])
        profile['G'].append(counts['G'])
        profile['T'].append(counts['T'])
    return profile

def compute_consensus_string(profile):
    consensus = ''
    for i in range(len(profile['A'])):
        counts = {'A': profile['A'][i], 'C': profile['C'][i], 'G': profile['G'][i], 'T': profile['T'][i]}
        consensus += max(counts, key=counts.get)
    return consensus

# Example usage
sequences = read_fasta_file('/content/rosalind_cons.txt')
profile = compute_profile_matrix(sequences)
consensus = compute_consensus_string(profile)
print(consensus)
print('A:', ' '.join(map(str, profile['A'])))
print('C:', ' '.join(map(str, profile['C'])))
print('G:', ' '.join(map(str, profile['G'])))
print('T:', ' '.join(map(str, profile['T'])))

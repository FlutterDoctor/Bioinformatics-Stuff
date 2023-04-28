# Problem

# Assume that an alphabet 𝒜 has a predetermined order; that is, we write the alphabet as a permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

# Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in 𝒜.

# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).


# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
import itertools

def generate_strings(alphabet, n):
    # Generate all combinations of length n from the alphabet symbols
    all_combinations = itertools.product(alphabet, repeat=n)
    
    # Convert each combination to a string and sort the strings lexicographically
    sorted_strings = sorted([''.join(combination) for combination in all_combinations])
    
    return sorted_strings

# Example usage:
alphabet = ['A', 'C', 'G', 'T']
n = 2
result = generate_strings(alphabet, n)
for string in result:
    print(string)

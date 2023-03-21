# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

# Reverse the DNA sequence Pattern
def Reverse(Pattern):
    return Pattern[::-1]

# Find complement of the input DNA sequence Pattern
def Complement(Pattern):
    res = ""
    d = {"A":"T", "T":"A", "C":"G", "G":"C"}
    
    for i in Pattern:
        if i in d:
            res += d[i]
            
    return res

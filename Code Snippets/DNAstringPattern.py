# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    res = ""
    d = {"A":"T", "T":"A", "C":"G", "G":"C"}
    
    for i in Pattern:
        if i in d:
            res += d[i]
            
    return res

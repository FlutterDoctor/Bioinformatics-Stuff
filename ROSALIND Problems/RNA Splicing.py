# Problem

# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)


# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def transcribe(dna_string):
    # Transcribe DNA to RNA by replacing 'T' with 'U'
    rna_string = dna_string.replace('T', 'U')
    return rna_string


def translate(rna_string):
    # Define the codon to amino acid mapping
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
        'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein_string = ""
    codon = ""
    
    for base in rna_string:
        codon += base
        if len(codon) == 3:
            if codon in codon_table:
                amino_acid = codon_table[codon]
                if amino_acid != "":
                    protein_string += amino_acid
            codon = ""
    
    return protein_string


def transcribe_translate(dna_string, introns):
    # Remove introns from the DNA string
    for intron in introns:
        dna_string = dna_string.replace(intron, "")

    # Transcribe the DNA string to RNA
    rna_string = transcribe(dna_string)

    # Translate the RNA string to protein
    protein_string = translate(rna_string)

    # Add the stop codon to the protein sequence
    # protein_string += "*"

    return protein_string


# Test the function with the sample dataset
dna_string = "ATGTGGAAGCCTACCCTTGCGCGATGCATAGTAGTTACTGGTGGGATGAAACCATTCAAAGAAACCAGTATTGCATGTACGCGGTCGCTCGGGCGCTTCACGCCACAACCGCGTCAGCTGTTGCTCGAAATAGAATGTTGCTTCGACGGGACGCTCGGCAGCCCTCAAATTGGTTCACACTGCCGAGTCCTTCTCTCTCTCTCGCTCAAACCCTGCTGGATGCACGGGTCAGATGACACGCAGCTGCGCACTCATGCAAAAACGGCTCGTAGGAACATGCAATCCCATTGGGTCCGCACGTTTAAAGAAAATTCTCGTTGGGGCCGGTCATATCTACGAACAGCTGTTGCAGCGGAGGTAATCTACACTATACAGTTCGAGCAATCCGGTATTTAATCTGTATGCTACAACTGACCAGCTGTACGAAAAATGTAACTTCCGGCGGATTCGACAGGAGGTGGTTCCACCGGGCCGGGCCAGTTCGGTATCGTTGGTCCTCATTTCTTCGCAGGCGGAGAAATATCCTATCTACCTCCGTCGAAGATCAGGGCAGAGACGCGAGGCCACAGCTCGGTGATCCATGATGGCGAGACTACGACCTCCCGAATCTACAATAGAGGCTGTCATAAATGTCCCAAGGCGTAGACGGTAGGAGTCAACTGAGCTAGATGAAGGCGATGTGTGTGATAGGGGTCAGGGATCACGAATATGTATTGTGGCACTGATCATAAAATGGATAGTGCTGGGCATAGGATCATCGTGTCTCGTTAGTCCTCTGCAACATAAAGTTACCGTCGACAACAGGCTAAATTCGTCAGGTCTTCTCCACAAGGCGTAGAGTCTGGTCACCTTTCCCTGGCGTTGGCTCTGCGCTAGGCATGCTTACTTGAAATCGCGAGCGAGCGCTAACGTGCCTGCCTCTTTACTGTAAATTGGGCCTTATACCATTCCAGGATTTTACCTGGCGGTAGGTCCTTAG"
introns = ["GAGGCCACAGCTCG", "ACTACGACCTCCCGAATCTACAATAGAGGCTGTCATAAATGTC", "CGGTATCGTTGGTCCTCATT", "AGGCGTAGAGTCTGGTC", "TCATCGTGTC", "TCACACTGCCGAGTCCTTCTCTCTCTCTCGC", "CTTTACTGTAAATTGGGCCTTATACCATTCCAGGATTTTAC", "GAAACCAGTATTGCATGTACGCGGTCGCTCGGGCGCTTCACGCC", "ATGCTACAACTGACCAGCTGTACGAAAAATGTAACTTCCGGCGGA", "GGCTAAATTCGT" ,"ATGACACGCAGCTGCGCACTCATGCAAAAACGGCTCGTAGGA", "CTCTGCGCTAGGCATGCTTACTTGA", "GACGCTCGGC", "TACGAACAGC", "TAGGAGTCAACTGAGCTAGATGAAGGCGATGTGTGTGATAGGGGTCAG"]
protein_string = transcribe_translate(dna_string, introns)
print(protein_string)

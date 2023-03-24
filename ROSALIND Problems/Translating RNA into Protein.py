# In this problem, we need to translate an RNA sequence into a protein sequence.
# The RNA sequence is a string of nucleotides that correspond to a strand of mRNA.
# The protein sequence is a string of amino acids that are encoded by the RNA sequence.

# The 20 amino acids are represented by 20 letters from the English alphabet,
# excluding B, J, O, U, X, and Z. Protein strings are constructed from these 20 symbols.

# The RNA codon table maps every three-letter RNA codon to one of the 20 amino acids
# or a stop codon. The codons are read in groups of three nucleotides to encode
# individual amino acids in a protein sequence.

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
rna_codon_table = {
'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
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
'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

rna_seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
protein_seq = ''
for i in range(0, len(rna_seq), 3):
  codon = rna_seq[i:i+3]
  amino_acid = rna_codon_table[codon]
  if amino_acid == 'Stop':
    break
  protein_seq += amino_acid

print(protein_seq)
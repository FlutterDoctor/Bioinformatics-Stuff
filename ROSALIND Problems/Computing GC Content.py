# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
# read in the input file
with open('/content/rosalind_gc.txt', 'r') as f:
    # parse the input file into a dictionary of ID:sequence pairs
    fasta = {}
    for line in f:
        if line.startswith('>'):
            seq_id = line[1:].strip()
            fasta[seq_id] = ''
        else:
            fasta[seq_id] += line.strip()

# calculate the GC-content for each sequence and store the maximum
max_gc = 0
max_gc_id = ''
for seq_id, sequence in fasta.items():
    # calculate the GC-content as a percentage of the total sequence length
    gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    if gc_content > max_gc:
        max_gc = gc_content
        max_gc_id = seq_id

# print the ID of the sequence with the highest GC-content and the GC-content itself
print(max_gc_id)
print('{:.6f}'.format(max_gc))
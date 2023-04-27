# Problem

# A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

# A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

# For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

# Return: The adjacency list corresponding to O3. You may return edges in any order.

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def parse_fasta_file(file_path):
    """
    Parse a FASTA file and return a dictionary of DNA sequences.

    Args:
        file_path (str): Path to the input file.

    Returns:
        dict: A dictionary with DNA sequence identifiers as keys and sequences as values.
    """
    sequences = {}
    with open(file_path) as f:
        current_sequence = None
        for line in f:
            if line.startswith('>'):
                current_sequence = line[1:].strip()
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line.strip()
    return sequences


def create_substrings(sequences, k):
    """
    Create all substrings of length k from the given DNA sequences.

    Args:
        sequences (dict): A dictionary with DNA sequence identifiers as keys and sequences as values.
        k (int): The length of the substrings.

    Returns:
        set: A set of all substrings of length k from the given DNA sequences.
    """
    substrings = set()
    for sequence in sequences.values():
        for i in range(len(sequence) - k + 1):
            substrings.add(sequence[i:i+k])
    return substrings


def overlap_graph(sequences, k):
    """
    Generate an overlap graph for the given DNA sequences.

    Args:
        sequences (dict): A dictionary with DNA sequence identifiers as keys and sequences as values.
        k (int): The length of the substrings to use for matching.

    Returns:
        list: A list of directed edges in the overlap graph.
    """
    substrings = create_substrings(sequences, k)
    adjacency_list = []
    for s1 in sequences:
        for s2 in sequences:
            if s1 != s2 and sequences[s1][-k:] == sequences[s2][:k]:
                # Add a directed edge from s1 to s2 if there is a match between s1[-k:] and s2[:k].
                adjacency_list.append((s1, s2))
    return adjacency_list


if __name__ == '__main__':
    # Parse the input file.
    sequences = parse_fasta_file('/content/rosalind_grph.txt')

    # Generate the overlap graph with k=3.
    adjacency_list = overlap_graph(sequences, 3)

    # Print the adjacency list.
    for edge in adjacency_list:
        print(edge[0], edge[1])

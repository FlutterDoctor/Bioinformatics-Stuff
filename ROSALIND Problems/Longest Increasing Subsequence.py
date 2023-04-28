# Problem

# A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

# A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

# Given: A positive integer n≤10000 followed by a permutation π of length n.

# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def longest_increasing_subsequence(permutation):
    n = len(permutation)
    # Initialize an array to store the length of the longest increasing subsequence ending at each index
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if permutation[i] > permutation[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1

    # Find the maximum LIS length
    max_length = max(lis_lengths)

    # Reconstruct the LIS
    lis = []
    for i in range(n - 1, -1, -1):
        if lis_lengths[i] == max_length:
            lis.append(permutation[i])
            max_length -= 1
            if max_length == 0:
                break

    return lis[::-1]

def longest_decreasing_subsequence(permutation):
    n = len(permutation)
    # Initialize an array to store the length of the longest decreasing subsequence ending at each index
    lds_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if permutation[i] < permutation[j] and lds_lengths[i] < lds_lengths[j] + 1:
                lds_lengths[i] = lds_lengths[j] + 1

    # Find the maximum LDS length
    max_length = max(lds_lengths)

    # Reconstruct the LDS
    lds = []
    for i in range(n - 1, -1, -1):
        if lds_lengths[i] == max_length:
            lds.append(permutation[i])
            max_length -= 1
            if max_length == 0:
                break

    return lds[::-1]

# Read input from a file
filename = '/content/rosalind_lgis.txt'

with open(filename, 'r') as file:
    n = int(file.readline().strip())
    permutation = list(map(int, file.readline().split()))

lis = longest_increasing_subsequence(permutation)
lds = longest_decreasing_subsequence(permutation)

print(' '.join(str(num) for num in lis))
print(' '.join(str(num) for num in lds))

# Problem

# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

# Given: A positive integer n≤7.

# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).


# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
from itertools import permutations

n = 7
perms = list(permutations(range(1, n+1)))

with open('/content/permutations.txt', 'w') as f:
    f.write(str(len(perms)) + '\n')
    for perm in perms:
        f.write(' '.join(map(str, perm)) + '\n')

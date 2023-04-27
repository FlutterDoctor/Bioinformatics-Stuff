Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def mortal_fibonacci(n, m):
    # Initialize a list to keep track of the number of rabbit pairs in each age group
    ages = [0] * m
    # Start with one pair of rabbits in the first age group
    ages[0] = 1
    # Iterate through each month
    for i in range(1, n):
        # The number of new pairs born is equal to the number of mature pairs (all except the youngest)
        new_pairs = sum(ages[1:])
        # Shift all age groups up by one (the oldest die off)
        ages[1:] = ages[:-1]
        # The number of new pairs becomes the new youngest age group
        ages[0] = new_pairs
    # Return the total number of rabbit pairs
    return sum(ages)

n = 95
m = 16
result = mortal_fibonacci(n, m)
print(result)  

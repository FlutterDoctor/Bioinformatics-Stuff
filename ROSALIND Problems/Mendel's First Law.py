# Problem
# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by:
# Pr(X=red) = 3/5
# Pr(X=blue) = 2/5.

# Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes:
# Pr(X=blue and Y=blue) + Pr(X=red and Y=blue),
# or (3/10) + (1/10) = 1/4 (see Figure 2 above).

# Given three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive. 
# Return the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample Dataset:
# 2 2 2

# Sample Output:
# 0.78333

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::

def calculate_dominant_allele_probability(homozygous_recessive_count: int, heterozygous_count: int, homozygous_dominant_count: int) -> float:
    total_population = homozygous_recessive_count + heterozygous_count + homozygous_dominant_count
    
    # Calculate the probability of selecting two recessive alleles from the population
    prob_homozygous_recessive = (homozygous_recessive_count * (homozygous_recessive_count - 1) 
                                + 2 * heterozygous_count * homozygous_recessive_count 
                                + 0.25 * heterozygous_count * (heterozygous_count - 1)) / (2 * total_population * (total_population - 1))
    
    # Calculate the probability of a dominant allele
    prob_dominant_allele = 1 - prob_homozygous_recessive
    
    return prob_dominant_allele


homozygous_recessive_count = 20
heterozygous_count = 17
homozygous_dominant_count = 30

dominant_allele_probability = calculate_dominant_allele_probability(homozygous_recessive_count, heterozygous_count, homozygous_dominant_count)
print(dominant_allele_probability)
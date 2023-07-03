"""
Formula for pentagonal number is n * (3n-1) / 2

Inverse formula, given a pentagonal number p:
n = ( 1 +- sqrt(1 + 24*p) ) / 6

P1 = 1
P2 = 5
P3 = 12
P4 = 22
P5 = 35
P6 = 51

This solution iterates through all possible pairs with distance 1 until we hit an upper bound
This is repeated for distance 2,3, etc... until we find a desired number below the upper bound

It is guaranteed to produce the minimum, but it is also very sub-optimal.
A better solution is provided on the forum by "Nightingale" on April 4, 2020
"""

import math 

def nth_pentagonal(n):
    return (n*(3*n - 1)) // 2

def is_pentagonal(p):
    n = ( 1 + math.sqrt(1 + 24*p) ) / 6
    return n.is_integer()


# The pair we are trying to find. choose an upper limit, which I increased until a number is found
p_pair = [10000000, 0]

n = 2
k = 1 # distance between the pairs of pentagonal numbers

while (nth_pentagonal(k) - 1) < abs(p_pair[1] - p_pair[0]):
    n = k + 1 
    while (nth_pentagonal(n) - nth_pentagonal(n - k)) < abs(p_pair[1] - p_pair[0]):
        pn = nth_pentagonal(n)
        p_n_minus_k = nth_pentagonal(n-k)

        if is_pentagonal(pn + p_n_minus_k) and is_pentagonal(pn - p_n_minus_k):
            p_pair = [pn, p_n_minus_k]
            break # no need to increment n further

        n += 1
    k += 1

print( abs(p_pair[0] - p_pair[1]) )

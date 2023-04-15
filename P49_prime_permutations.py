"""
Find 3 numbers, between 1000 and 9999, that form an arithmetic progression and whose digits are permutations of each other

a2 - a1 = a1 - a0

a2 = a1 + d
a1 = a0 + d
a2 = a0 + 2d

After getting the answer, I see that the difference 'd' does have some patterns

3330 shows up a lot.
All the numbers are divisible by 18. so they all have 9 and 2 as a prime factor. WHY?

"""

import numpy as np
import math

def permutation_check(L:list):
    # given a list of (3) integers, check if their digits are permutations of each other
    L = [ sorted(str(n)) for n in L ]
    return all( [n == L[0] for n in L] )

def prime_bool_arr(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr


limit = 100000
is_prime_arr = prime_bool_arr(limit)
prime_arr = np.flatnonzero(is_prime_arr)
prime_arr = prime_arr[ prime_arr > 1000 ]

result_list = []
for p in prime_arr:
    d = 0
    while True:
        d += 2
        if p + 2*d >= limit: break

        if not is_prime_arr[p+d]: continue
        if not is_prime_arr[p+2*d]: continue

        result_list.append( [p, p+d, p+d+d] )


result_triples = [t for t in result_list if permutation_check(t)]

given_set = set([1487, 4817, 8147])
[  ''.join( [str(n) for n in t] ) for t in result_triples if set(t) != given_set]
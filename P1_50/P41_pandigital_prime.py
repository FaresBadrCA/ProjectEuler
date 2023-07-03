"""
what is the largest pandigital prime number?

Some observations: 
    #1) 9-pandigital numbers cannot be prime.
    because sum of digits 1+2+...+9 = 45, which is divisible by 3. So they are all divisible by 3
    same for 8-pandigital numbers

    Let's test 7-pandigital numbers for primality. It's best to search in descending order and terminate if we find a prime.
    #2) last digit cannot be 2. 
"""

import numpy as np
import math
from itertools import permutations

def prime_bool_arr(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr

upper_bound = 7654321
digits = [7,6,5,4,3,2,1]
is_prime_arr = prime_bool_arr(upper_bound + 1)
for n in permutations(digits):
    n = int( ''.join( map(str, n) ) ) # change permutation of digits to an integer
    if is_prime_arr[n]:
        print("Found prime: ", n)
        break

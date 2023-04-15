"""
What is the smallest odd composite (n) that cannot be written as the sum of a prime (p) and twice a square (a^2)?

n = p + 2*a^2

forward search through odd numbers (n).
then forward search through primes (p) less than n.

a = sqrt( (n - p) / 2 )

if such an integer 'a' exists, go to the next prime.
If we go through all primes less than n, then we found the desired number

"""

import numpy as np
import math

def prime_bool_arr(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr


def P46():
    is_prime_arr = prime_bool_arr(1000000)
    primes = np.flatnonzero(is_prime_arr)
    primes = primes[1:] # Exclude '2' from primes
    n = 3
    while True:
        n += 2 # next odd number
        if is_prime_arr[n]: continue # Only interested in composite 'n'

        for p in primes:
            if p >= n: return n # No result was found so 'n' is the number we're looking for
            if  math.sqrt( (n - p) // 2 ).is_integer(): break # 'a^2' exists, go to next number

P46()
